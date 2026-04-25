---
title: Agent Skills Systems
type: concept
tags:
- ai-coding-agents
- skill-systems
- engineering-practices
- lifecycle
- agent-extensibility
created: '2026-04-21'
updated: '2026-04-21'
confidence: high
status: current
priority: important
summary: Pattern of organizing AI coding agent capabilities as structured skills mapped
  to software development lifecycle phases. Skills encode workflows, quality gates,
  and best practices — not just prompts. Anti-rationalization and verification are
  mandatory.
sources:
- agent-skills-osmani-2026-04
---

# Agent Skills Systems

## Summary

Agent skills systems organize AI coding agent capabilities as structured, reusable workflows mapped to software development lifecycle phases. Unlike simple prompt templates, skills encode complete workflows with steps, checkpoints, anti-rationalization tables, and evidence-based verification gates. The pattern separates *what* to do (process) from *how* to prompt (implementation).

## Key Concepts

### Lifecycle-Phase Organization

The dominant pattern organizes skills into development phases:

```
Define → Plan → Build → Verify → Review → Ship
```

Each phase has specific skills with clear triggering conditions. Skills auto-activate based on context (e.g., designing API triggers API design skill).

### Skill Anatomy

Every well-designed skill follows:

| Section | Purpose |
|---------|---------|
| Frontmatter | Name, description, triggering conditions |
| Overview | What this skill does |
| When to Use | Explicit trigger conditions |
| Process | Step-by-step workflow with checkpoints |
| Rationalizations | Common excuses agents use to skip steps + counter-arguments |
| Red Flags | Signs something's wrong |
| Verification | Evidence requirements — "seems right" never sufficient |

### Anti-Rationalization Tables

Critical innovation: every skill includes a table of common excuses agents make to skip steps, with documented counter-arguments. Example:

| Excuse | Counter-argument |
|--------|-----------------|
| "I'll add tests later" | Tests are proof, not decoration. No test = no evidence it works |
| "It's a small change" | Small changes cause most production incidents |

### Verification is Non-Negotiable

Skills end with evidence requirements:
- Tests passing, build output, runtime data
- "Seems right" or "looks correct" never sufficient
- Human-readable evidence of correctness

### Progressive Disclosure

Entry point (SKILL.md) is minimal. Supporting references load only when needed, keeping token usage efficient.

### Multi-Tool Compatibility

Good skill systems work across tools:
- Claude Code (native slash commands)
- Cursor (agent rules)
- Gemini CLI (native skills)
- Windsurf, OpenCode, GitHub Copilot, Kiro, Codex
- Plain Markdown works with any agent accepting system prompts

## Implementation Patterns

### Slash Commands as Entry Points

Map commands to lifecycle phases:
- `/spec` → Define phase
- `/plan` → Plan phase
- `/build` → Build phase
- `/test` → Verify phase
- `/review` → Review phase
- `/ship` → Ship phase

### Agent Personas

Pre-configured specialist perspectives:
- Code Reviewer (Senior Staff Engineer standard)
- Test Engineer (QA Specialist)
- Security Auditor (threat modeling)

### Reference Checklists

Supplementary material loaded on-demand:
- Testing patterns
- Security checklist
- Performance checklist
- Accessibility checklist

## Key Insights

- **Process > Prompts** — workflows with steps and checkpoints beat one-shot prompts
- **Anti-rationalization** — prevents agents from skipping "boring" but critical steps
- **Verification gates** — evidence-based proof, not agent confidence
- **Lifecycle mapping** — organize by what developer is doing, not by tool capability
- **Senior engineering encoded** — practices like Hyrum's Law, Beyonce Rule, test pyramid baked into workflows

## Related Concepts

- [[skill-graphs]] — Three-level composition: atoms, molecules, compounds
- [[ai-coding-agents]]
- [[claude-skills]]
- [[skill-registry]]
- [[context-engineering]]
- [[test-driven-development]]
- [[multica-platform]]

- [[agent-skills-osmani-2026-04]]
- [[resolvers]]
- [[skill-graphs-shivsakhuja-2026-04]]