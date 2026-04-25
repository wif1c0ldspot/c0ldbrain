---
title: "Multica Platform"
type: concept
tags: [multi-agent, agent-platform, agent-teams, agent-harness, coding-agents, autopilot]
created: '2026-04-21'
updated: '2026-04-21'
confidence: high
status: current
priority: important
summary: "Open-source platform (17.5k★) for humans + AI agents as equal teammates. Shared workspace, issues, PRs, skills, autopilot scheduling. Supports multiple runtimes (Kimi Code CLI, Claude Code, Codex)."
sources:
- multica-kimi-k26-agent-teams-multicaai-2026-04
- multica-agent-memory-mem0ai-2026-04
---

# Multica Platform

## Summary

Multica is an open-source platform (17.5k★ GitHub stars) where humans and AI agents work as equal teammates on the same repository. Unlike single-agent tools (Claude Code, Cursor), Multica provides a shared workspace with unified issues, PRs, permissions, and conversation threads — enabling true multi-agent engineering teams.

## Key Concepts

### Core Primitives

- **Workspace** — isolated shared space with members, repos, settings
- **Member** — humans and agents share one permission model (both can be assigned issues, @-mentioned)
- **Agent** — named teammate with Prompt, Runtime, and Model. Runs 24/7
- **Runtime** — pluggable coding engine: Kimi Code CLI, Claude Code, Codex, etc.
- **Skill** — reusable procedure any agent or human can invoke ("team playbook")
- **Autopilot** — scheduled/webhook-triggered jobs that hand work to agents without human kickoff

### Agent Role Design Pattern

Effective multi-agent teams use distinct roles with clear boundaries:

| Role | Responsibility | Red Lines |
|------|---------------|-----------|
| Engineer | Pick up issues, write code + tests, open PRs | Never review PRs, never change issue status |
| Tech Lead | Break complex tasks into sub-issues, assign | Never write code directly |
| Reviewer | Comment on PRs (readability → correctness → coverage) | Never merge |
| Triager | Triage new issues, ask clarifying questions | Never close issues, never guess |
| Reporter | Produce periodic summaries/reports | No code authority |

### Prompt Engineering for Agents

Template:
```
You are <Name>, <Role> at <Org>.
Your job: <what you do>
Your personality: <voice, preferences>
What you DO NOT do: <red lines>
Your output format: <example>
```

**Key insight:** Red lines ("what you DO NOT do") matter more than responsibilities. Without boundaries, agents drift into unauthorized areas.

### Autopilot Pattern

Autopilot = trigger + agent + task description

Enables team rhythms without human intervention:
- Issue triage on new issues
- Code review when PRs open
- Weekly reports on schedule
- On-call rotations

### Agent Pipeline

Chain agents for end-to-end automation:
```
Tia (triage) → Kai (code) → Rae (review) → Ren (report)
```

### Model Cost Optimization

Use cheap models for routine roles (triager, reporter), premium models for hard work (engineering, tech lead). Don't overpay for simple tasks.

## Human-in-the-Loop Patterns

- Human reviews Kai's PRs after Rae's first pass
- Tia pushes ambiguous issues to "Needs Human Triage" list
- Humans @-mention agents to trigger work instantly
- Merge authority always stays with humans

## Implementation

- Desktop app (macOS/Linux/Windows) — multi-session, notifications, local repo
- Web app — same features minus native notifications
- Self-host — clone repo, full feature parity

## Related Concepts

- [[ai-coding-agents]]
- [[agent-architecture]]
- [[multica-relational-agent-memory]]
- [[multi-agent-collaboration]]
- [[claude-code]]
- [[agent-harness]]
- [[context-engineering]]

- [[agent-orchestration-stacks]]
- [[agent-skills-systems]]
- [[multi-agent-systems]]
- [[multica-kimi-k26-agent-teams-multicaai-2026-04]]