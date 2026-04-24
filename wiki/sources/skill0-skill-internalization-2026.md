---
title: 'SKILL0: In-Context Agentic RL for Skill Internalization'
type: source
tags:
- ai-agents
- procedural-memory
- habit-formation
- skill-internalization
- reinforcement-learning
confidence: high
status: current
summary: 'Converts dynamic skill loading into permanent procedural knowledge via RL.
  Score: 9/10 emergence potential.'
priority: important
updated: '2026-04-24'
created: '2026-04-24'
compiled: true
---

# SKILL0: In-Context Agentic RL for Skill Internalization

**Source:** Lu et al., 2026

## Key Findings

- Transforms **retrieval-based skill loading** into **permanent procedural knowledge** via RL
- Agents internalize skills that were previously loaded dynamically
- The transition: retrieval → habitual execution (basal ganglia pathway analog)
- Addresses the overhead of repeated skill retrieval in production agents

## Emergence Potential: 9/10

**Why it matters:** This is the most direct analog to the basal ganglia pathway in the research. The transition from declarative (retrieved) to procedural (habitual) knowledge is the core mechanism of human skill learning.

## Implementation Fit

- **Implementability:** Research prototype
- **Small-model feasible:** Yes — internalization reduces inference overhead
- **Integration fit:** High — maps directly to Hermes skill loading mechanism

## Architecture Analogy
```
Human Basal Ganglia          SKILL0 Mechanism
─────────────────          ─────────────────
Striatum (learning)    →    RL optimization of skill execution
Dopamine (reward)      →    Task success signal
Habit formation        →    Skill internalization into model weights
Procedural memory      →    No longer needs skill documentation
```

## Related Concepts
- [[skill-composition-procedural-learning]] — Day 2 research concept
- [[memory-systems]] — Agent memory architecture
