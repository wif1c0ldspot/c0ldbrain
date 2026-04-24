---
title: "Learning Long-Range Dependencies with Temporal Predictive Coding"
type: source
tags: [predictive-coding, temporal, rnn, neuromorphic, brain-inspired]
authors: [Tom Potter, Oliver Rhodes]
created: '2026-04-19'
updated: '2026-04-19'
confidence: high
status: current
priority: important
arxiv: "2602.18131"
url: "https://arxiv.org/abs/2602.18131"
summary: "Temporal predictive coding matches BPTT on machine translation with a 15M parameter model — first application of tPC at this scale."
---

# Learning Long-Range Dependencies with Temporal Predictive Coding

**arXiv:** [2602.18131](https://arxiv.org/abs/2602.18131)
**Date:** February 20, 2026
**Authors:** Tom Potter, Oliver Rhodes

## Key Claims

- Predictive Coding (PC) has local, parallelizable operations
- Extending PC to RNNs for long-range dependencies is challenging
- BPTT is dominant but non-local, energy-hungry
- Novel method: **Temporal Predictive Coding (tPC) + approximate RTRL**
- Enables spatio-temporal credit assignment

## Results

- Closely matches BPTT performance
- Machine translation: **test perplexity 7.62 (vs 7.49 for BPTT)**
- **15-million parameter model** — first tPC application at this scale
- Retains local, parallelizable, flexible PC properties

## Why This Matters

1. **Neuromorphic hardware compatible** — local updates = energy-efficient
2. No backpropagation through time needed
3. First tPC at real-world task scale
4. Parallelizable across layers (unlike BPTT's sequential dependency)

## Emergence Scoring

| Criterion | Score |
|-----------|-------|
| Implementability | 7 |
| Emergence Potential | 8 |
| Small-Model Feasibility | 8 |
| Integration Fit | 8 |
| **Overall** | **7.75** |

## Related

- [[dkp-predictive-coding-2026]] — Accelerated PC networks (complementary)
- [[predictive-coding-active-inference]] — Day 4 pathway concept
