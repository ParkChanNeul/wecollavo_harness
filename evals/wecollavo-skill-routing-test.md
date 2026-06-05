# WeCollavo Skill Routing Eval

Status: v1.1 interview subskill routing validation

## Scenario 1. Router does not execute subcommands

Input:

```text
$wecollavo-interview /interview-unknown
```

Expected:

- `wecollavo-interview` acts as router/intake alias
- Does not execute unknown handling itself
- Recommends `$wecollavo-interview-unknown`
- Does not read/write/update/lock workspace files

## Scenario 2. Slash command mapping

Expected mapping:

- `/interview-start` -> `wecollavo-interview-intake` or `wecollavo-workspace-resume`
- `/interview-turn` -> `wecollavo-interview-turn`
- `/interview-pivot` -> `wecollavo-interview-turn`
- `/interview-unknown` -> `wecollavo-interview-unknown`
- `/interview-lock-check` -> `wecollavo-request-lock`
- `/interview-lock` -> `wecollavo-request-lock`
- `/interview-handoff` -> `wecollavo-department-brief`
- `/interview-close` -> `wecollavo-meeting-close`

## Scenario 3. Fixture is not active client

Input:

```text
$wecollavo-interview
```

Expected:

- `clients/gt-engineering` is treated only as a fixture
- The router does not infer it as active client
- No workspace read occurs
- Intake guidance is returned

## Scenario 4. Clear existing client id permits read only

Input:

```text
gt-engineering 기준으로 이어서 봐줘.
```

Expected:

- `gt-engineering` is an existing client id, so workspace read is allowed
- Write/update/lock is not allowed without `client_dir=clients/gt-engineering`
- Next skill recommendation is `$wecollavo-workspace-resume`

## Scenario 5. Request lock without client_dir is draft only

Input:

```text
/interview-lock
```

Expected:

- Recommends `$wecollavo-request-lock`
- May draft Hard Lock / Assumption Lock items conversationally
- Does not write/update/lock workspace files
- Asks for `client_dir=clients/<client>` before file reflection

## Scenario 6. Department brief does not create proposal data

Input:

```text
/interview-handoff client_dir=clients/gt-engineering
```

Expected:

- Recommends `$wecollavo-department-brief`
- Can create a conversational Department Analysis Brief
- Can update the explicit workspace only if asked to write
- Must not create `proposal-data.json`
