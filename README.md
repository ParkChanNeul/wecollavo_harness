# WeCollavo Live Execution Harness

Last updated: 2026-06-06

WeCollavo 내부용 미팅 실행 하네스입니다.

목표는 앱 완성이 아니라 실제 고객 1건에서 아래 흐름이 끝까지 작동하는지 검증하는 것입니다.

```text
client.json
  -> meeting-state.md
  -> proposal-review.md
  -> proposal-data.json
  -> proposal.html
  -> delivery-plan.json
  -> proof-loop.json
```

## 구조

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

최신 실행 흐름은 아래와 같습니다.

```text
client.json
  -> meeting-state.md

[Live Meeting Skills]
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

## 현재 v1 검증 케이스

- 원본 고객 자료: `project/gt-engineering/`
- 실행 산출물: `clients/gt-engineering/`
- 고객용 HTML 제안서: `clients/gt-engineering/proposal.html`

`clients/gt-engineering`은 검증 fixture다. Bare `$wecollavo-interview`의 active
client로 추정하지 않는다.

## 실행 명령

```bash
python scripts/validate_client.py clients/gt-engineering/client.json
python scripts/validate_proposal.py clients/gt-engineering/proposal-data.json
python scripts/render_proposal.py clients/gt-engineering
python scripts/check_proposal_safety.py clients/gt-engineering --allow-pending
```

고객 전달 전에는 `human_review_status`가 `approved`여야 하므로, 기본 안전 검사는 `pending` 상태를 실패 처리한다.
`proposal_review_decision`은 pre-render seed 승인 상태이고,
`human_review_status`는 고객 전달 승인 상태다. 고객 전달 gate에서는 두 값이 모두
`approved`여야 한다.

Core Policy 기준 파일은 `docs/service-catalog.md`, `docs/pricing-policy.md`,
`docs/revision-policy.md`, `docs/payment-delivery-policy.md`,
`docs/language-contract.md`, `docs/department-analysis-method.md`,
`docs/proposal-review.md`, `docs/motion-policy.md`, `docs/security.md`와 아래
템플릿에 둔다.

- `harness/templates/service-catalog.json`
- `harness/templates/price-breakdown.json`
- `harness/templates/commercial-terms.json`

v1의 Proposal Renderer는 static `proposal.html`만 생성한다. HyperFrames는
v1.5 이후 선택 output adapter이며, 별도 데이터 구조를 만들지 않는다.

`wecollavo-interview`는 router/intake alias다. Bare invocation은 client
workspace를 읽지 않고 intake 안내만 하며, 단계별 작업은 독립 skill로 진행한다.
Workspace write/update/lock은 `client_dir=clients/<client>`가 있을 때만 가능하다.

모든 `wecollavo-*` Skill은 공통 `Next Skill Handoff`로 다음 Skill을 추천한다.
추천은 자동 실행이 아니다. 사용자가 "진행", "계속", "다음"이라고 해도 필요한
gate condition이나 `client_dir`가 없으면 먼저 부족 조건을 반환하거나
`client_dir=clients/<client>`를 질문한다.

Non-linear Entry는 현재 입력만으로 conversational output이나 missing condition을
반환하는 지원 규칙이다. Request Lock, Proposal Review Seed, delivery gate,
workspace gate를 우회하지 않는다.

`proposal-review.md`는 HTML 생성 후 검수 문서가 아니라 pre-render seed다.
실제 client seed 파일은 `proposal_review_decision` frontmatter를 사용한다.
`proposal.html`은 문서 형식이며 기본 전달 방식은 로컬 Live Server 브리핑이다.
배포 링크는 기본 전달 방식이 아니다. HyperFrames는 future output adapter이며
이번 v1.1 작업 범위가 아니다.

## 읽는 순서

1. `docs/source-of-truth.md`
2. `docs/language-contract.md`
3. `docs/principles.md`
4. `docs/tracks.md`
5. `docs/department-analysis-method.md`
6. `docs/wecollavo-interview.md`
7. `docs/proposal-review.md`
8. `docs/workflow.md`
9. `docs/harness.md`
10. `docs/proposal-system.md`
11. `docs/motion-policy.md`
12. `docs/delivery-os.md`
13. `docs/proof-loop.md`
14. `docs/security.md`

## 경계

- AI는 고객에게 직접 말하지 않는다.
- `project/` 원본 자료는 수정하지 않는다.
- 고객별 실행 결과는 `clients/<client>/`에 둔다.
- `proposal.html`은 생성물이므로 수동 수정하지 않는다.
- 최종 가격, 범위, 공개 문구, 납품 약속은 Human Linchpin Review 이후 확정한다.
