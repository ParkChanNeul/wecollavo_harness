---
name: wecollavo-request-lock
description: Check WeCollavo request lock readiness and draft Hard Lock / Assumption Lock items before proposal-data.json creation.
---

# WeCollavo Request Lock

Use this skill for `/interview-lock-check` and `/interview-lock`.

## Read First

- `docs/source-of-truth.md`
- `docs/language-contract.md`
- `docs/wecollavo-interview.md`
- `docs/department-analysis-method.md`
- `docs/security.md`
- `docs/workflow.md`

## Role

Decide whether a customer request is proposal-ready. Separate Hard Lock /
Assumption Lock draft creation from actual workspace file updates.

## Inputs

- AI Interview Card or current temporary interview state.
- Unknown classifications.
- Customer-approved assumptions, if any.
- Optional `client_dir=clients/<client>` for explicit workspace write/update/lock.

## Output

- recommended `request_lock_status`: `open`, `partial`, or `locked`
- missing lock conditions
- Hard Lock draft items
- Assumption Lock draft items
- Do Not Promise list
- recommended next skill

File reflection/write/update/lock is allowed only when explicit
`client_dir=clients/<client>` is provided.

## Forbidden

- Do not read an existing workspace unless a path or existing client id is
  clearly named.
- Do not write/update/lock workspace files without explicit `client_dir`.
- Do not infer a workspace from recent work or fixture files.
- Do not turn assumptions into confirmed facts.
- Do not create `proposal-data.json`.
- Do not create Department Analysis Brief here; route to
  `$wecollavo-department-brief`.

## Next Skill Handoff

- Use `$wecollavo-interview-unknown` if blocking unknowns remain.
- Use `$wecollavo-department-brief` after `request_lock_status: locked`.
- Use `$wecollavo-meeting-close` if the meeting should end before lock.
