---
author: Garry Tan
confidence: high
created: '2026-04-16'
priority: reference
published: 2026-04
source_url: https://github.com/garrytan/gstack
stars: 74.8k
status: current
summary: Garry Tan's exact Claude Code setup - 23 opinionated tools that serve as
  CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA. Ships 10,000-20,000
  lines of code per day part-time.
tags:
- claude-code
- gstack
- garry-tan
- ai-agents
- skills
- y-combinator
title: gstack - Garry Tan's Claude Code Setup
type: source
updated: 2026-04-17
---


# gstack - Garry Tan's Claude Code Setup

**GitHub:** https://github.com/garrytan/gstack  
**Author:** Garry Tan (President & CEO of Y Combinator)  
**Stars:** 74.8k  
**Forks:** 10.6k

## Overview

> "I don't think I've typed like a line of code probably since December, basically, which is an extremely large change." — Andrej Karpathy, No Priors podcast, March 2026

Garry Tan's open source software factory. Turns Claude Code into a virtual engineering team. 23 specialists and 8 power tools, all slash commands, all Markdown, all free, MIT license.

**Recent Stats:**
- 600,000+ lines of production code in last 60 days (35% tests)
- 10,000-20,000 lines per day, part-time
- 1,237 contributions in 2026
- Last /retro: 140,751 lines added, 362 commits, ~115k net LOC in one week

## The 23 Specialists

| Role | Tool | Purpose |
|------|------|---------|
| CEO | `/office-hours`, `/plan-ceo-review` | Rethinks the product |
| Eng Manager | `/plan-eng-review` | Locks architecture |
| Designer | `/design-consultation`, `/design-shotgun` | Catches AI slop |
| Reviewer | `/review` | Finds production bugs |
| QA Lead | `/qa` | Opens a real browser |
| Security Officer | `/cso` | Runs OWASP + STRIDE audits |
| Release Engineer | `/ship`, `/land-and-deploy` | Ships the PR |
| + 16 more specialized tools | | |

## 8 Power Tools

- `/browse` - Web browsing skill
- `/benchmark` - Performance benchmarking
- `/connect-chrome` - Browser integration
- `/setup-browser-cookies` - Auth setup
- `/setup-deploy` - Deployment configuration
- `/retro` - Weekly retrospective
- `/investigate` - Root cause analysis
- `/autoplan` - Auto-review pipeline

## Key Concepts

### 1. Confusion Protocol

When encountering high-stakes ambiguity during coding:
- Two plausible architectures or data models for the same requirement
- A request that contradicts existing patterns
- A destructive operation where scope is unclear
- Missing context that would change approach significantly

**Action:** STOP. Name the ambiguity in one sentence. Present 2-3 options with tradeoffs. Ask the user. Do not guess on architectural or data model decisions.

### 2. Completeness Principle — Boil the Lake

AI makes completeness near-free. Always recommend the complete option over shortcuts — the delta is minutes with CC+gstack.

**Compression Ratios:**
| Task Type | Human Team | CC+gstack | Compression |
|-----------|-----------|-----------|-------------|
| Boilerplate | 2 days | 15 min | ~100x |
| Tests | 1 day | 15 min | ~50x |
| Feature | 1 week | 30 min | ~30x |
| Bug fix | 4 hours | 15 min | ~20x |

### 3. 6 Decision Principles (for /autoplan)

1. **Choose completeness** — Ship the whole thing
2. **Boil lakes** — Fix everything in blast radius
3. **Pragmatic** — 5 seconds choosing, not 5 minutes
4. **DRY** — Reject duplicates, reuse what exists
5. **Explicit over clever** — 10-line obvious fix > 200-line abstraction
6. **Bias toward action** — Merge > review cycles > stale deliberation

### 4. User Sovereignty

The user always has context models don't have — domain knowledge, business relationships, strategic timing, taste. When models agree on a change, that agreement is a **recommendation, not a decision**. Present it. The user decides.

## Multi-Agent Support

Works on 10 AI coding agents:
- Claude Code (primary)
- OpenAI Codex CLI
- OpenCode
- Cursor
- Factory Droid
- Slate
- Kiro
- Hermes
- GBrain (mod)

## Installation

```bash
# Step 1: Install on your machine
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
cd ~/.claude/skills/gstack && ./setup

# Step 2: Team mode (auto-updates)
cd ~/.claude/skills/gstack && ./setup --team
cd <your-repo>
~/.claude/skills/gstack/bin/gstack-team-init required
git add .claude/ CLAUDE.md && git commit -m "require gstack for AI-assisted work"
```

## Core Skills

### Product & Strategy
- `/office-hours` — Product interrogation with 6 forcing questions
- `/plan-ceo-review` — Strategic challenge with 4 scope modes

### Planning & Review
- `/autoplan` — Full review pipeline (CEO → Design → Eng → DX)
- `/plan-eng-review` — Architecture & tests review
- `/plan-design-review` — UI/UX gaps review
- `/plan-devex-review` — Developer experience review

### Execution
- `/ship` — Create PR, run tests, merge
- `/land-and-deploy` — Deploy to production
- `/qa` — Test the site, find bugs
- `/review` — Code review

### Operations
- `/investigate` — Root cause debugging
- `/retro` — Weekly engineering retrospective
- `/cso` — Security audit (OWASP + STRIDE)
- `/benchmark` — Performance testing

### Design
- `/design-consultation` — Design system review
- `/design-shotgun` — Rapid design variations
- `/design-html` — HTML/CSS implementation
- `/design-review` — Visual audit

## Repo Modes

- **solo** — You own everything. Investigate and fix proactively.
- **collaborative** — Flag issues via AskUserQuestion, don't fix (may be someone else's).

## Related Concepts

- [[claude-code]] — Claude Code ecosystem
- [[resolvers]] — Garry Tan's resolver pattern
- [[agency-agents]] — AI agency personas
- [[brain-inspired-agent-architecture]] — Layered decision making

## References

- Garry Tan's X: @garrytan
- Y Combinator
- Boil the Lake essay: https://garryslist.org/posts/boil-the-ocean
