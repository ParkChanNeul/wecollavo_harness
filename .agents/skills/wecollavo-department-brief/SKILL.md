---
name: wecollavo-department-brief
description: Create a structured WeCollavo Department Analysis Brief after Request Lock without creating proposal-data.json.
---

# WeCollavo Department Brief

Use this skill for the legacy `/interview-handoff` path after Request Lock.

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

If Request Lock context is missing or not locked, return the missing lock
condition instead of creating a Department Analysis Brief.

## Forbidden

- Do not create `proposal-data.json`.
- Do not dump raw customer notes as department handoff.
- Do not read an existing workspace unless a path or existing client id is
  clearly named.
- Do not write/update workspace files without explicit `client_dir`.
- Do not expose internal risks as customer-facing copy.

## Non-linear Entry

This skill can be invoked directly, but direct invocation does not bypass
Request Lock. If locked request context, Hard Locks, or Assumption Locks are
missing, return missing condition and recommend `$wecollavo-request-lock`.

## Next Skill Handoff

- Recommended Next Skill: `$wecollavo-proposal-review`
- Why: Use after the structured Department Analysis Brief is ready.
- Ready To Continue: yes | no
- Need Channeul Confirmation: yes
- Requires client_dir: yes | no
- Suggested Prompt: `$wecollavo-proposal-review client_dir=clients/<client> proposal-review.md pre-render seed를 만들어줘.`

If the meeting needs a client-safe close first, recommend
`$wecollavo-meeting-close` instead.

This handoff is a recommendation only. It does not automatically run the next
skill.
