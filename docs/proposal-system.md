# Proposal HTML System

Status: v1.1 proposal renderer policy
Last updated: 2026-06-05

The proposal is generated static HTML in v1.

Do not manually edit `proposal.html`. Update `proposal-data.json` and
`client.json`, then render:

```bash
python scripts/render_proposal.py clients/<client>
```

`proposal-data.json` is a post-lock artifact. Do not create or render it from
raw meeting notes while `request_lock_status` is `open` or `partial`. First use
the WeCollavo Interview Loop to create Request Lock and structured Department
Analysis Brief.

`proposal-review.md` is a pre-render seed, not an after-HTML QA document.
Proposal Renderer assumes proposal data has already passed Request Lock,
Department Analysis Brief, and proposal-review seed.

`proposal_review_decision` is the pre-render seed approval state.
`human_review_status` is the customer delivery approval state. Customer delivery
safety requires both values to be `approved`; internal draft checks may allow
`proposal_review_decision: approved` while `human_review_status` is still
`pending`. Internal drafts must not have `proposal_review_decision: pending`
while `human_review_status` is already `approved`.

`strategy_context` is not rendered directly in v1, but delivery safety requires
minimum non-empty strategic context before customer delivery.

It must follow 11 sections:

1. 오늘의 결론
2. 왜 이런 결론이 나왔는가
3. 미팅 질문과 답변
4. 고객 상황 진단
5. 우선순위
6. 1차 착수 범위
7. 가격 분해표
8. 추가비 발생 조건
9. 필요한 자료
10. 30일 실행 계획
11. 본 제작 제안

The price section must include:

> 본 제안은 미팅 내용 기준의 1차 제안이며, 최종 견적은 기존 자료 확인 후 확정됩니다.

The price section is generated from `pricing_items` and `commercial_terms`. It
must include public starting price, minimum project fee, pricing rationale,
payment terms, revision/feedback rounds, extra-cost conditions, delivery
condition, and the final-estimate notice.

If `assumptions` or `assumption_locks` are used, the customer-facing proposal
must explain the assumption basis in Korean. A recommended phrase is:

> 이번 제안은 아래 가정을 기준으로 작성되었습니다.

The proposal must not expose internal notes, AI Interview Card fields, or domain
agent output.

## Output Adapter

v1 output adapter is HTML only.

```text
proposal-review.md -> proposal-data.json -> proposal.html
```

HyperFrames is a future output adapter, not a separate data source. The proposal
should feel like a briefing deck, but it remains one self-contained HTML file in
v1.

`proposal.html` is a document for local Live Server briefing by default. A
deployment link is not the default delivery method.

See `docs/motion-policy.md` for motion and HyperFrames boundaries.
