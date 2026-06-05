---
name: wecollavo-meeting-close
description: Produce a safe WeCollavo meeting close, next action, and client-safe phrase after an interview turn or lock check.
---

# WeCollavo Meeting Close

Use this skill for the legacy `/interview-close` path.

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

Close the meeting safely for Channeul without overpromising price, scope,
delivery, or approval status.

Frame the close around the first trust-building brand asset and the signal to
check after 30 days. Do not close by implying that more assets or a larger
package is automatically better.

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

## Non-linear Entry

This skill can be used at any point to produce a safe closing phrase. If Request
Lock is not ready, do not speak as if the scope, price, or proposal is locked.
Return the next missing condition and a safe next action.

## Next Skill Handoff

- Recommended Next Skill: `$wecollavo-interview-turn`
- Why: Use if the customer adds new information after the close.
- Ready To Continue: yes | no
- Need Channeul Confirmation: yes
- Requires client_dir: no
- Suggested Prompt: `$wecollavo-interview-turn 고객 발화: <추가 답변>`

If lock readiness should be checked, recommend `$wecollavo-request-lock`. Use
`$wecollavo-proposal-review` only after Request Lock and Department Brief. This
handoff is a recommendation only.
