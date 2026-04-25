---
title: 'Skill Graphs 2.0: Atoms, Molecules, Compounds'
author: '@shivsakhuja'
date: 2026-04-23
source: https://x.com/shivsakhuja/status/2047124337191444844
type: source
tags:
- ai-agents
- skill-graphs
- skill-composition
- agent-orchestration
confidence: high
status: current
priority: important
updated: '2026-04-24'
created: '2026-04-24'
summary: 'Auto-generated placeholder for Skill Graphs 2.0: Atoms, Molecules, Compounds'
compiled: true
source_url: https://x.com/shivsakhuja/status/2047124337191444844
---

## Summary

Shiv Sakhuja proposes a three-level skill composition framework (atoms, molecules, compounds) to solve the reliability problem of deep skill graphs. Atoms are deterministic primitives, molecules chain 2-10 atoms with explicit orchestration, and compounds are high-level playbooks requiring human supervision. The core insight: human brain RAM is the limiting resource, so agents should drive compounds (100x leverage) not atoms.

## Key Points

- **Problem:** Dense skill graphs suffer from non-determinism at depth — agents fail to reliably call skills past certain dependency chain lengths
- **Solution:** Compose skills at three distinct levels rather than arbitrary graph depth
- **Atoms:** Single-purpose, deterministic primitives (e.g., scrape LinkedIn, verify email). Don't call other skills.
- **Molecules:** Scoped tasks using 2-10 atoms with explicit instructions on when/how to call them. Two structures: (1) structured workflow chain, (2) orchestrator with judgement.
- **Compounds:** High-level orchestrators running multiple molecules (e.g., "run outbound sales playbook"). Require human driver. Less deterministic by nature.
- **Leverage math:** 5 compounds × 10 molecules × 10 atoms = 500 atomic units of work for same brain RAM as driving 5 atomic tasks
- **Reliability ceiling:** Compounds spanning >8-10 molecules may hit reliability limits
- **Implementation names:** capabilities (atoms), composites (molecules), playbooks (compounds)
- **Testing bottleneck:** Reliability/consistency at every level is non-trivial and time-consuming to test

## Full Content

See raw source: [[skill-graphs-shivsakhuja-2026-04]]

## Related Concepts

- [[skill-graphs]] — Main concept page for the atoms/molecules/compounds framework
- [[skill-composition-procedural-learning]] — Brain-inspired research on skill composition
- [[agent-skills-systems]] — Lifecycle-phase skill organization pattern
- [[agent-orchestration-stacks]] — Two-layer orchestration + memory stacks
