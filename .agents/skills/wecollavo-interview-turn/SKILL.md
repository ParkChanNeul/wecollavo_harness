---
name: wecollavo-interview-turn
description: Process one WeCollavo customer utterance, including pivot detection, and return an AI Interview Card.
---

# WeCollavo Interview Turn

Use this skill for legacy `/interview-turn` and `/interview-pivot` paths.

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
- `meeting_state_update_suggestions`
- `request_lock_candidate_status`
- recommended next skill

If no `client_dir` is provided, output is temporary state only and must not
update files.

`request_lock_candidate_status` is only an AI Interview Card candidate. It is
not the actual `request_lock_status` data contract.

## Forbidden

- Do not read an existing workspace unless a path or existing client id is
  clearly named.
- Do not write/update/lock files without explicit `client_dir=clients/<client>`.
- Do not create `proposal-data.json`.
- Do not present field pricing as final estimate.
- Do not expose internal reasoning as customer-facing text.

## Non-linear Entry

This skill can start from one customer utterance even without intake. In that
case, treat the output as temporary state only and return
`meeting_state_update_suggestions`, not file updates. If required context is
missing, ask the next useful question instead of pretending the request is
locked.

## Next Skill Handoff

- Recommended Next Skill: `$wecollavo-interview-unknown`
- Why: Use when unknowns need guided handling before lock readiness.
- Ready To Continue: yes | no
- Need Channeul Confirmation: yes
- Requires client_dir: no
- Suggested Prompt: `$wecollavo-interview-unknown 방금 unknown을 기준으로 선택 질문과 기본 추천안을 만들어줘.`

If the request appears lock-ready, recommend `$wecollavo-request-lock`. If the
meeting needs a safe close, recommend `$wecollavo-meeting-close`. This handoff
is a recommendation only.
