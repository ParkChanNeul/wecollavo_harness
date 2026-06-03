# WeCollavo Harness

Status: Current harness spec
Source: docs/live-cockpit.md, AGENTS.md, and .agents/skills/

## Purpose

The WeCollavo Harness is a Live Linchpin Harness / Meeting Cockpit. It helps
Channeul structure confusion, ask better questions, identify the real bottleneck,
route the track, frame scope, and give safe field pricing during a live client
meeting.

It also supports downstream proposal production, but proposal production is not
the core identity.

It is not a customer-facing product name, not a Claude project, not a generic AI
proposal writer, not a client-facing chatbot, and not a SaaS product.

## Codex-Native Surfaces

- `AGENTS.md`: durable repository instructions.
- `.agents/skills/`: reusable Codex workflows.
- `.codex/agents/`: manually requested parallel review agents.
- `harness/`: templates, checklists, and client workspaces.

Do not port Claude `.claude/agents` or `.claude/skills` files directly. Translate
the intent into Codex Skills and Codex custom agents.

## Skill Routing

Use specialized skills instead of one giant prompt.

| Situation | Skill | Purpose |
| --- | --- | --- |
| Customer wants one thing but needs another | `/office-hours` | Reframe the real buying job and bottleneck |
| Scope may expand beyond what should be sold | `/plan-ceo-review` | Separate what to sell from what not to sell |
| Materials, timeline, cost, or failure modes are unclear | `/plan-eng-review` | Clarify scope, checklist, failure modes, and Proof Loop |
| Visual trust is weak | `/plan-design-review` | Check design risk for the asset or page |
| Logo, CI, BI, or brand-system direction is needed | `/design-consultation` | Decide brand-system direction |
| Customer-facing wording is needed | `/copywriting` | Draft proposal, message, website, or follow-up copy |
| Content operation may follow | `/content-strategy` | Build Media Funnel Map and 30-day plan |
| Homepage delivery needs checking | `/qa-only` | Check links, dummy content, responsive behavior, and forms |

Skill output is internal input. Do not forward it directly to the customer.
WeCollavo must judge, edit, and make it client-safe.

For live meetings, prefer `$wecollavo-live-cockpit` before downstream proposal
skills. Use `$wecollavo-proposal-harness` after live notes need to become
workspace artifacts and HTML.

## Subagent Policy

Subagents are optional and manual.

Use subagents only when the user explicitly asks for parallel review. Recommended
roles:

- `client-context-analyst`
- `scope-pricing-architect`
- `proposal-storyboarder`
- `risk-proof-loop-reviewer`

Wait for all summaries, consolidate them, and avoid parallel edits to the same
output file.

## Local LLM Boundary

Local LLM is allowed for first-pass processing when client confidentiality
matters.

Allowed:

- Meeting summary
- Missing material checklist
- Homepage dummy-data replacement table
- Company profile outline draft
- Client question list
- Linchpin Scorecard draft
- Skill routing recommendation

Not allowed:

- Final estimate
- Public-disclosure judgment
- Legal or bid wording
- Executive profile fabrication
- Project achievement exaggeration
- Automatic client document sending
- Replacing WeCollavo's accept/reject judgment

Local LLM reduces external AI transfer risk, but does not eliminate security
risk. Local storage, logs, backups, device loss, and human handoff still need
controls.

## Automation Limits

- Do not send client documents automatically.
- Do not treat AI output as the final estimate.
- Do not spawn subagents unless the user explicitly asks for parallel agents.
- Do not expose "Harness" as a client-facing product name.
- Do not show the AI backchannel to the client.
- Do not promise unlimited revisions, guaranteed revenue, or unreviewed public claims.

Customer-facing explanation:

> We use an internal AI-assisted review workflow after the meeting to organize
> missing materials, scope, homepage content, and next actions. AI helps us check
> for gaps faster, but WeCollavo makes the final judgment.
