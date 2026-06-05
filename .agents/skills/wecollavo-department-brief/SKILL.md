---
name: wecollavo-department-brief
description: Create a structured WeCollavo Department Analysis Brief after Request Lock without creating proposal-data.json.
---

# WeCollavo Department Brief

Use this skill for the legacy `/interview-handoff` path after Request Lock.

## Read First

- `docs/source-of-truth.md`
- `docs/wecollavo-brand-execution-sprint.md`
- `docs/language-contract.md`
- `docs/wecollavo-interview.md`
- `docs/department-analysis-method.md`
- `docs/proposal-system.md`
- `docs/proposal-review.md`
- `docs/security.md`
- `docs/workflow.md`

## Role

Create a structured Department Analysis Brief from locked customer signals. This
can be conversational output or an explicit workspace update when
`client_dir=clients/<client>` is provided.

Translate the locked request through Brand Diagnosis Map, Execution Asset Brief,
Next 30 Days Operating Plan, and Proof Loop criteria. Do not pass raw notes
forward as the brief.

## Inputs

- Locked request context.
- Hard Lock draft items.
- Assumption Lock draft items.
- Desired Change, SVM, Trust Indicators.
- Optional `client_dir=clients/<client>` for explicit workspace update.

## Output

Default output must be a Korean Department Analysis Brief, not a department key
dump.

Use this shape:

```text
# Department Analysis Brief

## 마케팅 기획 관점
-

## 가격/범위 관점
-

## 디자인 관점
-

## 웹/기술 관점
-

## 콘텐츠 관점
-

## 리스크 관점
-

## 제안서 작성 관점
-
```

Each department should still reason through diagnosis, recommendation, scope
impact, price impact, risks, missing inputs, proposal points, client-safe
phrase, and trust indicator, but the default output should be readable Korean
prose.

When internal handoff is necessary, add an optional final
`Internal Structured Fields` section after the Korean brief.

Always include the common `Next Skill Handoff` section.

If Request Lock context is missing or not locked, return the missing lock
condition instead of creating a Department Analysis Brief.

## Forbidden

- Do not create `proposal-data.json`.
- Do not dump raw customer notes as department handoff.
- Do not read an existing workspace unless a path or existing client id is
  clearly named.
- Do not write/update workspace files without explicit `client_dir`.
- Do not expose internal risks as customer-facing copy.

## Non-linear Entry

This skill can be invoked directly, but direct invocation does not bypass
Request Lock. If locked request context, Hard Locks, or Assumption Locks are
missing, return missing condition and recommend `$wecollavo-request-lock`.

## Next Skill Handoff

- Recommended Next Skill: `$wecollavo-proposal-review`
- Why: Use after the structured Department Analysis Brief is ready.
- Ready To Continue: yes | no
- Need Channeul Confirmation: yes
- Requires client_dir: yes | no
- Suggested Prompt: `$wecollavo-proposal-review client_dir=clients/<client> proposal-review.md pre-render seed를 만들어줘.`

If the meeting needs a client-safe close first, recommend
`$wecollavo-meeting-close` instead.

This handoff is a recommendation only. It does not automatically run the next
skill.
