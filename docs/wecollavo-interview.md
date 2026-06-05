# WeCollavo Interview

Status: v1.1 front-stage interview subskill routing doctrine
Last updated: 2026-06-05

## Purpose

WeCollavo Interview는 고객이 이미 알고 있는 답을 받아 적는 절차가 아니다.
미팅 중 고객 발화를 기준으로 찬늘이 다음 질문, 전략적 해석, 병목, 가격/범위
신호를 빠르게 판단하도록 돕는 live loop다.

AI는 고객과 직접 대화하지 않는다. AI는 찬늘에게만 백채널 판단을 제공한다.
고객에게 보이는 제안서는 Request Lock 이후에만 만든다.

Department Analysis Brief는 `docs/department-analysis-method.md` 기준으로
작성한다. 고객 발화는 최종 요구사항이 아니라 raw signal이다.

## WeCollavo Interview Philosophy

고객이 아는 것은 확인한다.

고객이 모르는 것은 드러낸다.

끝내 답하지 못하는 것은 WeCollavo가 선택지와 추천안으로 좁힌 뒤, 고객 승인
하에 Assumption Lock으로 기록한다.

고객이 모르는 것은 실패가 아니라 diagnosis input이다. 인터뷰의 목적은 즉시
견적을 내는 것이 아니라, 제안 가능한 요청을 만드는 것이다.

## Marketing Diagnosis Equation

```text
Linchpin Judgment
× Desired Change
× Service Target
× Smallest Viable Market
× Worldview
× Brand Promise
× Tension
× Pattern Interruption
× Trust Gap
× Asset Gap
× Execution Capacity
× Budget Reality
× Timeline Reality
- Tactical Trap
- Risk
= Recommended Scope + Price Band + Proposal Direction
```

이 식은 견적 계산기가 아니다. 미팅 중 빠진 맥락을 찾고, 어떤 정보가 가격과
범위를 흔드는지 판단하기 위한 진단 프레임이다.

## Subskill Routing

```text
wecollavo-interview
  -> router/intake alias only

[Interview Subskills]
  -> wecollavo-interview-intake
  -> wecollavo-workspace-resume
  -> wecollavo-interview-turn
  -> wecollavo-interview-unknown
  -> wecollavo-request-lock
  -> wecollavo-department-brief
  -> wecollavo-meeting-close

[After Request Lock]
  -> proposal-review.md
  -> proposal-data.json
  -> proposal.html
  -> delivery-plan.json
  -> proof-loop.json
```

`wecollavo-interview`는 compatibility router이자 intake alias다. 실제 하위
명령을 실행하지 않고, 사용할 독립 skill을 추천한다.

Slash command mapping은 backward compatibility 안내용이다.

- `/interview-start` -> `wecollavo-interview-intake` 또는 `wecollavo-workspace-resume`
- `/interview-turn` -> `wecollavo-interview-turn`
- `/interview-pivot` -> `wecollavo-interview-turn`
- `/interview-unknown` -> `wecollavo-interview-unknown`
- `/interview-lock-check` -> `wecollavo-request-lock`
- `/interview-lock` -> `wecollavo-request-lock`
- `/interview-handoff` -> `wecollavo-department-brief`
- `/interview-close` -> `wecollavo-meeting-close`

## Invocation Modes

### Intake Mode - default

Bare `$wecollavo-interview`, bare `/interview-start`, and interview starts
without explicit workspace context must use `wecollavo-interview-intake`.

Intake Mode does not read, write, update, or lock client workspace files.
It outputs an Interview Intake Card and asks for customer context first.

`clients/gt-engineering` is a fixture. It must never be inferred as the active
client for a bare invocation.

### Workspace Read Mode

Workspace read is allowed only when the user directly names a
`clients/<client>` path or clearly names an existing client id. Recent work,
customer name inference, context inference, and the fact that the repo has a
single client are not valid read triggers.

Workspace Read Mode uses `wecollavo-workspace-resume` and remains read-only.

### Temporary Turn Mode

`/interview-turn` without `client_dir` uses `wecollavo-interview-turn` as
temporary state only. It may output an AI Interview Card, next question,
unknowns, and client-safe phrase. It must not read or update `meeting-state.md`.

### Workspace Write / Update / Lock Mode

Workspace write, update, or lock requires explicit
`client_dir=clients/<client>`. If the user says "meeting-state.md에 반영해줘",
"파일에 써줘", or "잠가줘" without `client_dir`, ask for
`client_dir=clients/<client>` first.

## Interview Intake Card

Bare intake output should use:

```text
# WeCollavo Interview Intake

## Before We Start
아직 client workspace를 읽지 않았습니다.
고객 정보를 먼저 입력해 주세요.

## Intake Questions
1. 신규 고객인가요, 기존 고객인가요?
2. 고객/회사명은 무엇인가요?
3. 오늘 미팅 목적은 무엇인가요?
4. 고객이 처음 한 말 또는 문의 내용은 무엇인가요?
5. 관심 서비스는 무엇인가요?
   - 홈페이지 / 랜딩페이지 / 로고 / 브로셔 / 회사소개서 / 브랜드 키트 / 콘텐츠 / 마케팅 운영 / 기타
6. 예산, 일정, 자료 상태 중 이미 알고 있는 것이 있나요?
7. 기존 client workspace에 연결할까요, 아니면 임시 인터뷰로 진행할까요?

## Next Action
고객 발화를 받으면 `wecollavo-interview-turn`으로 AI Interview Card를 생성합니다.
기존 워크스페이스를 사용하려면 `client_dir=clients/<client>`를 명시해 주세요.
```

## Subskill Handoff

1차 refactor의 Next Skill Handoff는 단순 다음 skill 추천만 포함한다. Cross-Skill
Continue Protocol, handoff schema, Non-linear Entry 세부 복구 규칙은 2차
보강에서 확장한다.

## AI Interview Card

AI Interview Card는 찬늘에게만 보이는 백채널 카드다. 고객용 문안이 아니라
다음 판단을 위한 내부 구조다.

필수 필드:

- `raw_request`
- `desired_change`
- `current_state`
- `target_state`
- `tension`
- `change_type`
- `smallest_viable_market`
- `worldview`
- `trust_indicator`
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

Department Handoff는 Request Lock 이후 생성되는 Department Analysis Brief다.
고객 발화를 받아 적은 메모가 아니라, 각 부서 관점으로 진단, 추천, 범위 영향,
가격 영향, 리스크, 제안서 반영 포인트, 고객용 표현, 신뢰 지표를 정리한 분석
브리프다.

Do not summarize customer words as-is.

For every Department Handoff, transform customer signals through:

1. Desired Change Method
2. Smallest Viable Market Method
3. Linchpin Lens
4. Department Method Card
5. Scope / price / risk impact
6. Trust Indicator
7. Client-safe proposal language

필수 영역:

- `marketing_planning`
- `commercial_pricing`
- `design`
- `web_development`
- `content`
- `risk_guard`
- `proposal_writer`

각 영역의 preferred format:

- `diagnosis`
- `recommendation`
- `scope_impact`
- `price_impact`
- `risks`
- `missing_inputs`
- `proposal_points`
- `client_safe_phrase`
- `trust_indicator`

handoff는 내부 분석 브리프다. 고객용 HTML에는 domain agent output이나 내부
위험 표현을 그대로 노출하지 않는다.
