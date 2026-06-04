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
