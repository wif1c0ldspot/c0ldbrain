---
title: Synergistic RL by Cooperation of Cerebellum and Basal Ganglia
type: source
tags:
- brain-inspired
- basal-ganglia
- cerebellum
- dual-system
- neuromorphic
- reinforcement-learning
confidence: high
status: current
summary: 'Dual-system RL with cerebellum (predictive/supervised) + BG (reward-driven).
  Score: 9/10 emergence potential.'
priority: reference
updated: '2026-04-24'
created: '2026-04-24'
compiled: true
---

# Synergistic RL by Cooperation of Cerebellum and Basal Ganglia

**Source:** Yoshida et al., 2025

## Key Findings

- **Dual-system RL:** Cerebellum (supervised/predictive) + Basal Ganglia (reward-driven)
- Complementary learning rules in cooperative architecture
- Most biologically faithful BG-agent architecture found in this research cycle

## Emergence Potential: 9/10

**Why it matters:** The dual-system architecture maps directly to human skill learning:
- **Cerebellum:** Predicts outcomes, provides supervised corrections
- **Basal Ganglia:** Drives reward-based skill selection and habit formation

## Implementation Fit

- **Implementability:** Research prototype
- **Small-model feasible:** Yes — dual-system doesn't require massive models
- **Integration fit:** High — could enhance existing agent loop

## Architecture for AI Agents
```
Agent Decision Loop
├── Cerebellum Module (Predictive)
│   ├── World model predictions
│   ├── Error prediction
│   └── Supervised corrections
├── Basal Ganglia Module (Reward-Driven)
│   ├── Skill selection policy
│   ├── Reward-based learning
│   └── Habit formation
└── Cooperative Interface
    ├── Predictions inform selection
    ├── Selection improves predictions
    └── Synergistic skill learning
```

## Related Concepts
- [[skill-composition-procedural-learning]] — Day 2 research concept
- [[brain-inspired-agent-architecture]] — Master architecture
