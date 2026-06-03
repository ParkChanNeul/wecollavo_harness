# WeCollavo Live Cockpit

Status: Current primary harness mode
Source: docs/source-of-truth.md

## Purpose

WeCollavo Live Cockpit is a real-time diagnostic consulting cockpit.

It is not a client-facing chatbot and not a delivery automation pipeline. It is
an internal backchannel that helps Channeul listen, diagnose, ask, scope, and
price during a client meeting.

```text
client / representative  <->  Channeul  <->  AI Backchannel
                              |
                        Human Linchpin
```

AI must not talk directly to the client.

AI는 고객에게 직접 말하지 않는다.

The AI backchannel speaks only to Channeul. Channeul translates the judgment into
client-safe language.

## Operating Mode

Use Markdown and Codex conversation, not a separate app UI.

Recommended workspace files:

- `live-meeting.md`: customer utterances, decisions, open issues, material requests, budget and schedule signals.
- `ai-backchannel.md`: next questions, hidden bottleneck, track judgment, risks, do-not-sell list, suggested wording.
- `proposal-snapshot.md`: meeting-end or 10-minute-after first proposal snapshot.

Keep these files in `harness/workspaces/<client-slug>/` when running a real
client case.

## Live Flow

```text
live-start
  -> live-capture
  -> live-read
  -> live-ask
  -> live-diagnose
  -> live-route
  -> live-scope
  -> live-price
  -> live-proposal
  -> live-close
```

### live-start

Before the meeting, capture:

```text
client_name:
industry:
known_request:
meeting_goal:
known_assets:
expected_track:
```

Backchannel output:

- 5 questions to confirm today
- 3 likely bottlenecks
- scope that must not be promised too early
- when to ask about budget

### live-capture

During the meeting, type what the customer says. Keep it raw enough to preserve
phrasing.

Capture:

- customer utterances
- decisions
- undecided issues
- material requests
- budget signals
- schedule signals
- decision maker signals

### live-read

Separate the live notes into:

- stated request
- actual bottleneck
- confirmed facts
- assumptions
- missing inputs
- risk flags

### live-ask

Recommend questions for Channeul to ask next.

Use three categories:

- diagnostic questions
- money questions
- scope questions

The highest-value output of the Live Cockpit is often the next question, not the
answer draft.

### live-diagnose

Update the working diagnosis while the meeting is still happening.

Output:

- current diagnosis
- hidden bottleneck
- what the customer thinks they need
- what WeCollavo believes should happen first
- client-safe framing

### live-route

Choose the primary track.

Output:

```text
primary_track:
reason:
do_not_sell:
secondary_opportunity:
```

If the customer fits both tracks, choose the primary buying job for the first
proposal and keep the secondary opportunity for a later phase.

### live-scope

Draft the field scope.

Output:

- included scope
- excluded scope
- optional scope
- client dependencies
- change-order triggers
- what must not be promised in the room

### live-price

Give a field price frame, not a final estimate.

Use this safety ladder:

```text
Field diagnostic proposal
자료 검토 전 기준

-> First proposal
자료 일부 확인 후 기준

-> Final estimate
전체 자료 확인 후 확정
```

Client-safe wording:

> 오늘은 방향과 예상 범위를 먼저 잡아드릴게요. 다만 정확한 견적은 기존
> 자료를 확인한 뒤 최종 확정하는 게 서로 안전합니다.

### live-proposal

Create a first proposal snapshot before the end of the meeting or within 10
minutes after the meeting.

Required sections:

1. 오늘 미팅 기준 결론
2. 현재 병목
3. 추천 작업
4. 포함 범위
5. 포함하지 않는 범위
6. 자료 검토 전 예상 범위
7. 다음 액션

### live-close

Close the meeting with:

- what WeCollavo understood
- what will be checked next
- what the customer must send
- what is only a field diagnostic proposal
- when the first proposal or final estimate will be delivered

## Guardrails

- Do not show the AI backchannel to the client.
- Do not present field pricing as the final estimate.
- Do not promise full rebrand, new logo, large rebuild, or unlimited revisions in the room.
- Do not hide missing materials behind confident wording.
- Final price, scope, public wording, delivery promise, and payment terms must pass Human Linchpin Review.
