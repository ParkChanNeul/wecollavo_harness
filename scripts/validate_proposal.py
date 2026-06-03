#!/usr/bin/env python3
"""Validate the WeCollavo proposal-data.json contract."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


EXPECTED_SECTION_IDS = [
    "today-conclusion",
    "why-this-conclusion",
    "meeting-qa",
    "situation-diagnosis",
    "priority-decision",
    "first-scope",
    "price-breakdown",
    "extra-cost",
    "materials-needed",
    "thirty-day-plan",
    "next-production-proposal",
]

PRICING_STATUSES = {"field_diagnostic_proposal", "first_written_proposal", "final_estimate"}
HUMAN_REVIEW_STATUSES = {"pending", "approved", "blocked"}


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"JSON parse failed: {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"Expected object: {path}")
    return data


def non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def non_empty_string_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(non_empty_string(item) for item in value)


def validate_commercial_terms(data: dict[str, Any], errors: list[str]) -> None:
    terms = data.get("commercial_terms")
    if not isinstance(terms, dict):
        errors.append("commercial_terms must be an object")
        return

    if not non_empty_string(terms.get("payment_terms")):
        errors.append("commercial_terms.payment_terms must be non-empty")
    if not non_empty_string(terms.get("final_estimate_notice")):
        errors.append("commercial_terms.final_estimate_notice must be non-empty")
    if not non_empty_string_list(terms.get("additional_terms")):
        errors.append("commercial_terms.additional_terms must be a non-empty string list")

    revisions = terms.get("revision_policy")
    if not isinstance(revisions, list) or not revisions:
        errors.append("commercial_terms.revision_policy must be a non-empty list")
        return
    for index, item in enumerate(revisions):
        if not isinstance(item, dict):
            errors.append(f"commercial_terms.revision_policy[{index}] must be an object")
            continue
        if not non_empty_string(item.get("asset")):
            errors.append(f"commercial_terms.revision_policy[{index}].asset must be non-empty")
        rounds = item.get("feedback_rounds")
        if not isinstance(rounds, int) or rounds < 0:
            errors.append(f"commercial_terms.revision_policy[{index}].feedback_rounds must be a non-negative integer")
        if not non_empty_string(item.get("description")):
            errors.append(f"commercial_terms.revision_policy[{index}].description must be non-empty")


def validate_sections(data: dict[str, Any], errors: list[str]) -> None:
    sections = data.get("sections")
    if not isinstance(sections, list):
        errors.append("sections must be a list")
        return
    if len(sections) != len(EXPECTED_SECTION_IDS):
        errors.append(f"sections must contain exactly {len(EXPECTED_SECTION_IDS)} items")

    seen_ids: list[str] = []
    for index, section in enumerate(sections):
        if not isinstance(section, dict):
            errors.append(f"sections[{index}] must be an object")
            continue
        section_id = section.get("id")
        seen_ids.append(section_id if isinstance(section_id, str) else "")
        if not non_empty_string(section_id):
            errors.append(f"sections[{index}].id must be non-empty")
        if not non_empty_string(section.get("title")):
            errors.append(f"sections[{index}].title must be non-empty")
        body = section.get("body")
        if not isinstance(body, list) or not all(isinstance(item, str) for item in body):
            errors.append(f"sections[{index}].body must be a string list")

    if seen_ids != EXPECTED_SECTION_IDS:
        errors.append(f"section ids must match expected order: {', '.join(EXPECTED_SECTION_IDS)}")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_proposal.py path/to/proposal-data.json", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    data = load_json(path)
    errors: list[str] = []

    for key in ("client_id", "proposal_title", "track", "pricing_note"):
        if not non_empty_string(data.get(key)):
            errors.append(f"{key} must be non-empty")

    if data.get("pricing_status") not in PRICING_STATUSES:
        errors.append(f"pricing_status must be one of: {', '.join(sorted(PRICING_STATUSES))}")
    if data.get("human_review_status") not in HUMAN_REVIEW_STATUSES:
        errors.append(f"human_review_status must be one of: {', '.join(sorted(HUMAN_REVIEW_STATUSES))}")
    if not non_empty_string_list(data.get("confirmed_facts")):
        errors.append("confirmed_facts must be a non-empty string list")
    if not non_empty_string_list(data.get("assumptions")):
        errors.append("assumptions must be a non-empty string list")

    validate_commercial_terms(data, errors)
    validate_sections(data, errors)

    if errors:
        print("proposal validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"proposal validation ok: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
