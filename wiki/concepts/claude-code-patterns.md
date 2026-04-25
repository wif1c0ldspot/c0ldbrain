---
confidence: high
created: '2026-04-06'
date: 2026-04-18
priority: important
status: current
summary: Proven Claude Code workflows and patterns - token optimization, skill graphs, planning, and automation
tags:
- claude-code
- workflows
- patterns
- token-optimization
- automation
title: Claude Code Patterns
type: concept
updated: '2026-04-18'
---

# Claude Code Patterns

## Overview

Claude Code is Anthropic's CLI tool for AI-assisted coding. These are proven patterns and workflows discovered through community usage.

## Core Patterns

### Token Optimization

#### Caveman Prompting
Minimal, direct prompts that reduce tokens while maintaining effectiveness:

**Verbose → Compressed:**
```
Verbose: "Please provide a detailed explanation of..."
Caveman: "Explain..."
```

**Best for:**
- Code generation
- Simple Q&A
- Routine edits
- Quick fixes

**Not for:**
- Complex reasoning
- Nuanced tasks
- Creative writing
- Ambiguous requirements

**Savings:** 50-75% token reduction reported

Sources:
- [[claude-caveman-prompting-strategy-2026-04]]

#### Model Routing
Use appropriate model tiers for tasks:

| Task | Model | Rationale |
|------|-------|-----------|
| Planning | Opus | Best reasoning |
| Implementation | Sonnet | Balance |
| Quick fixes | Haiku | Speed |

Commands:
- `/model opus` — Switch to Opus for complex planning
- `/model sonnet` — Default for implementation
- `/model haiku` — Fast for simple tasks

Sources:
- [[claude-code-opus-planning-2026-04]]

### Skill Organization

#### Skill Graphs
Visualize and organize Claude Code skills as a graph:

**Features:**
- Visual relationship mapping
- Dependency tracking
- Gap identification
- Coverage analysis

**Best Practices:**
- One skill per file
- Clear naming
- Link dependencies
- Keep hierarchy shallow

**Discovery:**
- Skill graphs revealed after months of usage
- Many users miss this feature initially
- Worth exploring for organization

Sources:
- [[claude-code-skill-graphs-2026-04]]

### Workflow Patterns

#### Agent Automation
Claude Code as autonomous agent:

**Job Search System:**
- Scrapes listings
- Generates applications
- Tracks status
- 700+ applications processed

**Implementation:**
- Custom tool integration
- Workflow orchestration
- State management
- Quality control

Sources:
- [[claude-caveman-token-strategy-2026-04]]

### Planning Workflow

```
1. /model opus — Switch to best reasoning
2. Describe architecture/problem
3. Get detailed plan
4. /model sonnet — Switch to implementation
5. Execute based on plan
```

**Benefits:**
- High-quality planning
- Focused implementation
- Reduced iteration
- Better outcomes

## Best Practices

### Effective Prompting

| Technique | Example | When |
|-----------|---------|------|
| Be specific | "Add error handling" | Clear intent |
| Show context | "This is a login function" | Relevant background |
| State constraints | "Must work offline" | Non-negotiables |
| Ask for options | "Suggest 3 approaches" | Decision needed |

### Workflow Optimization

1. **Start with `/model opus`** for complex tasks
2. **Use skill graphs** to organize reusable patterns
3. **Apply caveman prompting** for repetitive tasks
4. **Switch models** based on task complexity
5. **Track patterns** that work for your use case

### Integration Patterns

#### With Excalidraw
- Diagrams stream to Claude in real-time
- Shape-by-shape visualization
- Architecture discussions
- Visual + textual reasoning

Sources:
- [[excalidraw-claude-streaming-2026-04]]

## Anti-Patterns

### What NOT to Do

| Anti-Pattern | Problem | Better Approach |
|--------------|---------|-----------------|
| Verbose everything | Wastes tokens | Caveman prompting |
| Always Opus | Expensive | Route by task |
| No skill organization | Reinventing | Use skill graphs |
| Ignore model routing | Inefficient | Match model to task |

## Tool Integrations

### External Tools
Claude Code integrates with:

- **Excalidraw** — Diagram streaming
- **Git** — Version control
- **Shell** — Command execution
- **Editor** — Direct file manipulation

### Custom Tools
Extend via:
- Tool definitions
- Script execution
- API integrations
- Environment variables

## Related Concepts

- [[claude-code]] — Tool documentation
- [[token-optimization]] — Cost reduction
- [[skill-registry]] — Skill management
- [[agentic-ai]] — Autonomous patterns
- [[model-routing]] — Optimal model selection

## Sources

- [[claude-caveman-prompting-strategy-2026-04]]
- [[claude-code-skill-graphs-2026-04]]
- [[claude-code-opus-planning-2026-04]]
- [[excalidraw-claude-streaming-2026-04]]

- [[claude-integration]]
- [[jarvis-obsidian-claude-code-cyrilxbt-2026-04]]
- [[prompt-engineering]]