---
title: "When to Forget: A Memory Governance Primitive"
type: source
tags: [brain-inspired-ai, memory-governance, hippocampus-pathway, memory-pruning, continual-learning]
sources: []
created: '2026-04-20'
confidence: high
status: current
priority: important
summary: "Memory Worth (MW) metric — a lightweight 2-counter signal tracking memory quality through outcome co-occurrence. Converges to conditional success probability. Spearman rho=0.89 vs ground truth."
---

# When to Forget: A Memory Governance Primitive

**Source:** Simsek, arXiv:2604.12007, April 2026  
**Category:** cs.AI  
**Link:** https://arxiv.org/abs/2604.12007

## Summary

Agent memory systems accumulate experience but lack principled operational metrics for memory quality governance — deciding which memories to trust, suppress, or deprecate. This paper proposes **Memory Worth (MW)**: a two-counter per-memory signal that tracks how often a memory co-occurs with successful versus failed outcomes.

## Key Results

- **Memory Worth (MW):** Two scalar counters per memory — success/failure co-occurrence tracking
- **Convergence:** MW converges almost surely to conditional success probability p+(m) = Pr[y_t = +1 | m in M_t]
- **Validation:** Spearman rank-correlation rho = 0.89 ± 0.02 (after 10k episodes) vs ground-truth utilities
- **Baseline comparison:** Systems that never update have rho = 0.00
- **Embedding retrieval:** Stale memories drop to MW = 0.17 while specialist memories remain at MW = 0.77
- **Minimal overhead:** Only 2 scalar counters per memory unit

## Relevance to Hippocampus Pathway

**Pathway 1 Alignment: HIGH (8/10)**

This directly addresses the **memory consolidation and pruning** component of the Hippocampus pathway:
- **Memory consolidation** → MW identifies which episodes to keep vs forget
- **Synaptic homeostasis** analog — preventing memory bloat
- **Active forgetting** as a feature, not a bug

This paper provides the **pruning mechanism** that complements Evo-MedAgent's storage mechanism. Together, they form a complete hippocampal memory lifecycle.

## Emergence Scoring

| Criterion | Score | Notes |
|-----------|-------|-------|
| Implementability | 9/10 | Just 2 counters per memory, drops into any system |
| Emergence Potential | 7/10 | Enables adaptive memory but doesn't directly create emergence |
| Small-Model Feasibility | 10/10 | Minimal overhead, works with any retrieval system |
| Integration Fit | 9/10 | Directly implements hippocampal consolidation/pruning |

**Average: 8.75/10**

## Predicted Emergent Behaviors

- [ ] Agents develop "expertise" as domain-specific memories get reinforced
- [ ] Natural forgetting of outdated or harmful patterns
- [ ] Adaptive memory budget allocation across domains
- [ ] Implicit quality signal without explicit human feedback

## Implementation Notes

- No open-source code yet (theoretical framework)
- Requires logging retrievals and episode outcomes
- Could be added to MemPalace or any vector store as a post-retrieval filter
- Works with all-MiniLM-L6-v2 embeddings (validated)

## Related Concepts

- [[brain-inspired-agent-architecture]] — Hippocampus consolidation
- [[memory-systems]] — Memory management patterns
- [[demand-paging-for-agent-memory]] — Complementary memory management
- [[emergence-tracking]] — Research tracking
