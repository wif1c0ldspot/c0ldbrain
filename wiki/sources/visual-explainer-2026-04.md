---
confidence: high
created: '2026-04-16'
priority: important
sources:
- visual-explainer-2026-04
status: current
summary: Claude Code plugin (7.3k stars) that converts terminal output (tables, diffs,
  plans) into styled HTML with Mermaid diagrams, dark/light themes, and slide deck
  support.
tags:
- ai-coding-agents
- open-source
- developer-tools
title: visual-explainer - Claude Code Visualization Skill
type: source
updated: '2026-04-07'
compiled: true
---


# visual-explainer — Claude Code Visualization Skill

**Source:** https://github.com/nicobailon/visual-explainer
**Type:** Claude Code plugin / agent skill
**Author:** nicobailon
**Version:** 0.6.3 (Mar 29, 2026)
**Stats:** 7.3k stars, 498 forks, 38 commits, 16 tags
**License:** MIT

## Summary

A Claude Code plugin skill that converts complex terminal output (diffs, plans, architecture, data tables) into styled HTML pages with proper typography instead of ASCII art. Solves the problem of unreadable box-drawing diagrams and wrapping tables in terminal output.

## Key Features

| Feature | Detail |
|--------|--------|
| Auto-detect | Routes to HTML when output has 4+ rows or 3+ columns |
| Mermaid diagrams | Interactive with zoom and pan |
| Themes | Dark/light |
| Slide deck mode | `--slides` flag converts scrollable pages to slides |
| Vercel deploy | `share.sh` deploys HTML for live URLs |
| No dependencies | Only needs a browser, no build step |

## Commands

| Command | Output |
|---------|--------|
| /generate-web-diagram | HTML diagram |
| /generate-visual-plan | Implementation plan |
| /generate-slides | Magazine slide deck |
| /diff-review | Architecture + code review |
| /plan-review | Plan vs codebase risk assessment |
| /project-recap | Context switch summary |
| /fact-check | Document vs code accuracy |
| /share | Vercel deployment |

## Architecture

SKILL.md + commands/ + references/ (CSS patterns, libraries, responsive nav, slide patterns) + templates/ (architecture, flowchart, data table, slide deck) + scripts/share.sh

## Supported Agents

Claude Code (marketplace), Pi, OpenAI Codex

## Key Insight

Replaces our `ascii-art`, `ascii-video`, and `mermaid-video` skills for a more practical approach — HTML output that opens in browser, terminal-agnostic.

## Related Concepts

- [[ai-coding-agents]] — AI coding tool ecosystem
- [[hermes-agent-architecture]] — Hermes agent capabilities
- [[open-source-ai-infra]] — Open source AI tools
