---
name: wecollavo-build-delivery-plan
description: Use when converting an accepted WeCollavo proposal scope into delivery-plan.json tasks, owners, dependencies, and acceptance checks.
---

# WeCollavo Delivery Plan

Use this skill after the first engagement scope in `proposal-data.json` is ready to become work.

## Read First

- `docs/source-of-truth.md`
- `docs/language-contract.md`
- `docs/delivery-os.md`
- `docs/security.md`

## Inputs

- `clients/<client>/proposal-data.json`
- `clients/<client>/proposal.html`
- Any confirmed schedule or material constraints

## Output

Create or update `clients/<client>/delivery-plan.json`.

## Required Fields

- engagement_name
- scope_source
- tasks
- dependencies
- client_materials
- decision_points
- acceptance_checks
- timeline
- risks
- proof_loop_link

## Rules

- Convert only the accepted first engagement scope.
- Do not include future production work as committed delivery.
- Every task needs an owner, input, output, due window, and acceptance check.
- Any missing client material must become a dependency, not an invisible assumption.

## Non-linear Entry

If accepted first engagement scope or delivery approval context is missing,
return the missing condition instead of creating `delivery-plan.json`.

## Next Skill Handoff

- Recommended Next Skill: `$wecollavo-proof-loop`
- Why: Use after the accepted delivery plan needs 30-day evidence criteria.
- Ready To Continue: yes | no
- Need Channeul Confirmation: yes
- Requires client_dir: yes
- Suggested Prompt: `$wecollavo-proof-loop client_dir=clients/<client> 기준으로 proof-loop.json 기준을 잡아줘.`

This handoff is a recommendation only. It does not automatically run the next
skill.
