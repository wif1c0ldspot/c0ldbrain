---
title: 'ADAM: Privacy Attack on Agent Memory'
type: source
tags:
- arxiv
- security
- privacy
- agent-memory
- attack
- extraction
created: 2026-04-20
updated: 2026-04-20
confidence: high
status: current
priority: critical
url: https://arxiv.org/abs/2604.09747
summary: 100% success rate extracting sensitive data from agent memory systems — more
  severe than memory poisoning
compiled: true
source_url: https://arxiv.org/abs/2604.09747
---

# ADAM: Privacy Attack on Agent Memory

## Overview

**ADAM** (ArXiv:2604.09747) demonstrates **100% attack success rate** extracting sensitive data from agent memory systems. This goes beyond the [[memory-firewall]] pattern (which focuses on injection/poisoning) — ADAM is about **extraction/exfiltration**.

## Attack Model

Unlike MINJA (which injects malicious memories), ADAM reads/existing/ memories to extract:
- Personal information stored by users
- Sensitive data from past conversations
- Confidential business information accumulated over time

**100% success rate** means no existing agent memory system has adequate access controls for stored memories.

## Severity Comparison

| Attack | Type | Success Rate | Defense |
|--------|------|-------------|---------|
| MINJA | Injection/Poisoning | >95% | Input validation, semantic drift detection |
| OWASP ASI06 | Injection/Poisoning | Reference impl | Memory write gates |
| **ADAM** | **Extraction/Exfiltration** | **100%** | **Encryption + access controls** |

## Why This Is More Severe

1. **Poisoning** corrupts future behavior (bad but detectable)
2. **Extraction** exposes all accumulated knowledge (worse — the more useful the memory, the more data at risk)
3. Agent memory systems accumulate sensitive data over time — the attack surface grows with usage

## Required Defenses

1. **Encryption at rest** — memory stores should be encrypted, not plaintext
2. **Access controls** — who can query which memories?
3. **Audit logging** — track all memory reads
4. **Memory compartmentalization** — sensitive memories in separate stores with stricter access
5. **Differential privacy** — add noise to memory retrieval to prevent exact extraction

## Implications for Hermes/MemPalace

- **MemPalace**: Consider encrypting sensitive drawer contents
- **Hermes**: Memory queries should be auditable
- **General**: Agent memory is a high-value target — it accumulates everything the agent knows about the user

## Related Concepts

- [[memory-firewall]] — Defense against memory injection (complementary to ADAM defense)
- [[memory-systems]] — Memory security as architectural concern
- [[ai-security-synthesis]] — Security landscape overview

## Sources

- ADAM: arxiv.org/abs/2604.09747
