#!/usr/bin/env python3
"""Check language-contract boundaries without changing repo files."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LANGUAGE_CONTRACT = "docs/language-contract.md"
LANGUAGE_CONTRACT_BASENAME = "language-contract.md"
HANGUL = re.compile(r"[가-힣]")

REFERENCE_PATHS = [
    ROOT / "AGENTS.md",
    ROOT / "docs" / "README.md",
]

JSON_CONTRACT_ROOTS = [
    ROOT / "harness" / "schemas",
    ROOT / "harness" / "templates",
    ROOT / "clients" / "_template",
]

REQUIRED_PROPOSAL_FIELDS = [
    "client_id",
    "proposal_title",
    "pricing_status",
    "human_review_status",
    "request_lock_status",
    "confirmed_facts",
    "assumptions",
    "hard_locks",
    "assumption_locks",
    "remaining_unknowns",
    "department_handoff",
    "pricing_items",
    "commercial_terms",
    "sections",
]

AGENT_FIELD_ORDER = [
    "domain",
    "confidence",
    "diagnosis",
    "ask_next",
    "recommendation",
    "scope",
    "risks",
    "price_impact",
    "client_safe_phrase",
    "internal_note",
]

INTERNAL_HTML_PHRASES = [
    "internal_note",
    "AI 백채널",
    "내부 메모",
    "Human Linchpin Review",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def iter_skill_files() -> list[Path]:
    return sorted((ROOT / ".agents" / "skills").glob("*/SKILL.md"))


def iter_agent_files() -> list[Path]:
    return sorted((ROOT / ".codex" / "agents").glob("*.toml"))


def iter_json_contract_files() -> list[Path]:
    files: list[Path] = []
    for root in JSON_CONTRACT_ROOTS:
        if root.exists():
            files.extend(sorted(root.rglob("*.json")))
    return files


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def collect_json_key_errors(value: Any, path: Path, key_path: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            next_path = f"{key_path}.{key}" if key_path else key
            if HANGUL.search(key):
                errors.append(f"{relative(path)} has Korean JSON key: {next_path}")
            collect_json_key_errors(child, path, next_path, errors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            collect_json_key_errors(child, path, f"{key_path}[{index}]", errors)


def check_language_contract_references(errors: list[str]) -> None:
    for path in REFERENCE_PATHS + iter_skill_files() + iter_agent_files():
        if not path.exists():
            errors.append(f"missing reference file: {relative(path)}")
            continue
        text = read_text(path)
        if LANGUAGE_CONTRACT not in text and LANGUAGE_CONTRACT_BASENAME not in text:
            errors.append(f"{relative(path)} must reference {LANGUAGE_CONTRACT}")


def check_json_contract_keys(errors: list[str]) -> None:
    for path in iter_json_contract_files():
        try:
            data = json.loads(read_text(path))
        except json.JSONDecodeError as exc:
            errors.append(f"{relative(path)} JSON parse failed: {exc}")
            continue
        collect_json_key_errors(data, path, "", errors)


def check_required_proposal_fields(errors: list[str]) -> None:
    paths = [
        ROOT / "harness" / "schemas" / "proposal.schema.json",
        ROOT / "harness" / "templates" / "proposal-data.json",
        ROOT / "clients" / "_template" / "proposal-data.json",
    ]
    for path in paths:
        if not path.exists():
            errors.append(f"missing proposal contract file: {relative(path)}")
            continue
        text = read_text(path)
        for field in REQUIRED_PROPOSAL_FIELDS:
            if field not in text:
                errors.append(f"{relative(path)} missing explicit contract field: {field}")


def check_agent_output_contract(errors: list[str]) -> None:
    for path in iter_agent_files():
        text = read_text(path)
        cursor = -1
        for field in AGENT_FIELD_ORDER:
            marker = f"{field}:"
            index = text.find(marker)
            if index == -1:
                errors.append(f"{relative(path)} missing agent output field: {marker}")
                continue
            if index < cursor:
                errors.append(f"{relative(path)} agent output field is out of order: {marker}")
            cursor = index


def check_customer_html_exposure(errors: list[str]) -> None:
    clients_root = ROOT / "clients"
    if not clients_root.exists():
        return
    for path in sorted(clients_root.glob("*/proposal.html")):
        text = read_text(path)
        for phrase in INTERNAL_HTML_PHRASES:
            if phrase in text:
                errors.append(f"{relative(path)} exposes internal phrase: {phrase}")


def main() -> int:
    errors: list[str] = []

    if not (ROOT / LANGUAGE_CONTRACT).exists():
        errors.append(f"missing {LANGUAGE_CONTRACT}")

    check_language_contract_references(errors)
    check_json_contract_keys(errors)
    check_required_proposal_fields(errors)
    check_agent_output_contract(errors)
    check_customer_html_exposure(errors)

    if errors:
        print("language consistency check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("language consistency check ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
