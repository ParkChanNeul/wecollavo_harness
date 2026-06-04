# Workflow

The v1 workflow is data-first, but proposal data is created only after Request
Lock.

```text
client.json
  -> meeting-state.md

[WeCollavo Interview Loop]
  -> /interview-start
  -> /interview-turn 반복
  -> /interview-pivot
  -> /interview-unknown
  -> /interview-lock-check
  -> /interview-lock
  -> /interview-handoff
  -> /interview-close

[After Request Lock]
  -> proposal-data.json
  -> proposal.html
  -> delivery-plan.json
  -> proof-loop.json
```

## Step 1. Client

`client.json` records the client's basic identity, track, source materials, and
theme tokens.

## Step 2. Meeting State

`meeting-state.md` is the live interview state. It captures customer utterances,
AI Interview Card output, unknown handling, question ledger, diagnosis state,
commercial signals, scope state, Request Lock, Department Handoff, do-not-promise
list, and client-safe phrase.

The default `request_lock_status` in `meeting-state.md` is `open`.

## Step 3. WeCollavo Interview Loop

The interview loop turns a raw customer request into a proposal-ready request.
It does not create `proposal-data.json` while `request_lock_status` is `open` or
`partial`.

- `/interview-start`: initialize the live state from `client.json` and source context.
- `/interview-turn`: process each customer utterance and return the next question.
- `/interview-pivot`: change direction when the real bottleneck differs from the stated request.
- `/interview-unknown`: classify unknowns and guide choices.
- `/interview-lock-check`: decide whether enough information exists for Request Lock.
- `/interview-lock`: record Hard Locks and Assumption Locks.
- `/interview-handoff`: prepare Department Handoff.
- `/interview-close`: close the meeting with client-safe next steps.

## Step 4. Proposal Data

`proposal-data.json` is a post-lock artifact. Its template default
`request_lock_status` is `locked`.

If `request_lock_status` is `open` or `partial`, return missing lock conditions
and the recommended `/interview-*` action instead of creating proposal data.

## Step 5. HTML Proposal

`proposal.html` is a static horizontal-style briefing document. It uses customer
theme colors and the 11-section proposal structure.

## Step 6. Delivery Plan

`delivery-plan.json` converts the approved first scope into tasks, dependencies,
review points, and delivery checks.

## Step 7. Proof Loop

`proof-loop.json` records before/after/30-day signals and the retainer bridge.
