---
client_id: gt-engineering
client_name: GT 엔지니어링
workflow_stage: live_interview
track: Track 1
pricing_status: field_diagnostic_proposal
human_review_status: pending
request_lock_status: partial
next_file: proposal-review.md
---

# GT 엔지니어링 Meeting State

Client: GT 엔지니어링
Operator: Channeul
Source: `project/gt-engineering/`
Current file flow: `client.json -> meeting-state.md -> Request Lock -> proposal-review.md -> proposal-data.json -> proposal.html -> delivery-plan.json -> proof-loop.json`

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

- `raw_request`: 기존 브로셔, 홈페이지, 로고/CI 프로토타입을 공식 소개 자산으로 정리하고 싶다는 요청.
- `desired_change`: 말로 설명해야 이해되는 회사를 공식 자료와 홈페이지만 봐도 신뢰할 수 있는 회사로 전환한다.
- `current_state`: 기존 제작물은 있으나 공개 가능한 회사 정보, 사업 메시지, 자료 제공 범위, 우선순위가 아직 정리되지 않았다.
- `target_state`: 외부 제출과 영업 대화에서 바로 사용할 수 있는 공식 회사소개서와 홈페이지 콘텐츠 기준을 갖춘다.
- `tension`: 낮은 비용으로 넓은 범위를 처리하고 싶지만 자료와 승인 경로가 정리되지 않으면 최종 견적과 일정이 흔들린다.
- `change_type`: trust_change
- `smallest_viable_market`: broad; 고객, 제휴사, 투자자, 관공서/입찰, 내부 영업팀 중 1순위 확인 필요.
- `worldview`: 외부 이해관계자가 사업 영역과 신뢰 근거를 빠르게 확인해야 하는 B2B 공식 자료 맥락.
- `trust_indicator`: 기존 브로셔, 홈페이지, 로고 프로토타입을 출발점으로 관찰하고 하지 않을 범위와 별도 산정 조건을 먼저 제시한다.
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

## Desired Change

- Raw Request: 기존 브로셔를 정리하고, 납품된 홈페이지를 실제 회사 정보로 마감하며, 로고/CI 프로토타입 적용 범위를 판단한다.
- Current State: 기존 자산은 있으나 공개 가능한 회사 정보, 사업별 설명, 프로젝트/사진 자료, 홈페이지 더미 데이터 교체 범위가 정리되지 않았다.
- Target State: 고객, 제휴사, 투자자, 관공서/입찰, 내부 영업팀 중 우선 대상에게 공식적으로 보여줄 수 있는 소개 자산 기준을 만든다.
- Tension: 전체 비용은 낮게 유지하고 싶지만 요구 범위가 넓고 자료 제공 범위가 미확정이다.
- Change Type: trust_change
- Required Asset: 공식 회사소개서 목차/페이지 구성안, 홈페이지 콘텐츠 구조안, 로고/CI 적용 범위표.

## Smallest Viable Market

- SVM Status: broad
- First Audience: 고객, 제휴사, 투자자, 관공서/입찰, 내부 영업팀 중 1순위 확인 필요
- Worldview: 외부 이해관계자는 복수 사업 영역을 짧은 시간 안에 신뢰할 수 있는 증거로 확인하고 싶어한다.
- Exclusion: 블로그/인사이트 운영, 전체 CI/BI 재정의, 전체 홈페이지 개편은 1차 착수에서 제외한다.
- Viability Signal: 기존 PPT, 브로셔, Framer 홈페이지, 로고 프로토타입이 있어 1차 정리의 출발점은 있다.
- Founder-Market Fit: 대표 또는 회장이 최종 판단에 직접 관여할 가능성은 있으나 확인 필요.

## Trust Indicators

- Warm Pistachio Signal: 기존 브로셔, Framer 홈페이지, 로고 프로토타입을 모두 관찰한 뒤 한 번에 섞인 병목을 분리한다.
- Strategic No Signal: 전체 제작비, 전체 페이지 수, 전체 홈페이지 마감, 로고 신규 제작을 미팅 중 확정하지 않는다.
- Judgment Benchmark: 자료 확인, 페이지 범위, 콘텐츠 작성 범위, 로고/이미지 보정 범위를 최종 견적 기준으로 둔다.
- Status Shift Narrative: 여러 사업 영역을 말로 설명해야 하는 상태에서 공식 소개 자산만으로 신뢰를 얻는 상태로 이동한다.
- Dip / Sustainability Signal: 자료 수급과 승인 경로가 지연될 수 있으므로 30일 안에 범위표와 본 제작 견적 기준을 먼저 만든다.

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

## Department Handoff / Analysis Brief

### marketing_planning

- diagnosis: 복수 사업 영역을 하나의 공식 소개 흐름으로 묶어야 하나 1순위 제출 대상이 아직 확인되지 않았다.
- recommendation: 제출 대상별 메시지 우선순위와 공식 회사소개서 목차를 먼저 정리한다.
- scope_impact: 1차 착수에는 목차, 메시지 흐름, 홈페이지 콘텐츠 구조 기준을 포함한다.
- price_impact: 대상과 페이지 범위가 확정되기 전에는 본 제작비를 확정하지 않는다.
- risks: 관공서/입찰용, 제휴용, 영업용 목적이 섞이면 페이지와 문구 범위가 확장될 수 있다.
- missing_inputs: 공식 회사소개서 1순위 제출 대상, 홈페이지 우선 마감 페이지.
- proposal_points: 공식 소개 자산 기준 수립을 먼저 제안한다.
- client_safe_phrase: 먼저 보여줄 대상과 자료 범위를 정하면 제작비와 일정도 훨씬 명확해집니다.
- trust_indicator: 기존 자산을 모두 관찰한 뒤 우선순위를 나누는 판단을 보여준다.

### commercial_pricing

- diagnosis: 낮은 비용 선호와 넓은 요청 범위 사이의 간극이 크다.
- recommendation: 1차 착수 구간과 본 제작 구간을 분리한다.
- scope_impact: 페이지 수, 원고 작성, 이미지 보정, 로고/CI 범위 변경은 추가 산정 조건으로 둔다.
- price_impact: 1차 착수는 150만~200만 원 기준으로 설명하되 최종 견적은 자료 확인 후 산정한다.
- risks: 자료 미제공, 피드백 초과, 방향 변경, 긴급 일정은 비용과 일정 리스크다.
- missing_inputs: 자료 제공 범위, 최종 외부 공개 목표일, 승인 경로.
- proposal_points: 최종 견적이 아니라 1차 진단/구조화 착수 방식임을 명확히 쓴다.
- client_safe_phrase: 이번 금액은 전체 제작비 확정이 아니라 본 제작 범위를 명확히 잡기 위한 1차 착수 구간입니다.
- trust_indicator: 최종 견적 오해를 막는 전략적 no를 포함한다.

### design

- diagnosis: 기존 브로셔와 로고 프로토타입은 출발점이지만 유지, 리터칭, 변경 방향이 확정되지 않았다.
- recommendation: Track 1에서는 유지 또는 리터칭 가능성을 우선 검토한다.
- scope_impact: 신규 로고, 브랜드 가이드, 응용물 제작은 별도 범위로 둔다.
- price_impact: 로고/CI 변경 폭에 따라 추가 비용이 발생할 수 있다.
- risks: "알아서" 진행하면 나중에 취향 변경과 반복 수정으로 이어질 수 있다.
- missing_inputs: 로고 방향, 기존 원본 파일, 적용 대상.
- proposal_points: 디자인은 취향 맞춤보다 공식 신뢰 자산을 만드는 방향으로 설명한다.
- client_safe_phrase: 기존 로고 방향을 먼저 정해야 홈페이지와 회사소개서의 톤도 안정적으로 맞출 수 있습니다.
- trust_indicator: 하지 않을 디자인 범위와 별도 산정 조건을 명확히 한다.

### web_development

- diagnosis: Framer 홈페이지는 납품 상태지만 실제 회사 정보와 더미 데이터 교체 범위가 필요하다.
- recommendation: 회사 소개, 사업 분야, 대표 프로젝트, 문의 동선의 우선 마감 범위를 확인한다.
- scope_impact: 단순 콘텐츠 교체와 메뉴/CTA/폼/CMS 변경을 분리한다.
- price_impact: 폼, 지도, 예약, CMS, SEO/GEO 세부 세팅은 별도 산정 가능성이 있다.
- risks: 전체 페이지 동시 마감은 자료 수급 병목을 키울 수 있다.
- missing_inputs: Framer 접근 권한, 우선 페이지, 문의 수신 담당자 정보.
- proposal_points: 홈페이지 마감은 더미 데이터를 실제 공개 가능한 회사 콘텐츠로 바꾸는 작업이라고 설명한다.
- client_safe_phrase: 홈페이지 전체를 한 번에 확정하기보다 먼저 보여줄 페이지부터 실제 정보로 마감하는 방식이 안전합니다.
- trust_indicator: 플랫폼과 운영 역량에 맞춘 현실적 범위를 제안한다.

### content

- diagnosis: 공개 가능한 사업 설명문, 프로젝트 리스트, 인증/협력사 자료가 아직 정리되지 않았다.
- recommendation: 고객 제공 자료와 WeCollavo 정리 자료의 경계를 먼저 분리한다.
- scope_impact: 원고 신규 작성과 기술 원고 정리는 별도 범위 또는 본 제작 산정 기준이 된다.
- price_impact: 자료 정리 대행 범위가 커질수록 비용과 일정이 늘어난다.
- risks: 공개 가능 여부가 확인되지 않은 사진/프로젝트/협력사 자료를 확정 표현으로 쓰면 안 된다.
- missing_inputs: 사업 분야별 공식 설명문, 프로젝트 공개 가능 여부, 사진/인증/협력사 자료.
- proposal_points: 자료 제공 기준과 마감일을 고객이 이해할 수 있게 쓴다.
- client_safe_phrase: 자료가 준비될수록 비용과 일정은 줄고, 저희가 직접 정리해야 하는 범위가 커질수록 비용은 늘어납니다.
- trust_indicator: 콘텐츠 범위를 숨기지 않고 가격 영향으로 연결한다.

### risk_guard

- diagnosis: 최종 견적 오해, 자료 제공 지연, 승인 경로 분리, 범위 확장 가능성이 있다.
- recommendation: 확정 견적, 전체 납품일, 전체 페이지 수, 무제한 수정은 약속하지 않는다.
- scope_impact: 1차 착수 결과 없이 본 제작 범위와 최종 납품 범위를 고정하지 않는다.
- price_impact: 변경, 추가 피드백, 긴급 일정은 별도 협의 조건으로 둔다.
- risks: 최종 의사결정자가 분리되어 있으면 피드백과 일정이 지연될 수 있다.
- missing_inputs: 최종 의사결정자, 자료 제공 담당자, 외부 공개 목표일.
- proposal_points: final estimate notice와 추가비 조건을 가격 섹션에 반복한다.
- client_safe_phrase: 자료와 승인 경로가 확인된 뒤에 최종 제작비와 일정이 확정됩니다.
- trust_indicator: 빠른 제안이 날림이 아니라 자료 확인 전 확정하지 않는 판단임을 보여준다.

### proposal_writer

- diagnosis: 고객용 문장은 브로셔 재디자인보다 공식 소개 자산 마감과 신뢰 전환으로 설명해야 한다.
- recommendation: 가격보다 왜 1차 착수가 필요한지 먼저 설명한다.
- scope_impact: 오늘의 결론, 왜 이런 결론이 나왔는가, 1차 착수 범위, 가격 분해표에 분석 브리프를 반영한다.
- price_impact: 150만~200만 원은 전체 제작비가 아니라 구조화 착수 구간이라고 명시한다.
- risks: 내부 분석어와 위험 표현을 그대로 고객용 HTML에 노출하지 않는다.
- missing_inputs: 고객에게 보여줄 최종 전달 문구는 Human Review 필요.
- proposal_points: 가정 안내, 자료 요청, 추가비 조건, 30일 계획을 읽기 쉽게 연결한다.
- client_safe_phrase: GT 엔지니어링은 공식 소개 자산의 기준을 먼저 세운 뒤 본 제작 범위를 명확히 산정하는 방식이 적합합니다.
- trust_indicator: 고객이 자신의 상황을 정확히 이해받았다고 느끼는 제안 문장을 만든다.

## Proposal Readiness

- Status: partial
- Missing before proposal-review:
  - 공식 회사소개서 1순위 제출 대상
  - 홈페이지 우선 마감 페이지
  - 고객 제공 자료와 WeCollavo 정리 자료의 경계
  - 로고 방향
  - 외부 공개 목표일
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
