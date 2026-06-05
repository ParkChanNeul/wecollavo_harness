---
name: wecollavo-interview-turn
description: Process one WeCollavo customer utterance, including pivot detection, and return an AI Interview Card.
---

# WeCollavo Interview Turn

Use this skill for legacy `/interview-turn` and `/interview-pivot` paths.

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

Transform a customer utterance into an AI Interview Card for Channeul. Detect
when the real bottleneck differs from the stated request and pivot the next
question accordingly.

Interpret the utterance through the Brand Execution Sprint lens: do not simply
summarize the request, identify the likely track candidate, narrow toward one
core brand asset, suggest the first 30-day proof signal, and never execute
Request Lock from this skill.

## Inputs

- Customer utterance typed by Channeul.
- Optional temporary interview context.
- Optional `client_dir=clients/<client>` for explicit workspace use.

## Output

Default output must be a Korean Meeting Coach View, not a JSON/key-value dump.
Do not expose snake_case field names in the default card.

Use this shape:

```text
# AI Interview Card

## 한 줄 진단
-

## 내가 들은 내용
-

## 전략적 해석
-

## 핵심 병목
-

## 변화 목표
-

## 첫 타겟 / 최소 유효 시장
-

## 아직 모르는 것

### 제안 전에 꼭 확인할 것
-

### 가격/범위에 영향을 주는 것
-

### 리스크가 될 수 있는 것
-

## 가격/범위 신호
-

## 지금 약속하면 안 되는 것
-

## 지금 고객에게 물어볼 질문
1.
2.
3.

## 고객에게 말해도 되는 문장
-

## 미팅 기록 반영 후보
-

## 요청 잠금 후보 상태
open | partial | locked 후보 중 하나로 설명한다.
여기서 실제 request lock을 실행하지 않는다.
```

When internal handoff is necessary, add an optional final
`Internal Structured Fields` section after the Korean coach view. Keep internal
field names out of the default card.

Always include the common `Next Skill Handoff` section.

If no `client_dir` is provided, output is temporary state only and must not
update files.

The request lock candidate shown in this card is only a candidate. It is not the
actual `request_lock_status` data contract.

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
Korean "미팅 기록 반영 후보", not file updates. If required context is missing,
ask the next useful question instead of pretending the request is locked.

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
