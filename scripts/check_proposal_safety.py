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
REVIEW_DECISIONS = ("pending", "approved", "blocked")
REQUIRED_REVIEW_HEADINGS = (
    "Desired Change Check",
    "SVM Check",
    "Department Analysis Check",
    "Commercial Check",
    "Trust Indicator Check",
)
STRATEGY_REQUIRED_PATHS = (
    ("desired_change", "raw_request"),
    ("desired_change", "current_state"),
    ("desired_change", "target_state"),
    ("desired_change", "tension"),
    ("desired_change", "change_type"),
    ("desired_change", "required_asset"),
    ("smallest_viable_market", "svm_status"),
    ("smallest_viable_market", "first_audience"),
    ("smallest_viable_market", "worldview"),
    ("trust_indicators", "strategic_no_signal"),
    ("trust_indicators", "judgment_benchmark"),
    ("trust_indicators", "status_shift_narrative"),
)
SVM_EVIDENCE_TERMS = ("SVM", "대상", "audience", "시장", "1순위", "제출 대상")
UNKNOWN_KEYS = ("harmless_unknown", "proposal_blocking_unknown", "price_affecting_unknown", "risk_unknown")
DEPARTMENT_KEYS = (
    "marketing_planning",
    "commercial_pricing",
    "design",
    "web_development",
    "content",
    "risk_guard",
    "proposal_writer",
)
DEPARTMENT_FIELDS = (
    "diagnosis",
    "recommendation",
    "scope_impact",
    "price_impact",
    "risks",
    "missing_inputs",
    "proposal_points",
    "client_safe_phrase",
    "trust_indicator",
)


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


def text_items(value: Any) -> list[str]:
    if isinstance(value, str) and value.strip():
        return [value]
    if isinstance(value, list):
        return string_items(value)
    return []


def string_items(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str) and item.strip()]


def collect_department_text(department_value: Any) -> list[str]:
    """Collect text from legacy list[str] or structured department object."""
    if isinstance(department_value, list):
        return string_items(department_value)
    if not isinstance(department_value, dict):
        return []

    items: list[str] = []
    for field in DEPARTMENT_FIELDS:
        items.extend(text_items(department_value.get(field)))
    return items


def collect_department_field_text(department_value: Any, field: str) -> list[str]:
    if not isinstance(department_value, dict):
        return []
    return text_items(department_value.get(field))


def is_structured_department(value: Any) -> bool:
    return isinstance(value, dict)


def has_minimum_analysis(value: Any) -> bool:
    if not is_structured_department(value):
        return False
    return bool(collect_department_field_text(value, "diagnosis") or collect_department_field_text(value, "recommendation"))


def has_any_field_text(value: Any, fields: tuple[str, ...]) -> bool:
    if not is_structured_department(value):
        return False
    return any(collect_department_field_text(value, field) for field in fields)


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end_index = text.find("\n---", 4)
    if end_index == -1:
        return {}, text

    raw_frontmatter = text[4:end_index]
    body_start = end_index + len("\n---")
    if body_start < len(text) and text[body_start] == "\n":
        body_start += 1
    fields: dict[str, str] = {}
    for line in raw_frontmatter.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, text[body_start:]


def read_proposal_review(client_dir: Path) -> str | None:
    path = client_dir / "proposal-review.md"
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def extract_review_decision(review_text: str, errors: list[str]) -> tuple[str | None, bool]:
    frontmatter, body = parse_frontmatter(review_text)
    if frontmatter is not None:
        if frontmatter.get("review_type") != "proposal_review_seed":
            errors.append("proposal-review.md frontmatter review_type must be proposal_review_seed")
        if frontmatter.get("review_stage") != "pre_render":
            errors.append("proposal-review.md frontmatter review_stage must be pre_render")
        decision = frontmatter.get("proposal_review_decision")
        if decision not in REVIEW_DECISIONS:
            errors.append("proposal-review.md frontmatter proposal_review_decision must be pending, approved, or blocked")
            return None, True
        return decision, True

    match = re.search(r"(?im)^\s*(?:-\s*)?Decision:\s*(pending|approved|blocked)\s*$", body)
    if match:
        return match.group(1).lower(), False
    return None, False


def get_nested(data: dict[str, Any], path: tuple[str, ...]) -> Any:
    value: Any = data
    for key in path:
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


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


def check_proposal_review_seed(
    client_dir: Path,
    data: dict[str, Any],
    delivery_gate: bool,
    errors: list[str],
) -> tuple[str | None, str]:
    review_text = read_proposal_review(client_dir)
    if review_text is None:
        errors.append("proposal-review.md missing from client directory")
        return None, ""

    for heading in REQUIRED_REVIEW_HEADINGS:
        if f"## {heading}" not in review_text:
            errors.append(f"proposal-review.md missing heading: {heading}")

    decision, _has_frontmatter = extract_review_decision(review_text, errors)
    human_status = data.get("human_review_status")

    if decision is None:
        errors.append("proposal_review_decision missing from frontmatter and legacy body Decision fallback")
    elif decision == "blocked":
        errors.append("proposal_review_decision is blocked")
    elif decision == "pending" and human_status == "approved":
        errors.append("proposal_review_decision is pending while human_review_status is approved")
    elif delivery_gate and decision != "approved":
        errors.append("proposal_review_decision must be approved before delivery")

    return decision, review_text


def strategy_text_contains_confirmation_need(value: Any) -> bool:
    if not non_empty_string(value):
        return False
    text = value.strip()
    return "1순위" in text and ("확인" in text or "필요" in text)


def contains_svm_evidence(text: str) -> bool:
    return any(term in text for term in SVM_EVIDENCE_TERMS)


def has_svm_structured_evidence(data: dict[str, Any], review_text: str) -> bool:
    first_audience = get_nested(data, ("strategy_context", "smallest_viable_market", "first_audience"))
    if strategy_text_contains_confirmation_need(first_audience):
        return True

    handoff = data.get("department_handoff")
    if isinstance(handoff, dict):
        for department in handoff.values():
            if not isinstance(department, dict):
                continue
            for item in collect_department_field_text(department, "missing_inputs"):
                if contains_svm_evidence(item):
                    return True

    for item in string_items(data.get("assumptions")) + string_items(data.get("assumption_locks")):
        if contains_svm_evidence(item):
            return True

    return contains_svm_evidence(review_text) and ("확인" in review_text or "필요" in review_text)


def check_strategy_context_for_delivery(
    data: dict[str, Any],
    review_text: str,
    delivery_gate: bool,
    errors: list[str],
) -> None:
    if not delivery_gate:
        return

    strategy = data.get("strategy_context")
    if not isinstance(strategy, dict):
        errors.append("strategy_context missing from proposal-data.json")
        return

    for path in STRATEGY_REQUIRED_PATHS:
        value = get_nested(strategy, path)
        if not non_empty_string(value):
            errors.append(f"strategy_context.{'.'.join(path)} must be non-empty before delivery")

    svm_status = get_nested(strategy, ("smallest_viable_market", "svm_status"))
    if svm_status == "undefined":
        errors.append("strategy_context.smallest_viable_market.svm_status is undefined before delivery")
    elif svm_status == "broad" and not has_svm_structured_evidence(data, review_text):
        errors.append("strategy_context.svm_status is broad but no SVM assumption or missing input is documented")


def check_department_handoff(data: dict[str, Any], delivery_gate: bool, errors: list[str]) -> None:
    handoff = data.get("department_handoff")
    if not isinstance(handoff, dict):
        errors.append("department_handoff missing from proposal-data.json")
        return

    for key in DEPARTMENT_KEYS:
        if key not in handoff:
            errors.append(f"department_handoff.{key} missing")
            continue
        value = handoff.get(key)
        if is_structured_department(value):
            if delivery_gate and not has_minimum_analysis(value):
                errors.append(f"department_handoff.{key} must include diagnosis or recommendation before delivery")
            if delivery_gate and key == "risk_guard":
                if not has_any_field_text(value, ("risks", "recommendation")):
                    errors.append("department_handoff.risk_guard must include risks or recommendation before delivery")
                if not has_any_field_text(value, ("client_safe_phrase", "proposal_points")):
                    errors.append(
                        "department_handoff.risk_guard must include client_safe_phrase or proposal_points before delivery"
                    )
            if delivery_gate and key == "proposal_writer":
                if not has_any_field_text(value, ("recommendation",)):
                    errors.append("department_handoff.proposal_writer must include recommendation before delivery")
                if not has_any_field_text(value, ("proposal_points", "client_safe_phrase")):
                    errors.append(
                        "department_handoff.proposal_writer must include proposal_points or client_safe_phrase before delivery"
                    )
            if delivery_gate and key == "commercial_pricing":
                if not has_any_field_text(value, ("price_impact",)):
                    errors.append("department_handoff.commercial_pricing must include price_impact before delivery")
                if not has_any_field_text(value, ("risks", "client_safe_phrase")):
                    errors.append(
                        "department_handoff.commercial_pricing must include risks or client_safe_phrase before delivery"
                    )
        elif not isinstance(value, list):
            errors.append(f"department_handoff.{key} must be a legacy list or structured object")


def check_request_lock(data: dict[str, Any], html_text: str, delivery_gate: bool, errors: list[str]) -> None:
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
    if isinstance(handoff, dict):
        risk_guard = collect_department_text(handoff.get("risk_guard"))
    else:
        risk_guard = []
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

    delivery_gate = not args.allow_pending

    _review_decision, review_text = check_proposal_review_seed(client_dir, data, delivery_gate, errors)
    check_strategy_context_for_delivery(data, review_text, delivery_gate, errors)
    check_request_lock(data, html_text, delivery_gate, errors)
    check_department_handoff(data, delivery_gate, errors)
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
