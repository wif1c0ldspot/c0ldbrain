---
title: "DESIGN.md — Format Specification for Agent Design Systems"
type: source
tags: [ai-agents, developer-tools, design-systems, hermes, infrastructure]
sources: []
updated: 2026-04-22
confidence: high
status: current
summary: "Google Labs open-source format for describing visual identity to coding agents. Combines YAML design tokens with markdown rationale. Includes CLI toolkit for lint, diff, export, and spec generation."
created: 2026-04-22
priority: important
---

# DESIGN.md — Format Specification for Agent Design Systems

**Author:** Google Labs (david east / @davideast)  
**Repository:** https://github.com/google-labs-code/design.md  
**Stars:** 1.4k | **Forks:** 93  
**License:** Apache 2.0  
**Status:** Alpha (active development)

## Summary

DESIGN.md is a file format that gives coding agents a persistent, structured understanding of a design system. It combines machine-readable design tokens (YAML front matter) with human-readable design rationale (markdown prose). Agents read the file and produce UIs that match the specified visual identity.

## Key Takeaways

1. **Two-layer format**: YAML tokens (normative values) + markdown prose (context for application)
2. **Agent-native**: Designed specifically for AI coding agents, not just human designers
3. **CLI toolkit**: Lint, diff, export (Tailwind/DTCG), and spec generation
4. **W3C-aligned**: Tokens inspired by W3C Design Token Format
5. **WCAG-aware**: Built-in contrast ratio checking

## Token Schema

```yaml
version: <string>          # optional, current: "alpha"
name: <string>
description: <string>      # optional
colors:
  <token-name>: <Color>
typography:
  <token-name>: <Typography>
rounded:
  <scale-level>: <Dimension>
spacing:
  <scale-level>: <Dimension | number>
components:
  <component-name>:
    <token-name>: <string | token reference>
```

## Section Order (Canonical)

| # | Section | Aliases |
|:--|:--------|:--------|
| 1 | Overview | Brand & Style |
| 2 | Colors | |
| 3 | Typography | |
| 4 | Layout | Layout & Spacing |
| 5 | Elevation & Depth | Elevation |
| 6 | Shapes | |
| 7 | Components | |
| 8 | Do's and Don'ts | |

## CLI Commands

| Command | Purpose | Exit Code |
|:--------|:--------|:----------|
| `lint` | Validate structure, broken refs, WCAG contrast | 1 if errors |
| `diff` | Compare two DESIGN.md versions for regression | 1 if regressions |
| `export --format tailwind|dtcg` | Convert tokens to other formats | — |
| `spec` | Output format spec for agent prompt injection | — |

## Linting Rules

| Rule | Severity | What it checks |
|:-----|:---------|:---------------|
| `broken-ref` | error | Unresolvable token references |
| `missing-primary` | warning | No primary color defined |
| `contrast-ratio` | warning | WCAG AA contrast below 4.5:1 |
| `orphaned-tokens` | warning | Colors never referenced |
| `missing-typography` | warning | No typography tokens |
| `section-order` | warning | Sections out of canonical order |
| `token-summary` | info | Token count per section |
| `missing-sections` | info | Optional sections absent |

## Related Concepts

- [[design-md|related]] — The DESIGN.md format concept page
- [[ai-coding-agents|related]] — Agents that consume DESIGN.md
- [[hermes-agent-architecture|related]] — Agent execution layer that could integrate DESIGN.md
- [[mcp-protocol|related]] — Protocol patterns for agent tool design
