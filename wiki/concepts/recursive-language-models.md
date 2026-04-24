---
title: Recursive Language Models (RLMs)
type: concept
tags:
- rlm
- recursive-language-models
- reasoning
- test-time-compute
- inference-scaling
- dspy
- long-context
- benchmarks
created: '2026-04-21'
updated: '2026-04-21'
confidence: high
status: current
priority: important
summary: Inference paradigm where LM treats its prompt as an environment to inspect,
  slice, and recursively query. Collapses reasoning + tool use into one abstraction.
  Processes 100× beyond context window. Small models + RLM compete with frontier LLMs.
sources:
- rlms-new-reasoning-models-rawworks-2026-04
- recursive-language-models-rlm-2026
---

# Recursive Language Models (RLMs)

## Summary

A Recursive Language Model treats its input prompt as an environment rather than a fixed string. The model gets a REPL where the prompt is bound to a variable it can inspect, slice, and partition programmatically. When a region warrants closer inspection, it issues a recursive subcall — to itself or another LM — over that slice. This collapses reasoning and tool use into a single inference abstraction, making input size no longer a hard ceiling.

## Key Concepts

### Core Mechanism

1. Root LM receives prompt bound to a variable in a REPL
2. Model programmatically inspects, slices, partitions the context
3. Issues recursive subcalls (to self or other LMs) over slices
4. Incorporates results back into main computation
5. Recursion bottoms out at base model's ordinary forward pass

**Result:** Input size is no longer a hard ceiling — RLMs process inputs up to 100× beyond the underlying model's context window.

### The Convergence

RLMs represent the collapse of two previously separate axes:

| Axis | Traditional | With RLM |
|------|------------|----------|
| Reasoning | Chain-of-thought, self-consistency, tree search | Integrated into recursive decomposition |
| Tool Use | Function calling, API discipline, structured invocation | Prompt slices become "tools" the model calls on itself |

The model treats context itself as the object of computation.

### Benchmark Performance

Three failure modes of the single forward pass, all conquered by RLMs:

**1. Long Context (Oolong)**
- Analyze many local chunks, aggregate into global answer
- GPT-5, Claude-Sonnet-4, Gemini-2.5-Pro all score <50% at 128K
- GPT-5-mini RLM beats GPT-5 by 2× while being cheaper

**2. Memory (LongMemEval)**
- 500 questions over sustained chat histories
- DSPy.RLM: 89.2-89.8% — competitive without classical retrieval stack

**3. Long Reasoning (LongCoT)**
- 2,500 expert-designed long-horizon CoT problems
- Best frontier models: <10% (GPT-5.2 at 9.8%)
- Claude Sonnet 4.5 + RLM: 45.4% vs 2.6% without recursion (17× improvement)
- Qwen3.5-27B + RLM: 22.18%, 2× GPT-5.2

### Democratization Effect

Small models + RLM on consumer hardware can compete with frontier models:
- Qwen3-8B: 0/507 → 33/507 on LongCoT with RLM
- Qwen3.5-9B + RLM: 15.69% on full LongCoT, 1.6× GPT-5.2
- Individual/consortium on affordable compute can reach frontier capabilities
- The frontier stops being exclusive to largest labs

### Historical Arc

```
2022: Chain-of-Thought, Self-Consistency (reasoning without tools)
2022: ReAct (first bridge: reasoning ↔ acting)
2023: Toolformer, OpenAI function calling (tool use as API discipline)
2023: Tree of Thoughts (internal search, still separate from tools)
2024: o1 (reasoning models as product category, no function calling)
2024: Claude computer use, Gemini agentic era (axes starting to merge)
2025: RLMs collapse the split
```

## Limitations

- **Cost**: Expensive — many recursive calls per query
- **Time**: Unpredictable in naive implementation (model decides decomposition depth)
- **Recursion depth**: Deeper recursion can "overthink" — hurt accuracy, explode runtime
- **Native recursion**: Models generally don't behave recursively well without scaffolding
- **Optimal recursion**: What's the reward function? Multi-billion-dollar question

## Tooling Ecosystem

| Tool | Description |
|------|------------|
| **rlm** | Reference implementation from Alex Zhang (paper author) |
| **DSPy.RLM** | Composable module inside DSPy programs |
| **Ax** | TypeScript DSPy-style framework with first-class RLM |
| **rawrlm** | CLI wrapper with directory-as-context, JSON output |
| **jawn** | Recursive coding agent: rlm_query + rlm_map with jj workspaces |

## Related Concepts

- [[test-time-compute-scaling]]
- [[reasoning-paradigms]]
- [[inference-scaling]]
- [[dspy]]
- [[agent-architecture]]
- [[context-engineering]]
- [[chain-of-thought]]
