---
title: "Memory Firewall"
type: concept
tags: [ai-security, memory-systems, agent-security, defense-in-depth]
created: '2026-04-19'
updated: '2026-04-19'
confidence: medium
status: emerging
priority: high
summary: "Defense pattern for agent memory systems — validates, quarantines, and audits memory writes to prevent poisoning attacks."
sources:
- agent-memory-poisoning-security-2026-04
---

# Memory Firewall

## Overview

An architectural pattern for protecting agent memory systems from poisoning attacks. Emerged in April 2026 in response to MINJA framework (>95% injection success rate) and OWASP ASI06 classification.

## The Threat

Memory poisoning exploits persistent memory in AI agents:
- **MINJA framework**: >95% injection success with zero elevated access
- **ZombieAgent**: ChatGPT connector + memory features combined for indirect injection
- **OWASP ASI06**: Officially classified as "Memory & Context Poisoning"

## Defense Layers

### 1. Semantic Drift Detection
Compare new memory entries against existing knowledge graph. Flag entries that:
- Contradict established facts
- Introduce entities/relationships with no prior context
- Contain instruction-like patterns (potential prompt injection)

### 2. Write Gate
Intercept all memory writes before persistence:
- Validate against authoritative sources when possible
- Apply time-based quarantine for suspicious entries
- Require confidence threshold for automatic persistence

### 3. Audit Trail
Log all memory modifications:
- What was written/modified/deleted
- Source of the memory (user, tool, retrieved context)
- Confidence score at time of persistence

### 4. Periodic Integrity Checks
- Re-validate memories against authoritative sources
- Flag memories that haven't been accessed recently
- Detect orphaned or contradictory memory clusters

## Implementation: OWASP Agent Memory Guard

Three-tier defense:
1. **Validate**: Check new entries against existing knowledge
2. **Delay**: Time-based quarantine before persistence
3. **Quarantine**: Isolate suspicious entries for review

## Related Concepts

- [[memory-systems]] — Hub for agent memory patterns
- [[prompt-injection-comprehensive-2026]] — Related attack vector
- [[agent-harness]] — Security boundaries in agent frameworks
- [[demand-paging-for-agent-memory]] — Memory architecture this protects

## Integration with MemPalace

MemPalace's knowledge graph (SQLite-backed, temporal validity) is well-positioned for memory firewall integration:
- Existing fact validation could extend to semantic drift detection
- Temporal validity enables "expire suspicious memories" pattern
- Drawers provide natural quarantine isolation


## Implementation: Belief Gate (Update 2026-04-21)

The **[[belief-gate]]** is a specific implementation of the memory firewall concept:
- Write-time filter that rejects model-derived claims
- Only `tool_verified`, `user_confirmed`, `repository_derived`, `test_verified` claims survive
- Benchmark-verified: 0 reasoning leaks

See [[claim-based-memory]] for the full PCKC model.
