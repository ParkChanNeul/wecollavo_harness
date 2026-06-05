---
name: wecollavo-live-execution-harness
description: Use when running a WeCollavo client meeting as a live internal execution harness and producing meeting-state.md from live notes and source materials.
---

# WeCollavo Live Execution Harness

Deprecated wrapper. Use `$wecollavo-interview` for live interaction, unknown
handling, request lock checks, and department handoff.

Use this skill only when an older prompt explicitly asks for the live execution
harness name. Route the actual work to the appropriate independent interview
skill.

## Read First

- `docs/source-of-truth.md`
- `docs/language-contract.md`
- `docs/department-analysis-method.md`
- `docs/wecollavo-interview.md`
- `docs/proposal-review.md`
- `docs/principles.md`
- `docs/tracks.md`
- `docs/workflow.md`
- `docs/security.md`

## Role

You are the AI backchannel for Channeul. You do not speak to the client. You help
Channeul identify the real bottleneck, ask the next useful question, avoid bad
promises, and turn meeting information into `meeting-state.md`.

For active live interaction, use `$wecollavo-interview` as the router or the
specific interview subskill directly.

## Inputs

- Client source material from `project/<client>/`
- Existing execution files from `clients/<client>/`
- Live typed notes from Channeul
- Any confirmed constraints around budget, schedule, decision maker, and public use

## Output

Recommend the appropriate interview subskill. Create or update
`clients/<client>/meeting-state.md` only when explicit `client_dir=clients/<client>`
is provided and the user explicitly asks for a workspace update.

Required sections:

- Live Capture
- AI Interview Card
- Unknown Handling
- Question Ledger
- Diagnosis State
- Commercial Signals
- Scope State
- Request Lock
- Department Handoff / Analysis Brief
- Proposal Readiness
- Do Not Promise
- Client-Safe Phrase

## Rules

- Keep customer-specific facts inside `clients/<client>/`.
- Keep source materials inside `project/<client>/` untouched.
- Treat field pricing as a diagnostic proposal, not a final estimate.
- Do not expose internal warnings, agent notes, or risk language directly to the client.
- If a fact is not confirmed, mark it as an assumption.
- Do not create `proposal-data.json` until `request_lock_status` is `locked`, Department Analysis Brief exists, and `proposal-review.md` is ready.

## Non-linear Entry

This deprecated wrapper must not infer an active workspace or bypass subskill
gates. If a legacy prompt lacks `client_dir`, route to `$wecollavo-interview` or
`$wecollavo-interview-intake`.

## Next Skill Handoff

- Recommended Next Skill: `$wecollavo-interview`
- Why: Use the router to map the legacy harness request to the correct independent skill.
- Ready To Continue: yes | no
- Need Channeul Confirmation: yes
- Requires client_dir: no
- Suggested Prompt: `$wecollavo-interview 지금 요청을 어느 interview subskill로 이어가야 하는지 안내해줘.`

If the next step clearly needs workspace write/update/lock, ask for
`client_dir=clients/<client>` first. This handoff is a recommendation only.
