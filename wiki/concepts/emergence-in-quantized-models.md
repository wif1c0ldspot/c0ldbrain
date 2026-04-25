---
confidence: high
created: '2026-04-17'
priority: important
sources:
- arXiv:2307.08072
status: current
summary: Empirical findings on how quantization affects emergent abilities in LLMs.
  4-bit models retain CoT, ICL, and instruction-following; 2-bit models degrade severely.
tags:
- quantization
- emergent-abilities
- small-models
- chain-of-thought
- research-findings
title: Emergence in Quantized Models
type: concept
updated: '2026-04-18'
---


# Emergence in Quantized Models

## Key Research

**Paper:** "Do Emergent Abilities Exist in Quantized Large Language Models: An Empirical Study"
- Authors: Liu, Liu, Gao, Gao, Zhao, Li, Ding, Wen
- arXiv:2307.08072 (July 2023)

## Main Findings

### Emergent Abilities Tested
1. **In-Context Learning (ICL)** — Learning from examples in the prompt
2. **Chain-of-Thought Reasoning (CoT)** — Step-by-step problem solving
3. **Instruction-Following (IF)** — Adhering to complex instructions

### Quantization Impact

| Bit Width | Emergent Abilities | Performance |
|-----------|-------------------|-------------|
| 4-bit | Fully retained | Minimal degradation |
| 3-bit | Partially retained | Noticeable degradation |
| 2-bit | Severely degraded | Loss of emergence |

### Critical Insight

Emergent abilities are NOT solely dependent on raw parameter count. They depend on:
- **Effective capacity** (information content of weights)
- **Weight precision** (granularity of representation)
- **Architectural preservation** (attention patterns, feed-forward structures)

## Implications for Small Model Design

1. **4-bit is the sweet spot** — You can run 2x larger models at 4-bit vs 8-bit with preserved emergence
2. **Emergence per FLOP** — Quantized small models may achieve better emergence-per-compute than full-precision models
3. **Deployment feasibility** — Emergent capabilities on consumer hardware via quantization

## Component Sensitivity Analysis

The paper analyzed which model components are most sensitive to quantization:

- **Attention layers** — More sensitive (require higher precision)
- **Feed-forward networks** — Less sensitive (can tolerate more compression)
- **Embedding layers** — Moderate sensitivity

## Performance Compensation Strategies

### Fine-Tuning on Quantized Models
- QLoRA-style fine-tuning can recover degraded performance
- Target specific emergent abilities rather than general loss

### Component-Aware Quantization
- Use higher precision for attention layers
- Aggressive quantization for FFNs
- Mixed-precision strategies

## Related Concepts

- [[quantization-techniques]] — QLoRA, K-quants, TurboQuant
- [[emergent-agent-evolution-synthesis]] — Broader context on agent evolution
- [[teaching-small-models-agentic-behavior]] — Teaching tool use to small models

## Source

Liu, P., Liu, Z., Gao, Z., Gao, D., Zhao, W., Li, Y., Ding, B., & Wen, J. (2023). Do Emergent Abilities Exist in Quantized Large Language Models: An Empirical Study. arXiv:2307.08072. https://arxiv.org/abs/2307.08072

- [[training-free-self-improvement]]