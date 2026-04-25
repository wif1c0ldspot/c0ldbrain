---
title: 'MemMachine: Multi-Tier Agent Memory System'
type: source
tags:
- arxiv
- agent-memory
- token-efficiency
- benchmark
- locomo
created: 2026-04-20
updated: 2026-04-20
confidence: high
status: current
priority: important
url: https://arxiv.org/abs/2604.04853
category: Hybrid
summary: Open-source memory with short-term, episodic, and profile memory. Achieves
  0.9169 LoCoMo with 80% fewer tokens than Mem0
compiled: true
source_url: https://arxiv.org/abs/2604.04853
---

# MemMachine: Multi-Tier Agent Memory System

## Overview

**MemMachine** (ArXiv:2604.04853) is an open-source agent memory system implementing a three-tier memory architecture:

1. **Short-term memory** — recent conversation context
2. **Long-term episodic memory** — distilled experiences and events
3. **Profile memory** — user preferences and persistent attributes

## Key Results

| Benchmark | Score | Comparison |
|-----------|-------|------------|
| LoCoMo | 0.9169 | Competitive with Mem0 |
| LongMemEvalS | 93.0% | Among highest reported |
| **Token efficiency** | **80% fewer tokens than Mem0** | Major cost reduction |

The 80% token reduction is the headline finding — it means MemMachine achieves similar accuracy at a fraction of the cost.

## Architecture

The three-tier design mirrors the [[demand-paging-for-agent-memory]] OS analogy:
- **Short-term** = RAM/cache (recent context, always available)
- **Episodic** = swap (compressed past experiences, retrieved on demand)
- **Profile** = persistent storage (user attributes, rarely changes)

## Camp Classification

**Camp: Hybrid** — Uses Camp 1 storage techniques (vector retrieval) but thinks in Camp 2 terms (what context should be assembled for the agent).

## Why It Matters

1. **Token efficiency is king**: 80% reduction means 5x more conversations per dollar
2. **Three-tier architecture is convergent**: Multiple independent teams (MemoryOS, GAM, Pichay) are arriving at similar hierarchical designs
3. **Benchmark-competitive**: 0.9169 LoCoMo means hierarchical memory doesn't sacrifice accuracy for efficiency

## Related Concepts

- [[memory-systems]] — Multi-tier memory architecture pattern
- [[demand-paging-for-agent-memory]] — OS virtual memory analogy for agent context
- [[context-engineering-synthesis]] — Token efficiency as context engineering concern

## Comparison with Mem0

| Metric | MemMachine | Mem0 |
|--------|-----------|------|
| LoCoMo | 0.9169 | ~0.91 |
| Token usage | 20% of Mem0 | 100% (baseline) |
| Architecture | 3-tier hierarchical | Flat + graph variant |
| Open source | Yes | Yes |
