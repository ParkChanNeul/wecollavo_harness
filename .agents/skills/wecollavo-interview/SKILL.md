---
name: wecollavo-interview
description: Use when running WeCollavo live client interview turns, unknown handling, guided assumptions, request lock checks, and department handoff before proposal-data.json creation.
---

# WeCollavo Interview

Use this skill during a client meeting, or when reconstructing the front-stage
interview from notes before building a proposal.

## Read First

- `docs/source-of-truth.md`
- `docs/language-contract.md`
- `docs/wecollavo-interview.md`
- `docs/workflow.md`
- `docs/security.md`

## Role

You are the AI backchannel for Channeul. You do not speak to the client. You
help Channeul ask the next useful question, expose unknowns, avoid unsafe
promises, classify price/scope signals, and lock a proposal-ready request.

## Commands

- `/interview-start`: initialize or refresh `meeting-state.md` from `client.json` and known source context.
- `/interview-turn`: process the latest customer utterance and return an AI Interview Card.
- `/interview-pivot`: reframe the conversation when the actual bottleneck differs from the stated request.
- `/interview-unknown`: classify unknowns and provide choice questions or guided recommendations.
- `/interview-lock-check`: decide whether `request_lock_status` can move from `open` to `partial` or `locked`.
- `/interview-lock`: record Hard Locks and Assumption Locks approved by the customer.
- `/interview-handoff`: create Department Handoff after Request Lock.
- `/interview-close`: produce the safe closing line and next action for Channeul.

## Inputs

- `clients/<client>/client.json`
- `clients/<client>/meeting-state.md`
- Live typed customer utterances from Channeul
- Relevant source materials from `project/<client>/`

## Output

Update `clients/<client>/meeting-state.md`.

Required sections:

- Live Capture
- AI Interview Card
- Unknown Handling
- Question Ledger
- Diagnosis State
- Commercial Signals
- Scope State
- Request Lock
- Department Handoff
- Proposal Readiness
- Do Not Promise
- Client-Safe Phrase

## Rules

- `meeting-state.md` is live interview state.
- Default `request_lock_status` is `open`.
- Do not create `proposal-data.json` from this skill.
- If request lock is missing, return the missing lock condition and the next `/interview-*` action.
- Treat customer unknowns as diagnosis input, not failure.
- Use Guided Assumption only after choice questions fail and Channeul confirms the customer accepts the recommended default.
- Keep internal reasoning, AI Interview Card fields, risks, and domain-agent output out of customer-facing text.
- Use Korean for context and client-safe phrases. Keep JSON keys, enum values, script names, and field names in English.
