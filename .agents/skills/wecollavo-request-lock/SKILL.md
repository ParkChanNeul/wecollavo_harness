---
name: wecollavo-request-lock
description: Check WeCollavo request lock readiness and draft Hard Lock / Assumption Lock items before proposal-data.json creation.
---

# WeCollavo Request Lock

Use this skill for legacy `/interview-lock-check` and `/interview-lock` paths.

## Read First

- `docs/source-of-truth.md`
- `docs/wecollavo-brand-execution-sprint.md`
- `docs/language-contract.md`
- `docs/wecollavo-interview.md`
- `docs/department-analysis-method.md`
- `docs/proposal-system.md`
- `docs/proposal-review.md`
- `docs/security.md`
- `docs/workflow.md`

## Role

Decide whether a customer request is proposal-ready. Separate Hard Lock /
Assumption Lock draft creation from actual workspace file updates.

Before recommending locked, confirm that the one core brand asset, what not to
do now, and the first 30-day Proof Loop signal are sufficiently clear. If those
conditions are weak, keep the candidate status at open or partial.

## Inputs

- AI Interview Card or current temporary interview state.
- Unknown Handling 결과.
- Customer-approved assumptions, if any.
- Optional `client_dir=clients/<client>` for explicit workspace write/update/lock.

## Output

Default output must be a Korean Request Lock Check, not a field dump.

Use this shape:

```text
# Request Lock Check

## 지금 확정된 것
-

## 위콜라보 추천 전제로 잠글 수 있는 것
-

## 아직 잠그면 안 되는 것
-

## 가격/범위 때문에 더 확인할 것
-

## 현재 잠금 판단
open | partial | locked 후보와 이유
```

Hard Lock / Assumption Lock items are draft candidates unless explicit
`client_dir=clients/<client>` is provided for workspace file reflection.

Always include the common `Next Skill Handoff` section.

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

## Non-linear Entry

This skill can be invoked directly to draft lock readiness from current
conversation. Without explicit `client_dir`, it may return only conversational
Hard Lock / Assumption Lock draft items and missing lock conditions. It must not
write/update/lock workspace files.

## Next Skill Handoff

- Recommended Next Skill: `$wecollavo-department-brief`
- Why: Use after the request is ready to lock and Department Analysis Brief is needed.
- Ready To Continue: yes | no
- Need Channeul Confirmation: yes
- Requires client_dir: yes | no
- Suggested Prompt: `$wecollavo-department-brief client_dir=clients/<client> locked request를 기준으로 Department Analysis Brief를 만들어줘.`

If blocking unknowns remain, recommend `$wecollavo-interview-unknown`. If the
meeting should end before lock, recommend `$wecollavo-meeting-close`. This
handoff is a recommendation only.
