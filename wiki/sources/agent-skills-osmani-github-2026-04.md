---
title: "addyosmani/agent-skills"
source: "https://github.com/addyosmani/agent-skills"
fetched: 2026-04-21
stars: 17k+

type: source
tags: [ai-agents, coding-agents, skills]
compiled: true
date: 2026-04-22---

# Agent Skills

Production-grade engineering skills for AI coding agents.

Skills encode the workflows, quality gates, and best practices that senior engineers use when building software. Packaged so AI agents follow them consistently across every phase of development.

## Lifecycle

```
  DEFINE          PLAN           BUILD          VERIFY         REVIEW          SHIP
 ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐
 │ Idea │ ───▶ │ Spec │ ───▶ │ Code │ ───▶ │ Test │ ───▶ │  QA  │ ───▶ │  Go  │
 │Refine│      │  PRD │      │ Impl │      │Debug │      │ Gate │      │ Live │
 └──────┘      └──────┘      └──────┘      └──────┘      └──────┘      └──────┘
  /spec          /plan          /build        /test         /review       /ship
```

## 7 Slash Commands

| Command | Purpose |
|---------|---------|
| /spec | Spec before code |
| /plan | Small, atomic tasks |
| /build | One slice at a time |
| /test | Tests are proof |
| /review | Improve code health |
| /code-simplify | Clarity over cleverness |
| /ship | Faster is safer |

## 20 Skills

### Define
- idea-refine — structured divergent/convergent thinking
- spec-driven-development — PRD covering objectives, commands, structure, testing, boundaries

### Plan
- planning-and-task-breakdown — decompose into small verifiable tasks with acceptance criteria

### Build
- incremental-implementation — thin vertical slices, feature flags, rollback-friendly
- test-driven-development — Red-Green-Refactor, test pyramid (80/15/5), DAMP, Beyonce Rule
- context-engineering — right info at right time, rules files, MCP integrations
- source-driven-development — ground decisions in official docs
- frontend-ui-engineering — component architecture, design systems, WCAG 2.1 AA
- api-and-interface-design — contract-first, Hyrum's Law, One-Version Rule

### Verify
- browser-testing-with-devtools — Chrome DevTools MCP for live runtime data
- debugging-and-error-recovery — 5-step triage: reproduce, localize, reduce, fix, guard

### Review
- code-review-and-quality — five-axis review, ~100 line changes, severity labels
- code-simplification — Chesterton's Fence, Rule of 500
- security-and-hardening — OWASP Top 10, auth patterns, secrets management
- performance-optimization — measure-first, Core Web Vitals, profiling

### Ship
- git-workflow-and-versioning — trunk-based dev, atomic commits, commit-as-save-point
- ci-cd-and-automation — Shift Left, feature flags, quality gates
- deprecation-and-migration — code-as-liability, zombie code removal
- documentation-and-adrs — Architecture Decision Records, document the *why*
- shipping-and-launch — pre-launch checklists, staged rollouts, rollback

## Agent Personas
- code-reviewer — Senior Staff Engineer standard
- test-engineer — QA Specialist, Prove-It pattern
- security-auditor — vulnerability detection, threat modeling

## Skill Anatomy

Frontmatter → Overview → When to Use → Process → Rationalizations (excuses + rebuttals) → Red Flags → Verification (evidence requirements)

Key principles:
- Process, not prose
- Anti-rationalization tables
- Verification non-negotiable
- Progressive disclosure (minimal tokens)

## Compatibility
Claude Code, Cursor, Gemini CLI, Windsurf, OpenCode, GitHub Copilot, Kiro, Codex
