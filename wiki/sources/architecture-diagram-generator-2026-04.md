---
compiled: 2026-04-15
confidence: high
created: '2026-04-16'
priority: 2
source_url: https://github.com/Cocoon-AI/architecture-diagram-generator
status: current
summary: Claude.ai Skill by Cocoon AI that generates professional dark-themed architecture
  diagrams as self-contained HTML/SVG files. Semantic color coding, no JS dependencies,
  MIT licensed. Describe system in plain English, get a shareable diagram.
tags:
- developer-tools
- ai-agents
- open-source
title: Architecture Diagram Generator — Claude Skill for Dark-Themed System Diagrams
type: source
updated: '2026-04-18'
---


# Architecture Diagram Generator — Claude Skill for Dark-Themed System Diagrams

**Author:** Cocoon AI (hello@cocoon-ai.com)
**Platform:** GitHub
**License:** MIT

## Key Insights

### Semantic Color Coding

The skill uses consistent color semantics across all diagrams:

| Color | Hex | Category |
|-------|-----|----------|
| Cyan | — | Frontend components |
| Emerald | — | Backend services |
| Violet | — | Database/storage |
| Amber | — | Cloud/infrastructure |
| Rose | — | Security layer |
| Slate | — | External systems |

### Zero Dependencies Output

- Single self-contained HTML file with embedded CSS and inline SVG
- No JavaScript dependencies — opens in any modern browser
- Dark theme with slate-950 background (#020617) and 40px grid pattern
- JetBrains Mono font (Google Fonts)
- SVG viewBox: typically 1000-1100px wide, responsive
- Output includes header with animated status indicator, main SVG diagram, 3 summary cards, and footer

### Installation Methods

1. **Claude.ai Skill** (requires Pro/Max/Team/Enterprise): Upload architecture-diagram.zip via Settings > Capabilities > Skills
2. **Claude Code CLI:** Extract to ~/.claude/skills/
3. **Project Knowledge:** Add to Claude.ai Projects as knowledge

### Usage Workflow

1. Install the skill
2. Describe your architecture (plain text, or have AI analyze your codebase)
3. Ask: "Use your architecture diagram skill to create an architecture diagram from this description"
4. Iterate via chat — add components, change layouts, fix issues

## Technical Details

### Skill Structure

```
architecture-diagram/
├── SKILL.md              # Skill instructions
└── assets/
    └── template.html     # Base template
```

### Output Capabilities

- Shareable as-is, printable, exportable to PDF, hostable statically
- Adaptable template for custom skill integration
- Related to excalidraw skill (different approach — HTML/SVG vs Excalidraw JSON)

### Integration Potential

- Could adapt the template for Hermes Agent skill to auto-generate architecture docs
- Complements [[visual-explainer]] skill (Mermaid diagrams) with static SVG approach
- Potential addition to [[skill-registry]] as a diagramming capability

## Related Concepts

- [[skill-registry]] — index of Hermes agent skills
- [[visual-explainer]] — terminal-to-HTML with Mermaid diagrams
- [[ai-coding-agents]] — agent ecosystem and tooling
