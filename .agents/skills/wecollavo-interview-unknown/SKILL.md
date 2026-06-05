---
name: wecollavo-interview-unknown
description: Classify WeCollavo interview unknowns and produce choice questions or guided assumption candidates.
---

# WeCollavo Interview Unknown

Use this skill when customer answers are missing, vague, or blocking proposal
readiness.

## Read First

- `docs/source-of-truth.md`
- `docs/language-contract.md`
- `docs/wecollavo-interview.md`
- `docs/department-analysis-method.md`
- `docs/security.md`

## Role

Turn uncertainty into useful diagnosis input. Classify unknowns and narrow them
through open questions, choice questions, and guided assumption candidates.

## Inputs

- Customer utterance or unresolved unknown list.
- Optional AI Interview Card.
- Optional `client_dir=clients/<client>` for explicit workspace use.

## Output

- Unknown classification:
  - `harmless_unknown`
  - `proposal_blocking_unknown`
  - `price_affecting_unknown`
  - `risk_unknown`
- open question
- choice question
- default recommendation candidate
- assumption_to_lock candidate
- recommended next skill

## Forbidden

- Do not read an existing workspace unless a path or existing client id is
  clearly named.
- Do not record Hard Lock or Assumption Lock as a file update.
- Do not write/update/lock files without explicit `client_dir=clients/<client>`.
- Do not treat customer uncertainty as failure.
- Do not create `proposal-data.json`.

## Next Skill Handoff

- Use `$wecollavo-interview-turn` after the next customer answer.
- Use `$wecollavo-request-lock` when blocking unknowns are resolved or an
  assumption candidate is ready for approval.
