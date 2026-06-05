# WeCollavo Interview Eval

Status: v1 interview loop validation

## Scenario 1. 가격 문의

고객 발화:

> 홈페이지 보고 연락드렸는데요. 로고랑 랜딩페이지 같이 하면 얼마예요?

기대:

- `proposal-data.json` 생성 금지
- `request_lock_status`: `open` 또는 `partial`
- `ask_next` 생성
- 로고 25만부터, 랜딩 기본형 39만부터, 브랜드 랜딩 80만부터 가능성을 안내
- 총액 확정 금지
- 자료 확인 전 최종 견적 금지

## Scenario 2. 고객이 모름

고객 발화:

> 잘 모르겠고 그냥 알아서 잘 해주세요.

기대:

- Unknown Handling 실행
- open question -> choice question -> recommended default -> assumption lock
- 의사결정자 확인
- 방향 변경 시 별도 범위 안내

## Scenario 3. 마케팅 대행 위임

고객 발화:

> 마케팅은 잘 몰라서 그냥 맡기려고요.

기대:

- Operation Gap 또는 Execution Capacity Gap 진단
- 콘텐츠 운영/SNS 운영/체험단 운영을 기본 포함하지 않음
- 월간 운영은 선택 모듈
- 매출 보장 금지

## Scenario 4. Request Lock

충분한 정보:

- 신규 로고
- 브랜드 랜딩페이지
- 원고 없음
- 고객이 방향 제안 위임
- 공개 일정 3주 후
- 예산 100~150만
- SNS 운영 제외

기대:

- `request_lock_status=locked` 가능
- Hard Locks와 Assumption Locks 분리
- Department Handoff 생성 가능
- `proposal-data.json` 생성 가능

## Scenario 5. Department Handoff must not be raw note dump

고객 발화:

> 홈페이지랑 로고가 필요해요. 마케팅은 잘 모르겠고 그냥 알아서 해주세요.

기대:

- 단순 요약 금지
- Desired Change 추론
- SVM이 `broad` 또는 assumption-needed로 표시
- Unknown Handling 실행
- Request Lock 전 `proposal-data.json` 생성 금지
- Department Analysis Brief는 각 부서별 diagnosis, recommendation, scope_impact, price_impact, risks, proposal_points, client_safe_phrase, trust_indicator를 포함
- "로고와 홈페이지가 필요하다"를 그대로 반복하는 수준이면 실패
- 고객에게 말할 수 있는 client_safe_phrase와 내부 분석을 분리

## Scenario 6. Change Alignment

고객 요청:

> 브로셔 예쁘게 다시 만들고 싶어요.

기대:

- requested deliverable: 브로셔
- desired_change: 말로 설명해야 하는 회사를 공식 자료만 봐도 이해되는 회사로 전환
- service_role_in_change: 변화의 증거를 공식 자료화
- risk: 자료 확인 전 최종 페이지/견적 확정 금지

## Scenario 7. SVM Check

고객 답변:

> 모든 고객이 봤으면 좋겠어요.

기대:

- SVM status: `broad`
- ask_next에 가장 먼저 설득해야 할 고객군 질문 포함
- "모두"를 그대로 타겟으로 lock하지 않음
- 필요하면 assumption lock 후보 생성
