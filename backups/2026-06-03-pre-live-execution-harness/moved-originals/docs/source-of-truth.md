# WeCollavo Source Of Truth

Status: Working source of truth
Parent archive: docs/archive-prd-v1.md
Last updated: 2026-06-03

## How to Use This Document

AI agents should read this file first, then read the domain document that matches
the task.

Reading order:

```text
docs/source-of-truth.md
  -> docs/tracks.md
  -> docs/live-cockpit.md
  -> docs/workflow.md
  -> docs/harness.md
  -> docs/decision-tools.md
  -> docs/estimate-template.md or docs/one-page-proposal.md
  -> docs/validation-plan.md
  -> docs/archive-prd-v1.md only for historical rationale
```

Use `docs/archive-prd-v1.md` only as the long-form archive for historical review
logs, prior decisions, and detailed rationale. Do not use it as the primary
operating spec, estimate template, or customer proposal source.

## Product Definition

WeCollavo is an AI-assisted collaborative linchpin partner for small brands.

It helps small brands clarify direction, organize content flow, and produce
brand execution assets. The product is not generic outsourcing and not "AI
agency" positioning. AI is a harness that increases speed, density, and
consistency. The core value is WeCollavo's judgment, collaboration, and
execution.

Core philosophy:

> We combine the customer's field knowledge, WeCollavo's linchpin judgment, and
> an AI harness so small brands can make better decisions and execute faster.

## Harness Identity

The WeCollavo Harness is a **Live Linchpin Harness / Meeting Cockpit**.

Its primary value is not delivery automation. Its primary value is amplifying
WeCollavo's judgment during a client meeting.

```text
client / representative  <->  Channeul  <->  AI Backchannel
                              |
                        Human Linchpin
```

AI does not consult directly with the client. It listens through internal notes
and acts as a backchannel advisor for Channeul: next questions, hidden
bottlenecks, track judgment, risks, scope boundaries, price framing, and proposed
wording.

The client-facing HTML proposal remains important, but it is a downstream output
after Live Cockpit judgment.

## Strategic Principles

1. WeCollavo is a collaborative linchpin partner, not a simple production vendor.
2. AI is a harness, not the pitch.
3. Customers buy clearer judgment, faster execution, and more trustworthy brand assets.
4. Track 1 and Track 2 must not be mixed in one generic offer.
5. Brand assets are not decoration. They are the first usable piece of a content-driven brand system.
6. Proof Loop is mandatory. Delivery alone is not success.
7. Do not build a client portal before recurring demand exists.

## Domain Documents

- `docs/tracks.md`: Track 1 and Track 2 definitions, boundaries, and mixing guardrails.
- `docs/live-cockpit.md`: Live meeting cockpit flow, backchannel rules, and field proposal safety.
- `docs/workflow.md`: The fixed meeting-to-proposal data flow and workspace outputs.
- `docs/harness.md`: Codex Skill harness boundaries, routing, subagent use, and automation limits.
- `docs/decision-tools.md`: Linchpin Scorecard, Media Funnel Map, Proof Loop, and Human Linchpin Review.
- `docs/estimate-template.md`: General Track 1 estimate guide. Do not put customer-specific values here.
- `docs/one-page-proposal.md`: General Track 1 one-page proposal structure.
- `docs/validation-plan.md`: Business/process validation scenarios and confidence gate.

## Customer-Specific Material

General product documents belong in `docs/`.

Client-specific materials belong in `project/<client>/`.

Harness execution outputs belong in `harness/workspaces/<client>/`.

GT Engineering is the current live case, but its specific facts, pricing
judgment, homepage details, and proposal drafts must stay in:

- `project/gt-engineering/`
- `harness/workspaces/gt-engineering/`

Do not move GT-specific conclusions into general templates.

## Open Risks

- Scorecard thresholds are theoretical until 3 real projects are scored.
- Proof Loop ownership is not assigned.
- Track 1 public proof may make WeCollavo look like a corporate brochure fixer unless Track 2 stays visible in strategy.
- No runnable local skill runner exists yet.
- Local LLM security controls are not documented yet.
