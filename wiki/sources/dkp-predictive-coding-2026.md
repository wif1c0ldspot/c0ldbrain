---
title: Accelerated Predictive Coding Networks via Direct Kolen-Pollack Feedback Alignment
type: source
tags:
- predictive-coding
- feedback-alignment
- hardware-efficient
- brain-inspired
authors:
- Davide Casnici
- Martin Lefebvre
- Justin Dauwels
- Charlotte Frenkel
created: '2026-04-19'
updated: '2026-04-19'
confidence: high
status: current
priority: reference
arxiv: '2602.15571'
url: https://arxiv.org/abs/2602.15571
summary: DKP-PC reduces predictive coding error propagation from O(L) to O(1) using
  learnable direct feedback connections.
compiled: true
source_url: https://arxiv.org/abs/2602.15571
---

# Accelerated Predictive Coding Networks via Direct Kolen-Pollack Feedback Alignment

**arXiv:** [2602.15571](https://arxiv.org/abs/2602.15571)
**Date:** February 17, 2026 (v2: March 7, 2026)
**Authors:** Casnici, Lefebvre, Dauwels, Frenkel

## Key Claims

- PC faces two limitations: inference-phase propagation and exponential feedback decay
- **DKP-PC** introduces learnable direct feedback connections from output to all hidden layers
- Reduces error propagation time complexity from **O(L) to O(1)**
- Removes depth-dependent delay in error signals

## Results

- Performance at least comparable to, often exceeding standard PC
- Improved latency and computational performance
- Supports custom hardware-efficient implementations

## Why This Matters

1. Makes deep PC networks practical (no depth-dependent slowdown)
2. Hardware-efficient — critical for neuromorphic deployment
3. Complements tPC for complete PC training pipeline

## Emergence Scoring

| Criterion | Score |
|-----------|-------|
| Implementability | 8 |
| Emergence Potential | 6 (optimization, not behavior-focused) |
| Small-Model Feasibility | 9 |
| Integration Fit | 7 |
| **Overall** | **7.50** |

## Related

- [[temporal-predictive-coding-2026]] — Temporal PC (complementary)
- [[predictive-coding-active-inference]] — Day 4 pathway concept
