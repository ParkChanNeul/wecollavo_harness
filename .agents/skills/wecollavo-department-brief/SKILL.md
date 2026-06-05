---
name: wecollavo-department-brief
description: Create a structured WeCollavo Department Analysis Brief after Request Lock without creating proposal-data.json.
---

# WeCollavo Department Brief

Use this skill for `/interview-handoff` after Request Lock.

## Read First

- `docs/source-of-truth.md`
- `docs/language-contract.md`
- `docs/wecollavo-interview.md`
- `docs/department-analysis-method.md`
- `docs/security.md`
- `docs/workflow.md`

## Role

Create a structured Department Analysis Brief from locked customer signals. This
can be conversational output or an explicit workspace update when
`client_dir=clients/<client>` is provided.

## Inputs

- Locked request context.
- Hard Lock draft items.
- Assumption Lock draft items.
- Desired Change, SVM, Trust Indicators.
- Optional `client_dir=clients/<client>` for explicit workspace update.

## Output

Structured Department Analysis Brief with:

- `marketing_planning`
- `commercial_pricing`
- `design`
- `web_development`
- `content`
- `risk_guard`
- `proposal_writer`

Each department should include diagnosis, recommendation, scope_impact,
price_impact, risks, missing_inputs, proposal_points, client_safe_phrase, and
trust_indicator.

## Forbidden

- Do not create `proposal-data.json`.
- Do not dump raw customer notes as department handoff.
- Do not read an existing workspace unless a path or existing client id is
  clearly named.
- Do not write/update workspace files without explicit `client_dir`.
- Do not expose internal risks as customer-facing copy.

## Next Skill Handoff

- Use `$wecollavo-proposal-review` after the Department Analysis Brief is ready.
- Use `$wecollavo-meeting-close` if the meeting needs a closing summary first.
