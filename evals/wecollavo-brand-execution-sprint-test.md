# WeCollavo Brand Execution Sprint Eval

Status: v1 brand execution sprint linkage validation

## Scenario 1. Strategic Skills Read Brand Execution Sprint

대상 Skill:

- `wecollavo-interview-turn`
- `wecollavo-interview-unknown`
- `wecollavo-request-lock`
- `wecollavo-department-brief`
- `wecollavo-proposal-review`
- `wecollavo-build-proposal`
- `wecollavo-meeting-close`

기대:

- Read First에 `docs/wecollavo-brand-execution-sprint.md` 포함
- 전략 Skill은 WeCollavo를 제작 외주가 아니라 협업형 브랜드 실행 파트너로 해석
- archive PRD 또는 GT 전용 가격/범위/사실관계를 일반화하지 않음

## Scenario 2. Interview Turn Interprets The Request

Input:

```text
$wecollavo-interview-turn
고객 발화: 로고랑 블로그가 필요해요.
```

기대:

- 고객 요청을 단순 요약하지 않음
- Track 1 / Track 2 중 어디에 가까운지 임시 판단
- 지금 필요한 핵심 브랜드 자산 1개 제안
- 지금 하지 않을 것 제안
- 30일 후 확인할 Proof Loop 신호 제안
- Request Lock 실행 금지

## Scenario 3. Unknown Handling Uses Sprint Diagnosis

Input:

```text
$wecollavo-interview-unknown
고객 발화: 잘 모르겠고 그냥 알아서 해주세요.
```

기대:

- unknown을 실패가 아니라 브랜드 실행 스프린트 진단 입력으로 처리
- 핵심 브랜드 자산 1개 선정에 영향을 주는 unknown 구분
- Proof Loop 신호에 영향을 주는 unknown 구분
- 고객 승인 없는 Assumption Lock 기록 금지

## Scenario 4. Request Lock Requires Sprint Readiness

Input:

```text
$wecollavo-request-lock
로고랑 블로그가 필요하다는 정보만 있음.
```

기대:

- 핵심 브랜드 자산 1개가 불명확하면 `locked` 후보로 가지 않음
- 지금 하지 않을 것이 정리되지 않았으면 `partial` 또는 `open` 후보
- 30일 Proof Loop 신호가 부족하면 `partial` 또는 `open` 후보
- 부족한 조건과 다음 추천 Skill 반환

## Scenario 5. Department Brief Uses Sprint Structure

Input:

```text
$wecollavo-department-brief
locked request를 기준으로 부서별 브리프를 정리해줘.
```

기대:

- raw memo dump 금지
- Brand Diagnosis Map 관점 포함
- Execution Asset Brief 관점 포함
- Next 30 Days Operating Plan 관점 포함
- Proof Loop 기준 포함
- `proposal-data.json` 생성 금지

## Scenario 6. Build Proposal Uses Sprint Proposal Standard

Input:

```text
$wecollavo-build-proposal client_dir=clients/<client> approved proposal-review.md를 기준으로 제안서를 만들어줘.
```

기대:

- raw meeting notes를 그대로 sections로 옮기지 않음
- proposal-review seed와 Department Brief를 바탕으로 구성
- 단순 견적서가 아니라 브랜드 실행 스프린트 제안 기준을 참고
- proposal-data contract와 section ID/order 변경 금지
- `render_proposal.py` 구조 변경 금지
