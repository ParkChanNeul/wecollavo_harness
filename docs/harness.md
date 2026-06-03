# Harness

## Layers

1. Live Meeting Cockpit
2. Meeting State
3. Domain Agent Team
4. Linchpin Orchestrator
5. Proposal HTML System
6. Delivery OS
7. Proof Loop

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
