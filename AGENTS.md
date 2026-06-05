# WeCollavo Live Execution Harness

Last updated: 2026-06-06

Read `docs/source-of-truth.md` first, then `docs/language-contract.md`,
`docs/department-analysis-method.md`, `docs/wecollavo-interview.md`, and
`docs/proposal-review.md`.
Read `docs/motion-policy.md` before suggesting HyperFrames or other motion
output adapters.

This repo is the internal WeCollavo Live Execution Harness. Its job is to turn a
client meeting into a live diagnosis, proposal data, an HTML briefing, a delivery
plan, and a 30-day proof loop.

The architecture is:

```text
Core Policy
+ WeCollavo Interview Subskills
+ Department Analysis Method
+ Client Workspace
+ Proposal Review Seed
+ Proposal Renderer
+ Validation Guardrails
+ Delivery Flow
+ Proof Loop
```

```text
client.json
  -> meeting-state.md

[Live Meeting Skills]
  -> wecollavo-interview-intake
  -> wecollavo-workspace-resume
  -> wecollavo-interview-turn
  -> wecollavo-interview-unknown
  -> wecollavo-request-lock
  -> wecollavo-department-brief
  -> wecollavo-meeting-close

[Proposal Seed]
  -> wecollavo-proposal-review
  -> proposal-review.md
  -> wecollavo-build-proposal
  -> proposal-data.json
  -> proposal.html

[After Client Briefing]
  -> delivery-plan.json
  -> proof-loop.json
```

## Boundaries

- `project/` contains source client materials. Do not edit it unless explicitly asked.
- `clients/` contains harness execution files for each client.
- AI proposes judgment. Channeul makes the final Linchpin decision.
- Customer requests and actual bottlenecks must be separated.
- Unknown customer answers are diagnosis input, not failure.
- `wecollavo-interview` is a router/intake alias. Step-level interview work uses
  independent subskills.
- Bare `$wecollavo-interview` must not read or write client workspaces.
- `clients/gt-engineering` is a fixture, not the active client for bare
  invocation.
- Workspace write/update/lock requires explicit `client_dir=clients/<client>`.
- All `wecollavo-*` skills use `Next Skill Handoff` to recommend the next skill.
  Handoff is not automatic execution.
- Non-linear Entry returns conversational output or missing condition only. It
  must not bypass workspace, Request Lock, Proposal Review Seed, or delivery
  gates.
- `proposal-data.json` is a post-lock artifact. Do not create it while
  `request_lock_status` is `open` or `partial`.
- `proposal-review.md` is a pre-render seed, not after-HTML QA.
- `proposal_review_decision` is pre-render seed approval; `human_review_status`
  is customer delivery approval. Delivery gate requires both to be `approved`.
- Department Handoff must be a Department Analysis Brief, not a raw memo.
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
