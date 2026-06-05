---
name: wecollavo-proposal-review
description: Use when creating or checking WeCollavo proposal-review.md as a pre-render seed before proposal-data.json and proposal.html.
---

# WeCollavo Proposal Review

Use this skill after Request Lock and structured Department Analysis Brief, but
before building `proposal-data.json`.

## Read First

- `docs/source-of-truth.md`
- `docs/language-contract.md`
- `docs/proposal-review.md`
- `docs/department-analysis-method.md`
- `docs/wecollavo-interview.md`
- `docs/proposal-system.md`
- `docs/security.md`

## Role

Create or review `clients/<client>/proposal-review.md` as a pre-render proposal
seed. This is not an after-HTML QA document.

## Inputs

- `clients/<client>/meeting-state.md`
- `clients/<client>/proposal-review.md`
- Structured `department_handoff`
- Relevant source materials from `project/<client>/`

## Output

Create or update `clients/<client>/proposal-review.md`.

Required checks:

- Desired Change Check
- SVM Check
- Department Analysis Check
- Commercial Check
- Trust Indicator Check
- Decision

## Rules

- Do not edit `proposal.html`.
- Do not change `human_review_status` to `approved`; only Channeul can approve.
- Do not create proposal data directly from raw meeting notes.
- Confirm that Department Handoff is a structured Department Analysis Brief, not a raw memo.
- Keep customer-facing language separate from internal reasoning.
