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
