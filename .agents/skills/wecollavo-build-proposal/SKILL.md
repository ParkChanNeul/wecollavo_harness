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
- `docs/wecollavo-interview.md`
- `docs/proposal-system.md`
- `docs/tracks.md`
- `docs/security.md`

## Inputs

- `clients/<client>/meeting-state.md`
- `clients/<client>/client.json`
- Relevant source materials from `project/<client>/`

## Outputs

- `clients/<client>/proposal-data.json`
- `clients/<client>/proposal.html`

## Request Lock Gate

Do not run proposal build when `request_lock_status` is `open` or `partial`.

If Request Lock is missing, do not create `proposal-data.json`. Return:

- missing lock conditions
- remaining unknown types
- whether Hard Locks or Assumption Locks are missing
- recommended next `/interview-*` action

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
