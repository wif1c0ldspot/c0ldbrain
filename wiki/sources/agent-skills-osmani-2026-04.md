---
title: Agent Skills — Addy Osmani's Production-Grade Engineering Skills for AI Coding
  Agents
type: source
author: '@addyosmani (Google Chrome team)'
date: 2026-04-21
source: https://github.com/addyosmani/agent-skills
stars: 17k+
updated: '2026-04-21'
created: '2026-04-16'
confidence: high
status: current
priority: important
tags:
- ai-coding-agents
- developer-tools
- skill-systems
- engineering-practices
- google-swe
summary: 20 production-grade skills for AI coding agents, organized by development
  lifecycle (Define→Plan→Build→Verify→Review→Ship). Encodes Google SWE practices —
  Hyrum's Law, Beyonce Rule, test pyramid, trunk-based dev. Works with Claude Code,
  Cursor, Gemini CLI, Windsurf, Copilot.
compiled: true
---

## Summary

Addy Osmani's agent-skills is a 17k+ star collection of 20 production-grade engineering skills for AI coding agents. Organized as 6 lifecycle phases with 7 slash commands as entry points. Encodes senior engineering practices from Google's SWE culture directly into agent workflows.

## Key Points

- **20 skills** across 6 phases: Define → Plan → Build → Verify → Review → Ship
- **7 slash commands** map to lifecycle: /spec, /plan, /build, /test, /review, /code-simplify, /ship
- Skills auto-activate based on context (designing API triggers api-and-interface-design)
- **Anti-rationalization tables** — every skill has common excuses + counter-arguments
- **Verification is non-negotiable** — evidence requirements, "seems right" never sufficient
- Encodes Google SWE practices: Hyrum's Law, Beyonce Rule, test pyramid (80/15/5), Chesterton's Fence, trunk-based dev, Shift Left
- Works with: Claude Code, Cursor, Gemini CLI, Windsurf, OpenCode, GitHub Copilot, Kiro, Codex

## 20 Skills by Phase

### Define
| Skill | Purpose |
|-------|---------|
| idea-refine | Divergent/convergent thinking, vague ideas → concrete proposals |
| spec-driven-development | PRD before code: objectives, commands, structure, testing, boundaries |

### Plan
| Skill | Purpose |
|-------|---------|
| planning-and-task-breakdown | Decompose specs into small verifiable tasks with acceptance criteria |

### Build
| Skill | Purpose |
|-------|---------|
| incremental-implementation | Thin vertical slices, feature flags, safe defaults, rollback-friendly |
| test-driven-development | Red-Green-Refactor, test pyramid, DAMP over DRY, Beyonce Rule |
| context-engineering | Feed agents right info at right time, rules files, MCP integrations |
| source-driven-development | Ground decisions in official docs, verify and cite sources |
| frontend-ui-engineering | Component architecture, design systems, WCAG 2.1 AA accessibility |
| api-and-interface-design | Contract-first, Hyrum's Law, One-Version Rule, error semantics |

### Verify
| Skill | Purpose |
|-------|---------|
| browser-testing-with-devtools | Chrome DevTools MCP for live runtime data, DOM, console, network |
| debugging-and-error-recovery | Five-step triage: reproduce, localize, reduce, fix, guard |

### Review
| Skill | Purpose |
|-------|---------|
| code-review-and-quality | Five-axis review, ~100 line changes, severity labels (Nit/Optional/FYI) |
| code-simplification | Chesterton's Fence, Rule of 500, reduce complexity preserving behavior |
| security-and-hardening | OWASP Top 10, auth patterns, secrets management, dependency auditing |
| performance-optimization | Measure-first, Core Web Vitals, profiling, bundle analysis |

### Ship
| Skill | Purpose |
|-------|---------|
| git-workflow-and-versioning | Trunk-based dev, atomic commits, commit-as-save-point |
| ci-cd-and-automation | Shift Left, Faster is Safer, feature flags, quality gates |
| deprecation-and-migration | Code-as-liability, compulsory vs advisory deprecation, zombie removal |
| documentation-and-adrs | Architecture Decision Records, document the *why* |
| shipping-and-launch | Pre-launch checklists, staged rollouts, rollback procedures |

## Agent Personas

| Agent | Role |
|-------|------|
| code-reviewer | Senior Staff Engineer — "would a staff engineer approve this?" |
| test-engineer | QA Specialist — test strategy, Prove-It pattern |
| security-auditor | Security Engineer — vulnerability detection, threat modeling |

## Skill Anatomy

Each skill follows:
```
Frontmatter → Overview → When to Use → Process (steps) → Rationalizations (excuses + rebuttals) → Red Flags → Verification (evidence requirements)
```

Key design: process not prose, anti-rationalization tables, verification non-negotiable, progressive disclosure (minimal tokens).

## Concepts

- [[agent-skills-systems]]
- [[ai-coding-agents]]
- [[claude-skills]]
- [[skill-registry]]
