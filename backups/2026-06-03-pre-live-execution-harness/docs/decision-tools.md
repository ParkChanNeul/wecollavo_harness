# WeCollavo Decision Tools

Status: Current decision-tool spec
Source: docs/source-of-truth.md and docs/archive-prd-v1.md

## Purpose

Use these tools to turn meeting context into a defensible recommendation. They
support WeCollavo's judgment; they do not replace it.

## Linchpin Scorecard

Score after the meeting.

```text
1. Is the minimum viable audience clear? /10
2. Is the brand promise expressed in customer language? /10
3. Do current assets connect to sales/trust flow? /10
4. Is there a content funnel? /10
5. Is the owner willing to execute and improve? /10
6. Can WeCollavo create visible change within 30 days? /10
```

Recommended judgment:

- 48+ suitable for sprint
- 36-47 scope down or entry package
- 35 or below defer or reject after free advice

Scorecard risk:

- Do not fill the score after the decision merely to justify it.
- Treat borderline scores as scope-down signals, not automatic approval.
- Recalibrate thresholds after the first 3 real projects are scored.

## Media Funnel Map

Media Funnel Map explains how the delivered asset becomes part of trust and
conversion flow.

```text
Interest content  ->  Trust content  ->  Authority content  ->  Conversion content
Problem/empathy       Process/cases      Criteria/compare       Offer/inquiry/meeting
```

Use it to answer:

- What problem or context makes the customer care?
- What proof or process builds trust?
- What standard or comparison creates authority?
- What next action should the customer take?

Avoid generic content advice. The map must connect to the selected track, the
client's actual asset, and the 30-day use plan.

## Proof Loop

Every sprint needs a Proof Loop. Delivery alone is not success.

```text
Before
- old brochure/homepage/content state
- what the client struggled to explain
- why the asset could not be shown externally

After
- where the asset was used
- what message the client can now explain
- whether it was shared or used in a real meeting

30-day signal
- inquiries
- meeting reaction
- content published
- continued execution
- next work request
```

Proof Loop is not a revenue guarantee. Its purpose is to check whether the
client actually used the asset, whether the asset changed the explanation, and
whether a next buying reason appeared.

Client-specific Proof Loop signals belong in `project/<client>/` or
`harness/workspaces/<client>/`.

## Human Linchpin Review

Before delivery, a human operator must review:

- final recommendation
- scope and exclusions
- price and payment terms
- additional-fee conditions
- public claims and confidential information
- delivery wording
- assumptions and missing materials

Only reviewed output should be shown to the client.
