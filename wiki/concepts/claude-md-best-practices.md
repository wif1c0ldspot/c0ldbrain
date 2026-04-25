---
title: CLAUDE.md Best Practices & Claude Code Automation
type: concept
tags:
- claude-code
- claude-md
- karpathy
- automation
- agent-systems
- token-bug
sources:
- claude-caveman-prompting-strategy-2026-04
- noisyb0y1-claude-code-thread-2026-04
- google-engineer-claude-code-automation-2026-04
- claude-code-from-source-2026-04
created: '2026-04-15'
updated: '2026-04-15'
confidence: medium
status: current
agents:
- claude
- codex
- cursor
- opencode
priority: important
summary: Karpathy CLAUDE.md principles, Everything Claude Code agent system (153K+
  stars), and Claude Code v2.1.100 token inflation bug. Full automation case study.
---

# CLAUDE.md Best Practices & Claude Code Automation

## Summary

Comprehensive system for automating development with Claude Code, based on three components: Karpathy-inspired CLAUDE.md behavioral rules, the Everything Claude Code multi-agent system, and awareness of token inflation bugs in recent versions.

## Karpathy CLAUDE.md Principles

Andrej Karpathy identified predictable LLM coding mistakes (over-engineering, ignoring patterns, unnecessary dependencies). These were codified into a single CLAUDE.md file — 15K GitHub stars in one week.

**Four core principles:**
1. Think Before Coding — stops wrong assumptions and missed tradeoffs
2. Simplicity First — stops over-engineering and bloated abstractions
3. Surgical Changes — stops touching code nobody asked to touch
4. Goal-Driven Execution — tests first, verified success criteria

**Results:** Convention violations drop from ~40% to ~3%. Setup time: 5 minutes.

**Auto-generate command:**
```
claude -p "Read the entire project and create a CLAUDE.md based on: Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution. Adapt to the real architecture you see." --allowedTools Bash,Write,Read
```

## Everything Claude Code

GitHub: https://github.com/affaan-m/everything-claude-code (153,000+ stars)

Complete AI operating system for building products. Not just prompts — a multi-agent engineering system.

**Components:**
- 30+ specialized agents (planner, architect, TDD guide, code reviewer, security reviewer, loop operator)
- 180+ skills (TDD, security, research, content)
- AgentShield: 1,282 security tests built into config
- Cross-platform: Claude, Codex, Cursor, OpenCode, Gemini

**Install:** `/plugin marketplace add affaan-m/everything-claude-code`

**Critical warning:** Don't load all agents at once. 27 agents + 64 skills simultaneously burns context limits fast. Load only what you need.

## Claude Code v2.1.100 Token Inflation Bug

**Claim:** HTTP proxy testing revealed v2.1.100 charges ~20K more tokens than v2.1.98 for equivalent requests (fewer bytes sent, more tokens billed). Inflation is server-side and invisible.

**Impact:**
- CLAUDE.md instructions diluted by hidden 20K tokens
- Quality degrades faster in long sessions
- Claude Max limits burn ~40% faster

**Fix:** `npx claude-code@2.1.98`

**Note:** This claim is from a viral thread (2.1M views). Treat as unverified — the token inflation numbers should be independently confirmed.

## Full Automation Case Study

Google engineer (11 years exp) built a three-part system with Claude Code + dotnet:

1. **Classification** (every 15 min): GitLab API → Claude reads issue → decides if ready for dev → posts draft if not
2. **Execution**: Subagent starts → pushes to branch → creates PR
3. **PR workflow**: Checks for PR/comments → implements review feedback

**Result:** 8h/day coding → 2-3h/day review. Same code quality. 80% automation.

## Setup Checklist (15-20 min)

1. CLAUDE.md (5 min)
2. Everything Claude Code (10 min) — selective install only
3. Token fix (30 sec) — downgrade to v2.1.98

## Related Concepts

- [[ai-coding-agents]] — broader agent ecosystem
- [[token-optimization-and-efficiency]] — token management strategies
- [[agentic-ai]] — agent architectures and patterns

## Source Reference

Additional source: [[google-engineer-claude-code-automation-2026-04]] — provides expanded detail on the same automation case study, including the full setup checklist and reliability assessment. Key additions from this source: the 3-step automation system (classify → execute → PR workflow) running on 15-minute cycles via dotnet + GitLab API integration.

## Claude Code Internals (from claude-code-from-source-2026-04)

18-chapter reverse-engineering book provides deep architectural context:
- Agent loop: perception-action cycle with tool pipeline
- Multi-agent orchestration and sub-agent delegation
- File-based memory via CLAUDE.md persistence
- Context window management for long sessions
- Validates and extends the patterns described above

- [[claude-code-from-source-2026-04]]
- [[langflow-claude-code-integration]]
- [[token-optimization]]
- [[karpathy-wiki-self-evolving-claude-2026-04-06]]
- [[noisyb0y1-claude-code-thread-2026-04]]