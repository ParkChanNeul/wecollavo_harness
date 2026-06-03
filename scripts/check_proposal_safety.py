#!/usr/bin/env python3
"""Check whether a rendered proposal is safe for customer delivery."""

from __future__ import annotations

import argparse
import json
import sys
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
]

REQUIRED_HTML_PHRASES = [
    "선결제 100%",
    "피드백 1회",
    "피드백 2회",
    "최종 견적",
    "자료 확인 후 확정",
]


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"JSON parse failed: {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"Expected object: {path}")
    return data


def collect_text(value: Any) -> str:
    if isinstance(value, dict):
        return "\n".join(collect_text(item) for item in value.values())
    if isinstance(value, list):
        return "\n".join(collect_text(item) for item in value)
    if isinstance(value, str):
        return value
    return ""


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
    errors: list[str] = []

    status = data.get("human_review_status")
    if status == "blocked":
        errors.append("human_review_status is blocked")
    elif status == "pending" and not args.allow_pending:
        errors.append("human_review_status is pending; pass --allow-pending only for internal draft checks")
    elif status != "approved" and not (status == "pending" and args.allow_pending):
        errors.append("human_review_status must be approved before delivery")

    for phrase in BLOCKED_PHRASES:
        if phrase in html:
            errors.append(f"blocked phrase found in HTML: {phrase}")

    for phrase in REQUIRED_HTML_PHRASES:
        if phrase not in html:
            errors.append(f"required safety phrase missing from HTML: {phrase}")

    terms = data.get("commercial_terms")
    if not isinstance(terms, dict):
        errors.append("commercial_terms missing from proposal-data.json")
    else:
        for key in ("payment_terms", "revision_policy", "additional_terms", "final_estimate_notice"):
            if key not in terms:
                errors.append(f"commercial_terms.{key} missing")

    data_text = collect_text(data)
    if "무제한 수정" in data_text:
        errors.append("proposal-data.json contains unlimited revision language")
    if "확정 견적서입니다" in data_text:
        errors.append("proposal-data.json presents the proposal as a confirmed estimate")

    if errors:
        print("proposal safety check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"proposal safety check ok: {client_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
