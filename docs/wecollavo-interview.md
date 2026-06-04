# WeCollavo Interview

Status: v1 front-stage interview doctrine
Last updated: 2026-06-04

## Purpose

WeCollavo Interview는 고객이 이미 알고 있는 답을 받아 적는 절차가 아니다.
미팅 중 고객 발화를 기준으로 찬늘이 다음 질문, 전략적 해석, 병목, 가격/범위
신호를 빠르게 판단하도록 돕는 live loop다.

AI는 고객과 직접 대화하지 않는다. AI는 찬늘에게만 백채널 판단을 제공한다.
고객에게 보이는 제안서는 Request Lock 이후에만 만든다.

## WeCollavo Interview Philosophy

고객이 아는 것은 확인한다.

고객이 모르는 것은 드러낸다.

끝내 답하지 못하는 것은 WeCollavo가 선택지와 추천안으로 좁힌 뒤, 고객 승인
하에 Assumption Lock으로 기록한다.

고객이 모르는 것은 실패가 아니라 diagnosis input이다. 인터뷰의 목적은 즉시
견적을 내는 것이 아니라, 제안 가능한 요청을 만드는 것이다.

## Marketing Diagnosis Equation

```text
Goal
× Audience
× Trust Gap
× Asset Gap
× Channel Fit
× Offer Clarity
× Execution Capacity
× Budget Reality
× Timeline Reality
- Risk
= Recommended Scope + Price Band + Proposal Direction
```

이 식은 견적 계산기가 아니다. 미팅 중 빠진 맥락을 찾고, 어떤 정보가 가격과
범위를 흔드는지 판단하기 위한 진단 프레임이다.

## Interview Loop

```text
client.json
  -> meeting-state.md

[WeCollavo Interview Loop]
  -> /interview-start
  -> /interview-turn
  -> /interview-pivot
  -> /interview-unknown
  -> /interview-lock-check
  -> /interview-lock
  -> /interview-handoff
  -> /interview-close

[After Request Lock]
  -> proposal-data.json
  -> proposal.html
  -> delivery-plan.json
  -> proof-loop.json
```

`/interview-turn`은 반복 실행한다. 고객 발화가 새로 들어올 때마다
`meeting-state.md`를 갱신하고 AI Interview Card를 만든다.

`wecollavo-interview`는 loop/skill이다. 파일처럼 `wecollavo-interview`를
생성하지 않는다.

## AI Interview Card

AI Interview Card는 찬늘에게만 보이는 백채널 카드다. 고객용 문안이 아니라
다음 판단을 위한 내부 구조다.

필수 필드:

- `what_i_heard`
- `strategic_decode`
- `bottleneck_hypothesis`
- `marketing_diagnosis_equation`
- `ask_next`
- `unknowns`
- `guided_options`
- `default_recommendation`
- `assumption_to_lock`
- `service_mapping`
- `price_scope_signals`
- `risks`
- `do_not_promise`
- `client_safe_phrase`
- `meeting_state_updates`
- `request_lock_status`

`client_safe_phrase`만 고객에게 말할 수 있는 표현으로 정리한다. 나머지 필드는
내부 판단이다.

## Unknown Handling

Unknown Handling은 고객이 모르는 항목을 방치하지 않고 제안 가능한 상태로
좁히는 절차다.

```text
open question
  -> choice question
  -> default recommendation
  -> customer approval
  -> Assumption Lock
```

고객이 모른다고 답하면 먼저 열린 질문을 한다. 그래도 답이 없으면 선택지를
제시한다. 선택지도 어렵다면 WeCollavo의 기본 추천안을 제시하고, 고객이
동의한 경우에만 Assumption Lock으로 기록한다.

## Unknown Types

- `harmless_unknown`: 제안 방향에는 영향을 주지 않지만 나중에 확인할 정보
- `proposal_blocking_unknown`: 제안서 생성 전 반드시 풀어야 하는 정보
- `price_affecting_unknown`: 가격, 착수금, 범위, 추가비 조건을 흔드는 정보
- `risk_unknown`: 납품 약속, 책임 범위, 권한 이전, 공개 가능성에 영향을 주는 정보

v1의 `remaining_unknowns`는 string array로 시작한다. 향후 각 unknown의 owner,
deadline, source, resolution status가 필요해지면 object array로 확장할 수 있다.

## Guided Assumption

Guided Assumption은 고객이 끝내 답하지 못한 항목에 대해 WeCollavo가 선택지와
추천안을 제시하는 방식이다.

예:

- 고객이 제출 대상자를 모르면 `관공서/입찰`, `제휴사`, `기존 고객`, `내부 영업팀`
  중 우선순위를 고르게 한다.
- 고객이 로고 방향을 모르면 `유지`, `리터칭`, `신규 제작`의 가격/일정 차이를
  설명하고 기본 추천안을 제시한다.
- 고객이 예산을 모르면 최소 착수 가능 구간과 확장 구간을 분리해 설명한다.

Guided Assumption은 고객 승인 없이 확정 사실로 쓰지 않는다.

## Hard Lock vs Assumption Lock

Hard Lock은 고객 자료, 고객 발화, 기존 파일, 명시 승인으로 확인된 사실이다.

Assumption Lock은 고객이 직접 답하지 못했지만 WeCollavo가 선택지와 추천안을
제시했고, 고객이 그 전제를 기준으로 진행하자고 승인한 항목이다.

`proposal-data.json`에서는 `confirmed_facts`, `hard_locks`, `assumption_locks`,
`assumptions`를 분리한다.

## Request Lock

Request Lock은 proposal-data 생성 가능 여부를 판단하는 gate다.

상태값:

- `open`: 고객 요청이 아직 제안 가능한 형태가 아니다.
- `partial`: 일부 lock은 잡혔지만 blocking unknown이 남아 있다.
- `locked`: 제안서 초안을 만들 수 있을 만큼 요청, 범위, 가격 신호, 리스크가
  정리되었다.

`meeting-state.md`의 기본 `request_lock_status`는 `open`이다.

`proposal-data.json`은 post-lock artifact이므로 template 기본값은 `locked`다.
단, 검증 스크립트는 데이터 상태 점검을 위해 `open | partial | locked`를 모두
허용한다.

고객 전달 safety gate는 반드시 `locked`를 요구한다.

## Department Handoff

Department Handoff는 Request Lock 이후 제안서 작성 전에 각 판단 영역으로
넘겨야 할 작업 메모다.

필수 영역:

- `marketing_planning`
- `commercial_pricing`
- `design`
- `web_development`
- `content`
- `risk_guard`
- `proposal_writer`

handoff는 내부 메모다. 고객용 HTML에는 domain agent output이나 내부 위험
표현을 그대로 노출하지 않는다.
