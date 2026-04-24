---
title: Skill Composition & Procedural Learning (Basal Ganglia Pathway)
type: concept
tags: [ai-agents, brain-inspired, skill-composition, procedural-memory, basal-ganglia, reinforcement-learning]
sources: [herakles-skill-chaining-2025, skillx-skill-kb-2026, toolrla-reward-decomposition-2026, pass-k-t-rl-capability-2026, metaclaw-meta-learning-2026, steps-compositional-generalization-2026, pi07-compositional-robotics-2026, evolving-programmatic-skill-networks-2026, skill0-skill-internalization-2026, smith-cognitive-memory-2025, synergistic-rl-cerebellum-basalganglia-2025]
confidence: high
status: current
agents: [hermes]
priority: critical
summary: "Pathway 2 of brain-inspired AI architecture: skill composition and procedural learning inspired by basal ganglia mechanisms for emergent agent capabilities."
---

# Skill Composition & Procedural Learning (Basal Ganglia Pathway)

Brain-inspired pathway for achieving emergent behavior in AI agents through modular skill composition and procedural memory mechanisms.

## Research Summary (2026-04-21)

Day 2 of 5-day brain-inspired research rotation. Reviewed 50+ papers (2025-2026) across four sub-areas.

## Key Findings

### 1. Automatic Skill Chaining
The dominant paradigm is **atomic skill decomposition** — breaking complex tasks into reusable, composable atomic skills.

| Paper | Score | Key Mechanism |
|-------|-------|---------------|
| [[herakles-skill-chaining-2025]] | 9/10 | Hierarchical RL + language for automatic skill compilation |
| [[skillx-skill-kb-2026]] | 9/10 | Automated cross-agent skill knowledge base construction |
| [[deco-task-decomposition-2026]] | 8/10 | Model-agnostic zero-shot composition from atomic decomposition |
| [[atomicvla-atomic-skill-2026]] | 8/10 | VLA model with atomic skill decomposition and continual acquisition |

**Critical insight:** Language serves as the **compositional backbone** — skill taxonomies, task descriptions, and instruction-following all enable cross-domain skill composition.

### 2. RL for Tool Selection
Moving beyond binary rewards to fine-grained credit assignment.

| Paper | Score | Key Mechanism |
|-------|-------|---------------|
| [[toolrla-reward-decomposition-2026]] | 9/10 | Multiplicative reward decomposition for tool agents (SFT→GRPO→DPO) |
| [[pass-k-t-rl-capability-2026]] | 9/10 | Proof RL genuinely expands capability (not just reliability) |
| [[autotool-dynamic-selection-2025]] | 8/10 | Dynamic tool selection with 200k rationale dataset |
| [[tinr-tool-internalized-2026]] | 8/10 | Internalizing tool knowledge into model parameters |

**Breakthrough:** PASS@(k,T) proves that RL enables **emergent compositional strategies** in tool-use that re-sampling cannot recover.

### 3. Procedural Memory & Habit Formation
**Procedural memory is the most underdeveloped component in AI agents** (confirmed by [[ai-hippocampus-survey-2026]]).

| Paper | Score | Key Mechanism |
|-------|-------|---------------|
| [[skill0-skill-internalization-2026]] | 9/10 | Converts dynamic skill loading → permanent procedural knowledge via RL |
| [[implicitmembench-2026]] | 9/10 | First benchmark for implicit/procedural memory in LLMs |
| [[lifebench-memory-2026]] | 9/10 | First benchmark separating declarative vs procedural memory |
| [[smith-cognitive-memory-2025]] | 9/10 | Unified procedural (tool creation) + declarative (knowledge) pathways |

**Key finding:** SKILL0 demonstrates the transition from **retrieval to habitual execution** — the basal ganglia pathway analog.

### 4. Basal Ganglia–Inspired Architectures

| Paper | Score | Key Mechanism |
|-------|-------|---------------|
| [[synergistic-rl-cerebellum-basalganglia-2025]] | 9/10 | Dual-system: cerebellum (predictive) + BG (reward-driven) |
| [[bg-rl-framework-2026]] | 8/10 | Three-layer BG emulation with dopamine-modulated STDP |
| [[bg-spijaker-neuromorphic-2025]] | 7/10 | BG on SpiNNaker neuromorphic hardware |

### 5. Skill Graph Composition (Highest Emergence)
**Evolving Programmatic Skill Networks (PSN)** scored **10/10** — skills as executable programs forming compositional networks that evolve through experience.

## Top Mechanisms by Emergence Score

| Rank | Paper | Score | Implementability |
|------|-------|-------|------------------|
| 1 | PSN (Evolving Programmatic Skill Networks) | 10/10 | Research prototype |
| 2 | HERAKLES (Hierarchical Skill Compilation) | 9/10 | Research |
| 3 | SkillX (Cross-Agent Skill KB) | 9/10 | **Practical — buildable now** |
| 4 | ToolRLA (Fine-Grained RL for Tools) | 9/10 | **Practical — GRPO/DPO pipeline** |
| 5 | PASS@(k,T) (RL Expands Capability) | 9/10 | Theoretical validation |
| 6 | SKILL0 (Procedural Internalization) | 9/10 | Research |
| 7 | STEPS (Skill Taxonomy Data Synthesis) | 9/10 | **Practical — data synthesis** |
| 8 | π₀.₇ (Compositional Robotics) | 9/10 | Industrial |

## Implementation Roadmap

### Immediate (Build Now)
1. **SkillX-style skill knowledge base** — Automated extraction of reusable skills from agent repositories
2. **ToolRLA-style reward decomposition** — Fine-grained GRPO/DPO pipeline for tool-using agents
3. **STEPS-style data synthesis** — Skill taxonomy-guided training data generation

### Near-Term (3-6 months)
4. **SKILL0-style procedural internalization** — Convert skill retrieval to habitual execution via RL
5. **Dual-system architecture** — Cerebellum (predictive/supervised) + BG (reward-driven) agent loop

### Long-Term (6-12 months)
6. **Evolving PSN** — Full programmatic skill network with creation, refinement, and reuse
7. **LifeBench/ImplicitMemBench integration** — Systematic evaluation of procedural memory

## Cross-Pathway Connections

- **Pathway 1 (Memory):** Procedural memory must integrate with episodic memory systems (Evo-MedAgent, HyperMem)
- **Pathway 3 (Global Workspace):** Skill composition requires broadcast mechanisms for skill selection
- **Pathway 4 (Predictive Coding):** Cerebellum component of dual-system uses predictive processing
- **Pathway 5 (Integration):** Neuromodulation (dopamine) drives the BG reward signal for skill learning

## Related Concepts
- [[skill-graphs]] — Practical three-level skill composition framework
- [[brain-inspired-agent-architecture]] — Master architecture document
- [[agentic-ai]] — General agent architecture patterns
- [[memory-systems]] — Persistent state management
- [[hermes-agent-architecture]] — This agent's architecture

## Sources
All sources listed above with `wikilink` citations.
