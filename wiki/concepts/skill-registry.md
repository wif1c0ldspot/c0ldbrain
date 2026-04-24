---
title: Skill Registry
type: reference
tags: [hermes, ai-agents]
sources:
- hermes-agent-skills-hub-2026-04
- claude-code-skill-graphs-2026-04
- architecture-diagram-generator-2026-04
- agent-skills-osmani-2026-04
created: '2026-04-06'
updated: '2026-04-15'
confidence: high
status: current
agents: [hermes]
priority: important
summary: Index of all 45+ skills available to Hermes Agent, organized by category
 with descriptions and locations.
---


# Skill Registry

## Summary

Index of skills available to Hermes Agent. Skills are procedural knowledge — how to do things.
The official Skills Hub catalogs 643 total skills across 4 registries (see [[skill-registry]]).

## How Skills Work

Skills are markdown files with YAML frontmatter that inject instructions into Hermes' context when loaded:
- Check available: `skills_list()` returns all loaded skills
- Load skill: `skill_view()` reads full skill content
- Update skill: `skill_manage()` to patch/edit/create
- Follow instructions: skills contain numbered steps, warnings, verification

## Crypto-Quant Skills (11+)

| Skill | Purpose | Location |
|-------|---------|----------|
| crypto-quant | Production crypto trading architecture | ~/.hermes/skills/crypto-quant/ |
| backtesting-workflow | End-to-end backtesting | Backtest pipeline |
| multi-bot-management | Manage concurrent bot processes | Bot runner |
| strategy-optimization | End-to-end strategy optimization | Strategy runner |
| debugging-playbook | Debug live trading issues | Debug guide |
| live-troubleshooting | Transition to live trading | Live guide |
| hourly-momentum-optimizer | Hourly momentum strategy | Hourly optimizer |
| hourly-momentum-live-bot | 3 optimized strategies, live | Live bot |
| minutes_15m_momentum | 15-min momentum for TRX/PENGU | Strategy file |
| shadow_strategy | Shadow trading mode | Shadow mode |

## AI & Research Skills

| Skill | Purpose |
|-------|---------|
| arxiv | Search academic papers |
| duckduckgo-search | Free web search (text, news, images) |
| blogwatcher | Monitor blogs and RSS feeds |
| ml-paper-writing | Write NeurIPS/ICML/ICLR papers |
| dspy | Declarative AI system programming |
| domain-intel | Passive domain reconnaissance |

## Devops & Infrastructure

| Skill | Purpose |
|-------|---------|
| python-uv-packaging | uv package manager setup |
| webhook-subscriptions | Create event-driven webhooks |
| bot-process-discovery | Manage bot instances via shell |
| smart-model-routing | Auto-route tasks to optimal model tier |
| local-model-configuration | Use local models for tool calling |
| hermes-agent-setup | Configure Hermes Agent |
| hermes-local-model-config | Local model routing |

## Software Development

| Skill | Purpose |
|-------|---------|
| code-review | Security and performance reviews |
| test-driven-development | TDD implementation |
| systematic-debugging | Debug any bug or failure |
| subagent-driven-development | Parallelize complex work |
| self-correction-loop | 4-phase reflexive validation |
| plan | Implementation plan writing |
| writing-plans | Multi-step planning |
| post-implementation-audit | Verify labels, docs, code |

## Productivity

| Skill | Purpose |
|-------|---------|
| daily-ai-research-workflow | Automated research pipeline |
| daily-ai-training-lessons | Structured training delivery |
| google-workspace | Gmail, Calendar, Drive |
| obsidian | Read/search/create Obsidian notes |
| notion | Notion API operations |
| nano-pdf | Edit PDFs with natural language |
| streamlit-dashboard | Functional dashboard creation |

## Other Skills

| Skill | Purpose |
|-------|---------|
| ascii-art, ascii-video | Visual content |
| excalidraw | Hand-drawn diagrams |
| songwriting, heartmula | Music generation |
| home-assistant, openhue | Smart home |
| github-*, codebase-inspection | GitHub integration |
| mcp tools, native-mcp, mcporter | MCP server management |

## Diagram & Visualization Skills

| Skill | Purpose | Source |
|-------|---------|--------|
| excalidraw | Hand-drawn diagrams | Built-in |
| architecture-diagram-generator | Dark-themed HTML/SVG architecture diagrams | [[architecture-diagram-generator-2026-04]] |

### Architecture Diagram Generator

Cocoon AI skill that generates professional dark-themed architecture diagrams as self-contained HTML files. Describe your system in plain English, get a shareable SVG diagram.

- **Output:** Single HTML file with inline SVG, no JS dependencies
- **Theme:** Slate-950 background, JetBrains Mono font, 40px grid
- **Semantic colors:** Cyan (frontend), Emerald (backend), Violet (database), Amber (cloud), Rose (security), Slate (external)
- **Install:** Upload zip to Claude.ai Settings > Capabilities > Skills, or extract to ~/.claude/skills/
- **License:** MIT
- **GitHub:** https://github.com/Cocoon-AI/architecture-diagram-generator

## External Skill Patterns (from agent-skills-osmani-2026-04)

Addy Osmani's Agent Skills (15.6k stars) provides 7 slash commands demonstrating the skill/command pattern:
- `/plan`, `/debug`, `/review`, `/refactor`, `/test`, `/document`, `/ship`
- Each command encapsulates a complete workflow
- Chainable for full development lifecycle
- Compatible with Claude Code, Cursor, and generic agents

## Related Concepts

- [[career-ops]] — Job search pipeline via Claude Code

[[visual-explainer]], [[ai-coding-agents]], [[token-optimization]], [[agent-cli-tools]]
