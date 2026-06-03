---
name: wecollavo-proposal-harness
description: Use after a WeCollavo Live Cockpit session or client meeting notes need to become structured workspace artifacts, diagnosis, scope, pricing rationale, and a customer-ready HTML proposal presentation.
---

# WeCollavo Proposal Harness

Use this skill to run the downstream WeCollavo meeting-to-proposal pipeline.
For live meeting judgment, use `$wecollavo-live-cockpit` first.

## Grounding

Read these general documents first:
- `docs/source-of-truth.md`
- `docs/tracks.md`
- `docs/live-cockpit.md`
- `docs/workflow.md`
- `docs/harness.md`
- `docs/decision-tools.md`

Use `docs/estimate-template.md` when pricing Track 1 work. Use
`docs/archive-prd-v1.md` only when historical rationale is needed.

Check the relevant client folder under `project/` and the active workspace under
`harness/workspaces/`.

## Boundary

The Harness supports WeCollavo judgment. It does not replace it.

Do not:
- present AI output as the final estimate
- auto-send client documents
- promise unlimited revisions
- hide assumptions behind confident wording
- spawn subagents unless the user explicitly asks for parallel agents
- expose "Harness" as a client-facing product name

## Workflow

1. **Live Cockpit Inputs**
   - If available, read `live-meeting.md`, `ai-backchannel.md`, and
     `proposal-snapshot.md` first.
   - Treat field pricing as provisional until Human Linchpin Review.

2. **Client Snapshot**
   - Create or update `harness/workspaces/<client-slug>/client-snapshot.md`.
   - Separate confirmed facts, assumptions, constraints, materials, budget
     signals, schedule signals, and decision maker context.

3. **Preview Questions**
   - Create or update `preview-questions.md`.
   - Include discovery questions, decision questions, and follow-up/risk
     questions.
   - Questions must help determine conclusion, scope, price, additional-fee
     conditions, and required client materials.

4. **Answer Capture**
   - Create or update `answers.md` from meeting notes.
   - Mark each answer as confirmed, unclear, missing, or needs follow-up.

5. **Diagnosis**
   - Create or update `diagnosis.md`.
   - State the real bottleneck, what the client thinks they need, what
     WeCollavo believes should happen first, and why.

6. **Scope And Pricing**
   - Create or update `scope-pricing.md`.
   - Include first-phase scope, excluded scope, price decomposition,
     additional-fee triggers, schedule assumptions, and client dependencies.

7. **HTML Presentation**
   - Render or update `client-presentation.html` using
     `harness/templates/client-presentation.html`.
   - Required sections:
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

8. **Human Linchpin Review**
   - Run `harness/checklists/human-linchpin-review.md`.
   - Final judgment, price, public wording, delivery promise, and payment terms
     must be reviewed by the human operator.

9. **Optional HyperFrames**
   - Only after the HTML presentation is approved, prepare it as source material
     for a HyperFrames video.

## Subagent Use

Subagents are useful for parallel read-heavy review only when the user asks for
parallel agents.

Recommended Codex custom agents:
- `client-context-analyst`
- `scope-pricing-architect`
- `proposal-storyboarder`
- `risk-proof-loop-reviewer`

Wait for all agent summaries, then consolidate. Do not let subagents directly
edit the same output file in parallel.
