# WeCollavo Docs

Last updated: 2026-06-06

These are current v1 operating documents for the WeCollavo Live Execution
Harness.

Read in this order:

1. `source-of-truth.md`
2. `wecollavo-brand-execution-sprint.md`
3. `language-contract.md`
4. `principles.md`
5. `tracks.md`
6. `department-analysis-method.md`
7. `wecollavo-interview.md`
8. `proposal-review.md`
9. `workflow.md`
10. `harness.md`
11. `proposal-system.md`
12. `motion-policy.md`
13. `delivery-os.md`
14. `proof-loop.md`
15. `security.md`
16. `service-catalog.md`
17. `pricing-policy.md`
18. `revision-policy.md`
19. `payment-delivery-policy.md`

Core Policy documents are `service-catalog.md`, `pricing-policy.md`,
`revision-policy.md`, `payment-delivery-policy.md`, `language-contract.md`,
`wecollavo-brand-execution-sprint.md`, `department-analysis-method.md`,
`motion-policy.md`, and `security.md`.
`wecollavo-brand-execution-sprint.md` is current Harness judgment material
extracted from the archive PRD. It can guide interview/proposal judgment, but
archive PRD or GT-specific facts, price, and scope must not be generalized.
Front-stage interview rules are in `wecollavo-interview.md`, and pre-render
proposal seed rules are in `proposal-review.md`.
`wecollavo-interview` is a router/intake alias. Step-level interview work uses
independent skills such as `wecollavo-interview-intake`,
`wecollavo-interview-turn`, `wecollavo-request-lock`, and
`wecollavo-department-brief`.
All `wecollavo-*` skills use `Next Skill Handoff` to recommend the next skill;
handoff is not automatic execution. Non-linear Entry can return conversational
output or missing condition, but it never bypasses workspace, Request Lock,
Proposal Review Seed, or delivery gates.
`proposal_review_decision` is the pre-render seed approval state;
`human_review_status` is the customer delivery approval state.

Client-specific source materials belong in `project/<client>/`.
Harness execution files belong in `clients/<client>/`.
