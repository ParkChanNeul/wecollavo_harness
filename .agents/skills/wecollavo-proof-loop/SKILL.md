---
name: wecollavo-proof-loop
description: Use when defining proof-loop.json for WeCollavo follow-up evidence, 30-day usage signals, and next operating proposal criteria.
---

# WeCollavo Proof Loop

Use this skill when the proposal or delivery plan needs evidence criteria for follow-up.

## Read First

- `docs/source-of-truth.md`
- `docs/language-contract.md`
- `docs/proof-loop.md`
- `docs/security.md`

## Inputs

- `clients/<client>/proposal-data.json`
- `clients/<client>/delivery-plan.json`
- Confirmed client use case and channel

## Output

Create or update `clients/<client>/proof-loop.json`.

## Required Fields

- client
- asset_under_test
- before_state
- after_state
- thirty_day_signals
- evidence_to_collect
- follow_up_questions
- retainer_bridge
- stop_conditions

## Rules

- Measure whether the asset is used, not whether it looks complete.
- Track evidence that can support a follow-up operating proposal.
- Include stop conditions so WeCollavo does not keep working without proof of use.

## Non-linear Entry

If `delivery-plan.json`, accepted scope, or proof target is missing, return the
missing condition instead of creating `proof-loop.json`.

## Next Skill Handoff

- Recommended Next Skill: none
- Why: Proof Loop is the final v1 follow-up evidence step.
- Ready To Continue: no
- Need Channeul Confirmation: yes
- Requires client_dir: yes
- Suggested Prompt: `30일 후 proof-loop 신호를 기준으로 후속 운영 제안을 검토하자.`

This handoff is a recommendation only. It does not automatically run another
skill.
