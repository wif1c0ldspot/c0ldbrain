---
title: Harness Design
type: concept
tags:
- ai-engineering
- agentic-coding
- harness-design
- multi-agent
- context-management
sources:
- anthropic-harness-design-long-running-apps
- thealexker-harness-optimization-guide-2026-04
- agent-harnesses-harrison-chase-2026
- hwchase17-agent-harnesses-2026-04
- claude-code-agent-design-space-arxiv-2026-04
created: '2026-04-19'
updated: '2026-04-19'
confidence: high
status: current
priority: important
summary: Design patterns for AI agent harnesses — GAN-inspired multi-agent systems,
  progressive disclosure, R.P.I. framework, context management, and optimization strategies
---

# Harness Design

## Summary

Harness design is the engineering discipline of building scaffolding that turns raw LLMs into capable, long-running agents. Key patterns include multi-agent architectures (planner/generator/evaluator), progressive disclosure for context management, and the R.P.I. (Research/Plan/Implement) framework.

## Core Patterns

### GAN-Inspired Multi-Agent Harness
[[anthropic-harness-design-long-running-apps]] describes Anthropic's three-agent system:
- **Planner** — high-level task decomposition
- **Generator** — implements code, manages context resets
- **Evaluator** — independent review, avoids self-evaluation bias

### Progressive Disclosure & R.P.I. Framework
[[thealexker-harness-optimization-guide-2026-04]] outlines:
- Lean config files (avoid instruction budget bloat)
- R.P.I. prompt framework: Research → Plan → Implement
- Subagent patterns for clean context management
- LLMs enter "dumb zone" after a few hundred instructions

### Context Reset Patterns
Long-running sessions require periodic context resets to maintain coherence. Anthropic's harness uses checkpoint-and-restart to push beyond context window limits.

## Related
- [[agent-harness]] — general concept of agent scaffolding
- [[claude-code]] — primary harness implementation
- [[context-engineering]] — context window strategies
- [[multi-agent-systems]] — coordination patterns
