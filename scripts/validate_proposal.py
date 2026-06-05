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
REQUEST_LOCK_STATUSES = {"open", "partial", "locked"}
SVM_STATUSES = {"undefined", "broad", "narrow_but_not_viable", "viable", "locked"}
PRICING_MODELS = {"starting_price", "package", "page_based", "project_based", "retainer", "cost_plus"}
TIERS = {"basic", "standard", "premium", "custom"}
ROUND_KEYS = ("planning", "copy", "design", "development", "final_check")
UNKNOWN_KEYS = ("harmless_unknown", "proposal_blocking_unknown", "price_affecting_unknown", "risk_unknown")
STRATEGY_DESIRED_CHANGE_KEYS = ("raw_request", "current_state", "target_state", "tension", "change_type", "required_asset")
STRATEGY_SVM_KEYS = ("svm_status", "first_audience", "worldview", "exclusion", "viability_signal", "founder_market_fit")
STRATEGY_TRUST_KEYS = (
    "warm_pistachio_signal",
    "strategic_no_signal",
    "judgment_benchmark",
    "status_shift_narrative",
    "dip_response",
)
HANDOFF_KEYS = (
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


def non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def non_empty_string_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(non_empty_string(item) for item in value)


def string_list(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value)


def validate_strategy_context(data: dict[str, Any], errors: list[str]) -> None:
    context = data.get("strategy_context")
    if not isinstance(context, dict):
        errors.append("strategy_context must be an object")
        return

    desired = context.get("desired_change")
    if not isinstance(desired, dict):
        errors.append("strategy_context.desired_change must be an object")
    else:
        for key in STRATEGY_DESIRED_CHANGE_KEYS:
            if key not in desired:
                errors.append(f"strategy_context.desired_change.{key} missing")
            elif not isinstance(desired.get(key), str):
                errors.append(f"strategy_context.desired_change.{key} must be a string")

    svm = context.get("smallest_viable_market")
    if not isinstance(svm, dict):
        errors.append("strategy_context.smallest_viable_market must be an object")
    else:
        for key in STRATEGY_SVM_KEYS:
            if key not in svm:
                errors.append(f"strategy_context.smallest_viable_market.{key} missing")
            elif not isinstance(svm.get(key), str):
                errors.append(f"strategy_context.smallest_viable_market.{key} must be a string")
        if isinstance(svm.get("svm_status"), str) and svm.get("svm_status") not in SVM_STATUSES:
            errors.append(f"strategy_context.smallest_viable_market.svm_status must be one of: {', '.join(sorted(SVM_STATUSES))}")

    trust = context.get("trust_indicators")
    if not isinstance(trust, dict):
        errors.append("strategy_context.trust_indicators must be an object")
    else:
        for key in STRATEGY_TRUST_KEYS:
            if key not in trust:
                errors.append(f"strategy_context.trust_indicators.{key} missing")
            elif not isinstance(trust.get(key), str):
                errors.append(f"strategy_context.trust_indicators.{key} must be a string")


def validate_department_value(value: Any, label: str, errors: list[str]) -> None:
    if string_list(value):
        return
    if not isinstance(value, dict):
        errors.append(f"{label} must be a legacy string list or structured object")
        return
    for field in DEPARTMENT_FIELDS:
        if field not in value:
            errors.append(f"{label}.{field} missing")
        elif not string_list(value.get(field)):
            errors.append(f"{label}.{field} must be a string list")


def validate_lock_contract(data: dict[str, Any], errors: list[str]) -> None:
    if data.get("request_lock_status") not in REQUEST_LOCK_STATUSES:
        errors.append(f"request_lock_status must be one of: {', '.join(sorted(REQUEST_LOCK_STATUSES))}")

    for key in ("hard_locks", "assumption_locks"):
        if not string_list(data.get(key)):
            errors.append(f"{key} must be a string list")

    unknowns = data.get("remaining_unknowns")
    if not isinstance(unknowns, dict):
        errors.append("remaining_unknowns must be an object")
    else:
        for key in UNKNOWN_KEYS:
            if key not in unknowns:
                errors.append(f"remaining_unknowns.{key} missing")
            elif not string_list(unknowns.get(key)):
                errors.append(f"remaining_unknowns.{key} must be a string list")

    handoff = data.get("department_handoff")
    if not isinstance(handoff, dict):
        errors.append("department_handoff must be an object")
    else:
        for key in HANDOFF_KEYS:
            if key not in handoff:
                errors.append(f"department_handoff.{key} missing")
            else:
                validate_department_value(handoff.get(key), f"department_handoff.{key}", errors)


def validate_commercial_terms(data: dict[str, Any], errors: list[str]) -> None:
    terms = data.get("commercial_terms")
    if not isinstance(terms, dict):
        errors.append("commercial_terms must be an object")
        return

    if not non_empty_string(terms.get("payment_terms")):
        errors.append("commercial_terms.payment_terms must be non-empty")
    if not non_empty_string(terms.get("final_estimate_notice")):
        errors.append("commercial_terms.final_estimate_notice must be non-empty")
    if not non_empty_string(terms.get("delivery_condition")):
        errors.append("commercial_terms.delivery_condition must be non-empty")
    if not isinstance(terms.get("file_retention_days"), int) or terms["file_retention_days"] < 0:
        errors.append("commercial_terms.file_retention_days must be a non-negative integer")
    if not isinstance(terms.get("minor_fix_days"), int) or terms["minor_fix_days"] < 0:
        errors.append("commercial_terms.minor_fix_days must be a non-negative integer")
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


def validate_pricing_items(data: dict[str, Any], errors: list[str]) -> None:
    items = data.get("pricing_items")
    if not isinstance(items, list) or not items:
        errors.append("pricing_items must be a non-empty list")
        return

    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"pricing_items[{index}] must be an object")
            continue
        for key in ("service_id", "service_name", "public_starting_price", "minimum_project_fee"):
            if not non_empty_string(item.get(key)):
                errors.append(f"pricing_items[{index}].{key} must be non-empty")
        if item.get("pricing_model") not in PRICING_MODELS:
            errors.append(f"pricing_items[{index}].pricing_model must be one of: {', '.join(sorted(PRICING_MODELS))}")
        if item.get("tier") not in TIERS:
            errors.append(f"pricing_items[{index}].tier must be one of: {', '.join(sorted(TIERS))}")

        band = item.get("internal_price_band")
        if not isinstance(band, dict):
            errors.append(f"pricing_items[{index}].internal_price_band must be an object")
        else:
            for key in ("min", "standard", "premium", "basis"):
                if not non_empty_string(band.get(key)):
                    errors.append(f"pricing_items[{index}].internal_price_band.{key} must be non-empty")

        rounds = item.get("included_rounds")
        if not isinstance(rounds, dict):
            errors.append(f"pricing_items[{index}].included_rounds must be an object")
        else:
            for key in ROUND_KEYS:
                value = rounds.get(key)
                if not isinstance(value, int) or value < 0:
                    errors.append(f"pricing_items[{index}].included_rounds.{key} must be a non-negative integer")

        if not non_empty_string_list(item.get("extra_cost_triggers")):
            errors.append(f"pricing_items[{index}].extra_cost_triggers must be a non-empty string list")


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
    validate_strategy_context(data, errors)
    validate_lock_contract(data, errors)
    if not non_empty_string_list(data.get("confirmed_facts")):
        errors.append("confirmed_facts must be a non-empty string list")
    if not non_empty_string_list(data.get("assumptions")):
        errors.append("assumptions must be a non-empty string list")

    validate_commercial_terms(data, errors)
    validate_pricing_items(data, errors)
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
