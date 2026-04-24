---
title: "Skill Graphs"
type: concept
tags: [ai-agents, skill-graphs, skill-composition, agent-orchestration, agent-extensibility]
created: '2026-04-23'
updated: '2026-04-23'
confidence: high
status: current
priority: high
summary: "Three-level framework for composing agent skills: atoms (deterministic primitives), molecules (explicit orchestration of 2-10 atoms), and compounds (high-level playbooks requiring human supervision). Solves the reliability problem of deep skill graph dependencies."
sources:
- skill-graphs-shivsakhuja-2026-04
---

# Skill Graphs

## Overview

Skill Graphs organize agent capabilities as composable units at three distinct levels of abstraction: **atoms**, **molecules**, and **compounds**. This framework addresses the fundamental reliability problem of deep skill dependency chains — as skill graphs grow dense, agents become increasingly non-deterministic at calling skills past certain depths.

## The Problem with Deep Skill Graphs

Linking dependent skills in markdown files (Obsidian-style) works intuitively at small scale. However:

- **Depth fragility:** The more dependencies, the less reliable skill invocation becomes
- **Non-determinism:** Human drivers confront unpredictable agent behavior in dense graphs
- **Circular dependencies:** Unbounded chains create problematic loops
- **Judgement overreach:** Agents make too many runtime decisions when composition is implicit

## Three-Level Framework

### Atoms (Primitives)

Base-level, single-purpose building blocks. Narrow scope, almost deterministic.

**Characteristics:**
- Typically don't call other skills
- Super reliable (as close to deterministic as LLMs allow)
- Single capability per atom

**Examples:**
- Scrape LinkedIn profiles
- Verify email with Hunter
- Check email deliverability
- Research a topic
- Review a PR

### Molecules (Composites)

Scoped tasks composed of 2-10 atoms with explicit orchestration instructions.

**Characteristics:**
- Explicit instructions on when/how to call atomic skills
- Push composition into the skill, minimize runtime decision-making
- More agent judgement than atoms, but still constrained
- Two structural patterns:
  1. **Structured workflow:** Fixed chain of atoms (atom-1 → atom-2 → atom-3)
  2. **Orchestrator:** Knows available atoms, uses judgement to compose them for the prompt

**Example:**
> Find leads (atom-1 + atom-2) → qualify them (atom-3) → enrich them (atom-4) → add to spreadsheet (atom-5)

### Compounds (Playbooks)

High-level orchestrators running multiple molecules. This is where meaningful agent autonomy lives.

**Characteristics:**
- Less deterministic by nature (many judgement levels)
- Trickiest to get right
- Require human driver (at least today)
- Human judgement operates at this level or higher

**Examples:**
- "Run outbound sales playbook"
- "Plan and build this feature, then review and QA it"

## Leverage Economics

**Core insight:** Human brain RAM (parallel task context-switching capacity) is the limiting resource, not agent capability.

**Scenario:** Brain can context-switch between 5 agents in parallel

| Level | Tasks per Agent | Total Output |
|-------|----------------|--------------|
| Atomic | 1 task × 5 agents | 5 units |
| Molecular | 10 atoms × 5 agents | 50 units |
| Compound | 10 molecules × 10 atoms × 5 agents | **500 units** |

> "For the same amount of brain RAM and time, work output varies massively if you drive atomic work vs compound work."

**Analogy:** A CTO with 1000 employees doesn't fix every bug — trusts ICs to handle atomic work reliably while focusing on strategic direction.

## Implementation Naming

Different implementations use different terminology for the same three levels:

| Framework | Atoms | Molecules | Compounds |
|-----------|-------|-----------|-----------|
| Sakhuja framework | atoms | molecules | compounds |
| Practice (Sakhuja's co) | capabilities | composites | playbooks |
| Hermes skills | atomic skills | composite skills | playbook skills |

## Reliability Ceiling

Estimated practical limits:

- **Atoms:** Should be near-deterministic (no skill calls)
- **Molecules:** Very reliable with explicit orchestration (2-10 atoms)
- **Compounds:** Reliability degrades beyond 8-10 molecules
- **Beyond compounds:** Higher abstractions will be needed as compound reliability improves

## Key Requirements

For the framework to deliver leverage:

1. **Every atom solid** — deterministic, well-tested primitives
2. **Molecules chain dependably** — explicit composition, minimal runtime surprise
3. **Compound autonomy sufficient** — agent can make real decisions at this level
4. **Testing investment** — reliability at every level is non-trivial and time-consuming to validate

## Comparison with Other Patterns

| Pattern | Organization | Composition Level | Human Role |
|---------|-------------|-------------------|------------|
| Skill Graphs (this) | 3-level hierarchy | Explicit at molecule, autonomous at compound | Drive compounds |
| Agent Skills Systems | Lifecycle phases | Phase-mapped workflows | Phase-by-phase |
| Procedural Learning | Basal ganglia pathways | Automatic skill chaining | Supervise emergence |

## Related Concepts

- [[agent-skills-systems]] — Lifecycle-phase skill organization with anti-rationalization
- [[skill-composition-procedural-learning]] — Brain-inspired automatic skill chaining research
- [[agent-orchestration-stacks]] — Two-layer orchestration + memory architecture
- [[skill-registry]] — Skill metadata and discovery pattern
- [[skills-pattern]] — Dynamic skill loading and capability-based routing
