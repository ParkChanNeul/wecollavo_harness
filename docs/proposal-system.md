# Proposal HTML System

The proposal is generated static HTML in v1.

Do not manually edit `proposal.html`. Update `proposal-data.json` and
`client.json`, then render:

```bash
python scripts/render_proposal.py clients/<client>
```

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

The price section is generated from `commercial_terms` and must include payment
terms, revision/feedback rounds, extra-cost conditions, and the final-estimate
notice.

The proposal should feel like a briefing deck, but it remains one self-contained
HTML file in v1.
