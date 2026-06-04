#!/usr/bin/env python3
"""Check whether a rendered proposal is safe for customer delivery."""

from __future__ import annotations

import argparse
import json
import re
import sys
from html import unescape
from pathlib import Path
from typing import Any


BLOCKED_PHRASES = [
    "internal_note",
    "AI 백채널",
    "내부 메모",
    "Human Linchpin Review",
    "확정 견적서입니다",
    "확정된 견적서",
    "최종 확정 견적",
    "최종 가격입니다",
    "무제한 수정",
    "잔금 전 최종 파일 전달",
    "잔금 전 권한 이전",
    "잔금 전 전달",
]

MONEY_PATTERN = re.compile(r"(?P<number>[0-9,]+)\s*만")
UNKNOWN_KEYS = ("harmless_unknown", "proposal_blocking_unknown", "price_affecting_unknown", "risk_unknown")


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"JSON parse failed: {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"Expected object: {path}")
    return data


def parse_krw(value: Any) -> int | None:
    if isinstance(value, int):
        return value
    if not isinstance(value, str):
        return None
    match = MONEY_PATTERN.search(value)
    if not match:
        return None
    return int(match.group("number").replace(",", "")) * 10000


def non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def string_items(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str) and item.strip()]


def unknown_items(data: dict[str, Any], key: str) -> list[str]:
    unknowns = data.get("remaining_unknowns")
    if not isinstance(unknowns, dict):
        return []
    return string_items(unknowns.get(key))


def price_looks_confirmed(data: dict[str, Any], html_text: str) -> bool:
    if data.get("pricing_status") == "final_estimate":
        return True
    confirmed_markers = ("확정 견적서입니다", "확정된 견적서", "최종 확정 견적", "최종 가격입니다")
    if any(marker in html_text for marker in confirmed_markers):
        return True
    final_estimate_count = html_text.count("최종 견적")
    has_material_review_notice = "자료 확인 후 확정" in html_text or ("자료 확인" in html_text and "최종 견적" in html_text)
    return final_estimate_count > 0 and not has_material_review_notice


def has_assumption_notice(html_text: str) -> bool:
    return (
        "이번 제안은 아래 가정을 기준으로 작성되었습니다" in html_text
        or ("가정" in html_text and "기준" in html_text and "작성" in html_text)
    )


def require_html_value(html_text: str, value: Any, label: str, errors: list[str]) -> bool:
    if not non_empty_string(value):
        errors.append(f"{label} must be non-empty")
        return False
    if value not in html_text:
        errors.append(f"{label} value missing from HTML: {value}")
        return False
    return True


def check_final_estimate_notice(notice: Any, errors: list[str]) -> None:
    if not non_empty_string(notice):
        errors.append("commercial_terms.final_estimate_notice must be non-empty")
        return
    has_final_estimate = "최종 견적" in notice
    has_material_review = "자료 확인 후 확정" in notice or ("자료 확인" in notice and "확정" in notice)
    if not has_final_estimate or not has_material_review:
        errors.append("commercial_terms.final_estimate_notice must explain final estimate after material review")


def check_commercial_terms(data: dict[str, Any], html_text: str, errors: list[str]) -> None:
    terms = data.get("commercial_terms")
    if not isinstance(terms, dict):
        errors.append("commercial_terms missing from proposal-data.json")
        return

    for key in (
        "payment_terms",
        "revision_policy",
        "additional_terms",
        "final_estimate_notice",
        "delivery_condition",
        "file_retention_days",
        "minor_fix_days",
    ):
        if key not in terms:
            errors.append(f"commercial_terms.{key} missing")

    require_html_value(html_text, terms.get("payment_terms"), "commercial_terms.payment_terms", errors)
    require_html_value(
        html_text,
        terms.get("final_estimate_notice"),
        "commercial_terms.final_estimate_notice",
        errors,
    )
    require_html_value(html_text, terms.get("delivery_condition"), "commercial_terms.delivery_condition", errors)
    check_final_estimate_notice(terms.get("final_estimate_notice"), errors)

    retention_days = terms.get("file_retention_days")
    if not isinstance(retention_days, int) or retention_days < 0:
        errors.append("commercial_terms.file_retention_days must be a non-negative integer")
    elif f"파일 보관 기간은 {retention_days}일" not in html_text:
        errors.append("commercial_terms.file_retention_days value missing from HTML")

    minor_fix_days = terms.get("minor_fix_days")
    if not isinstance(minor_fix_days, int) or minor_fix_days < 0:
        errors.append("commercial_terms.minor_fix_days must be a non-negative integer")
    elif f"경미 수정 기준 기간은 {minor_fix_days}일" not in html_text:
        errors.append("commercial_terms.minor_fix_days value missing from HTML")

    revisions = terms.get("revision_policy")
    if not isinstance(revisions, list) or not revisions:
        errors.append("commercial_terms.revision_policy must be a non-empty list")
    else:
        for index, item in enumerate(revisions):
            if not isinstance(item, dict):
                errors.append(f"commercial_terms.revision_policy[{index}] must be an object")
                continue
            require_html_value(
                html_text,
                item.get("asset"),
                f"commercial_terms.revision_policy[{index}].asset",
                errors,
            )
            rounds = item.get("feedback_rounds")
            if not isinstance(rounds, int) or rounds < 0:
                errors.append(f"commercial_terms.revision_policy[{index}].feedback_rounds must be a non-negative integer")
            elif f"{rounds}회" not in html_text:
                errors.append(f"commercial_terms.revision_policy[{index}].feedback_rounds value missing from HTML")


def check_pricing_items(data: dict[str, Any], html_text: str, errors: list[str]) -> None:
    items = data.get("pricing_items")
    if not isinstance(items, list) or not items:
        errors.append("pricing_items missing from proposal-data.json")
        return
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"pricing_items[{index}] must be an object")
            continue
        public_price = parse_krw(item.get("public_starting_price"))
        minimum_fee = parse_krw(item.get("minimum_project_fee"))
        if public_price is not None and minimum_fee is not None and minimum_fee < public_price:
            errors.append(
                f"pricing_items[{index}] minimum_project_fee is below public_starting_price: "
                f"{item.get('minimum_project_fee')} < {item.get('public_starting_price')}"
            )
        require_html_value(
            html_text,
            item.get("public_starting_price"),
            f"pricing_items[{index}].public_starting_price",
            errors,
        )
        require_html_value(
            html_text,
            item.get("minimum_project_fee"),
            f"pricing_items[{index}].minimum_project_fee",
            errors,
        )

        triggers = item.get("extra_cost_triggers")
        if not isinstance(triggers, list) or not triggers:
            errors.append(f"pricing_items[{index}] missing extra_cost_triggers")
        else:
            reflected = [trigger for trigger in triggers if isinstance(trigger, str) and trigger in html_text]
            if not reflected:
                errors.append(f"pricing_items[{index}].extra_cost_triggers not reflected in HTML")
        rounds = item.get("included_rounds")
        if not isinstance(rounds, dict):
            errors.append(f"pricing_items[{index}] missing included_rounds")


def check_request_lock(data: dict[str, Any], html_text: str, errors: list[str]) -> None:
    if data.get("request_lock_status") != "locked":
        errors.append("request_lock_status must be locked before customer delivery")

    unknowns = data.get("remaining_unknowns")
    if not isinstance(unknowns, dict):
        errors.append("remaining_unknowns missing from proposal-data.json")
    else:
        for key in UNKNOWN_KEYS:
            if key not in unknowns:
                errors.append(f"remaining_unknowns.{key} missing")

    blocking_unknowns = unknown_items(data, "proposal_blocking_unknown")
    if blocking_unknowns:
        errors.append("remaining_unknowns.proposal_blocking_unknown must be empty before customer delivery")

    price_unknowns = unknown_items(data, "price_affecting_unknown")
    if price_unknowns and price_looks_confirmed(data, html_text):
        errors.append("price_affecting_unknown remains while proposal price looks confirmed")

    risk_unknowns = unknown_items(data, "risk_unknown")
    handoff = data.get("department_handoff")
    risk_guard = []
    if isinstance(handoff, dict):
        risk_guard = string_items(handoff.get("risk_guard"))
    if risk_unknowns and not risk_guard:
        errors.append("risk_unknown remains but department_handoff.risk_guard is empty")

    assumptions = string_items(data.get("assumptions")) + string_items(data.get("assumption_locks"))
    if assumptions and not has_assumption_notice(html_text):
        errors.append("assumptions or assumption_locks exist but HTML lacks a customer-safe assumption notice")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("client_dir", help="clients/<client> directory")
    parser.add_argument("--allow-pending", action="store_true", help="allow pending Human Review for internal drafts")
    args = parser.parse_args()

    client_dir = Path(args.client_dir)
    proposal_path = client_dir / "proposal-data.json"
    html_path = client_dir / "proposal.html"
    data = load_json(proposal_path)
    html = html_path.read_text(encoding="utf-8")
    html_text = unescape(html)
    errors: list[str] = []

    status = data.get("human_review_status")
    if status == "blocked":
        errors.append("human_review_status is blocked")
    elif status == "pending" and not args.allow_pending:
        errors.append("human_review_status is pending; pass --allow-pending only for internal draft checks")
    elif status != "approved" and not (status == "pending" and args.allow_pending):
        errors.append("human_review_status must be approved before delivery")

    for phrase in BLOCKED_PHRASES:
        if phrase in html_text:
            errors.append(f"blocked phrase found in HTML: {phrase}")

    check_request_lock(data, html_text, errors)
    check_commercial_terms(data, html_text, errors)
    check_pricing_items(data, html_text, errors)

    if errors:
        print("proposal safety check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"proposal safety check ok: {client_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
