---
name: wecollavo-build-proposal
description: Use when turning WeCollavo meeting-state.md into proposal-data.json and a client-facing static proposal.html.
---

# WeCollavo Proposal Build

Use this skill after `meeting-state.md` is clear enough to build a client-facing proposal.

## Read First

- `docs/source-of-truth.md`
- `docs/language-contract.md`
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
