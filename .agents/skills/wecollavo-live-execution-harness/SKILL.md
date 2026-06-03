---
name: wecollavo-live-execution-harness
description: Use when running a WeCollavo client meeting as a live internal execution harness and producing meeting-state.md from live notes and source materials.
---

# WeCollavo Live Execution Harness

Use this skill when a client meeting is starting, in progress, or being reconstructed from notes.

## Read First

- `docs/source-of-truth.md`
- `docs/principles.md`
- `docs/tracks.md`
- `docs/workflow.md`
- `docs/security.md`

## Role

You are the AI backchannel for Channeul. You do not speak to the client. You help Channeul identify the real bottleneck, ask the next useful question, avoid bad promises, and turn meeting information into `meeting-state.md`.

## Inputs

- Client source material from `project/<client>/`
- Existing execution files from `clients/<client>/`
- Live typed notes from Channeul
- Any confirmed constraints around budget, schedule, decision maker, and public use

## Output

Create or update `clients/<client>/meeting-state.md`.

Required sections:

- Meeting Metadata
- Customer Request
- Customer Words
- Actual Bottleneck
- Track Decision
- Domain Flags
- Scope Risk
- Budget and Pricing Signals
- Required Materials
- Decisions Made
- Open Questions
- Do Not Promise
- Client-Safe Proposal Line
- Next File to Build

## Rules

- Keep customer-specific facts inside `clients/<client>/`.
- Keep source materials inside `project/<client>/` untouched.
- Treat field pricing as a diagnostic proposal, not a final estimate.
- Do not expose internal warnings, agent notes, or risk language directly to the client.
- If a fact is not confirmed, mark it as an assumption.
