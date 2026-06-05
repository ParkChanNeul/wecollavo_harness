---
name: wecollavo-interview
description: Router/intake alias for WeCollavo interview subskills. Use for bare interview invocations and backward-compatible slash command routing guidance.
---

# WeCollavo Interview Router

`wecollavo-interview` is a compatibility router and intake alias. It does not
execute subcommands directly.

Bare `$wecollavo-interview` must not read, write, update, or lock any client
workspace. It should route to `$wecollavo-interview-intake`.

## Read First

- `docs/source-of-truth.md`
- `docs/language-contract.md`
- `docs/wecollavo-interview.md`
- `docs/department-analysis-method.md`
- `docs/security.md`
- `docs/workflow.md`

## Role

Route legacy `/interview-*` commands to the independent WeCollavo interview
subskills. Do not act as the full interview executor.

## Backward-Compatible Command Mapping

- `/interview-start` -> `$wecollavo-interview-intake` when no workspace is named.
- `/interview-start client_dir=clients/<client>` -> `$wecollavo-workspace-resume`.
- `/interview-turn` -> `$wecollavo-interview-turn`.
- `/interview-pivot` -> `$wecollavo-interview-turn` as a turn-level pivot.
- `/interview-unknown` -> `$wecollavo-interview-unknown`.
- `/interview-lock-check` -> `$wecollavo-request-lock`.
- `/interview-lock` -> `$wecollavo-request-lock`.
- `/interview-handoff` -> `$wecollavo-department-brief`.
- `/interview-close` -> `$wecollavo-meeting-close`.

This mapping is guidance only. The router does not run the target skill for the
user; it tells the user or agent which independent skill to use next.

## Inputs

- Bare interview invocation.
- Legacy `/interview-*` command.
- Optional explicit `client_dir=clients/<client>`.
- Optional clearly named existing client id, used for read-only resume guidance.

## Output

Return a routing note:

- which independent skill to use
- whether the request is Intake, Workspace Read, Temporary Turn, Request Lock,
  Department Brief, or Meeting Close
- whether a `client_dir=clients/<client>` is required before write/update/lock

## Forbidden

- Do not read existing client workspaces on bare invocation.
- Do not infer an active client from recent work, customer name, repo contents,
  or the fact that only one client exists.
- Do not treat `clients/gt-engineering` as active unless explicitly named.
- Do not write, update, or lock workspace files.
- Do not create `proposal-data.json`.
- Do not edit `proposal.html`.
- Do not run parallel agents.

## Workspace Gate

Workspace read is allowed only when the user directly names a `clients/<client>`
path or clearly names an existing client id.

Workspace write/update/lock requires explicit `client_dir=clients/<client>`.
If the user says "meeting-state.md에 반영해줘", "파일에 써줘", or "잠가줘"
without `client_dir`, ask for `client_dir=clients/<client>` first.

## Next Skill Handoff

Use the mapping above to recommend exactly one next skill. More detailed
Cross-Skill Continue Protocol is intentionally deferred to a later phase.
