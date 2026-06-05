# Workflow

Status: v1.1 workflow policy
Last updated: 2026-06-06

The v1 workflow is data-first, but proposal data is created only after Request
Lock.

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

## Step 3. Live Meeting Skills

The interview loop turns a raw customer request into a proposal-ready request.
It does not create `proposal-data.json` while `request_lock_status` is `open` or
`partial`.

Strategic interview skills read `docs/wecollavo-brand-execution-sprint.md` and
interpret the request as a Brand Execution Sprint signal: one core brand asset,
what not to do now, provisional Track 1 / Track 2 fit, and the 30-day Proof Loop
signal. The document is current operating judgment material extracted from the
archive PRD; GT-specific facts, price, or scope must not be generalized.

`wecollavo-interview` is a router/intake alias. It does not execute the
subcommands directly; it recommends the independent skill to use next.

The main flow is skill-name based:

- `wecollavo-interview-intake`
- `wecollavo-workspace-resume`
- `wecollavo-interview-turn`
- `wecollavo-interview-unknown`
- `wecollavo-request-lock`
- `wecollavo-department-brief`
- `wecollavo-meeting-close`

Non-linear Entry is allowed only as conversational support or missing condition
return. It is not permission to bypass Request Lock, Proposal Review Seed, or
workspace write gates.

### Backward Compatibility Mapping

- `/interview-start`: use `wecollavo-interview-intake` by default, or `wecollavo-workspace-resume` for explicit workspace read.
- `/interview-turn`: use `wecollavo-interview-turn`.
- `/interview-pivot`: use `wecollavo-interview-turn` as a turn-level pivot.
- `/interview-unknown`: use `wecollavo-interview-unknown`.
- `/interview-lock-check`: use `wecollavo-request-lock`.
- `/interview-lock`: use `wecollavo-request-lock`.
- `/interview-handoff`: use `wecollavo-department-brief`.
- `/interview-close`: use `wecollavo-meeting-close`.

Workspace read is allowed only when the user directly names a `clients/<client>`
path or clearly names an existing client id. Never infer a workspace from recent
work, customer name, context inference, or repo contents. Workspace
write/update/lock requires explicit `client_dir=clients/<client>`.

`clients/gt-engineering` is a fixture. It is not the active client for bare
interview invocation.

## Step 4. Proposal Review Seed

`proposal-review.md` is a pre-render seed, not after-HTML QA. It checks Desired
Change, SVM, Department Analysis Brief, commercial terms, and trust indicators
before proposal data is created.

`proposal_review_decision` is the pre-render seed approval state.
`human_review_status` is the customer delivery approval state. Internal drafts
may have `proposal_review_decision: approved` while `human_review_status` is
still `pending`, but must not have `proposal_review_decision: pending` while
`human_review_status` is already `approved`. Customer delivery requires both
values to be `approved`.

## Step 5. Proposal Data

`proposal-data.json` is a post-lock artifact. Its template default
`request_lock_status` is `locked`.

If `request_lock_status` is `open` or `partial`, return missing lock conditions
and the recommended interview skill instead of creating proposal data.

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
