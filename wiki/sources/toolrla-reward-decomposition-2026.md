---
title: 'ToolRLA: Multiplicative Reward Decomposition for Tool-Integrated Agents'
type: source
tags:
- ai-agents
- reinforcement-learning
- tool-selection
- reward-decomposition
- grpo
- dpo
confidence: high
status: current
summary: 'Three-stage post-training (SFT→GRPO→DPO) with fine-grained multiplicative
  reward for tool agents. Score: 9/10.'
priority: important
updated: '2026-04-24'
created: '2026-04-24'
compiled: true
source_url: aggregate

---

# ToolRLA: Multiplicative Reward Decomposition for Tool-Integrated Agents

**Source:** arXiv:2603.01620 (2026-03-11)
**Author:** Pengbo Liu

## Key Findings

- Three-stage post-training pipeline: SFT → GRPO → DPO for domain-specific tool agents
- **Core contribution:** Fine-grained reward with multiplicative decomposition
- Separately penalizes tool selection errors vs malformed parameters
- Goes beyond coarse binary rewards in existing RL approaches

## Emergence Potential: 9/10

**Why it matters:** Directly addresses RL-based tool selection with fine-grained credit assignment. The multiplicative reward decomposition enables agents to learn which tool selection errors matter most.

## Implementation Fit

- **Implementability: HIGH — Practical GRPO/DPO pipeline** buildable now
- **Small-model feasible:** Yes — works with existing RLHF infrastructure
- **Integration fit:** Directly applicable to Hermes tool-use training

## Pipeline
```
Stage 1: SFT (Supervised Fine-Tuning)
    → Learn tool call format

Stage 2: GRPO (Group Relative Policy Optimization)
    → Optimize tool selection with multiplicative reward

Stage 3: DPO (Direct Preference Optimization)
    → Refine parameter generation with preference pairs
```

## Reward Decomposition
```
R_total = R_tool_selection × R_parameter_quality × R_task_success
```
Each component independently scored, enabling precise credit assignment.

## Related Concepts
- [[skill-composition-procedural-learning]] — Day 2 research concept
- [[hermes-agent-architecture]] — Hermes tool-use patterns
