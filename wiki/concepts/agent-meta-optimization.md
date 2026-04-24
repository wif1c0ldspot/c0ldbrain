---
title: Agent Meta-Optimization
type: concept
tags: [ai-agents, autonomous-optimization, meta-agents, benchmarking]
sources:
- autoagent-kevinrgu-2026-04
- autogenesis-self-evolving-agent-protocol-2026-04
created: '2026-04-07'
updated: '2026-04-10'
status: current
confidence: high
agents: [hermes, claude, codex]
priority: critical
summary: Autonomous meta-agent systems that iteratively optimize AI agent configurations
 by modifying prompts, tools, and orchestration, then hill-climbing on benchmark
 scores.
---


# Agent Meta-Optimization

## Summary

Autonomous meta-agent systems represent the next evolution of AI agent engineering. Rather than developers manually tuning agent configurations, these systems autonomously iterate on agent parameters (prompts, tools, routing) and use score-driven hill-climbing to keep or discard changes.

## Core Pattern: Authorsearch for Agents

The pattern mirrors autoresearch (score-driven autonomous experimentation) but applies it to:

1. **Parameter Mutation:** Meta-agent modifies system prompts, tool definitions, agent configuration, and orchestration logic
2. **Benchmark Evaluation:** Changes are tested against a structured benchmark suite (Harbor format)
3. **Score-Driven Selection:** Changes are kept if they improve the score, discarded if worse
4. **Iterative Loop:** This runs overnight, accumulating improvements

## AutoAgent Implementation

From kevinrgu/autoagent (3.5k GitHub stars):

| Component | Purpose |
|-----------|---------|
| agent.py | Single-file harness containing config, tools, registry, routing, Harbor adapter |
| program.md | Human-written meta-agent instructions and task directives |
| tasks/ | Harbor-format evaluation tasks with tests and scoring |
| results.tsv | Experiment log tracking all iterations |
| Dockerfile.base | Containerized sandbox for safe autonomous execution |

## Design Philosophy

The human steers through `program.md` (what kind of agent to build), while the meta-agent handles the implementation details in `agent.py`. This separation of steering vs execution is the fundamental pattern of effective meta-agents.

## Score-Driven Optimization

Key principle: every experiment produces a numeric score (0.0-1.0) from deterministic test suites. The meta-agent uses this objective metric to guide its hill-climbing. This pattern appears in:

- Code agent optimization (AutoAgent)
- Trading strategy optimization (crypto-quant systems)
- Autonomous research pipelines (autoresearch)

## Benchmarking Standards

Harbor framework is emerging as the standard for agent evaluation:
- Tasks follow a consistent format (task.toml, instruction.md, tests, environment)
- Tests write scores (0.0-1.0) to verifier logs
- Deterministic or LLM-as-judge verification
- Docker-based isolation for reproducibility

## Related Concepts

[[coral-multi-agent-discovery]], [[ai-coding-agents]], [[hermes-agent-architecture]], [[quantitative-trading]]
