---
title: 'HERAKLES: Hierarchical Skill Compilation for Open-ended LLM Agents'
type: source
tags:
- ai-agents
- skill-chaining
- hierarchical-rl
- compositional-generalization
confidence: high
status: current
summary: 'Hierarchical RL + language for automatic skill chaining in autotelic agents.
  Score: 9/10 emergence potential.'
priority: important
updated: '2026-04-24'
created: '2026-04-24'
compiled: true
source_url: aggregate

---

# HERAKLES: Hierarchical Skill Compilation for Open-ended LLM Agents

**Source:** arXiv:2508.14751 (2025-08-20)
**Authors:** Carta, Romac, Gaven, Oudeyer, Sigaud

## Key Findings

- Hierarchical RL combined with language for skill compilation in autotelic (intrinsically motivated) agents
- Agents compose skills from lower-level primitives for increasingly complex, abstract goals
- Uses compositional structure of language to bootstrap skill chaining
- Limits sample complexity growth as goal complexity increases

## Emergence Potential: 9/10

**Why it matters:** Directly addresses automatic hierarchical skill chaining with language as the compositional glue. The language-as-composition approach enables cross-domain transfer of skill chains.

## Implementation Fit

- **Implementability:** Research prototype, but concepts applicable to Hermes skill system
- **Small-model feasible:** Yes — hierarchical RL doesn't require massive models
- **Integration fit:** High — aligns with existing skill graph architecture

## Related Concepts
- [[skill-composition-procedural-learning]] — Day 2 research concept
- [[agentic-ai]] — Agent architecture patterns
