# WeCollavo Codex Harness

Read `docs/source-of-truth.md` first. Then read the domain document that matches
the task:

- `docs/tracks.md` for Track 1 / Track 2 routing and offer boundaries.
- `docs/live-cockpit.md` for real-time meeting cockpit flow, AI backchannel, field scope, and field price framing.
- `docs/workflow.md` for the fixed meeting-to-proposal data flow.
- `docs/harness.md` for Codex Skill routing, subagent policy, Local LLM boundary, and automation limits.
- `docs/decision-tools.md` for Linchpin Scorecard, Media Funnel Map, Proof Loop, and Human Linchpin Review.
- `docs/estimate-template.md` and `docs/one-page-proposal.md` for Track 1 estimate and sales-material structure.

Use `docs/archive-prd-v1.md` only as the long-form archive for historical
decisions and rationale. Do not use it as the current operating spec, estimate
template, or customer proposal source.

## Harness Boundary

The WeCollavo Harness is a Live Linchpin Harness / Meeting Cockpit. Its primary
job is to amplify Channeul's judgment during the client meeting with an internal
AI backchannel. The downstream job is turning that meeting into a scope, price,
rationale, and customer-ready HTML presentation.
It is not a Claude project, not a generic AI proposal writer, and not a
customer-facing SaaS product.

Use Codex-native surfaces:

- `AGENTS.md` for durable repository instructions.
- `.agents/skills/` for reusable Codex workflows.
- `.codex/agents/` for manually requested parallel review agents.
- `harness/` for templates, checklists, and client workspaces.

Do not port Claude `.claude/agents` or `.claude/skills` files directly. Translate
the intent into Codex Skills and Codex custom agents.

## Operating Flow

```text
live-meeting.md
  -> ai-backchannel.md
  -> proposal-snapshot.md
  -> client-snapshot.md
  -> preview-questions.md
  -> answers.md
  -> diagnosis.md
  -> scope-pricing.md
  -> client-presentation.html
  -> Human Linchpin Review
  -> optional HyperFrames video
```

The first field result is `proposal-snapshot.md`. The full customer-facing
result is `client-presentation.html`.

Final judgment, pricing, public-disclosure decisions, delivery wording, and
scope promises must pass Human Linchpin Review before client delivery.

## Automation Limits

- Do not send client documents automatically.
- Do not treat AI output as the final estimate.
- Do not spawn subagents unless the user explicitly asks for parallel agents.
- Do not expose the Harness as a client-facing product name.
- Do not show the AI backchannel to the client.
