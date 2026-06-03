# WeCollavo Workflow

Status: Current operating flow
Source: docs/live-cockpit.md, AGENTS.md, harness/README.md, and .agents/skills/

## Purpose

This document connects the Live Cockpit flow to the downstream proposal
pipeline. Use it when running the WeCollavo harness, creating workspace files,
or checking whether a proposal is complete.

Live Cockpit is the top-level mode. The HTML proposal pipeline is the follow-up
artifact flow after live meeting judgment.

## Fixed Flow

```text
live-meeting.md
  -> ai-backchannel.md
  -> proposal-snapshot.md
  -> client-snapshot.md
  -> preview-questions.md
  -> answers.md
  -> diagnosis.md
  -> scope-pricing.md
  -> client-presentation.html
  -> Human Linchpin Review
  -> optional HyperFrames
```

The first field output is `proposal-snapshot.md`. The full customer-facing
result is `client-presentation.html`.

## Workspace Rules

Create one workspace per client:

```text
harness/workspaces/<client-slug>/
```

Required files:

- `live-meeting.md`
- `ai-backchannel.md`
- `proposal-snapshot.md`
- `client-snapshot.md`
- `preview-questions.md`
- `answers.md`
- `diagnosis.md`
- `scope-pricing.md`
- `client-presentation.html`

Use `harness/templates/` as the starting point for new workspaces.

## Step Requirements

1. **Live Meeting**
   - Capture customer utterances, decisions, undecided issues, material requests, budget signals, schedule signals, and decision maker signals.
   - Keep the AI backchannel hidden from the client.

2. **AI Backchannel**
   - Produce next questions, hidden bottleneck, track judgment, risks, do-not-sell list, scope boundaries, price frame, and suggested wording for Channeul.
   - Do not present backchannel output as final judgment.

3. **Proposal Snapshot**
   - Create the meeting-end or 10-minute-after first proposal snapshot.
   - Label pricing as field diagnostic proposal, not final estimate.

4. **Client Snapshot**
   - Separate confirmed facts, assumptions, constraints, materials, budget signals, schedule signals, and decision maker context.
   - Record the likely track, but do not force a final scope before questions are answered.

5. **Preview Questions**
   - Prepare discovery, decision, and follow-up/risk questions.
   - Questions must help determine conclusion, scope, price, additional-fee conditions, and required client materials.

6. **Answer Capture**
   - Convert meeting notes into answers.
   - Mark each answer as confirmed, unclear, missing, or needs follow-up.

7. **Diagnosis**
   - State the real bottleneck.
   - Separate what the customer thinks they need from what WeCollavo believes should happen first.
   - Explain the reason in plain language.

8. **Scope And Pricing**
   - Define first-phase scope, excluded scope, price decomposition, additional-fee triggers, schedule assumptions, and client dependencies.
   - Use `docs/estimate-template.md` for Track 1 estimate logic.

9. **HTML Presentation**
   - Render or update `client-presentation.html` using `harness/templates/client-presentation.html`.
   - Put the conclusion first, then explain why it was reached.

10. **Human Linchpin Review**
   - Run `harness/checklists/human-linchpin-review.md`.
   - Final judgment, price, public wording, delivery promise, and payment terms must be reviewed by the human operator.

## HTML Presentation Sections

`client-presentation.html` must include:

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

## Output Boundary

The HTML can be used as a browser presentation, PDF/capture source, HyperFrames
source, or client-safe written proposal.

It must not be delivered until Human Linchpin Review confirms scope, price,
public claims, assumptions, and additional-fee conditions.
