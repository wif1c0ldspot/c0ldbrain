---
title: "AXIOM: Learning to Play Games with Expanding Object-Centric Active Inference"
type: source
tags: [active-inference, object-centric, world-models, bayesian, free-energy-principle, brain-inspired]
authors: [Conor Heins, Toon Van de Maele, Alexander Tschantz, Karl Friston, et al.]
created: '2026-04-19'
updated: '2026-04-19'
confidence: medium
status: current
priority: important
arxiv: "2505.24784"
url: "https://arxiv.org/abs/2505.24784"
summary: "Object-centric active inference agent masters games in 10K steps with minimal parameters and no gradient optimization."
---

# AXIOM: Learning to Play Games in Minutes with Expanding Object-Centric Models

**arXiv:** [2505.24784](https://arxiv.org/abs/2505.24784)
**Date:** May 30, 2025
**Authors:** Heins, Van de Maele, Tschantz, Linander, Markovic, Salvatori, Pezzato, Catal, Wei, Koudahl, Perin, **Friston**, Verbelen, Buckley

## Key Claims

- DRL achieves SOTA but is data-inefficient compared to human learning
- Humans leverage **core priors about objects and interactions**
- Active inference integrates sensory info with prior knowledge
- Traditional active inference models are single-task, lack domain flexibility
- AXIOM combines: **object-centric priors + active inference + Bayesian model reduction**

## Architecture

- **Scene representation:** Compositions of objects
- **Dynamics:** Piecewise linear trajectories capturing sparse object-object interactions
- **Structure expansion:** Online growth of generative model from single events
- **Generalization:** Periodic Bayesian model reduction

## Results

- Masters various games in **only 10,000 interaction steps**
- Minimal parameters compared to DRL
- **No gradient-based optimization** required
- Interpretable world models

## Why This Matters

1. **Karl Friston as co-author** — the Free Energy Principle creator endorses this approach
2. Object-centric = interpretable, composable representations
3. Bayesian model reduction = built-in Occam's razor
4. 10K steps is dramatically more efficient than DRL

## Emergence Scoring

| Criterion | Score |
|-----------|-------|
| Implementability | 6 (complex Bayesian framework) |
| Emergence Potential | 9 (object-centric world models from interaction) |
| Small-Model Feasibility | 8 (very parameter-efficient) |
| Integration Fit | 7 (agent perception layer) |
| **Overall** | **7.50** |

## Related

- [[predictive-coding-active-inference]] — Day 4 pathway concept
- [[brain-inspired-agent-architecture]] — Master research concept
