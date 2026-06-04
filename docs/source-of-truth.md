# WeCollavo Source Of Truth

Status: v1 current source of truth
Last updated: 2026-06-04

## Definition

WeCollavo Live Execution Harness는 내부용 미팅 실행 하네스다.

하네스의 목적은 앱 완성이 아니라 고객 미팅에서 나온 정보를 Channeul의
Linchpin 판단으로 압축하고, 그 판단을 제안 데이터, HTML 브리핑, 납품 계획,
30일 Proof Loop로 연결하는 것이다.

```text
Core Policy
+ Client Workspace
+ Proposal Renderer
+ Delivery Flow
+ Validation Guardrails
+ Proof Loop
```

## Core Policy

Core Policy는 실행 레이어가 아니라 하네스의 판단 기준이다.

- 서비스 분류: `docs/service-catalog.md`
- 가격 기준: `docs/pricing-policy.md`
- 수정 기준: `docs/revision-policy.md`
- 결제/납품 기준: `docs/payment-delivery-policy.md`
- 언어 계약: `docs/language-contract.md`
- 모션/출력 어댑터 기준: `docs/motion-policy.md`
- 보안과 공개 경계: `docs/security.md`

## Core Flow

```text
client.json
  -> meeting-state.md
  -> proposal-data.json
  -> proposal.html
  -> delivery-plan.json
  -> proof-loop.json
```

## Current v1 Goal

v1은 실제 고객 1건이 위 흐름을 끝까지 통과하면 성공으로 본다.

첫 검증 케이스는 `project/gt-engineering/` 원본 자료를 사용한
`clients/gt-engineering/` 실행 폴더다.

## Non-Negotiables

- AI는 제안하고 Channeul이 최종 판단한다.
- 고객 요청과 실제 병목은 분리한다.
- Track 판정은 domain recommendation보다 먼저 한다.
- 포함 범위에는 반드시 제외 범위가 따라야 한다.
- 자료 확인 전 최종 견적을 확정하지 않는다.
- 제안서는 발표물이 아니라 납품 운영의 시작점이다.
- 모든 sprint는 30일 Proof Loop로 끝난다.
