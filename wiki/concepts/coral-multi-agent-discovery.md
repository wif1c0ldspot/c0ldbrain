---
confidence: high
created: '2026-04-16'
priority: important
sources:
- raw/github/coral-human-agent-society-2026-04.md
- raw/social/coral-multiagent-discovery.md
status: current
summary: "CORAL (arXiv 2604.01658): multi-agent self-evolution infrastructure. Coding agents in git worktrees, shared .coral/ state, eval loops, heartbeat reflection. SOTA 10+ tasks, 3-10x improvement. 526 stars, MIT, Python."
tags:
- ai-agents
- multi-agent
- self-evolving
- autonomous-optimization
- coding-agents
- claude-code
- codex
- alpha-evolve
title: CORAL - Autonomous Multi-Agent Evolution
type: concept
updated: '2026-04-23'
---

# CORAL - Autonomous Multi-Agent Evolution

## Core Idea

Multi-agent infrastructure where autonomous coding agents run in isolated git worktrees, share knowledge via symlinked `.coral/` directory, and continuously evolve solutions through eval loops + heartbeat-triggered reflection. Give it a codebase and a grading script — CORAL handles the rest.

## Architecture

- **Agent Manager** spawns N agents (Claude Code, Codex, or OpenCode) each in own git worktree
- **Shared state** `.coral/public/` (attempts, notes, skills) symlinked into every worktree — zero sync overhead
- **Eval loop**: agents call `coral eval -m "..."` → stage, commit, grade in one shot
- **Heartbeat system**: auto-triggered prompts (reflect, consolidate, pivot on plateau)
- **Warm-start**: pre-coding research phase with bundled deep-research skill
- **Web dashboard**: real-time leaderboard, attempt diffs, agent monitoring

## Results (arXiv 2604.01658)

- SOTA on 10+ tasks
- 3-10x improvement vs baselines
- 50%+ breakthroughs from cross-agent knowledge building
- 4 co-evolving agents: 1363→1103 cycles (TSP)

## Key Design Patterns

1. **Git worktree isolation** — Each agent works in its own branch; merge conflicts impossible
2. **Shared knowledge via symlinks** — `.coral/public/` visible to all agents in real time
3. **Heartbeat reflection** — Forced pauses: reflect (anchor in results), consolidate (synthesize notes), pivot (change direction on plateau)
4. **Grader protocol** — Subclass `TaskGrader`, implement `evaluate()`, agents can't see grader code
5. **CLI orchestration** — 17+ commands for full lifecycle management

## Task Domains

Kernel engineering, math (Erdős, packing), drug design, DNA design, SWE-bench, terminal bench, frontier CS (100+ problems), COVID vaccine prediction, ADRS cloud optimization

## Project Details

- **Repo**: https://github.com/Human-Agent-Society/CORAL
- **Stars**: 526 | **Forks**: 64
- **License**: MIT
- **Language**: Python
- **Created**: 2026-03-16 | **Updated**: 2026-04-23
- **Affiliations**: NUS, Stanford (logo assets in repo)

## Sources

- [[coral-human-agent-society-2026-04]]
- [[coral-multiagent-discovery]]

## Related Concepts

- [[multi-agent-systems]]
- [[multi-agent-collaboration]]
- [[claude-code]]
- [[ai-coding-agents]]
- [[agent-meta-optimization]]
- [[memory-systems]]
- [[mcp-protocol]]
