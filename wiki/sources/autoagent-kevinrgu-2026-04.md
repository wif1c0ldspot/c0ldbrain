---
title: AutoAgent - Autonomous Agent Harness Engineering
type: source
tags:
- ai-agents
- autonomous-optimization
- meta-agents
sources:
- github-autoagent
created: '2026-04-07'
updated: '2026-04-07'
status: compiled
confidence: high
priority: important
summary: AutoAgent is an autonomous meta-agent system that iteratively optimizes AI
 agent harnesses overnight by modifying prompts, tools, and configuration, then hill-climbing
 on benchmark scores via the Harbor framework.
---

# AutoAgent - Autonomous Agent Harness Engineering

**URL:** https://github.com/kevinrgu/autoagent
**Author:** kevinrgu (Third Layer Inc)
**Stars:** 3.5k | **Forks:** 373
**Last updated:** Apr 4, 2026
**License:** MIT

## Summary

AutoAgent is an autonomous meta-agent system that iteratively optimizes AI agent harnesses overnight. Like autoresearch but applied to agent engineering: the meta-agent modifies system prompts, tools, agent configuration, and orchestration; runs benchmarks via Harbor; checks scores; keeps or discards changes based on whether they improve the score.

## Key Architecture

- **Separation of Concerns:** Human edits `program.md` (instructions), meta-agent edits `agent.py` (harness)
- **Single-File Harness:** agent.py contains config, tools, registry, routing, and Harbor adapter
- **Harbor Integration:** Uses Harbor benchmark framework for deterministic evaluation
- **Score-Driven:** Hill-climbing on numeric scores (0.0-1.0) from test suites
- **Docker Isolation:** Agent runs in container, cannot damage host

## Relevance to Hermes

This pattern mirrors the quantitative trading strategy optimization loop: modify parameters, test against benchmark, keep if better. Could be applied to Hermes Agent skill optimization.

## Related Concepts

- [[ai-coding-agents]] - the broader ecosystem this fits into
- [[hermes-agent-architecture]] - could adopt this meta-optimization pattern
- [[memory-systems]] - agent skills are a form of persistent memory
- [[skill-registry]] - similar skill system structure
