---
title: Claude Skills — Reusable Agent Workflows
type: concept
tags:
- ai-agents
- claude
- skills
- development
- concept
sources:
- claude-skills-67-polydao-2026-04
created: '2026-04-15'
updated: '2026-04-15'
confidence: high
status: current
agents:
- hermes
priority: important
summary: "Claude's skill framework — SKILL.md folders with step-by-step processes, constraints, examples. Installed via npx, shared via GitHub repos and SkillsMP marketplace. 66k+ community skills available."
---

# Claude Skills — Reusable Agent Workflows

## Summary

Claude's skill framework for packaging reusable workflows as SKILL.md files. Each skill folder contains a markdown file that tells Claude exactly how to perform specific work: step-by-step processes, constraints, examples, and bundled helper scripts or templates. Installed via npm (`npx skills@latest add`), shared via GitHub repos, and discoverable via SkillsMP marketplace (66k+ skills).

## What a Skill Is

A skill is a folder with a `SKILL.md` file defining:
- **Purpose** — what the skill does and when to use it
- **Step-by-step process** — exact workflow for Claude to follow
- **Constraints** — boundaries, guardrails, and rules
- **Examples** — concrete usage patterns
- **Helper scripts** — bundled templates or utilities

Instead of re-explaining process every session, install once as skill and reuse forever.

## Installation

```bash
# Standard format
npx skills@latest add mattpocock/skills/[skill-name]

# Examples
npx skills@latest add mattpocock/skills/tdd
npx skills@latest add mattpocock/skills/grill-me
npx skills@latest add anthropics/skills/auto-commit
```

## Repositories

| Repo | Type | Notes |
|-------|-------|-------|
| github.com/anthropics/skills | Official | Core skills from Anthropic |
| github.com/mattpocock/skills | Personal | 15k stars, production-grade |
| skillsmp.com | Marketplace | 66k+ community skills |
| github.com/ComposioHQ/awesome-claude-skills | Curated | Aggregated list |
| github.com/obra/superpowers | Suite | TDD, debugging, refactoring |

## Key Skill Categories

### Meta Skills
- **Skill Creator** — Benchmarks Claude on task, drafts skills from real runs
- **Write a Skill** — Guides proper skill structure, progressive disclosure
- **Find Skills** — Searches SkillsMP for existing skills

### Planning & Design
- **Grill Me** — Relentless clarifying questions to resolve decision trees
- **Write a PRD** — Creates PRD via interview + codebase exploration
- **PRD to Plan** — Multi-phase implementation with tracer-bullet slices
- **Design an Interface** — 3-5 competing designs via parallel sub-agents

### Development
- **TDD** — Test-first red-green-refactor loop
- **Systematic Debugging** — 4-phase methodology, no random edits
- **Superpowers** — Battle-tested TDD/debugging/refactoring suite
- **QA** — Full QA pass with blocking relationships

### Tooling
- **Setup Pre-Commit** — Husky hooks, lint-staged, Prettier
- **Git Guardrails** — Blocks dangerous git commands (push, reset --hard)
- **Dependency Auditor** — Scans package.json for vulnerable packages

### Writing & Knowledge
- **Edit Article** — Restructures articles, improves clarity
- **Ubiquitous Language** — DDD glossary extraction from conversation
- **Obsidian Vault** — Manages vault notes with wikilinks

### Multi-Agent
- **Stochastic Multi-Agent Consensus** — Spawns many sub-agents, aggregates answers
- **Firecrawl Skill** — Scrapes hostile/complex sites

## Comparison with [[hermes-agent-architecture|Hermes Skills]]

| Aspect | Claude Skills | Hermes Skills |
|--------|---------------|---------------|
| Format | SKILL.md file | SKILL.md file |
| Storage | GitHub repos | ~/.hermes/skills/ |
| Installation | npm (npx) | Built-in (auto-loaded) |
| Discovery | SkillsMP marketplace | skills_list command |
| Categories | 66k+ community skills | 600+ curated skills |
| Runtime | Claude Code / API | Any MCP-compatible agent |

Claude Skills and Hermes Skills share the same conceptual model — reusable workflows packaged as markdown files. Hermes Skills are optimized for agent tool calling with skill_view() auto-loading, while Claude Skills integrate with Claude Code editor.

## Best Practices

1. **Search before building** — Check SkillsMP for existing skills before writing new ones
2. **Start with meta skills** — Install Write a Skill and Skill Creator first
3. **Use proper structure** — Write a Skill ensures progressive disclosure and bundled resources
4. **Layer systematically** — Planning → Dev → Tooling → Business skills
5. **Test skills** — Run 3-5 test prompts, inspect failures, iterate

## Related
- [[claude-skills-67-polydao-2026-04]] — curated 67 skills list
- [[hermes-agent-architecture]] — Hermes skills system
- [[claude-code-from-source-2026-04]] — Claude Code editor
- [[agentic-ai]] — agent development patterns
