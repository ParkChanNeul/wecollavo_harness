# WeCollavo Codex Harness

## 한글 실행 가이드

이 하네스는 터미널에서 실행하는 Python CLI가 아니라, Codex Skill과
작업 파일을 이용해 고객 미팅을 제안 결과물로 바꾸는 내부 운영체계다.[^1]

기본 실행은 미팅 중 Live Cockpit으로 시작한다.

```text
$wecollavo-live-cockpit

harness/workspaces/gt-engineering/을 기준으로
미팅 중 고객 발화, AI 백채널, 현장 제안 스냅샷을 정리해.
고객에게 AI 백채널은 보여주지 않는다.
```

미팅 후 HTML 제안서까지 정리할 때는 아래처럼 Skill을 호출한다.

```text
$wecollavo-proposal-harness

harness/workspaces/gt-engineering/을 기준으로
live-meeting.md, ai-backchannel.md, proposal-snapshot.md를 반영해
미팅 전 프리뷰 질문, 답변 정리, 진단, 범위/가격,
client-presentation.html까지 진행해.
```

미팅 전 질문만 만들 때는 아래 Skill을 쓴다.

```text
$wecollavo-preview-questions

harness/workspaces/gt-engineering/client-snapshot.md를 기준으로
대표님 미팅 전에 볼 프리뷰 질문을 보강해.
```

미팅 후 고객에게 바로 보여줄 HTML 제안서만 만들 때는 아래 Skill을 쓴다.

```text
$wecollavo-html-proposal

harness/workspaces/gt-engineering/의 자료를 바탕으로
client-presentation.html을 만들어.
```

운영 순서는 고정한다.

```text
live-meeting.md
  -> ai-backchannel.md
  -> proposal-snapshot.md
  -> client-snapshot.md
  -> preview-questions.md
  -> answers.md
  -> diagnosis.md
  -> scope-pricing.md
  -> client-presentation.html
  -> Human Linchpin Review
  -> optional HyperFrames
```

Subagent 병렬 리뷰는 자동 실행하지 않는다.[^2] 필요할 때만 Codex에게
명시적으로 요청한다.

```text
$wecollavo-proposal-harness

GT 엔지니어링 제안서를 병렬 리뷰해.
client-context-analyst, scope-pricing-architect,
proposal-storyboarder, risk-proof-loop-reviewer를 각각 subagent로 실행하고,
모든 결과를 기다린 뒤 수정 우선순위를 정리해.
```

최종 가격, 공개 문구, 납품 범위, 추가비 조건은 반드시 Human Linchpin
Review를 통과한 뒤 고객에게 전달한다.[^3]

This folder contains the internal WeCollavo proposal harness.

It is not a Python CLI and not a skill runner. The runnable intelligence lives
in Codex through:

- repo guidance: `AGENTS.md`
- workflows: `.agents/skills/`
- optional parallel reviewers: `.codex/agents/`

The harness folder holds templates, checklists, and per-client workspaces.

## Flow

```text
live-meeting.md
  -> ai-backchannel.md
  -> proposal-snapshot.md
  -> client-snapshot.md
  -> preview-questions.md
  -> answers.md
  -> diagnosis.md
  -> scope-pricing.md
  -> client-presentation.html
  -> Human Linchpin Review
  -> optional HyperFrames
```

## Customer-Facing Output

The first field output is `proposal-snapshot.md`.

The full output is `client-presentation.html`.

It must show:

- the conclusion
- why that conclusion came out
- the meeting Q&A trail
- the client's current situation
- priority order
- first-phase scope
- detailed price decomposition
- additional-fee conditions
- required client materials
- 30-day execution plan
- next production proposal

## Operating Rule

The Harness can accelerate live diagnosis and proposal production, but WeCollavo
makes the final judgment. Do not show the AI backchannel to the client.

[^1]: 여기서 "하네스"는 고객에게 판매하는 제품명이 아니라, WeCollavo가 미팅 중 판단과 질문, 범위, 가격 프레이밍을 빠르게 구조화하기 위해 쓰는 내부 콕핏이다.
[^2]: Codex subagent는 명시적으로 요청했을 때만 병렬 실행한다. 자동 실행 구조로 만들면 비용, 컨텍스트, 파일 충돌 관리가 어려워진다.
[^3]: Human Linchpin Review는 AI 결과물을 그대로 납품하지 않기 위한 최종 검수다. 가격, 범위, 일정, 공개 가능성, 고객이 오해할 수 있는 표현을 사람이 확인한다.
