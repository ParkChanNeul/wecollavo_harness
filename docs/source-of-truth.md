# WeCollavo Source Of Truth

Status: v1 current source of truth
Last updated: 2026-06-03

## Definition

WeCollavo Live Execution Harness is an internal brand execution OS.

It diagnoses a client meeting in real time, lets domain AI agents propose
questions, strategy, scope, pricing, and risks, lets Channeul make the final
Linchpin judgment, then converts that judgment into an HTML proposal, delivery
plan, and 30-day proof loop.

```text
Live Linchpin Cockpit
+ Domain Agent Team
+ Proposal HTML System
+ Delivery OS
+ Validation Guardrails
+ Proof Loop
```

## Core Flow

```text
client.json
  -> meeting-state.md
  -> proposal-data.json
  -> proposal.html
  -> delivery-plan.json
  -> proof-loop.json
```

## Current v1 Goal

v1 succeeds when one real client case can run through the full flow above.

The first validation case is `clients/gt-engineering/`, using source materials
from `project/gt-engineering/`.

## Non-Negotiables

- AI suggests. Channeul decides.
- Customer request and actual bottleneck are separate fields.
- Track routing happens before domain recommendations.
- Every included scope must have matching exclusions.
- Do not finalize estimates before material review.
- The proposal starts delivery operations, not just presentation.
- Every sprint ends with a 30-day Proof Loop.
