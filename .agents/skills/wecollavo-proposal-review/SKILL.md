---
name: wecollavo-proposal-review
description: Use when creating or checking WeCollavo proposal-review.md as a pre-render seed before proposal-data.json and proposal.html.
---

# WeCollavo Proposal Review

Use this skill after Request Lock and structured Department Analysis Brief, but
before building `proposal-data.json`.

## Read First

- `docs/source-of-truth.md`
- `docs/wecollavo-brand-execution-sprint.md`
- `docs/language-contract.md`
- `docs/wecollavo-interview.md`
- `docs/department-analysis-method.md`
- `docs/proposal-system.md`
- `docs/proposal-review.md`
- `docs/security.md`

## Role

Create or review `clients/<client>/proposal-review.md` as a pre-render proposal
seed. This is not an after-HTML QA document.

Review whether the proposal seed is a Brand Execution Sprint proposal, not a
plain estimate. Confirm that it includes reinterpretation of the request, the
real bottleneck, one core brand asset, what not to do now, and the first 30-day
evidence signal.

## Inputs

- `clients/<client>/meeting-state.md`
- `clients/<client>/proposal-review.md`
- Structured `department_handoff`
- Relevant source materials from `project/<client>/`

## Output

Create or update `clients/<client>/proposal-review.md`.

Client seed files must start with:

```yaml
---
review_type: proposal_review_seed
review_stage: pre_render
proposal_review_decision: pending
reviewer: Channeul
---
```

Required checks:

- Desired Change Check
- SVM Check
- Department Analysis Check
- Commercial Check
- Trust Indicator Check
- proposal_review_decision in frontmatter

## Rules

- Do not edit `proposal.html`.
- Do not change `human_review_status` to `approved`; only Channeul can approve.
- Do not set `proposal_review_decision` to `approved`; only Channeul can approve the pre-render seed.
- Do not create proposal data directly from raw meeting notes.
- Confirm that Department Handoff is a structured Department Analysis Brief, not a raw memo.
- Keep customer-facing language separate from internal reasoning.

## Non-linear Entry

If this skill is invoked without Request Lock or structured Department Analysis
Brief, return the missing condition and recommend `$wecollavo-request-lock` or
`$wecollavo-department-brief`. Do not create or approve a seed from raw notes.

## Next Skill Handoff

- Recommended Next Skill: `$wecollavo-build-proposal`
- Why: Use only after Channeul approves the pre-render proposal seed.
- Ready To Continue: yes | no
- Need Channeul Confirmation: yes
- Requires client_dir: yes
- Suggested Prompt: `$wecollavo-build-proposal client_dir=clients/<client> approved proposal-review.md를 기준으로 proposal-data.json과 proposal.html을 생성해줘.`

If `proposal_review_decision` is not approved, set `Ready To Continue: no` and
return the missing approval condition. This handoff is a recommendation only.
