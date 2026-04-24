---
title: Agent Memory Benchmark Critique (ATANT)
type: source
tags:
- arxiv
- benchmark
- continuity
- locomo
- longmemeval
- evaluation
created: 2026-04-20
updated: 2026-04-20
confidence: high
status: current
priority: important
url: https://arxiv.org/abs/2604.06710
summary: ATANT framework shows existing memory benchmarks don't measure 'continuity'
  — median covers 1 of 7 required properties
compiled: true
---

# ATANT: Agent Memory Benchmark Critique

## Overview

**ATANT v1.0/v1.1** (ArXiv:2604.06710 / 2604.10981) introduces a rigorous framework defining **continuity** as a system property with **7 required properties**, then shows that existing agent memory benchmarks fail to measure it.

## The 7 Properties of Continuity

The paper defines true agent memory continuity as requiring all of:

1. **Temporal ordering** — memories have sequence
2. **Causal linking** — memories connect cause → effect
3. **Contradiction detection** — identifying conflicting memories
4. **Entity resolution** — same entity across different mentions
5. **Temporal decay** — older memories less accessible (like human forgetting)
6. **Episodic reconstruction** — rebuilding event sequences
7. **Prospective memory** — remembering to do future tasks

## Benchmark Gap Analysis

| Benchmark | Properties Measured (of 7) | Key Gap |
|-----------|--------------------------|---------|
| LoCoMo | 2 | No causal linking, no contradiction detection |
| LongMemEval | 1 | Missing temporal decay and prospective memory |
| ConvoMem | 1 | No entity resolution |
| MemoryBench | 2 | No episodic reconstruction |

**Median: 1 of 7 properties.** Most benchmarks test retrieval accuracy, not actual continuity.

## Scoring Artifact

**23% of LoCoMo corpus is unscorable by construction** — the questions can't be answered even with perfect memory, indicating dataset design issues.

## Why This Matters

1. **Don't trust single-number scores**: A system scoring 0.95 on LoCoMo may still fail at temporal reasoning, contradiction detection, or prospective memory
2. **Design implications**: Memory systems should be evaluated on all 7 dimensions, not just retrieval accuracy
3. **Research direction**: The field needs new benchmarks that test actual continuity

## Implications for Hermes/MemPalace

When evaluating memory tools or designing memory architectures, test for:
- Can it detect contradictions between old and new information?
- Can it link events causally (A caused B)?
- Can it handle temporal decay (old memories fade)?
- Can it resolve entities (this "Joel" and that "Joel" are the same person)?

Don't rely on LoCoMo/LongMemEval scores alone.

## Related Concepts

- [[hierarchical-memory-architectures]] — Architecture designs that could address continuity
- [[memory-systems]] — Memory systems landscape
- [[context-engineering-synthesis]] — Evaluation as part of context engineering

## Sources

- ATANT v1.0: arxiv.org/abs/2604.06710
- ATANT v1.1: arxiv.org/abs/2604.10981
