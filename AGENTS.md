# WeCollavo Live Execution Harness

Read `docs/source-of-truth.md` first.

This repo is the internal WeCollavo Live Execution Harness. Its job is to turn a
client meeting into a live diagnosis, proposal data, an HTML briefing, a delivery
plan, and a 30-day proof loop.

```text
client.json
  -> meeting-state.md
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
- Field pricing is not the final estimate before material review.
- Customer-facing output must not expose internal notes or domain-agent output.

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
