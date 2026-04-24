---
title: "STEPS: Skill Taxonomy Guided Data Synthesis for Compositional Generalization"
type: source
tags: [ai-agents, compositional-generalization, data-synthesis, skill-taxonomy, training]
confidence: high
status: current
summary: "Skill taxonomy guided entropy-based post-training data synthesis. Score: 9/10 emergence potential."
---

# STEPS: Skill Taxonomy Guided Data Synthesis for Compositional Generalization

**Source:** arXiv:2601.03676 (2026-01-07)
**Authors:** Wei, Du, Yu, Feng, Li
**Code:** https://github.com/weiyifan1023/STEPS

## Key Findings

- Skill Taxonomy guided Entropy-based Post-training data Synthesis framework
- Targets compositional generalization by generating data for underrepresented skill combinations
- Addresses the long-tailed power-law distribution of skill combinations
- Data bottleneck is the core constraint for compositional generalization

## Emergence Potential: 9/10

**Why it matters:** Directly addresses the core problem — complex skill combinations are underrepresented in training data. By synthesizing data for these combinations, models can generalize compositionally.

## Implementation Fit

- **Implementability: HIGH — Data synthesis pipeline** buildable now
- **Small-model feasible:** Yes — generates training data, not model architecture
- **Integration fit:** Applicable to any agent training pipeline

## Key Insight
```
Problem: Skill combinations follow power-law distribution
         → Most training data covers common combinations
         → Long-tail combinations are underrepresented
         → Models fail at compositional generalization

Solution: STEPS identifies missing skill combinations
          → Synthesizes targeted training data
          → Fills the distribution gap
          → Enables compositional generalization
```

## Related Concepts
- [[skill-composition-procedural-learning]] — Day 2 research concept
- [[hermes-agent-architecture]] — Agent training patterns
