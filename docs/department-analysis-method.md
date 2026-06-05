# Department Analysis Method

Status: v1.1 analysis method
Last updated: 2026-06-05

## Purpose

Department Handoff를 raw note dump가 아니라 Department Analysis Brief로 정의한다.

단일 AI 오케스트레이터가 고객 발화를 Desired Change, SVM, Linchpin Lens, Trust
Indicator, Department Method Card를 통해 분석하게 한다.

병렬 에이전트 없이도 부서별 분석 렌즈를 적용한다.

## Core Principle

Department Handoff는 고객 발화를 받아 적은 메모가 아니다.
Request Lock 이후, 각 부서 관점에서 진단, 추천, 범위 영향, 가격 영향,
리스크, 제안서 반영 포인트, 고객용 표현, 신뢰 지표를 정리한 분석 브리프다.

Customer words are raw signals, not final requirements.
Do not summarize customer words as-is.
Transform raw signals into change, promise, trust gap, asset gap, scope, pricing,
and risk.

## Desired Change Method

고객이 요청한 산출물 뒤에 있는 상태 변화를 찾는다.

질문:

- 고객은 무엇을 만들고 싶다고 말했는가?
- 실제로 누구를 어떤 상태에서 어떤 상태로 바꾸고 싶은가?
- 현재 상태는 무엇인가?
- 원하는 상태는 무엇인가?
- 그 변화가 일어나려면 어떤 긴장이나 불안이 해소되어야 하는가?
- 그 변화를 증명할 자산은 무엇인가?

필드:

- `raw_request`
- `current_state`
- `target_state`
- `tension`
- `change_type`
- `required_asset`

`change_type`:

- `belief_change`
- `behavior_change`
- `perception_change`
- `identity_change`
- `trust_change`
- `community_change`
- `local_recognition_change`
- `operation_change`

서비스별 해석:

- 로고 = 변화의 약속을 시각화
- 홈페이지/랜딩 = 변화의 이유와 경로를 설명
- 브로셔/회사소개서 = 변화의 증거를 공식 자료화
- 콘텐츠 = 변화의 약속을 반복
- 인플루언서/체험단 = 사람들이 말할 이유가 있는 경험 설계

## Smallest Viable Market Method

SVM은 단순히 작은 타겟이 아니라, 고객이 처음으로 깊게 섬겨야 할 가장 작은
유효 문화다.

주의:

- 모두를 대상으로 하지 않는다.
- 인구통계가 아니라 세계관, 불안, 욕망, 기대를 본다.
- 좁지만 비즈니스로 유효해야 한다.
- 이 서비스가 누구를 위한 것이 아닌지도 말할 수 있어야 한다.
- 이미 존재하거나 성장 가능한 작은 문화를 찾아야 한다.
- 창업자/브랜드가 지속적으로 섬길 수 있어야 한다.

필드:

- `svm_status`: `undefined | broad | narrow_but_not_viable | viable | locked`
- `first_audience`
- `worldview`
- `exclusion`
- `viability_signal`
- `founder_market_fit`

질문:

- 가장 먼저 설득해야 할 고객군은 누구인가?
- 그들은 무엇을 불안해하는가?
- 그들이 믿을 수 있는 증거는 무엇인가?
- 이번 제안에서 과감히 제외할 고객군은 누구인가?
- 이 고객군이 실제로 돈을 내거나 반복 수요를 만들 가능성이 있는가?

## Linchpin Lens

위콜라보의 린치핀 역량은 AI가 대체하기 어려운 판단력, 창의력, 연결력이다.

필드:

- `judgment`
- `initiative`
- `humanity`
- `tactical_trap`
- `pattern_interruption`
- `status_shift`

질문:

- 이 고객이 전술의 늪에 빠져 있는 지점은 무엇인가?
- AI나 템플릿이 대신할 수 없는 판단은 무엇인가?
- 위콜라보가 고객에게 줄 수 있는 안정감, 확신, 위상은 무엇인가?
- 기존 방식과 다르게 보여줄 패턴 단절은 무엇인가?

## Trust Indicator Layer

위콜라보의 빠른 제안이 날림이 아니라 고도의 기획 판단임을 증명하는 신뢰
지표다.

필드:

- `warm_pistachio_signal`
- `strategic_no_signal`
- `judgment_benchmark`
- `status_shift_narrative`
- `dip_response`

설명:

- `warm_pistachio_signal`: 고객이 "이 팀은 나를 관찰했다"고 느끼는 작은 디테일
- `strategic_no_signal`: 하지 않을 것, 거절할 것, 별도 산정할 것을 명확히 하는 신뢰 신호
- `judgment_benchmark`: 왜 이 제안이 나왔는지 판단 기준을 보여주는 신뢰 신호
- `status_shift_narrative`: 고객이 어떤 위상으로 변화하는지 설명하는 신뢰 신호
- `dip_response`: 30일 실행 계획 안에서 예상 정체 구간과 대응책을 보여주는 신뢰 신호

## WeCollavo Diagnosis Equation

```text
Linchpin Judgment
× Desired Change
× Service Target
× Smallest Viable Market
× Worldview
× Brand Promise
× Tension
× Pattern Interruption
× Trust Gap
× Asset Gap
× Execution Capacity
× Budget Reality
× Timeline Reality
- Tactical Trap
- Risk
= Recommended Scope + Price Band + Proposal Direction
```

이 식은 견적 계산기가 아니다. 고객 발화가 어떤 변화, 시장, 약속, 신뢰 격차,
자산 격차, 실행 범위, 가격 리스크로 연결되는지 판단하기 위한 분석 프레임이다.

## Department Method Cards

### marketing_planning

분석 기준:

- `desired_change`
- `smallest_viable_market`
- `worldview`
- `promise`
- `trust_gap`
- `permission_path`

핵심 질문:

- 고객은 누구를 어떤 상태에서 어떤 상태로 바꾸고 싶은가?
- 가장 먼저 섬길 작은 시장은 누구인가?
- 현재 문제는 유입 부족인가, 신뢰 부족인가, 전환 구조 부족인가?
- 광고보다 먼저 자산 정리가 필요한가?

### commercial_pricing

분석 기준:

- `budget_reality`
- `timeline_reality`
- `scope_volatility`
- `price_affecting_unknowns`
- `tactical_trap_cost`

핵심 질문:

- 이 요청은 시작가로 처리 가능한가?
- 고객이 모르는 부분이 가격을 흔드는가?
- 기획/구조화가 포함되어야 하는가?
- 최소 착수와 본 제작을 나눠야 하는가?

### design

분석 기준:

- `brand_asset_state`
- `promise_visualization`
- `worldview_fit`
- `status_signal`
- `taste_change_risk`

핵심 질문:

- 기존 로고/브랜드 자산이 있는가?
- 이 디자인은 고객 취향을 맞추는가, 브랜드 약속을 기억시키는가?
- "알아서 해주세요"가 나중에 취향 변경 리스크가 되는가?

### web_development

분석 기준:

- `landing_vs_homepage_vs_solution`
- `permission_path`
- `cms_api_db_need`
- `platform_fit`
- `maintenance_capacity`

핵심 질문:

- 이건 랜딩인가, 기본 홈페이지인가, 웹솔루션인가?
- CMS/API/DB 요구가 숨어 있는가?
- Framer/Builder/직접 개발 중 무엇이 맞는가?
- 고객이 운영할 사람이나 자료를 갖고 있는가?

### content

분석 기준:

- `message_clarity`
- `source_material_gap`
- `promise_repetition`
- `tribe_language`
- `content_operation_capacity`

핵심 질문:

- 고객이 원고를 줄 수 있는가?
- 고객의 offer가 10초 안에 이해되는가?
- 콘텐츠는 업로드인가, 약속의 반복인가?
- 콘텐츠 운영까지 필요한가?

### risk_guard

분석 기준:

- `overpromise_risk`
- `ethical_risk`
- `decision_risk`
- `scope_creep_risk`
- `dip_or_culdesac`

핵심 질문:

- 매출 보장을 기대하고 있는가?
- 무제한 수정을 기대하는가?
- 최종 의사결정자가 따로 있는가?
- 자료 제공이 지연될 가능성이 있는가?
- 이 마케팅은 우리가 자랑스러워할 수 있는가?

### proposal_writer

분석 기준:

- `change_narrative`
- `client_readability`
- `assumption_clarity`
- `next_action`
- `customer_safe_language`

핵심 질문:

- 이 제안서는 고객을 설득하는가, 고객이 자신의 변화를 이해하게 돕는가?
- 가격보다 이유가 먼저 설명되는가?
- 내부 분석어가 고객용 문장으로 바뀌었는가?

## Department Analysis Brief Format

모든 structured `department_handoff`는 아래 구조를 따른다.

- `diagnosis`
- `recommendation`
- `scope_impact`
- `price_impact`
- `risks`
- `missing_inputs`
- `proposal_points`
- `client_safe_phrase`
- `trust_indicator`
