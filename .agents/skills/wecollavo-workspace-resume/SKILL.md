---
name: wecollavo-workspace-resume
description: Resume a clearly specified WeCollavo client workspace in read-only mode and recommend the next interview subskill.
---

# WeCollavo Workspace Resume

Use this skill when the user explicitly provides `client_dir=clients/<client>`
or clearly names an existing client id.

## Read First

- `docs/source-of-truth.md`
- `docs/language-contract.md`
- `docs/wecollavo-interview.md`
- `docs/department-analysis-method.md`
- `docs/security.md`
- `docs/workflow.md`

## Role

Read a specifically named client workspace and summarize where to resume the
interview. This skill is read-only.

## Inputs

- `client_dir=clients/<client>`, or a clearly named existing client id.
- `clients/<client>/client.json`.
- `clients/<client>/meeting-state.md`.

## Output

- Client identity summary.
- Current `request_lock_status`.
- Known request, unknowns, and next useful action.
- Recommended next skill.

## Forbidden

- Do not infer a workspace from recent work, customer name, repo state, or
  single-client repo contents.
- Do not write, update, or lock files in read-only resume mode.
- For write/update/lock, route to the appropriate subskill after explicit
  `client_dir=clients/<client>` is provided.
- Do not create `proposal-data.json`.
- Do not treat `clients/gt-engineering` as active unless explicitly named.

## Non-linear Entry

This skill can start from an explicitly named workspace path or existing client
id. It is read-only. If the workspace is only implied by recent work, customer
name, or repo contents, return missing condition and ask for the explicit client
workspace.

## Next Skill Handoff

- Recommended Next Skill: `$wecollavo-interview-turn`
- Why: Use for the next customer utterance after read-only resume.
- Ready To Continue: yes | no
- Need Channeul Confirmation: yes
- Requires client_dir: no
- Suggested Prompt: `$wecollavo-interview-turn client_dir=clients/<client> 고객 발화: <새 답변>`

If unknowns block the request, recommend `$wecollavo-interview-unknown`. If lock
readiness should be checked, recommend `$wecollavo-request-lock`. This handoff is
a recommendation only.
