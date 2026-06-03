#!/usr/bin/env python3
"""Render proposal.html from client.json and proposal-data.json."""

from __future__ import annotations

import json
import sys
from html import escape
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"JSON parse failed: {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"Expected object: {path}")
    return data


def as_text(value: Any, default: str = "") -> str:
    return value if isinstance(value, str) and value.strip() else default


def paragraph_list(items: Any) -> str:
    if not isinstance(items, list):
        return ""
    return "\n".join(f"          <p>{escape(item)}</p>" for item in items if isinstance(item, str) and item.strip())


def bullet_list(items: Any) -> str:
    if not isinstance(items, list):
        return ""
    rows = [f"            <li>{escape(item)}</li>" for item in items if isinstance(item, str) and item.strip()]
    return "          <ul>\n" + "\n".join(rows) + "\n          </ul>" if rows else ""


def data_table(rows: Any) -> str:
    if not isinstance(rows, list) or not rows:
        return ""
    keys: list[str] = []
    for row in rows:
        if isinstance(row, dict):
            for key in row:
                if key not in keys:
                    keys.append(key)
    if not keys:
        return ""
    labels = {
        "item": "구분",
        "basis": "기준",
        "amount": "금액",
    }
    header = "".join(f"<th>{escape(labels.get(key, key))}</th>" for key in keys)
    body_rows = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        cells = "".join(f"<td>{escape(str(row.get(key, '')))}</td>" for key in keys)
        body_rows.append(f"            <tr>{cells}</tr>")
    return (
        "          <table>\n"
        f"            <thead><tr>{header}</tr></thead>\n"
        "            <tbody>\n"
        + "\n".join(body_rows)
        + "\n            </tbody>\n"
        "          </table>"
    )


def commercial_terms_block(terms: dict[str, Any]) -> str:
    revisions = terms.get("revision_policy")
    revision_rows = []
    if isinstance(revisions, list):
        for item in revisions:
            if not isinstance(item, dict):
                continue
            revision_rows.append(
                "            <tr>"
                f"<td>{escape(as_text(item.get('asset')))}</td>"
                f"<td>{escape(str(item.get('feedback_rounds', '')))}회</td>"
                f"<td>{escape(as_text(item.get('description')))}</td>"
                "</tr>"
            )

    revision_table = ""
    if revision_rows:
        revision_table = (
            "          <table>\n"
            "            <thead><tr><th>자산</th><th>포함 피드백</th><th>기준</th></tr></thead>\n"
            "            <tbody>\n"
            + "\n".join(revision_rows)
            + "\n            </tbody>\n"
            "          </table>"
        )

    return (
        '          <div class="terms">\n'
        "            <h3>결제 및 피드백 기준</h3>\n"
        f"            <p><strong>결제 조건:</strong> {escape(as_text(terms.get('payment_terms')))}</p>\n"
        f"{revision_table}\n"
        "            <h3>추가 협의 조건</h3>\n"
        f"{bullet_list(terms.get('additional_terms'))}\n"
        f"            <p class=\"notice-inline\">{escape(as_text(terms.get('final_estimate_notice')))}</p>\n"
        "          </div>"
    )


def render_section(index: int, section: dict[str, Any], terms: dict[str, Any]) -> str:
    section_id = as_text(section.get("id"), f"section-{index}")
    title = as_text(section.get("title"), f"Section {index}")
    body = paragraph_list(section.get("body"))
    table = data_table(section.get("table"))
    terms_html = commercial_terms_block(terms) if section_id == "price-breakdown" else ""
    return f"""      <section class="slide" id="{escape(section_id)}">
        <div class="slide-count">{index:02d}</div>
        <div class="slide-content">
          <h2>{escape(title)}</h2>
{body}
{table}
{terms_html}
        </div>
      </section>"""


def load_theme(root: Path, client: dict[str, Any]) -> dict[str, Any]:
    fallback = load_json(root / "harness" / "templates" / "theme.json")
    theme = client.get("theme") if isinstance(client.get("theme"), dict) else {}
    colors = theme.get("colors") if isinstance(theme.get("colors"), dict) else {}
    fallback_colors = fallback.get("colors", {})
    typography = theme.get("typography") if isinstance(theme.get("typography"), dict) else {}
    fallback_typography = fallback.get("typography", {})
    return {
        "brand_name": as_text(theme.get("brand_name"), as_text(fallback.get("brand_name"), "WeCollavo Proposal")),
        "colors": {
            "background": as_text(colors.get("background"), as_text(fallback_colors.get("background"), "#ffffff")),
            "text": as_text(colors.get("text"), as_text(fallback_colors.get("text"), "#171717")),
            "accent": as_text(colors.get("accent"), as_text(fallback_colors.get("accent"), "#1f5eff")),
            "muted": as_text(colors.get("muted"), as_text(fallback_colors.get("muted"), "#f4f6f8")),
        },
        "typography": {
            "font_family": as_text(
                typography.get("font_family"),
                as_text(fallback_typography.get("font_family"), "system-ui, sans-serif"),
            )
        },
    }


def render(client_dir: Path) -> str:
    root = Path(__file__).resolve().parents[1]
    client = load_json(client_dir / "client.json")
    proposal = load_json(client_dir / "proposal-data.json")
    theme = load_theme(root, client)
    colors = theme["colors"]
    terms = proposal.get("commercial_terms") if isinstance(proposal.get("commercial_terms"), dict) else {}
    sections = proposal.get("sections") if isinstance(proposal.get("sections"), list) else []
    rendered_sections = "\n".join(
        render_section(index, section, terms)
        for index, section in enumerate(sections, start=1)
        if isinstance(section, dict)
    )

    title = as_text(proposal.get("proposal_title"), "WeCollavo Proposal")
    client_name = as_text(client.get("client_name"), as_text(proposal.get("client_id"), "Client"))
    pricing_note = as_text(
        terms.get("final_estimate_notice"),
        as_text(proposal.get("pricing_note"), "본 제안은 1차 제안이며 최종 견적은 자료 확인 후 확정됩니다."),
    )

    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <style>
    :root {{
      --bg: {escape(colors["background"])};
      --text: {escape(colors["text"])};
      --accent: {escape(colors["accent"])};
      --muted: {escape(colors["muted"])};
      --line: color-mix(in srgb, var(--text) 18%, transparent);
      --soft: color-mix(in srgb, var(--muted) 55%, white);
      --font: {escape(theme["typography"]["font_family"])};
    }}
    * {{ box-sizing: border-box; }}
    html, body {{ margin: 0; min-height: 100%; background: var(--bg); color: var(--text); font-family: var(--font); }}
    body {{ overflow: hidden; }}
    .deck {{ display: flex; width: 100vw; height: 100vh; overflow-x: auto; overflow-y: hidden; scroll-snap-type: x mandatory; scroll-behavior: smooth; }}
    .slide {{ position: relative; flex: 0 0 100vw; height: 100vh; padding: 56px clamp(24px, 6vw, 88px); scroll-snap-align: start; display: flex; align-items: center; border-right: 1px solid var(--line); }}
    .cover {{ background: linear-gradient(135deg, var(--muted), var(--bg) 52%); }}
    .slide-content {{ width: min(980px, 100%); max-height: calc(100vh - 112px); overflow: auto; }}
    .slide-count {{ position: absolute; top: 28px; right: clamp(24px, 6vw, 88px); color: var(--accent); font-weight: 800; letter-spacing: .08em; }}
    .eyebrow {{ color: var(--accent); font-size: 14px; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; }}
    h1 {{ max-width: 920px; margin: 12px 0 18px; font-size: clamp(36px, 6vw, 72px); line-height: 1.05; letter-spacing: 0; }}
    h2 {{ max-width: 860px; margin: 0 0 22px; font-size: clamp(30px, 4.5vw, 56px); line-height: 1.12; letter-spacing: 0; }}
    h3 {{ margin: 22px 0 8px; font-size: 18px; }}
    p, li, td, th {{ font-size: 18px; line-height: 1.7; }}
    p {{ max-width: 860px; margin: 0 0 14px; }}
    ul, ol {{ max-width: 860px; margin: 12px 0 0; padding-left: 22px; }}
    li {{ margin: 8px 0; }}
    table {{ width: min(920px, 100%); border-collapse: collapse; margin: 18px 0; background: white; }}
    th, td {{ border: 1px solid var(--line); padding: 12px 14px; text-align: left; vertical-align: top; }}
    th {{ background: var(--muted); color: var(--text); }}
    .notice {{ max-width: 860px; margin-top: 22px; padding: 16px 18px; background: white; border-left: 5px solid var(--accent); font-weight: 700; }}
    .notice-inline {{ margin-top: 18px; padding: 14px 16px; background: var(--muted); border-left: 4px solid var(--accent); font-weight: 700; }}
    .terms {{ margin-top: 22px; padding-top: 8px; border-top: 2px solid var(--line); }}
    .hint {{ position: fixed; left: 24px; bottom: 18px; font-size: 13px; color: color-mix(in srgb, var(--text) 62%, transparent); }}
    @media (max-width: 760px) {{
      body {{ overflow: auto; }}
      .deck {{ display: block; height: auto; overflow: visible; }}
      .slide {{ min-height: 100vh; height: auto; padding: 42px 20px 64px; }}
      .slide-content {{ max-height: none; overflow: visible; }}
      .hint {{ display: none; }}
    }}
  </style>
</head>
<body>
  <main class="deck" aria-label="{escape(title)}">
    <section class="slide cover" id="cover">
      <div class="slide-content">
        <div class="eyebrow">WeCollavo Live Execution Harness</div>
        <h1>{escape(title)}</h1>
        <p>{escape(client_name)}에게 맞춘 현장 진단 기반 1차 제안입니다.</p>
        <p class="notice">{escape(pricing_note)}</p>
      </div>
    </section>
{rendered_sections}
  </main>
  <div class="hint">가로로 스크롤해 브리핑을 넘겨볼 수 있습니다.</div>
</body>
</html>
"""


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: render_proposal.py clients/<client>", file=sys.stderr)
        return 2
    client_dir = Path(sys.argv[1])
    if not client_dir.is_dir():
        print(f"client directory not found: {client_dir}", file=sys.stderr)
        return 1
    html = render(client_dir)
    output = client_dir / "proposal.html"
    output.write_text(html, encoding="utf-8")
    print(f"rendered proposal: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
