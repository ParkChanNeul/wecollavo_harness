---
name: wecollavo-live-cockpit
description: Use during or immediately before a WeCollavo client meeting to run the Live Linchpin Harness / Meeting Cockpit: capture live notes, generate internal AI backchannel questions, diagnose hidden bottlenecks, route tracks, frame scope and field pricing, and produce a proposal snapshot without showing AI output to the client.
---

# WeCollavo Live Cockpit

Use this skill to run the internal live meeting cockpit.

## Grounding

Read:

- `docs/source-of-truth.md`
- `docs/tracks.md`
- `docs/live-cockpit.md`
- `docs/harness.md`
- `docs/decision-tools.md`
- `docs/estimate-template.md` when discussing Track 1 pricing

Check the relevant client folder under `project/` and the active workspace under
`harness/workspaces/`.

## Boundary

The AI backchannel is internal only.

Do not:

- show AI backchannel output to the client
- present field pricing as the final estimate
- promise full rebrand, new logo, large rebuild, or unlimited revisions in the room
- hide missing materials behind confident wording
- send client-facing documents automatically

## Workflow

1. **Live Meeting**
   - Create or update `harness/workspaces/<client-slug>/live-meeting.md`.
   - Capture customer utterances, decisions, undecided issues, material requests,
     budget signals, schedule signals, and decision maker signals.

2. **AI Backchannel**
   - Create or update `ai-backchannel.md`.
   - Produce next questions, hidden bottleneck, track judgment, risk signals,
     do-not-sell list, field scope direction, field price frame, and client-safe
     wording for Channeul.

3. **Ask**
   - Recommend diagnostic questions, money questions, and scope questions.
   - Prioritize the question that most improves scope, price, or delivery confidence.

4. **Diagnose And Route**
   - State the current diagnosis and primary track.
   - Separate the customer's stated request from WeCollavo's read of the real bottleneck.
   - Record what should not be sold in this meeting.

5. **Scope And Price**
   - Frame included scope, excluded scope, optional scope, client dependencies,
     change-order triggers, and field pricing.
   - Use the safety ladder: `현장 진단 제안 -> 1차 제안서 -> 최종 견적서`.

6. **Proposal Snapshot**
   - Create or update `proposal-snapshot.md`.
   - Produce a meeting-end or 10-minute-after first proposal snapshot with:
     1. 오늘 미팅 기준 결론
     2. 현재 병목
     3. 추천 작업
     4. 포함 범위
     5. 포함하지 않는 범위
     6. 자료 검토 전 예상 범위
     7. 다음 액션

7. **Close**
   - Tell the client what WeCollavo understood, what will be checked next, what
     the client must send, and when the first proposal or final estimate will be
     delivered.

## Price Language

Use this wording unless the user provides a better client-specific version:

> 오늘은 방향과 예상 범위를 먼저 잡아드릴게요. 다만 정확한 견적은 기존
> 자료를 확인한 뒤 최종 확정하는 게 서로 안전합니다.
