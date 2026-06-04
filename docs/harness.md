# Harness

## Layers

1. Live Meeting Cockpit
2. Meeting State
3. Domain Agent Team
4. Linchpin Orchestrator
5. Proposal HTML System
6. Delivery OS
7. Proof Loop
8. Pricing OS

## Pricing OS

Pricing OS maps customer requests to `pricing_items` before the proposal is
rendered. It uses:

- `docs/service-catalog.md`
- `docs/pricing-policy.md`
- `docs/revision-policy.md`
- `docs/payment-delivery-policy.md`
- `harness/templates/service-catalog.json`
- `harness/templates/price-breakdown.json`
- `harness/templates/commercial-terms.json`

The proposal renderer uses `pricing_items` and `commercial_terms` to generate the
price section. Internal price bands are not exposed as raw customer-facing price
tables; they are compressed into pricing rationale.

## Domain Output Contract

Every domain agent should return:

```text
domain:
confidence:
diagnosis:
ask_next:
recommendation:
scope:
risks:
price_impact:
client_safe_phrase:
internal_note:
```

Domain output is internal. The Linchpin Orchestrator compresses it before client
communication.

## Linchpin Orchestrator Output

- questions to ask now
- one-sentence diagnosis
- recommended offer direction
- what not to sell now
- price framing
- meeting-close checks
- client-safe phrase
