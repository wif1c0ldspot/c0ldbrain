---
title: DESIGN.md
type: concept
tags:
- ai-agents
- developer-tools
- design-systems
- knowledge-management
sources:
- design-md-google-labs-2026-04
updated: 2026-04-22
confidence: high
status: current
priority: important
summary: File format for describing visual identity to AI coding agents. Combines
  YAML design tokens with markdown rationale. Enables reproducible, agent-driven UI
  generation from structured design specifications.
created: '2026-04-24'
---

# DESIGN.md

## What It Is

DESIGN.md is an open-source file format specification from Google Labs for describing a visual identity to coding agents. It gives agents a persistent, structured understanding of a design system — replacing ad-hoc prompts with a declarative, versionable specification.

## Core Idea

Instead of telling an agent "make it look premium" every session, you write a DESIGN.md once. The agent reads it and produces consistent, on-brand UIs.

> "DESIGN.md gives agents a persistent, structured understanding of a design system."

## The Two-Layer Format

### Layer 1: YAML Front Matter (Machine-Readable Tokens)

Normative design values — exact colors, typography, spacing, rounding:

```yaml
---
name: Heritage
colors:
  primary: "#1A1C1E"
  secondary: "#6C7278"
  tertiary: "#B8422E"
  neutral: "#F7F5F2"
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 3rem
rounded:
  sm: 4px
  md: 8px
---
```

### Layer 2: Markdown Body (Human-Readable Rationale)

Context for how to apply the tokens:

```markdown
## Overview

Architectural Minimalism meets Journalistic Gravitas.

## Colors

- **Primary (#1A1C1E):** Deep ink for headlines and core text.
- **Tertiary (#B8422E):** "Boston Clay" — the sole driver for interaction.
```

## Token Types

| Type | Format | Example |
|:-----|:-------|:--------|
| Color | `#` + hex (sRGB) | `"#1A1C1E"` |
| Dimension | number + unit | `48px`, `-0.02em` |
| Token Reference | `{path.to.token}` | `{colors.primary}` |
| Typography | object with font properties | `fontFamily`, `fontSize`, etc. |

## Canonical Section Order

| # | Section | Purpose |
|:--|:--------|:--------|
| 1 | Overview | Brand identity, mood |
| 2 | Colors | Palette definitions |
| 3 | Typography | Font scales, styles |
| 4 | Layout | Spacing, grid |
| 5 | Elevation & Depth | Shadows, layering |
| 6 | Shapes | Borders, radii |
| 7 | Components | Reusable UI pieces |
| 8 | Do's and Don'ts | Usage guidelines |

## Agent Consumer Behavior

| Scenario | Behavior |
|:---------|:---------|
| Unknown section | Preserve; do not error |
| Unknown color name | Accept if value valid |
| Unknown typography name | Accept as valid |
| Unknown component property | Accept with warning |
| Duplicate section | Error; reject file |

## Tooling Ecosystem

### CLI (`@google/design.md`)

| Command | Purpose |
|:--------|:--------|
| `lint` | Validate structure, catch broken refs, WCAG contrast |
| `diff` | Token-level regression detection between versions |
| `export --format tailwind` | Convert to Tailwind theme config |
| `export --format dtcg` | Convert to W3C DTCG tokens.json |
| `spec` | Output spec for agent prompt injection |

### Programmatic API

```typescript
import { lint } from '@google/design.md/linter';
const report = lint(markdownString);
console.log(report.findings);       // Finding[]
console.log(report.summary);        // { errors, warnings, info }
console.log(report.designSystem);   // Parsed DesignSystemState
```

## Why It Matters

| Without DESIGN.md | With DESIGN.md |
|:------------------|:---------------|
| Repeated prompts per session | One file, persistent |
| Inconsistent agent output | Reproducible results |
| No version control for design | Git-tracked spec |
| Ad-hoc aesthetic descriptions | Structured, measurable tokens |
| Manual WCAG checking | Automated contrast validation |

## Applications

- **Design-to-code workflows**: Agents generate UI directly from spec
- **Design system versioning**: Diff versions to catch regressions
- **Multi-agent consistency**: All agents share same design source
- **Accessibility compliance**: Built-in WCAG AA contrast checks

## Challenges

- Format is `alpha` — expect breaking changes
- Requires agent to understand and respect the spec
- No visual preview (text-only format)
- Limited to tokenizable design properties

## Key Quotes

> "Tokens give agents exact values. Prose tells them why those values exist and how to apply them."

> "An agent that reads this file will produce a UI with deep ink headlines in Public Sans, a warm limestone background, and Boston Clay call-to-action buttons."

## Related Concepts

- [[ai-coding-agents|related]] — Agents that consume DESIGN.md
- [[hermes-agent-architecture|related]] — Execution layer integration potential
- [[mcp-protocol|related]] — Protocol patterns for agent-native tools
- [[skill-registry|related]] — Skill-driven agent capabilities

## Sources

- [[design-md-google-labs-2026-04]] — Source page with full specification
- https://github.com/google-labs-code/design.md
