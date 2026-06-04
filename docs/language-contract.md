# Language Contract

Status: v1 current operating contract

이 문서는 WeCollavo Live Execution Harness에서 언어를 다루는 기준이다.
목표는 문장을 모두 같은 언어로 만드는 것이 아니라, 문맥 언어와 명시
계약 언어를 분리해서 데이터 정합성을 지키는 것이다.

```text
문맥 언어 = 한국어
명시 계약 언어 = 영어
```

## Context Language

문맥 언어는 한국어다. 아래 내용은 한국어로 작성한다.

- 고객 상황, 고객 발화, 진단, 병목, 리스크 설명
- 가격 설명, 결제 조건, 수정 기준, 납품 조건
- 제안 문장, 고객-facing HTML 문구, 미팅 후 안내 문구
- Channeul의 운영 판단, Human Linchpin Review 판단 근거

한국어 문장은 고객이 마케팅, 디자인, 홈페이지를 잘 몰라도 바로 이해할 수
있어야 한다. 내부 경고나 agent 판단은 고객에게 직접 노출하지 않고,
client-safe phrase로 다시 써야 한다.

## Explicit Contract Language

명시 계약 언어는 영어다. 아래 값은 한국어로 번역하지 않는다.

- file path: `clients/<client>/proposal-data.json`
- JSON key: `human_review_status`, `pricing_items`, `commercial_terms`
- schema field: `sections[].id`, `sections[].title`
- enum: `pending`, `approved`, `blocked`
- script name and CLI: `python scripts/render_proposal.py clients/<client>`
- agent output field: `domain`, `confidence`, `diagnosis`, `ask_next`,
  `recommendation`, `scope`, `risks`, `price_impact`, `client_safe_phrase`,
  `internal_note`

명시 계약 언어는 Codex, 스키마, 검증 스크립트, 렌더러가 같은 데이터를
가리키기 위한 고정 인터페이스다. 필드명을 한국어로 바꾸면 데이터 흐름이
깨진다.

## Display Language

고객에게 보이는 표시 언어는 한국어다.

- `sections[].id`는 영어 slug를 유지한다.
- `sections[].title`은 한국어 표시명을 사용한다.
- `proposal.html`의 제목, 본문, 가격 설명, 조건 문구는 한국어로 출력한다.
- `proposal.html`은 생성물이므로 직접 수정하지 않는다.

## Proper Nouns

고유명사는 번역하지 않는다.

- Framer
- HyperFrames
- Codex
- URL
- 브랜드명
- 서비스 ID
- 파일명과 경로

## Data Integrity Priority

언어 통일보다 데이터 정합성이 우선이다.

- 스키마와 JSON key는 번역 대상이 아니다.
- enum 값은 영어로 유지한다.
- 고객-facing 문구와 내부 판단 메모를 섞지 않는다.
- 내부 agent output은 고객 문구로 다시 작성한 뒤 제안서에 반영한다.
- 확정되지 않은 사실은 `confirmed_facts`가 아니라 `assumptions`에 둔다.

