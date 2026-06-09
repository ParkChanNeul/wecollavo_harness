---
name: Korean Connection
name_ko: 코리안 커넥션
description: Use for Korean Connection lesson plans, classroom-ready student decks, HTML slides, image prompts, PDF export, and quality checks.
description_ko: 한국 문화 기반 수업 기획, 학생용 미션형 덱, HTML 슬라이드, 이미지 프롬프트, PDF 내보내기, 품질 검수에 사용한다.
canonical_skill: skills/korean_connection_lesson_builder/SKILL.md
---

# Korean Connection

Thin Codex UI entrypoint.

Use this skill when the user wants Korean Connection lesson materials.

The canonical generator lives at:

- `skills/korean_connection_lesson_builder/SKILL.md`

## Routes

| Request | Route |
|---|---|
| lesson plan / 교사용 레슨 기획 | `lesson_plan` |
| student deck / 학생용 미션형 덱 | `student_deck` |
| HTML slides / HTML 슬라이드 | `html_slides` |
| image prompts / 이미지 프롬프트 | `image_prompts` |
| PDF export / PDF 내보내기 | `pdf_export` |
| quality check / 품질 검수 | `quality_checklist` |

## Required Behavior

Read the canonical generator before producing outputs.

Do not duplicate the canonical skill here.

Generate classroom-ready materials, not skeleton outlines.

Generated lesson outputs must go under:

- `lessons/active/`

## Do Not

- Do not create a new harness.
- Do not create `COMMANDS.md`.
- Do not create `skill_invocation_contract.md`.
- Do not put generated lesson outputs under `curriculum/`.
- Do not commit or push unless the user explicitly asks.
