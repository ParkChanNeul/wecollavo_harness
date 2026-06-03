---
name: wecollavo-html-proposal
description: Use when creating or revising a WeCollavo customer-facing HTML diagnosis/proposal presentation from meeting answers, diagnosis, scope, pricing, and rationale.
---

# WeCollavo HTML Proposal

Use this skill to produce `client-presentation.html`.

Read:
- `docs/source-of-truth.md`
- `docs/tracks.md`
- `docs/live-cockpit.md`
- `docs/workflow.md`
- `docs/decision-tools.md`
- `docs/estimate-template.md` when pricing Track 1 work
- the client workspace under `harness/workspaces/<client-slug>/`
- any relevant client documents under `project/<client-slug>/`

## Presentation Rules

The HTML must be understandable to a representative or owner with little
marketing knowledge.

Put the conclusion first. Then explain why that conclusion was reached. Pricing
must be detailed enough to show scope, risk, and fairness.

Required sections:

1. 오늘의 결론
2. 왜 이런 결론이 나왔는가
3. 미팅 질문과 답변
4. 고객 상황 진단
5. 우선순위
6. 1차 착수 범위
7. 가격 분해표
8. 추가비 발생 조건
9. 필요한 자료
10. 30일 실행 계획
11. 본 제작 제안

## Writing Rules

- Use plain Korean.
- Avoid generic agency language.
- Mark assumptions clearly.
- Do not invent numbers, materials, achievements, or public claims.
- Avoid "무제한", "보장", "완벽" unless directly constrained.
- Make additional-fee conditions visible, not hidden.

## HTML Rules

Use `harness/templates/client-presentation.html` as the structure. Keep it
self-contained with inline CSS unless the user asks for a framework.

The HTML should be usable as:
- a browser presentation
- a PDF/capture source
- a HyperFrames video source
- a client-safe written proposal
