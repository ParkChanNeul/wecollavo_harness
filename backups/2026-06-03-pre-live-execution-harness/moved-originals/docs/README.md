# WeCollavo Docs

This directory contains general WeCollavo product documents only.

Client-specific materials belong in `project/<client>/`.
Harness execution outputs belong in `harness/workspaces/<client>/`.

## Reading Order

1. `source-of-truth.md`
   - Current product definition, strategic principles, document routing, and customer-specific material boundaries.
   - Read this first.

2. `tracks.md`
   - Track 1 and Track 2 definitions, target customers, offer boundaries, and mixing guardrails.

3. `live-cockpit.md`
   - Live Linchpin Harness / Meeting Cockpit flow for real-time meeting diagnosis, AI backchannel, field scope, and field price framing.

4. `workflow.md`
   - Fixed meeting-to-proposal flow from `client-snapshot.md` to `client-presentation.html`.

5. `harness.md`
   - Codex Skill harness boundary, skill routing, subagent policy, Local LLM boundary, and automation limits.

6. `decision-tools.md`
   - Linchpin Scorecard, Media Funnel Map, Proof Loop, and Human Linchpin Review.

7. `estimate-template.md`
   - General Track 1 estimate guide.
   - Do not put GT-specific pricing or customer assumptions here.

8. `one-page-proposal.md`
   - General Track 1 one-page proposal copy.
   - Use as sales material structure, not as a customer-specific proposal.

9. `validation-plan.md`
   - Business/process validation plan.
   - Use to check whether the offer and harness are producing evidence.

10. `archive-prd-v1.md`
   - Historical PRD and review archive.
   - Use only when old rationale or full review context is needed.

## Data-Flow Guardrail

```text
docs/source-of-truth.md
  -> docs/tracks.md
  -> docs/live-cockpit.md
  -> docs/workflow.md
  -> docs/harness.md
  -> docs/decision-tools.md
  -> docs/estimate-template.md or docs/one-page-proposal.md
  -> project/<client>/*
  -> harness/workspaces/<client>/client-snapshot.md
  -> preview-questions.md
  -> answers.md
  -> diagnosis.md
  -> scope-pricing.md
  -> client-presentation.html
```

Customer-specific conclusions must not flow back into general templates.
