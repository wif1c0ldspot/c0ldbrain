---
title: "CORAL — Human-Agent-Society/CORAL"
type: source
tags: [github, multi-agent, self-evolving, auto-research, coding-agents]
source_url: https://github.com/Human-Agent-Society/CORAL
sources: [raw/github/coral-human-agent-society-2026-04.md, raw/social/coral-multiagent-discovery.md]
created: '2026-04-23'
updated: '2026-04-23'
confidence: high
status: current
priority: important
summary: "Multi-agent self-evolution infrastructure. Coding agents in git worktrees, shared .coral/ state, eval loops, heartbeat prompts. 526 stars, MIT."
---

# CORAL — Human-Agent-Society/CORAL

**Source:** https://github.com/Human-Agent-Society/CORAL
**Stars:** 526 | **MIT** | **Python** | **arXiv 2604.01658**

## What It Does

Spawns N coding agents (Claude Code/Codex/OpenCode) in git worktrees. Agents write code, commit, eval, share knowledge via `.coral/` symlinks. Heartbeat triggers reflection, consolidation, pivoting. SOTA 10+ tasks, 3-10x vs baselines.

## Key Design

- Git worktree isolation per agent
- Shared state via symlinks (zero sync overhead)
- Heartbeat: reflect → consolidate → pivot (on plateau)
- Eval loop: `coral eval -m "..."` stages + commits + grades
- Warm-start: pre-coding literature review
- Web dashboard: real-time leaderboard

## Related

- [[coral-multi-agent-discovery]]
- [[multi-agent-systems]]
- [[claude-code]]
