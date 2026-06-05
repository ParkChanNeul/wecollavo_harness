---
name: wecollavo-meeting-close
description: Produce a safe WeCollavo meeting close, next action, and client-safe phrase after an interview turn or lock check.
---

# WeCollavo Meeting Close

Use this skill for `/interview-close`.

## Read First

- `docs/source-of-truth.md`
- `docs/language-contract.md`
- `docs/wecollavo-interview.md`
- `docs/department-analysis-method.md`
- `docs/security.md`

## Role

Close the meeting safely for Channeul without overpromising price, scope,
delivery, or approval status.

## Inputs

- Current temporary interview state or explicit client workspace context.
- Known customer request.
- Remaining unknowns.
- Current request lock recommendation.

## Output

- one-sentence diagnosis
- client-safe closing phrase
- next customer action
- next WeCollavo internal action
- do-not-promise reminders
- recommended next skill

## Forbidden

- Do not read an existing workspace unless a path or existing client id is
  clearly named.
- Do not present final estimate before material review.
- Do not promise delivery scope that has not passed Human Linchpin Review.
- Do not write/update workspace files without explicit `client_dir`.
- Do not create `proposal-data.json`.

## Next Skill Handoff

- Use `$wecollavo-interview-turn` if the customer adds new information.
- Use `$wecollavo-request-lock` if lock readiness should be checked.
- Use `$wecollavo-proposal-review` only after Request Lock and Department Brief.
