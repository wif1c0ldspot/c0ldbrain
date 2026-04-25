---
title: RLMs Are the New Reasoning Models
author: '@raw_works (Raymond Weitekamp)'
date: 2026-04-21
source: https://x.com/raw_works/status/2046240194999755153
tags:
- rlm
- recursive-language-models
- reasoning
- test-time-compute
- inference-scaling
- dspy
- benchmarks
type: source
created: 2026-04-21
updated: 2026-04-22
confidence: medium
status: current
priority: important
summary: Recursive Language Models merge reasoning and tool use into one abstraction.
  Beats frontier LLMs at 100x smaller size.
compiled: true
source_url: https://x.com/raw_works/status/2046240194999755153
---

## Summary

Comprehensive deep dive on Recursive Language Models (RLMs) — the convergence of reasoning and tool use into a single inference abstraction. The model treats its prompt as an environment it can inspect, slice, and recursively query. Across three key benchmarks (Oolong, LongMemEval, LongCoT), RLMs consistently beat frontier LLMs, sometimes with models 100× smaller.

## Key Points

- RLM = reasoning + tool use collapsed into one abstraction — prompt becomes environment, context becomes computation
- Input size no longer hard ceiling — RLMs process 100× beyond context window
- History: 2022 (CoT) → 2023 (ReAct, Toolformer) → 2024 (o1, computer use) → RLMs collapse the split
- Three benchmark failure modes of single forward pass: long context (Oolong), memory (LongMemEval), long reasoning (LongCoT)
- GPT-5-mini RLM beats GPT-5 by 2× on Oolong while being cheaper
- Claude Sonnet 4.5 + RLM: 45.4% on LongCoT vs 2.6% without recursion
- Qwen3.5-27B + RLM: 22.18% on LongCoT, 2× GPT-5.2
- **Democratization insight**: small models + RLM on consumer hardware can compete with frontier models
- Limitations: cost, time unpredictability, recursion depth (overthinking), models suck at behaving recursively natively
- Tooling: rlm (reference), DSPy.RLM, Ax (TypeScript), rawrlm (CLI), jawn (coding agent)

## Concepts

- [[recursive-language-models]]
- [[test-time-compute-scaling]]
- [[reasoning-paradigms]]
- [[inference-scaling]]
