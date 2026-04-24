---
confidence: high
created: '2026-04-17'
priority: important
sources:
- arXiv:2604.04651
status: current
summary: Small language models can achieve LLM-level performance on knowledge-intensive
  tasks through explicit training on search tool use and grounded generation.
tags:
- small-models
- agents
- tool-use
- search-agents
- knowledge-intensive-tasks
title: Teaching Small Models Agentic Behavior
type: concept
updated: '2026-04-18'
---


# Teaching Small Models Agentic Behavior

## Key Research

**Paper:** "Search, Do not Guess: Teaching Small Language Models to Be Effective Search Agents"
- Authors: Liu, Sun, Chen, Zhang, Zhao
- arXiv:2604.04651 (April 2026)

## The Problem

Small Language Models (SLMs) as search agents:
- Invoke search tools less frequently than LLMs
- More prone to hallucinations
- Rely on parametric knowledge instead of retrieval

## The Solution: \policy

A lightweight fine-tuning approach that explicitly trains SLMs to:
1. **Reliably retrieve** — Call search tools consistently
2. **Grounded generation** — Generate answers based on retrieved evidence

## Key Insight

**Consistent search behavior beats adaptive strategies for small models.**

SLMs with "adaptive" search strategies (deciding when to search) often perform worse than those with consistent search patterns.

## Results

| Benchmark | Improvement |
|-----------|-------------||
| Bamboogle | +17.3 scores |
| HotpotQA | +15.3 scores |

**Achievement:** LLM-level results via tool use, not parametric knowledge.

## Why This Matters for Emergence

### Tool Use as Emergence
For small models, effective tool use IS emergent behavior. The model+tool system exhibits capabilities beyond the base model.

### Composition Over Scale
- LLMs: Strong parametric reasoning
- SLMs + tools: Comparable performance via composition
- Implication: Emergence can be architected, not just scaled

## Method: \policy

### Training Approach
1. **Explicit retrieval training** — Force search tool invocation
2. **Grounded answer generation** — Train on evidence-based responses
3. **Consistency over adaptivity** — Regular search beats conditional search

### Comparison to Distillation
- **Agent distillation** — Copy LLM behavior (17-15 point gap)
- **\policy** — Train tool use directly (closes gap)

## Implications for Small Model Emergence

### Path 1: Tool-Augmented Small Agents
Small models + rich tool ecosystems = emergent system capabilities

### Path 2: Consistency Over Intelligence
SLMs don't need to "decide" when to use tools — they should use them consistently.

### Path 3: Specialization
Rather than one large model, use multiple small specialized models with tools.

## Connection to Self-Modification

This work enables:
- **Emergent strategy discovery** — Small models can solve problems beyond their parametric knowledge
- **Self-modification precursor** — Tool use is prerequisite to tool modification
- **Narrow improvement path** — Specific capability enhancement via targeted tool training

## Related Concepts

- [[emergent-agent-evolution-synthesis]] — Broader evolution context
- [[aster-agentic-scaling]] — Tool-integrated extended reasoning
- [[training-free-self-improvement]] — Memory-based improvement
- [[emergence-in-quantized-models]] — Small + quantized + tool-augmented

## Source

Liu, Y., Sun, Q., Chen, Y., Zhang, S., & Zhao, C. (2026). Search, Do not Guess: Teaching Small Language Models to Be Effective Search Agents. arXiv:2604.04651. https://arxiv.org/abs/2604.04651
