---
title: 'Evo-MedAgent: Agents That Remember, Reflect, and Improve'
type: source
tags:
- brain-inspired-ai
- episodic-memory
- agent-memory
- hippocampus-pathway
- emergence
sources: []
created: '2026-04-20'
confidence: high
status: current
priority: important
summary: 'Training-free self-evolving memory module for LLM agents with 3 complementary
  stores: retrospective episodes, adaptive heuristics, and tool reliability tracking.
  Raises accuracy from 0.68 to 0.79 on GPT-5-mini.'
updated: '2026-04-20'
compiled: true
---

# Evo-MedAgent: Beyond One-Shot Diagnosis with Agents That Remember, Reflect, and Improve

**Source:** Shen et al., arXiv:2604.14475, April 2026  
**Category:** cs.AI  
**Link:** https://arxiv.org/abs/2604.14475

## Summary

A self-evolving memory module that equips LLM agents with inter-case learning at test time. Three complementary memory stores mimic hippocampal and neocortical memory systems:

1. **Retrospective Clinical Episodes** — Retrieve problem-solving experiences from similar past cases (episodic memory)
2. **Adaptive Procedural Heuristics** — Priority-tagged diagnostic rules evolved via reflection (procedural memory)
3. **Tool Reliability Controller** — Tracks per-tool trustworthiness over time (metacognitive monitoring)

## Key Results

- MCQ accuracy on ChestAgentBench: GPT-5-mini 0.68→0.79, Gemini-3 Flash 0.76→0.87
- **Training-free** — requires only one additional retrieval pass + single reflection call per case
- Per-case overhead is bounded and deployable on top of any frozen model
- Evolving memory outperforms orchestrating external tools on qualitative tasks

## Relevance to Hippocampus Pathway

**Pathway 1 Alignment: HIGH (9/10)**

This paper directly implements the Hippocampus pathway from [[brain-inspired-agent-architecture]]:
- **Episodic memory** → Retrospective Clinical Episodes (fast store + retrieval)
- **Memory consolidation** → Reflection call after each case (replay + update)
- **Pattern completion** → Retrieval from similar past cases
- **Procedural transfer** → Heuristic bank evolves with experience

The 3-store architecture maps precisely to the Hippocampus→Neocortex consolidation model.

## Emergence Scoring

| Criterion | Score | Notes |
|-----------|-------|-------|
| Implementability | 9/10 | Training-free, drops onto any frozen LLM |
| Emergence Potential | 8/10 | Self-improving through memory, not just retrieval |
| Small-Model Feasibility | 9/10 | Tested on GPT-5-mini, lightweight overhead |
| Integration Fit | 10/10 | Perfect hippocampus module match |

**Average: 9.0/10**

## Predicted Emergent Behaviors

- [ ] Agents develop case-specific diagnostic intuition
- [ ] Heuristic bank converges to domain-optimal strategies
- [ ] Tool trust calibration adapts to model capabilities
- [ ] Cross-case analogical reasoning emerges from episode similarity

## Implementation Notes

- No open-source code available yet (paper only)
- Architecture is modular — each store operates independently
- Reflection is a single LLM call post-task
- Episode retrieval uses vector similarity (standard embedding models)

## Related Concepts

- [[brain-inspired-agent-architecture]] — Hippocampus module design
- [[memory-systems]] — Agent memory architectures
- [[emergence-tracking]] — Research tracking
- [[emergent-agent-evolution-synthesis]] — Evolution trajectory
