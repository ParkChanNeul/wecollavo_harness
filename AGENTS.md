# WeCollavo Live Execution Harness

Read `docs/source-of-truth.md` first, then `docs/language-contract.md` and
`docs/wecollavo-interview.md`.
Read `docs/motion-policy.md` before suggesting HyperFrames or other motion
output adapters.

This repo is the internal WeCollavo Live Execution Harness. Its job is to turn a
client meeting into a live diagnosis, proposal data, an HTML briefing, a delivery
plan, and a 30-day proof loop.

The architecture is:

```text
Core Policy
+ WeCollavo Interview Loop
+ Client Workspace
+ Proposal Renderer
+ Delivery Flow
+ Validation Guardrails
+ Proof Loop
```

```text
client.json
  -> meeting-state.md

[WeCollavo Interview Loop]
  -> request_lock_status: locked
  -> department_handoff

[After Request Lock]
  -> proposal-data.json
  -> proposal.html
  -> delivery-plan.json
  -> proof-loop.json
```

## Boundaries

- `project/` contains source client materials. Do not edit it unless explicitly asked.
- `clients/` contains harness execution files for each client.
- AI proposes judgment. Channeul makes the final Linchpin decision.
- Customer requests and actual bottlenecks must be separated.
- Unknown customer answers are diagnosis input, not failure.
- `proposal-data.json` is a post-lock artifact. Do not create it while
  `request_lock_status` is `open` or `partial`.
- Field pricing is not the final estimate before material review.
- Customer-facing output must not expose internal notes or domain-agent output.
- Context language is Korean. Explicit data contracts, field names, enum values,
  script names, and agent output fields remain English.
- v1 output is static `proposal.html`; HyperFrames is a future output adapter,
  not a separate proposal data flow.

## Main Surfaces

- `docs/` for current operating doctrine.
- `.agents/skills/` for Codex workflows.
- `.codex/agents/` for optional domain review agents.
- `harness/schemas/` for JSON shape checks.
- `harness/templates/` for reusable starting points.
- `clients/_template/` for new client setup.
- `evals/` and `logs/` for validation and operating evidence.

## Human Linchpin Review

Final price, scope, public wording, delivery promises, payment terms, and client
disclosure decisions must pass Human Linchpin Review before delivery.
