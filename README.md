# WeCollavo Live Execution Harness

WeCollavo 내부용 미팅 실행 하네스입니다.

목표는 앱 완성이 아니라 실제 고객 1건에서 아래 흐름이 끝까지 작동하는지 검증하는 것입니다.

```text
meeting-state.md
  -> proposal-data.json
  -> proposal.html
  -> delivery-plan.json
  -> proof-loop.json
```

## 현재 v1 검증 케이스

- 원본 고객 자료: `project/gt-engineering/`
- 실행 산출물: `clients/gt-engineering/`
- 고객용 HTML 제안서: `clients/gt-engineering/proposal.html`

## 실행 명령

```bash
python scripts/validate_client.py clients/gt-engineering/client.json
python scripts/validate_proposal.py clients/gt-engineering/proposal-data.json
python scripts/render_proposal.py clients/gt-engineering
python scripts/check_proposal_safety.py clients/gt-engineering --allow-pending
```

고객 전달 전에는 `human_review_status`가 `approved`여야 하므로, 기본 안전 검사는 `pending` 상태를 실패 처리한다.

## 읽는 순서

1. `docs/source-of-truth.md`
2. `docs/principles.md`
3. `docs/tracks.md`
4. `docs/workflow.md`
5. `docs/harness.md`
6. `docs/proposal-system.md`
7. `docs/delivery-os.md`
8. `docs/proof-loop.md`
9. `docs/security.md`

## 경계

- AI는 고객에게 직접 말하지 않는다.
- `project/` 원본 자료는 수정하지 않는다.
- 고객별 실행 결과는 `clients/<client>/`에 둔다.
- `proposal.html`은 생성물이므로 수동 수정하지 않는다.
- 최종 가격, 범위, 공개 문구, 납품 약속은 Human Linchpin Review 이후 확정한다.
