---
title: Top 67 Claude Skills - Full Dev Team Stack
type: source
tags:
- ai-agents
- skills
- claude
- development
- source
- social
- x
source_url: https://x.com/polydao/status/2044317956893471081
sources: []
created: '2026-04-15'
updated: '2026-04-15'
confidence: high
status: current
agents:
- hermes
priority: important
summary: '67 curated Claude Skills organized by use case: meta (Skill Creator, Write
  a Skill), planning (Grill Me, PRD), development (TDD, QA), tooling (Pre-Commit,
  Git Guardrails), writing, design, business, media, multi-agent orchestration.'
compiled: true
---

# Top 67 Claude Skills That Turn $20 Subscription Into Full Dev Team - Mr. Buzzoni (@polydao)

## Summary

Most people use Claude as a $20 autocomplete — type, get answer, move on. They don't realize Claude can run an entire dev team (architect, reviewer, debugger, docs writer) simultaneously. The difference: [[claude-skills|Claude Skills]] — reusable SKILL.md files that tell Claude exactly how to do specific work. 67 skills curated with full install commands, organized by use case.

## Key Concept: What Claude Skills Are

A skill is a folder with a SKILL.md file that tells Claude exactly how to do specific type of work:
- Step-by-step process
- Constraints
- Examples
- Helper scripts or templates

Instead of re-explaining process every session, install once as skill and reuse forever.

### Install Command Format
```bash
npx skills@latest add mattpocock/skills/[skill-name]
```

### Key Repos
- Official Anthropic skills: github.com/anthropics/skills
- Matt Pocock personal skills (15k stars): github.com/mattpocock/skills
- Community marketplace (66k+ skills): skillsmp.com

## Skills by Category

### Meta Skills - Managing AI Workspace

Skills to build, test, and organize other skills.

**Skill Creator**
- Purpose: Benchmarks Claude on your task, helps draft and iterate new skills based on real runs
- Use when: Turn messy workflow into clean SKILL.md
- Link: github.com/anthropics/skills/tree/main/skills/skill-creator
- How to use: Describe workflow in bullets, ask for first SKILL.md, run 3-5 test prompts, inspect failures, let it refine

**Write a Skill**
- Purpose: Guides Claude to write new skills with proper structure, progressive disclosure, bundled resources
- This is the right way to create skills that don't break over time
- Link: github.com/mattpocock/skills/tree/main/write-a-skill
- Install: `npx skills@latest add mattpocock/skills/write-a-skill`

**Find Skills**
- Purpose: Searches public marketplaces like SkillsMP for skills matching use case
- Tip: Treat finding skills like package management — search before you write, fork existing ones

### Planning and Design Skills

**Grill Me**
- Purpose: Forces Claude to ask relentless clarifying questions about your feature, one at a time, until every branch of decision tree is resolved
- Use for: New features, refactors, risky migrations
- Install: `npx skills@latest add mattpocock/skills/grill-me`
- Link: github.com/mattpocock/skills/tree/main/grill-me

**Write a PRD**
- Purpose: Creates PRD through interactive interview, codebase exploration, module design. Files as GitHub issue
- Install: `npx skills@latest add mattpocock/skills/write-a-prd`

**PRD to Plan**
- Purpose: Turns PRD into multi-phase implementation plan using tracer-bullet vertical slices. Reduces integration risk.
- Install: `npx skills@latest add mattpocock/skills/prd-to-plan`

**PRD to Issues**
- Purpose: Breaks PRD into independently-grabbable GitHub issues with vertical slices and blocking relationships
- Install: `npx skills@latest add mattpocock/skills/prd-to-issues`

**Design an Interface**
- Purpose: Generates 3-5 competing interface designs via parallel sub-agents
- Install: `npx skills@latest add mattpocock/skills/design-an-interface`

### Code Development Skills

**TDD**
- Purpose: Forces strict test-first, red-green-refactor loop
- Install: `npx skills@latest add mattpocock/skills/tdd`

**Triage Issue**
- Purpose: Investigates bug by exploring codebase, identifies root cause, files GitHub issue with TDD-based fix plan
- Install: `npx skills@latest add mattpocock/skills/triage-issue`

**QA**
- Purpose: Runs full QA pass over feature with issue breakdown including blocking relationships
- Install: `npx skills@latest add mattpocock/skills/qa`

**Improve Codebase Architecture**
- Purpose: Explores codebase for architectural improvement opportunities
- Install: `npx skills@latest add mattpocock/skills/improve-codebase-architecture`

**Systematic Debugging**
- Origin: Superpowers repo
- Purpose: 4-phase debugging methodology forbidding random "just try changing stuff" edits
- Link: github.com/obra/superpowers/tree/main/skills/systematic-debugging

**Superpowers**
- Full suite of battle-tested skills for TDD, debugging, refactoring, execution
- Link: github.com/obra/superpowers

### Tooling and Setup Skills

**Setup Pre-Commit**
- Purpose: Sets up Husky pre-commit hooks with lint-staged, Prettier, type checking, tests
- Install: `npx skills@latest add mattpocock/skills/setup-pre-commit`

**Git Guardrails for Claude Code**
- Purpose: Blocks dangerous git commands (push, reset --hard, clean) before execution
- Install: `npx skills@latest add mattpocock/skills/git-guardrails-claude-code`
- Note: Not optional for production repos — this is your safety net

**Dependency Auditor**
- Purpose: Scans package.json for outdated, vulnerable, or abandoned packages
- Install: `npx skills@latest add ComposioHQ/awesome-claude-skills/dependency-auditor`

### Writing and Knowledge Skills

**Edit Article**
- Purpose: Edits and improves articles by restructuring sections, improving clarity
- Install: `npx skills@latest add mattpocock/skills/edit-article`

**Ubiquitous Language**
- Purpose: Extracts DDD-style ubiquitous language glossary from conversation
- Install: `npx skills@latest add mattpocock/skills/ubiquitous-language`
- Note: Forces Claude to surface and define domain language before code. Codebase, docs, conversations share same words.

**Obsidian Vault**
- Purpose: Searches, creates, manages notes in Obsidian vault with wikilinks
- Install: `npx skills@latest add mattpocock/skills/obsidian-vault`

### UI, Design, Frontend

**Frontend Design**
- Link: github.com/anthropics/skills/tree/main/skills/frontend-design

**Theme Factory**
- Purpose: Generates complete color palettes and themes from text prompt
- Link: github.com/anthropics/skills/tree/main/skills/theme-factory

**Canvas Design**
- Purpose: Turns text prompts into social media graphics, posters
- Link: github.com/anthropics/skills/tree/main/skills/canvas-design

**Web Artifacts Builder**
- Purpose: Builds interactive dashboards, calculators, tools from natural language
- Link: github.com/anthropics/skills/tree/main/skills/web-artifacts-builder

### Business, Sales, Marketing

**Marketing Skills**
- 20+ skills for CRO, copywriting, email flows
- Link: github.com/coreyhaines31/marketingskills

**Claude SEO**
- Purpose: Full technical SEO audit, schema, on-page optimization
- Link: github.com/AgriciDaniel/claude-seo

### Multi-Agent Orchestration

**Stochastic Multi-Agent Consensus**
- Purpose: Spawns many sub-agents to solve same problem, aggregates answers
- Use for: Strategy decisions, architecture choices, risk analysis
- Link: github.com/hungv47/meta-skills

**Firecrawl Skill**
- Purpose: Scrapes structured data from hostile or complex sites
- Link: github.com/mendableai/firecrawl

## Recommended Workflow

1. **Start with meta skills** — Install Write a Skill and Skill Creator
2. **Add planning skills first** — Grill Me, Write a PRD, PRD to Plan (prevents 80% rework)
3. **Lock in code safety** — Git Guardrails, Setup Pre-Commit, TDD, Systematic Debugging on every repo
4. **Add Superpowers** as engineering base — github.com/obra/superpowers
5. **Use SkillsMP** to fill gaps — skillsmp.com (search before building)

## Related Concepts
- [[hermes-agent-architecture]] — agent skills system
- [[claude-skills]] — Claude Skills framework
- [[claude-code-from-source-2026-04]] — Claude Code editor

## Stats
177K views, 1828 bookmarks, 634 likes, 75 reposts (Apr 15, 2026)

## Author
Mr. Buzzoni (@polydao) — Posts on Claude, AI tools, prediction markets, crypto
