---
client_id: gt-engineering
client_name: GT 엔지니어링
workflow_stage: live_interview
track: Track 1
pricing_status: field_diagnostic_proposal
human_review_status: pending
request_lock_status: partial
next_file: proposal-data.json
---

# GT 엔지니어링 Meeting State

Client: GT 엔지니어링
Operator: Channeul
Source: `project/gt-engineering/`
Current file flow: `client.json -> meeting-state.md -> Request Lock -> proposal-data.json -> proposal.html -> delivery-plan.json -> proof-loop.json`

## Live Capture

### Meeting Metadata

- Meeting type: 회사소개서/홈페이지/브랜드 자산 마감 상담
- Decision maker: 대표 또는 회장 직접 의사결정 가능성이 높음
- Main use case: 고객, 제휴사, 투자자, 관공서/입찰, 내부 영업팀에 보여줄 공식 소개 자료
- External deadline: 미확정

### Customer Utterances

> 홈페이지와 브로셔 중 무엇이 먼저인지, 어디까지 해야 하는지 아직 명확하지 않은 상태로 보인다.

> 가격을 먼저 알고 싶지만, 자료와 범위가 확정되지 않으면 전체 제작비는 흔들릴 수밖에 없다.

### Customer Request

- 기존 브로셔를 다시 정리하거나 공식 회사소개서로 사용할 수 있게 만들고 싶다.
- 납품된 홈페이지를 실제 회사 정보로 마감하고 싶다.
- 기존 로고/CI 프로토타입을 유지할지, 리터칭할지, 변경할지 판단이 필요하다.
- 전체 비용은 낮게 유지하고 싶지만, 필요한 범위는 넓게 열려 있다.

## AI Interview Card

- `what_i_heard`: 공식 소개 자료, 홈페이지 콘텐츠, 로고 적용 범위가 한 번에 섞여 있다.
- `strategic_decode`: 고객의 표면 요청은 브로셔/홈페이지 수정이지만 실제 병목은 공개 가능한 회사 정보 구조화다.
- `bottleneck_hypothesis`: 자료 제공 담당자와 최종 의사결정자가 분리될 경우 일정과 수정 범위가 흔들릴 수 있다.
- `marketing_diagnosis_equation`: Goal, Audience, Trust Gap, Asset Gap, Budget Reality, Timeline Reality가 아직 partial이다.
- `ask_next`: 공식 회사소개서를 가장 먼저 제출할 대상과 홈페이지 우선 마감 페이지를 확인한다.
- `unknowns`: 외부 공개 목표일, 1순위 제출 대상, 고객 제공 자료 범위, 로고 방향, 공개 가능한 프로젝트/사진.
- `guided_options`: 제출 대상은 관공서/입찰, 제휴사, 고객, 투자자, 내부 영업팀 중 우선순위로 선택하게 한다.
- `default_recommendation`: 1차 착수 구간에서 회사소개서 목차, 홈페이지 콘텐츠 구조, 로고 적용 범위를 먼저 잠근다.
- `assumption_to_lock`: 의사결정자가 대표 또는 회장이고, 1차 착수 이후 본 제작 범위를 산정한다는 전제.
- `service_mapping`: 회사소개서/브로셔 구조기획형, 홈페이지 콘텐츠 마감, 로고/CI 작업 범위 판단.
- `price_scope_signals`: 1차 착수 구간은 150만~200만 원 기준으로 설명하되 최종 견적은 자료 확인 후 산정한다.
- `risks`: 전체 제작비를 먼저 확정하면 페이지 수, 콘텐츠 작성, 로고/이미지 보정 범위가 커질 수 있다.
- `do_not_promise`: 전체 제작비, 전체 페이지 수, 홈페이지 전 페이지 마감, 로고 신규 제작을 미팅 중 확정하지 않는다.
- `client_safe_phrase`: 전체 제작비를 바로 확정하기보다 1차 착수 구간에서 자료와 범위를 정리한 뒤 본 제작 견적을 명확하게 산정하는 방식을 제안드립니다.
- `meeting_state_updates`: Request Lock 전 확인 질문과 자료 요청을 우선한다.
- `request_lock_status`: partial

## Unknown Handling

### Harmless Unknown

- 주요 고객사 로고 사용 가능 여부

### Proposal Blocking Unknown

- 공식 회사소개서의 1순위 제출 대상
- 홈페이지에서 우선 마감해야 하는 페이지
- 고객이 직접 제공 가능한 자료와 WeCollavo가 정리해야 하는 자료의 경계

### Price Affecting Unknown

- 회사소개서 예상 페이지 수
- 홈페이지 적용 범위
- 로고/CI 유지, 리터칭, 변경 방향
- 프로필 사진, 현장 사진, 프로젝트 정보의 공개 가능 여부

### Risk Unknown

- 최종 외부 공개 목표일
- 자료 제공 담당자와 최종 의사결정자의 승인 경로

### Guided Assumption Candidates

- 제출 대상이 확정되지 않으면 관공서/입찰과 제휴사를 1순위 가정으로 두고 메시지 구조를 만든다.
- 로고 방향이 확정되지 않으면 기존 프로토타입 유지 또는 리터칭을 Track 1 기본값으로 둔다.
- 홈페이지 전체가 아니라 회사 소개, 사업 분야, 대표 프로젝트, 문의 동선을 우선 마감한다.

## Question Ledger

| Turn | Asked | Customer Answer | Result | Next Action |
|------|-------|-----------------|--------|-------------|
| 1 | 공식 회사소개서를 가장 먼저 제출할 대상은 누구인가? | 미확정 | proposal_blocking_unknown | `/interview-turn` |
| 2 | 홈페이지에서 우선 마감해야 하는 페이지는 무엇인가? | 미확정 | proposal_blocking_unknown | `/interview-unknown` |
| 3 | 기존 로고 프로토타입은 유지, 리터칭, 변경 중 어느 방향인가? | 미확정 | price_affecting_unknown | `/interview-unknown` |

## Diagnosis State

- Goal: 외부 제출 가능한 공식 소개 자산 만들기
- Audience: 고객, 제휴사, 투자자, 관공서/입찰, 내부 영업팀 중 우선순위 미확정
- Trust Gap: 복수 사업 영역을 한 메시지 체계로 정리해야 한다.
- Asset Gap: 기존 브로셔, 홈페이지, 로고 프로토타입은 있으나 공식 공개용 자료 기준이 부족하다.
- Channel Fit: 홈페이지와 회사소개서가 동시에 외부 신뢰 자산으로 쓰일 가능성이 높다.
- Offer Clarity: 브로셔 재디자인이 아니라 공식 소개 자산 마감으로 설명해야 한다.
- Execution Capacity: 자료 수급과 승인 경로가 일정 병목이다.
- Budget Reality: 낮은 비용 선호와 넓은 요청 범위 사이의 간극이 크다.
- Timeline Reality: 외부 공개 목표일이 미확정이다.
- Risk: 전체 제작비를 먼저 확정하면 범위 변경과 추가 비용 분쟁 가능성이 크다.
- Recommended Scope: 1차 착수 구간에서 자료, 목차, 홈페이지 콘텐츠 구조, 로고 적용 범위를 먼저 정리한다.
- Price Band: 1차 착수 구간 150만~200만 원 기준, 최종 견적은 자료 확인 후 산정.
- Proposal Direction: 공식 회사소개서/홈페이지 콘텐츠 기준 수립 후 본 제작 전환.

## Commercial Signals

- Field diagnostic proposal: 1차 착수 구간 150만~200만 원을 제안할 수 있다.
- First written proposal: 공식 회사소개서 목차, 홈페이지 콘텐츠 구조안, 로고 작업 범위표, 추가 작성 콘텐츠 목록을 산출물로 제시한다.
- Final estimate: 페이지 수, 콘텐츠 작성 범위, 홈페이지 적용 범위, 로고/이미지 보정 범위 확정 후 별도 산정한다.
- Payment signal: 1차 착수 구간은 선결제 100% 기준으로 설명한다.
- Revision/feedback signal: 기획/범위 산정 문서 1회, 고객용 HTML 제안서 2회 기준으로 설명한다.

## Scope State

### Track Decision

- Track: Track 1
- Reason: 완전한 브랜드 전환이 아니라, 이미 있는 브로셔/홈페이지/로고 출발점을 외부 제출 가능한 공식 자산으로 마감하는 작업이 우선이다.
- Track switch trigger: CI/BI를 새로 정의하거나 그룹 전체 브랜드 체계 재설계가 본격화되면 Track 2로 전환한다.

### Scope Draft

- Included:
  - 기존 브로셔, PPT, 홈페이지, 로고 파일 검토
  - 공식 회사소개서 목차와 페이지 구성안
  - 홈페이지 페이지별 콘텐츠 구조안과 더미 데이터 교체 범위
  - 로고/CI 유지, 리터칭, 변경 범위 판단
  - 고객 제공 자료와 WeCollavo 정리 자료 경계 분리
- Excluded:
  - 전체 CI/BI 재정의
  - 블로그/인사이트 운영
  - 전체 홈페이지 개편 확정
  - 모든 이미지/인물 사진 보정
  - 본 제작 최종 페이지 수 확정
- Needs lock:
  - 1순위 제출 대상
  - 홈페이지 우선 마감 페이지
  - 자료 제공 마감일
  - 로고 방향

## Request Lock

- `request_lock_status`: partial
- Hard Locks:
  - GT 엔지니어링은 복수 사업 영역을 운영한다.
  - 기존 브로셔 제작 이력과 기존 PPT 콘텐츠가 있다.
  - Framer 홈페이지는 납품된 상태지만 더미 데이터 교체가 필요하다.
  - 기존 로고/CI 프로토타입이 있다.
- Assumption Locks:
  - 대표 또는 회장이 최종 의사결정에 직접 관여할 가능성이 높다.
  - 1차 착수 결과를 기준으로 본 제작 범위와 견적을 산정한다.
- Lock blockers:
  - 공식 회사소개서 1순위 제출 대상
  - 홈페이지 우선 마감 페이지
  - 자료 제공 범위
  - 외부 공개 목표일

## Department Handoff

- `marketing_planning`:
  - 제출 대상별 메시지 우선순위와 공식 회사소개서 목차를 정리한다.
- `commercial_pricing`:
  - 1차 착수 구간과 본 제작 구간을 분리하고, 페이지/콘텐츠/로고 범위별 추가비 조건을 정리한다.
- `design`:
  - 기존 브로셔와 로고 프로토타입을 기준으로 유지/리터칭/변경 판단안을 만든다.
- `web_development`:
  - Framer 홈페이지의 더미 데이터 교체 범위, 페이지 우선순위, 문의 동선을 확인한다.
- `content`:
  - 사업 분야별 공식 설명문, 프로젝트 리스트, 인증/협력사 자료를 콘텐츠 구조로 정리한다.
- `risk_guard`:
  - 자료 제공 지연, 승인 경로 분리, 최종 견적 오해, 범위 확장 리스크를 점검한다.
- `proposal_writer`:
  - 고객용 문장은 공식 소개 자산 마감과 1차 착수 방식 중심으로 정리한다.

## Proposal Readiness

- Status: partial
- Missing before proposal-data:
  - 공식 회사소개서 1순위 제출 대상
  - 홈페이지 우선 마감 페이지
  - 고객 제공 자료와 WeCollavo 정리 자료의 경계
  - 로고 방향
  - 외부 공개 목표일
- Recommended next command: `/interview-lock-check`

## Do Not Promise

- 전체 제작비를 미팅 중 최종 견적으로 확정하지 않는다.
- 홈페이지 전체 페이지 마감, 회사소개서 전체 페이지 수, 로고/CI 변경을 한 번에 포함한다고 말하지 않는다.
- 고객 자료가 없는데 WeCollavo가 모든 콘텐츠를 같은 비용 안에서 대신 작성한다고 약속하지 않는다.
- AI 이미지 보정이나 인물 사진 개선을 승인 없이 진행한다고 말하지 않는다.
- 1차 착수 결과 없이 본 제작 일정과 최종 납품일을 고정하지 않는다.

## Client-Safe Phrase

GT 엔지니어링은 브로셔 하나를 다시 예쁘게 만드는 문제가 아니라, 여러 사업 영역을 외부 제출 가능한 공식 회사소개서와 홈페이지 콘텐츠로 정리해야 하는 상황입니다. 그래서 전체 제작비를 바로 확정하기보다 1차 착수 구간에서 자료, 목차, 홈페이지 콘텐츠 구조, 로고 적용 범위를 먼저 정리한 뒤 본 제작 견적을 명확하게 산정하는 방식을 제안드립니다.
