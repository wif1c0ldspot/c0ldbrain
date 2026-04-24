---
compiled: 2026-04-15
confidence: medium
created: '2026-04-16'
priority: important
source_url: https://x.com/noisyb0y1/status/2043609541477044439
status: current
summary: Google engineer (11yr exp) automated 80% of work using Claude Code, reducing
  8h/day to 2-3h/day. Covers Karpathy CLAUDE.md 4 principles, Everything Claude Code
  (153K+ stars), and Claude Code v2.1.100 token inflation bug.
tags:
- ai-agents
- developer-tools
- prompt-engineering
- token-optimization
- cost
title: Google Engineer Automated 80% Work with Claude Code — Full System Breakdown
type: source
updated: '2026-04-18'
---


# Google Engineer Automated 80% Work with Claude Code — Full System Breakdown

**Author:** @noisyb0y1 (Noisy)
**Platform:** X/Twitter
**Stats:** 2.1M views, 1.2K likes, 6.8K bookmarks, 168 reposts

## Key Insights

### Part 1 — Karpathy's CLAUDE.md Four Principles

Andrej Karpathy identified the most common LLM coding mistakes (over-engineering, ignoring existing patterns, adding unnecessary dependencies). Someone turned these into a single CLAUDE.md file — 15,000 GitHub stars in one week.

**Four principles:**
1. **Think Before Coding** — stops wrong assumptions and missed tradeoffs
2. **Simplicity First** — stops over-engineering and bloated abstractions
3. **Surgical Changes** — stops touching code nobody asked to touch
4. **Goal-Driven Execution** — tests first, verified success criteria

**Results:** Convention violations dropped from ~40% to ~3%. Setup: 5 minutes.

**Auto-generate command:**
```
claude -p "Read the entire project and create a CLAUDE.md based on: Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution. Adapt to the real architecture you see." --allowedTools Bash,Write,Read
```

### Part 2 — Everything Claude Code (153K+ GitHub stars)

GitHub: https://github.com/affaan-m/everything-claude-code

Complete AI operating system for building products — not just prompts.
- 30+ specialized agents (planner, architect, TDD guide, code reviewer, security reviewer, loop operator)
- 180+ skills (TDD, security, research, content)
- AgentShield: 1,282 security tests built into config
- Cross-platform: Claude, Codex, Cursor, OpenCode, Gemini

**WARNING:** Don't load everything at once — 27 agents + 64 skills burns context limits fast.

### Part 3 — Claude Code v2.1.100 Token Inflation Bug

HTTP proxy interception across 4 Claude Code versions revealed:
- v2.1.98: 169,514 bytes request → 49,726 tokens charged
- v2.1.100: 168,536 bytes request → 69,922 tokens charged
- Difference: -978 bytes but +20,196 tokens charged

Inflation is server-side, invisible to users, can't verify through /context.

**Impact:**
- CLAUDE.md instructions diluted by 20K tokens of hidden content
- Quality degrades faster in long sessions
- Claude ignores rules without explanation
- Claude Max limits burn 40% faster

**Fix:** `npx claude-code@2.1.98`

## Technical Details

### Full Automation Case Study

Google engineer (11 years exp) built three-part system:
1. **Classification** (every 15 min): dotnet app calls GitLab API → Claude reads issue, decides if ready for dev → posts draft response if not
2. **Execution:** Subagent starts working → pushes to new branch → creates PR
3. **PR workflow:** Checks for PR + comments → implements review feedback

**Result:** 8h/day → 2-3h/day of review/testing. Same code quality. 80% automation.

### Setup Checklist

1. Karpathy CLAUDE.md (5 min)
2. Everything Claude Code (10 min) — install only needed agents
3. Token fix (30 sec) — downgrade to v2.1.98

### Reliability Notes

- Token inflation claim is unverified — treat with skepticism
- Everything Claude Code repo is real and genuinely popular
- Karpathy's CLAUDE.md principles align with established prompt engineering best practices
- Claims of $28K passive income are marketing language — verify independently

## Related Concepts

- [[claude-md-best-practices]] — full concept page on CLAUDE.md
- [[ai-coding-agents]] — agent ecosystem overview
- [[token-optimization]] — token management and cost strategies
