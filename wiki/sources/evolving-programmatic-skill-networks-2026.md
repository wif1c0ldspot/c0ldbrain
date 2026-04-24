---
title: Evolving Programmatic Skill Networks (PSN)
type: source
tags:
- ai-agents
- skill-graphs
- programmatic-skills
- compositional-generalization
- emergence
confidence: high
status: current
summary: 'Skills as executable programs in evolving compositional networks. Score:
  10/10 emergence potential — highest this cycle.'
priority: important
updated: '2026-04-24'
created: '2026-04-24'
compiled: true
---

# Evolving Programmatic Skill Networks (PSN)

**Source:** Shi et al., 2026

## Key Findings

- Skills represented as **executable symbolic programs** in a compositional network
- Three mechanisms: skill creation, refinement, and reuse
- Network evolves through experience — skills improve and compose
- Programmatic representation enables verifiable, interpretable skill composition

## Emergence Potential: 10/10

**Why it matters:** This is the **highest-scoring paper in the Day 2 research cycle**. The programmatic representation of skills enables:
1. **Verifiable composition** — Programs can be checked for correctness before execution
2. **Interpretable skill chains** — Human-readable skill programs
3. **Evolutionary improvement** — Skills refine through use
4. **Emergent behavior** — Compositions produce capabilities beyond individual skills

## Implementation Fit

- **Implementability:** Research prototype, but concepts applicable to Hermes
- **Small-model feasible:** Yes — programmatic skills are symbolic, not learned end-to-end
- **Integration fit:** Directly maps to Hermes SKILL.md pattern with executable scripts

## Architecture
```
Skill Network (DAG)
├── Skill A (programmatic: execute, verify, refine)
├── Skill B (composable from A + C)
├── Skill C (evolved from repeated use)
└── Skill D (created from novel composition)
```

## Related Concepts
- [[skill-composition-procedural-learning]] — Day 2 research concept
- [[hermes-agent-architecture]] — Hermes skill registry pattern
