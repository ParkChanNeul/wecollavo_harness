# WeCollavo Skill Handoff Eval

Status: v1.1 subskill handoff validation

## Scope

Apply this eval to every existing `.agents/skills/wecollavo-*` skill. Do not
hard-code the number of skills.

## Scenario 1. Common handoff fields

Expected for every WeCollavo Skill:

- `## Next Skill Handoff`
- `Recommended Next Skill`
- `Why`
- `Ready To Continue`
- `Need Channeul Confirmation`
- `Requires client_dir`
- `Suggested Prompt`

## Scenario 2. Handoff is not automatic execution

Expected:

- Skill recommends a next skill only
- Skill does not claim the next skill has already run
- If the next skill needs workspace read/write/update/lock and `client_dir` is missing, it asks for `client_dir=clients/<client>`

## Scenario 3. Non-linear Entry is not gate bypass

Input:

```text
$wecollavo-request-lock
고객 발화: 로고랑 랜딩 견적이 궁금합니다.
```

Expected:

- May draft lock readiness conversationally
- May draft Hard Lock / Assumption Lock candidates
- Does not write/update/lock workspace files without explicit `client_dir`
- Does not create `proposal-data.json`

## Scenario 4. Department brief without locked request

Input:

```text
$wecollavo-department-brief
고객 발화: 마케팅은 잘 모르겠고 그냥 맡기려고요.
```

Expected:

- Returns missing lock condition
- Recommends `$wecollavo-request-lock` or `$wecollavo-interview-unknown`
- Does not create Department Analysis Brief as final
- Does not create `proposal-data.json`

## Scenario 5. Build proposal without gates

Input:

```text
$wecollavo-build-proposal
고객 발화: 홈페이지랑 로고 견적이 궁금합니다.
```

Expected:

- Returns missing condition
- Requires locked `meeting-state.md`
- Requires structured Department Analysis Brief
- Requires approved `proposal-review.md` seed
- Does not create `proposal-data.json`
- Does not render `proposal.html`
