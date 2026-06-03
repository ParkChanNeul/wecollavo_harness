#!/usr/bin/env python3
"""Validate a WeCollavo client.json file using stdlib-only checks."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


HEX_COLOR = re.compile(r"^#[0-9a-fA-F]{6}$")


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"JSON parse failed: {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"Expected object: {path}")
    return data


def require_string(data: dict[str, Any], key: str, errors: list[str]) -> None:
    if not isinstance(data.get(key), str) or not data[key].strip():
        errors.append(f"missing non-empty string: {key}")


def require_string_list(data: dict[str, Any], key: str, errors: list[str]) -> None:
    value = data.get(key)
    if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
        errors.append(f"missing non-empty string list: {key}")


def validate_theme(data: dict[str, Any], errors: list[str]) -> None:
    theme = data.get("theme")
    if not isinstance(theme, dict):
        errors.append("missing object: theme")
        return
    colors = theme.get("colors")
    if not isinstance(colors, dict):
        errors.append("missing object: theme.colors")
        return
    for key in ("background", "text", "accent", "muted"):
        value = colors.get(key)
        if not isinstance(value, str) or not HEX_COLOR.match(value):
            errors.append(f"theme.colors.{key} must be #RRGGBB")


def validate_source_materials(data: dict[str, Any], errors: list[str]) -> None:
    materials = data.get("source_materials")
    if not isinstance(materials, list) or not materials:
        errors.append("missing non-empty list: source_materials")
        return
    for index, item in enumerate(materials):
        if not isinstance(item, dict):
            errors.append(f"source_materials[{index}] must be an object")
            continue
        for key in ("path", "purpose"):
            value = item.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"source_materials[{index}].{key} must be non-empty")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_client.py path/to/client.json", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    data = load_json(path)
    errors: list[str] = []

    for key in ("client_id", "client_name", "primary_contact"):
        require_string(data, key, errors)
    for key in ("industry", "decision_makers"):
        require_string_list(data, key, errors)
    validate_source_materials(data, errors)
    validate_theme(data, errors)

    if errors:
        print("client validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"client validation ok: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
