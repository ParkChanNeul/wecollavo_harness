# Workflow

The v1 workflow is data-first.

```text
client.json
  -> meeting-state.md
  -> proposal-data.json
  -> proposal.html
  -> delivery-plan.json
  -> proof-loop.json
```

## Step 1. Client

`client.json` records the client's basic identity, track, source materials, and
theme tokens.

## Step 2. Meeting State

`meeting-state.md` is the live operating state. It captures customer utterances,
stated request, actual bottleneck, budget signal, track, domain flags, Q&A, scope
risk, current recommendation, do-not-promise list, and next action.

## Step 3. Proposal Data

`proposal-data.json` converts meeting judgment into the 11-section proposal data
model.

## Step 4. HTML Proposal

`proposal.html` is a static horizontal-style briefing document. It uses customer
theme colors and the 11-section proposal structure.

## Step 5. Delivery Plan

`delivery-plan.json` converts the approved first scope into tasks, dependencies,
review points, and delivery checks.

## Step 6. Proof Loop

`proof-loop.json` records before/after/30-day signals and the retainer bridge.
