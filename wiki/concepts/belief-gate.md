---
title: "Belief Gate"
type: concept
tags: [memory-systems, security, agent-memory, truth-filtering, belief-gate]
created: 2026-04-21
updated: 2026-04-21
confidence: high
status: current
priority: high
summary: "Write-time filter that rejects model-derived claims from durable memory. Only tool-verified, user-confirmed, or repository-derived facts survive."
sources:
- chum-mem-pckc-2026-04
- memory-firewall
- agent-memory-poisoning-security-2026-04
---

# Belief Gate

## Definition

A **write-time security filter** that prevents model-generated prose from becoming durable memory. Only claims with sufficient authority survive the gate.

## Why It Matters

Without a belief gate:
- LLM hallucinations become "facts" in memory
- Model reasoning leaks into stored knowledge
- Stale inferences persist indefinitely
- Memory poisoning attacks have no defense

With a belief gate:
- Memory quality >> memory quantity
- Trust levels are explicit and auditable
- Contradictions are caught at write time
- Model updates don't pollute verified facts

## Implementation (chum-mem)

```
Raw session events
  → Episode segmentation (conversation / implementation / debugging)
  → Atomic claim extraction with authority classification
  → Belief gate (reject model-generated prose)
  → Only tool_verified, user_confirmed, repository_derived, test_verified pass
```

### Hard Rejections
- `Reasoning` events: rejected by construction
- `TurnContext` events: rejected by construction
- `AgentMessage`: rejected unless user-confirmed

## Connection to [[memory-firewall]]

The belief gate is a specific implementation of the memory firewall concept:
- **Memory firewall**: broader security boundary for all memory operations
- **Belief gate**: focused on truth-filtering at write time

## Connection to OWASP Memory Guard

OWASP's ASI06 memory poisoning defense shares the same philosophy:
- Validate, delay, quarantine memory writes
- The belief gate is a lightweight, local-first implementation

## Integration Potential

For [[mempalace]]:
- Add `authority_class` metadata to KG facts
- Implement write-time validation for `mempalace_add_drawer`
- Filter model-inferred content from diary entries

## Related Concepts

- [[claim-based-memory]] — the memory primitive this gates
- [[memory-firewall]] — broader security boundary
- [[memory-systems]] — landscape overview
- [[agent-memory-poisoning-security-2026-04]] — attack vectors
