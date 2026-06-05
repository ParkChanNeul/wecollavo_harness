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

[Proposal Seed]
  -> proposal-review.md
  -> proposal-data.json
  -> proposal.html

[After Client Briefing]
  -> delivery-plan.json
  -> proof-loop.json
```

## Step 1. Client

`client.json` records the client's basic identity, track, source materials, and
theme tokens.

## Step 2. Meeting State

`meeting-state.md` is the live interview state. It captures customer utterances,
AI Interview Card output, Desired Change, SVM/Worldview, trust indicators,
unknown handling, question ledger, diagnosis state, commercial signals, scope
state, Request Lock, Department Analysis Brief, do-not-promise list, and
client-safe phrase.

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
- `/interview-handoff`: prepare structured Department Analysis Brief.
- `/interview-close`: close the meeting with client-safe next steps.

## Step 4. Proposal Review Seed

`proposal-review.md` is a pre-render seed, not after-HTML QA. It checks Desired
Change, SVM, Department Analysis Brief, commercial terms, and trust indicators
before proposal data is created.

## Step 5. Proposal Data

`proposal-data.json` is a post-lock artifact. Its template default
`request_lock_status` is `locked`.

If `request_lock_status` is `open` or `partial`, return missing lock conditions
and the recommended `/interview-*` action instead of creating proposal data.

`proposal-data.json` must be created from locked `meeting-state.md`, structured
Department Analysis Brief, and `proposal-review.md` seed.

## Step 6. HTML Proposal

`proposal.html` is a static horizontal-style briefing document. It uses customer
theme colors and the 11-section proposal structure.

## Step 7. Delivery Plan

`delivery-plan.json` converts the approved first scope into tasks, dependencies,
review points, and delivery checks.

## Step 8. Proof Loop

`proof-loop.json` records before/after/30-day signals and the retainer bridge.
