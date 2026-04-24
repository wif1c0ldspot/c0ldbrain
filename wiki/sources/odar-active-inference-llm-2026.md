---
title: "ODAR: Principled Adaptive Routing for LLM Reasoning via Active Inference"
type: source
tags: [active-inference, llm-routing, free-energy-principle, test-time-compute, brain-inspired]
authors: [Siyuan Ma, Bo Gao, Xiaojun Jia, Simeng Qin, Tianlin Li, Ke Ma, Xiaoshuang Jia, Wenqi Ren, Yang Liu]
created: '2026-04-19'
updated: '2026-04-19'
confidence: high
status: current
priority: critical
arxiv: "2602.23681"
url: "https://arxiv.org/abs/2602.23681"
summary: "Active inference framework for adaptive LLM reasoning routing — 98.2% MATH, 82% compute reduction, validated on Llama 4 + DeepSeek."
---

# ODAR: Principled Adaptive Routing for LLM Reasoning via Active Inference

**arXiv:** [2602.23681](https://arxiv.org/abs/2602.23681)
**Date:** February 27, 2026
**Authors:** Ma, Gao, Jia, Qin, Li, Ma, Jia, Ren, Liu

## Key Claims

- Paradigm shift from parameter scaling to **test-time compute scaling**
- Existing approaches (best-of-N, self-consistency) are costly brute-force sampling
- ODAR-Expert uses **amortized active inference** for difficulty estimation
- Routes queries between **Fast Agent** (heuristic) and **Slow Agent** (deliberative)
- **Free-energy-principled fusion** minimizes variational free energy objective
- Balances log-likelihood with **epistemic uncertainty (varentropy)**
- Replaces ad hoc voting with principled decision-making

## Results

| Benchmark | Score | Notes |
|-----------|-------|-------|
| MATH | 98.2% | Strong mathematical reasoning |
| Humanity's Last Exam (HLE) | 54.8% | Extremely challenging benchmark |
| Compute reduction | 82% | vs homogeneous sampling on Llama 4 + DeepSeek |

## Architecture

```
Query → Difficulty Estimator (Amortized Active Inference)
         ├── Easy → Fast Agent (heuristic)
         └── Hard → Slow Agent (deliberative)
         
Fast + Slow outputs → Free Energy Fusion
    → Minimize: -log-likelihood + λ·varentropy
    → Selected answer
```

## Why This Matters for Brain-Inspired AI

1. **Direct application of Free Energy Principle** to LLM reasoning — not theoretical
2. **Amortized inference** = learned fast approximate inference (System 1)
3. **Deliberative slow processing** = explicit reasoning (System 2)
4. Maps directly to **dual-process theory** from cognitive science
5. **Practical** — validated on open-source models

## Emergence Scoring

| Criterion | Score | Reasoning |
|-----------|-------|-----------|
| Implementability | 9 | Open-source stack validated |
| Emergence Potential | 8 | Adaptive reasoning emerges from routing |
| Small-Model Feasibility | 9 | Specifically designed for compute efficiency |
| Integration Fit | 9 | Directly applicable to agent model routing |
| **Overall** | **8.75** | **Highest-scoring finding today** |

## Implementation Notes

- Requires: Difficulty estimator (can be a small classifier)
- Requires: Two agent models (fast/slow)
- Requires: Free energy fusion mechanism
- Key insight: varentropy as epistemic uncertainty measure

## Related

- [[predictive-coding-active-inference]] — Day 4 pathway concept
- [[brain-inspired-agent-architecture]] — Master research concept
