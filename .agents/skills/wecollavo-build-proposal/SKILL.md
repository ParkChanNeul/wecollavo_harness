---
name: wecollavo-build-proposal
description: Use when turning WeCollavo meeting-state.md into proposal-data.json and a client-facing static proposal.html.
---

# WeCollavo Proposal Build

Use this skill only after Request Lock. It turns a locked `meeting-state.md` into
`proposal-data.json` and renders a client-facing static `proposal.html`.

## Read First

- `docs/source-of-truth.md`
- `docs/language-contract.md`
- `docs/department-analysis-method.md`
- `docs/wecollavo-interview.md`
- `docs/proposal-review.md`
- `docs/proposal-system.md`
- `docs/tracks.md`
- `docs/security.md`

## Inputs

- `clients/<client>/meeting-state.md`
- `clients/<client>/proposal-review.md`
- `clients/<client>/client.json`
- Relevant source materials from `project/<client>/`

## Outputs

- `clients/<client>/proposal-data.json`
- `clients/<client>/proposal.html`

## Request Lock Gate

Do not run proposal build when `request_lock_status` is `open` or `partial`.

proposal-data.json must not be created directly from raw meeting notes.
It must be created from locked meeting-state.md, structured Department Analysis
Brief, and proposal-review.md seed.

proposal-data.json은 원시 미팅 노트에서 바로 만들지 않는다. 반드시 Request
Lock, Department Analysis Brief, proposal-review.md 시드를 거친 뒤 생성한다.

Before creating `proposal-data.json`, confirm:

- `request_lock_status` is `locked`.
- Department Handoff is a structured Department Analysis Brief, not a raw memo.
- `clients/<client>/proposal-review.md` exists.
- `proposal-review.md` is written as a pre-render seed.
- Desired Change, SVM, and Trust Indicator are reflected in proposal-data sections.

If Request Lock is missing, do not create `proposal-data.json`. Return:

- missing lock conditions
- remaining unknown types
- whether Hard Locks or Assumption Locks are missing
- recommended next `/interview-*` action

If Department Analysis Brief or proposal-review seed is missing or weak, do not
create `proposal-data.json`. Return the missing condition and recommended next
action: `/interview-handoff` or `$wecollavo-proposal-review`.

`proposal-data.json` is a post-lock artifact. Its template default
`request_lock_status` is `locked`.

## Proposal Sections

The HTML proposal must include these 11 sections:

1. Today\'s conclusion
2. Why this conclusion was reached
3. Meeting questions and answers
4. Customer situation diagnosis
5. Priority decision
6. First engagement scope
7. Price breakdown
8. Extra-cost conditions
9. Materials needed
10. 30-day execution plan
11. Next production proposal

## Rules

- The proposal must be understandable to a non-marketing CEO.
- Explain why the recommendation exists before asking for money.
- Keep the first engagement narrower than the full desired production scope.
- Separate field diagnostic proposal, first written proposal, and final estimate.
- Never present assumptions as confirmed facts.
- If `assumptions` or `assumption_locks` exist, include a customer-safe assumption basis in the proposal.
- Never expose AI Interview Card fields, internal notes, or domain-agent output in `proposal.html`.
