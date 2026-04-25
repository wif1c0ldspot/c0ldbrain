---
title: How Honcho + Hermes-LCM Made Our Hermes Agent Smarter
type: source
tags:
- ai-agents
- hermes
- memory-systems
- observability
- infrastructure
sources: []
updated: 2026-04-22
confidence: high
status: current
summary: David Bayendor's production stack combining Hermes Agent (execution), self-hosted
  Honcho (memory), and Hermes-LCM (measurement/control). Emphasizes claim-mechanism-proof
  architecture for repeatable agent systems.
created: 2026-04-22
priority: important
compiled: true
source_url: https://x.com/bayendor/status/2046755138501800427
---

# How Honcho + Hermes-LCM Made Our Hermes Agent Smarter

**Author:** david bayendor (@bayendor)  
**Published:** 2026-04-21  
**Source:** https://x.com/bayendor/status/2046755138501800427  
**Engagement:** 1,927 views, 22 likes, 49 bookmarks

## Summary

Production implementation of a three-layer agent stack: Hermes Agent for execution, self-hosted Honcho for persistent memory/user modeling, and Hermes-LCM for measurement and control. The core thesis is that agents without memory are "fancy autocomplete loops," without observability are "black boxes," and without control are "liabilities."

## Key Takeaways

1. **Three-layer architecture**: Hermes acts → Honcho remembers → LCM proves
2. **Honcho is not a chat buffer** — it is a dual-peer memory system (user peer + AI peer) with durable writeback
3. **Claim → mechanism → proof** is the evaluation format for agent stack features
4. **Self-hosted stack** with 28 permissions, 12 groups, 21 CSRF-protected endpoints
5. **Goal is repeatable results**, not flashy demos — "result by data"

## Honcho Configuration (Documented)

| Setting | Value |
|---------|-------|
| baseUrl | http://localhost:8000 |
| recallMode | hybrid |
| writeFrequency | async |
| sessionStrategy | per-directory |
| dialecticReasoningLevel | low |
| dialecticDynamic | true |
| messageMaxChars | 25000 |

## Architecture Flow

```
User Input → Hermes Agent → Gateway API/CLI → Honcho Memory → LCM Measurement → Session state, logs, usage, results
```

## Claims with Proof

| Claim | Mechanism | Proof |
|-------|-----------|-------|
| More consistent | Honcho injects durable cross-session context | Hybrid recall, async writeback, dual-peer model |
| Easier to inspect | Hermes Control Interface dashboard | SSE streaming, session resume, real-time logs, token analytics |
| Safer to operate | Auth, RBAC, CSRF, rate limiting | 28 permissions, 12 groups, 21 CSRF-protected endpoints |

## Related Concepts

- [[honcho|related]] — Persistent memory and user-modeling layer
- [[hermes-lcm|related]] — Measurement, control, and repeatability layer
- [[hermes-agent-architecture|depends-on]] — Base execution layer
- [[memory-systems|extends]] — Broader memory system landscape
- [[agent-orchestration-stacks|related]] — Multi-layer agent stack patterns
