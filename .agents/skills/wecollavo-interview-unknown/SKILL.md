---
name: wecollavo-interview-unknown
description: Classify WeCollavo interview unknowns and produce choice questions or guided assumption candidates.
---

# WeCollavo Interview Unknown

Use this skill when customer answers are missing, vague, or blocking proposal
readiness.

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

Turn uncertainty into useful diagnosis input. Classify unknowns and narrow them
through open questions, choice questions, and guided assumption candidates.

Treat unknowns as Brand Execution Sprint diagnosis input, not failure. Separate
unknowns that affect the one core brand asset from unknowns that affect the
30-day Proof Loop signal.

## Inputs

- Customer utterance or unresolved unknown list.
- Optional AI Interview Card.
- Optional `client_dir=clients/<client>` for explicit workspace use.

## Output

Default output must be a Korean Unknown Handling Card, not a JSON/key-value
dump. Do not expose snake_case field names in the default card.

Use this shape:

```text
# Unknown Handling Card

## 지금 고객이 모르는 것
-

## 왜 중요한가
-

## 선택지로 바꾼 질문
1.
2.
3.

## 위콜라보가 제안할 수 있는 기본 전제 후보
-

## 반드시 고객 확인이 필요한 것
-

## 고객에게 말해도 되는 문장
-
```

When internal handoff is necessary, add an optional final
`Internal Structured Fields` section after the Korean card. Keep internal field
names out of the default card.

Always include the common `Next Skill Handoff` section.

## Forbidden

- Do not read an existing workspace unless a path or existing client id is
  clearly named.
- Do not record Hard Lock or Assumption Lock as a file update.
- Do not write/update/lock files without explicit `client_dir=clients/<client>`.
- Do not treat customer uncertainty as failure.
- Do not create `proposal-data.json`.

## Non-linear Entry

This skill can start directly from "모르겠다", "알아서 해달라", or any vague
customer answer. It may draft choice questions and assumption candidates, but it
must not record Assumption Lock in files without explicit `client_dir`.

## Next Skill Handoff

- Recommended Next Skill: `$wecollavo-interview-turn`
- Why: Use after Channeul gets the next customer answer.
- Ready To Continue: yes | no
- Need Channeul Confirmation: yes
- Requires client_dir: no
- Suggested Prompt: `$wecollavo-interview-turn 고객 발화: <고객의 다음 답변>`

If blocking unknowns are resolved or an assumption candidate is ready for
approval, recommend `$wecollavo-request-lock`. This handoff is a recommendation
only.
