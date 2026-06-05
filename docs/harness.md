# Harness

Status: v1.1 harness policy
Last updated: 2026-06-05

## Architecture

```text
Core Policy
+ WeCollavo Interview Loop
+ Department Analysis Method
+ Client Workspace
+ Proposal Review Seed
+ Proposal Renderer
+ Validation Guardrails
+ Delivery Flow
+ Proof Loop
```

## Core Policy

Core Policy는 하네스가 판단할 때 사용하는 기준 묶음이다. 가격은 독립 실행
레이어가 아니라 Core Policy의 일부다.

- `docs/service-catalog.md`
- `docs/pricing-policy.md`
- `docs/revision-policy.md`
- `docs/payment-delivery-policy.md`
- `docs/language-contract.md`
- `docs/department-analysis-method.md`
- `docs/proposal-review.md`
- `docs/motion-policy.md`
- `docs/security.md`
- `harness/templates/service-catalog.json`
- `harness/templates/price-breakdown.json`
- `harness/templates/commercial-terms.json`

서비스/가격 정책은 고객 요청을 `pricing_items`와 `commercial_terms`로
정리하기 위한 기준이다. Proposal Renderer는 이 데이터를 사용해 가격 섹션을
생성한다. 내부 산정가는 고객용 원시 표로 노출하지 않고 가격 근거 문장으로
압축한다.

## Client Workspace

고객별 실행 파일은 `clients/<client>/`에 둔다. 원본 고객 자료는
`project/<client>/`에 보존하고, 하네스 실행 중 직접 수정하지 않는다.

```text
client.json
  -> meeting-state.md

[WeCollavo Interview Loop]
  -> Desired Change
  -> SVM / Worldview
  -> Unknown Handling
  -> Assumption Lock
  -> request_lock_status: locked
  -> Department Analysis Brief

[Proposal Seed]
  -> proposal-review.md
  -> proposal-data.json
  -> proposal.html

[After Client Briefing]
  -> delivery-plan.json
  -> proof-loop.json
```

## WeCollavo Interview Loop

WeCollavo Interview Loop는 미팅 중 front-stage 판단을 담당한다. 고객 발화를
받아 다음 질문, Desired Change, SVM/Worldview, Unknown Handling, Track 판정,
범위/가격 신호, 팔면 안 되는 것, 고객에게 말할 수 있는 문장을 만든다.

AI는 고객에게 직접 말하지 않는다. AI Interview Card는 찬늘에게만 보이는
백채널이며, `client_safe_phrase`만 고객 표현으로 압축한다.

`request_lock_status`가 `open` 또는 `partial`이면 Proposal Renderer로 넘기지
않는다. 먼저 `/interview-unknown`, `/interview-lock-check`, `/interview-lock`,
`/interview-handoff`로 요청을 잠그고 Department Analysis Brief를 만든다.

## Proposal Review Seed

`proposal-review.md`는 HTML 생성 후 검수 문서가 아니라 pre-render seed다.
Request Lock과 Department Analysis Brief 이후, `proposal-data.json`을 만들기 전
Desired Change, SVM, Scope, Pricing, Risk, Trust Indicator를 점검한다.

`proposal_review_decision`은 pre-render seed 승인 상태이고,
`human_review_status`는 고객 전달 승인 상태다. 내부 초안에서는 seed approval과
human delivery approval이 불일치할 수 있지만, delivery gate에서는 두 값이 모두
`approved`여야 한다. 단, `proposal_review_decision: pending`인 상태에서
`human_review_status: approved`가 되는 것은 내부 초안에서도 허용하지 않는다.

## Proposal Renderer

v1 렌더러는 locked `proposal-data.json`과 `client.json`을 읽어 static
`proposal.html`을 만든다. HyperFrames는 별도 데이터 구조가 아니라 future output
adapter다.

```bash
python scripts/render_proposal.py clients/<client>
```

## Domain Output Contract

Every domain agent should return:

```text
domain:
confidence:
diagnosis:
ask_next:
recommendation:
scope:
risks:
price_impact:
client_safe_phrase:
internal_note:
```

Domain output is internal. The Linchpin Orchestrator compresses it before client
communication.

## Linchpin Orchestrator Output

- questions to ask now
- one-sentence diagnosis
- recommended offer direction
- what not to sell now
- price framing
- meeting-close checks
- client-safe phrase
