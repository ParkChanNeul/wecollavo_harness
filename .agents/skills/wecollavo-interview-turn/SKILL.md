---
name: wecollavo-interview-turn
description: Process one WeCollavo customer utterance, including pivot detection, and return an AI Interview Card.
---

# WeCollavo Interview Turn

Use this skill for `/interview-turn` and `/interview-pivot`.

## Read First

- `docs/source-of-truth.md`
- `docs/language-contract.md`
- `docs/wecollavo-interview.md`
- `docs/department-analysis-method.md`
- `docs/security.md`

## Role

Transform a customer utterance into an AI Interview Card for Channeul. Detect
when the real bottleneck differs from the stated request and pivot the next
question accordingly.

## Inputs

- Customer utterance typed by Channeul.
- Optional temporary interview context.
- Optional `client_dir=clients/<client>` for explicit workspace use.

## Output

- `what_i_heard`
- `strategic_decode`
- `bottleneck_hypothesis`
- `desired_change`
- `smallest_viable_market`
- `unknowns`
- `price_scope_signals`
- `risks`
- `do_not_promise`
- `ask_next`
- `client_safe_phrase`
- recommended next skill

If no `client_dir` is provided, output is temporary state only and must not
update files.

## Forbidden

- Do not read an existing workspace unless a path or existing client id is
  clearly named.
- Do not write/update/lock files without explicit `client_dir=clients/<client>`.
- Do not create `proposal-data.json`.
- Do not present field pricing as final estimate.
- Do not expose internal reasoning as customer-facing text.

## Next Skill Handoff

- Use `$wecollavo-interview-unknown` when unknowns need guided handling.
- Use `$wecollavo-request-lock` when the request may be ready to lock.
- Use `$wecollavo-meeting-close` when the meeting needs a safe close.
