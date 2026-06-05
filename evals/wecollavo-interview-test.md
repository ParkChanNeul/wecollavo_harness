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

## Scenario 8. Bare invocation should ask intake questions

Input:

```text
$wecollavo-interview
```

기대:

- 기존 client workspace를 읽지 않음
- `clients/gt-engineering`을 active client로 추정하지 않음
- 기존 `request_lock_status`를 언급하지 않음
- `# WeCollavo Interview Intake` 출력
- 신규/기존 고객 여부, 고객명, 미팅 목적, 첫 고객 발화, 관심 서비스, 예산/일정/자료 상태, workspace 연결 여부를 질문
- Next action은 `wecollavo-interview-turn`

## Scenario 9. interview-turn without client_dir must not write files

Input:

```text
$wecollavo-interview /interview-turn
고객 발화: 홈페이지랑 로고 견적이 궁금합니다.
```

기대:

- existing client workspace를 읽지 않음
- `meeting-state.md`를 업데이트하지 않음
- AI Interview Card 출력
- 다음 유용한 질문 생성
- workspace update는 explicit `client_dir=clients/<client>` 또는 explicit write request with client_dir가 필요하다고 안내

## Scenario 10. Write request without client_dir must ask for client_dir

Input:

```text
$wecollavo-interview /interview-turn
고객 발화: 홈페이지랑 로고 견적이 궁금합니다.
meeting-state.md에 반영해줘.
```

기대:

- `clients/gt-engineering`을 추정하지 않음
- 어떤 workspace도 write/update/lock 하지 않음
- 먼저 `client_dir=clients/<client>`를 요청
- Hard Lock / Assumption Lock 기록도 파일 반영이 아니라 초안으로만 제시

## Scenario 11. Explicit workspace read gate

Input:

```text
$wecollavo-interview /interview-start client_dir=clients/gt-engineering
```

기대:

- `clients/gt-engineering`은 fixture이지만 명시되었으므로 read 허용
- `clients/gt-engineering/client.json`과 `clients/gt-engineering/meeting-state.md`를 읽을 수 있음
- 현재 `request_lock_status` 보고
- 다음 독립 skill 추천
- `proposal-data.json` 생성 금지

## Scenario 12. AI Interview Card uses Korean Meeting Coach View

Input:

```text
$wecollavo-interview-turn
고객 발화: 로고랑 랜딩페이지를 같이 하면 얼마인지 궁금합니다.
```

기대:

- `# AI Interview Card` 출력
- 기본 출력에 `내가 들은 내용`, `전략적 해석`, `핵심 병목`, `지금 고객에게 물어볼 질문`, `고객에게 말해도 되는 문장` 포함
- `meeting_state_update_suggestions`를 기본 출력에 그대로 노출하지 않고 `미팅 기록 반영 후보`로 표시
- `request_lock_candidate_status`를 기본 출력에 그대로 노출하지 않고 `요청 잠금 후보 상태`로 표시
- 기본 출력에 `raw_request`, `current_state`, `target_state`, `svm_status`, `price_affecting_unknown` 같은 snake_case 필드명 노출 금지
- AI Interview Card 문맥에서 `meeting_state_updates` 사용 금지
- AI Interview Card 문맥에서 실제 계약 필드인 `request_lock_status`를 lock 실행 상태처럼 사용 금지
- 요청 잠금 후보 상태는 후보 판단이며 파일 업데이트나 lock 실행이 아님
- 필요한 경우 snake_case 필드명은 기본 한글 코치 뷰 뒤의 `Internal Structured Fields`에서만 허용

## Scenario 13. Non-linear unknown entry

Input:

```text
$wecollavo-interview-unknown
고객 발화: 잘 모르겠고 그냥 알아서 해주세요.
```

기대:

- intake 없이도 conversational output 가능
- `# Unknown Handling Card` 출력
- 기본 출력에 `지금 고객이 모르는 것`, `왜 중요한가`, `선택지로 바꾼 질문`, `위콜라보가 제안할 수 있는 기본 전제 후보` 포함
- 기본 출력에 unknown classification snake_case 노출 금지
- Assumption Lock을 파일에 기록하지 않음
- Next Skill Handoff 포함

## Scenario 14. Department brief without locked request returns missing condition

Input:

```text
$wecollavo-department-brief
고객 발화: 홈페이지랑 로고 견적이 궁금합니다.
```

기대:

- Department Analysis Brief를 확정 생성하지 않음
- `proposal-data.json` 생성 금지
- locked request context가 없다는 missing condition 반환
- 추천 next skill은 `wecollavo-request-lock` 또는 부족 unknown 처리 skill

## Scenario 15. Request Lock output avoids field dump

Input:

```text
$wecollavo-request-lock
현재 대화 기준으로 요청 잠금 가능성 확인해줘.
```

기대:

- `# Request Lock Check` 출력
- `지금 확정된 것`, `위콜라보 추천 전제로 잠글 수 있는 것`, `아직 잠그면 안 되는 것`, `가격/범위 때문에 더 확인할 것`, `현재 잠금 판단` 포함
- 기본 출력에 lock 관련 내부 필드명 덤프 금지
- 실제 파일 lock 실행 금지

## Scenario 16. Department Brief output uses Korean department headings

Input:

```text
$wecollavo-department-brief
locked request 초안을 기준으로 부서별 브리프를 정리해줘.
```

기대:

- `# Department Analysis Brief` 출력
- `마케팅 기획 관점`, `가격/범위 관점`, `디자인 관점`, `웹/기술 관점`, `콘텐츠 관점`, `리스크 관점`, `제안서 작성 관점` 포함
- 기본 출력에 부서 key 덤프 금지
- `proposal-data.json` 생성 금지
