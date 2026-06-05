# WeCollavo Source Of Truth

Status: v1 current source of truth
Last updated: 2026-06-06

## Definition

WeCollavo Live Execution Harness는 내부용 미팅 실행 하네스다.

하네스의 목적은 앱 완성이 아니라 고객 미팅에서 나온 정보를 Channeul의
Linchpin 판단으로 압축하고, 그 판단을 제안 데이터, HTML 브리핑, 납품 계획,
30일 Proof Loop로 연결하는 것이다.

```text
Core Policy
+ WeCollavo Interview Subskills
+ Department Analysis Method
+ Client Workspace
+ Proposal Review Seed
+ Proposal Renderer
+ Validation Guardrails
+ Delivery Flow
+ Proof Loop
```

## Core Policy

Core Policy는 실행 레이어가 아니라 하네스의 판단 기준이다.

- 서비스 분류: `docs/service-catalog.md`
- 가격 기준: `docs/pricing-policy.md`
- 수정 기준: `docs/revision-policy.md`
- 결제/납품 기준: `docs/payment-delivery-policy.md`
- 언어 계약: `docs/language-contract.md`
- 인터뷰 subskill routing: `docs/wecollavo-interview.md`
- 부서 분석 메소드: `docs/department-analysis-method.md`
- 제안 seed: `docs/proposal-review.md`
- 모션/출력 어댑터 기준: `docs/motion-policy.md`
- 보안과 공개 경계: `docs/security.md`

## Core Flow

```text
client.json
  -> meeting-state.md

[WeCollavo Interview Subskills]
  -> wecollavo-interview-intake
  -> wecollavo-workspace-resume
  -> wecollavo-interview-turn
  -> wecollavo-interview-unknown
  -> wecollavo-request-lock
  -> wecollavo-department-brief
  -> wecollavo-meeting-close

[Proposal Seed]
  -> wecollavo-proposal-review
  -> proposal-review.md
  -> wecollavo-build-proposal
  -> proposal-data.json
  -> proposal.html

[After Client Briefing]
  -> delivery-plan.json
  -> proof-loop.json
```

`meeting-state.md`는 live interview state다. 고객이 모르는 항목은 실패가
아니라 diagnosis input으로 기록한다. 고객이 끝내 답하지 못하는 항목은
WeCollavo가 선택지와 추천안을 제시하고, 고객 승인 하에 Assumption Lock으로
기록한다.

`wecollavo-interview`는 router/intake alias다. 하위 `/interview-*` 명령은
단계별 skill로 승격되었고, router는 실제 하위 명령을 실행하지 않고 적절한
독립 skill을 안내한다.

모든 `wecollavo-*` Skill은 공통 `Next Skill Handoff` 형식으로 다음 Skill을
추천한다. 추천은 자동 실행이 아니며, `client_dir`가 필요한 읽기/쓰기/잠금은
명시적인 `client_dir=clients/<client>` 없이 진행하지 않는다.

Non-linear Entry는 gate 우회가 아니라 현재 입력만으로 가능한 conversational
output 또는 missing condition을 반환하는 지원 규칙이다. 후단 Skill은 필요한
gate condition이 없으면 실행하지 않고 부족 조건을 반환한다.

`proposal-data.json`은 post-lock artifact다. Request Lock 없이 제안 데이터와
고객용 HTML을 만들지 않는다.

## Current v1 Goal

v1은 실제 고객 1건이 위 흐름을 끝까지 통과하면 성공으로 본다.

첫 검증 케이스는 `project/gt-engineering/` 원본 자료를 사용한
`clients/gt-engineering/` 실행 폴더다.

## Non-Negotiables

- AI는 제안하고 Channeul이 최종 판단한다.
- 고객 요청과 실제 병목은 분리한다.
- 고객이 모르는 항목은 Unknown Handling으로 처리한다.
- Bare `$wecollavo-interview`는 client workspace를 읽거나 쓰지 않는다.
- `clients/gt-engineering`은 fixture이며 active client로 추정하지 않는다.
- Workspace read는 명확한 `clients/<client>` 경로 또는 기존 client id 지목이
  있을 때만 허용한다. 최근 작업, 고객명, 문맥 추정으로 읽지 않는다.
- Workspace write/update/lock은 explicit `client_dir=clients/<client>`가
  있을 때만 가능하다.
- Next Skill Handoff는 다음 Skill 추천일 뿐 자동 실행이 아니다.
- Non-linear Entry는 Request Lock, Proposal Review Seed, delivery gate, workspace
  gate를 우회하지 않는다.
- Request Lock 전에는 `proposal-data.json`을 생성하지 않는다.
- Department Handoff는 raw memo가 아니라 Department Analysis Brief다.
- `proposal-review.md`는 HTML 이후 검수가 아니라 pre-render seed다.
- `proposal_review_decision`은 pre-render seed 승인이고,
  `human_review_status`는 고객 전달 승인이다.
- Delivery gate에서는 `proposal_review_decision`과 `human_review_status`가
  모두 `approved`여야 한다.
- Delivery gate에서는 `strategy_context`의 최소 전략 맥락이 비어 있으면 안 된다.
- Track 판정은 domain recommendation보다 먼저 한다.
- 포함 범위에는 반드시 제외 범위가 따라야 한다.
- 자료 확인 전 최종 견적을 확정하지 않는다.
- 제안서는 발표물이 아니라 납품 운영의 시작점이다.
- 모든 sprint는 30일 Proof Loop로 끝난다.
