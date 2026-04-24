---
title: Token Optimization & Efficiency
type: concept
tags:
  - token-optimization
  - prompt-engineering
  - cost
  - ai-agents
sources:
  - claude-caveman-prompting-strategy-2026-04
  - noisyb0y1-claude-code-thread-2026-04
  - mac-mini-35b-local-ai-agent-2026-04
  - axi-agent-experience-interface-2026-04
  - contextplus-mcp-2026-04
created: 2026-04-06
updated: 2026-04-15
confidence: high
status: current
agents:
  - hermes
  - claude
  - codex
priority: critical
summary: Strategies for reducing token usage, improving AI agent efficiency, and optimizing cost. Caveman-style prompting achieves 75% token reduction.
---


# Token Optimization & Efficiency

## Summary

Strategies for reducing token usage, improving AI agent efficiency, and optimizing cost without sacrificing quality.

## Key Techniques

### Caveman-Style Token Saving

One-line install for Claude Code skill:
- Cuts ~75% of tokens while keeping full technical accuracy
- Teaches Claude to talk like a caveman (short, direct, no fluff)
- Benchmark verified with real API token counts

### Model Tier Optimization

Using different models for different tasks:

| Task | Recommended Model | Why |
|------|------------------|-----|
| Planning | Claude Opus | Best reasoning for complex decisions |
| Execution | Claude Sonnet | Fast, good enough for implementation |
| Simple Q&A | Smaller models | Cost-effective for straightforward tasks |

Claude Code supports `/model opusplan` — uses Opus for planning, Sonnet for execution.

### KV Cache + TurboQuant Optimization

- Pre-fill KV cache with documents for instant querying
- Quantize models to reduce memory footprint by 50%+
- 3.15bit precision with no quality loss (verified benchmark)

### Prompt Engineering (Anthropic's Official Course)

Free interactive Jupyter notebooks:
- 12,200 stars on GitHub (+2,459 recently)
- Cover basic to advanced prompting
- Chain-of-thought and tool use
- Real agent patterns from Claude team

## Cost Impact

For agents running 8+ hours/day:
- Caveman style: 75% token reduction = 75% cost reduction
- Model tier optimization: ~40-60% savings from right-sizing
- Combined: up to 90% cost reduction vs. default settings

### Code Review Graph (Tree-sitter Indexing)

Local knowledge graph for Claude Code (tirth8205/code-review-graph, 5.6k stars):
- Builds persistent structural map of codebase using Tree-sitter
- 8.2x average token reduction, 49x on daily tasks
- Incremental updates under 2 seconds
- Multi-editor support: Claude Code, Cursor, Windsurf, Zed

### Claude Code v2.1.100 Token Inflation (April 2026)

Report from proxy interception testing:
- v2.1.98: 169,514 bytes → 49,726 tokens charged
- v2.1.100: 168,536 bytes → 69,922 tokens charged
- Same request, 20K+ more tokens charged in newer version
- Server-side inflation, invisible via /context
- Impact: CLAUDE.md dilution, faster limit burn (~40%)
- Fix: `npx claude-code@2.1.98`
- Note: Unverified claim from viral thread — confirm independently

## Local Context Compression (from mac-mini-35b-local-ai-agent-2026-04)

A production implementation of context compression using local models demonstrates dramatic token savings:

- **500-word messages → 30 words** before cloud API sees them (via local Gemma 4 E4B)
- **Full day of automation signals → dense summary** (15x token savings for Opus planning)
- **Memory consolidation:** cluster and merge daily agent notes locally
- **Signal compression:** The heavy tier (Qwen 35B via mmap) handles the most complex compression tasks — full-day signal rollups that feed into cloud model planning sessions

**Key insight:** Context compression is the highest-ROI use case for local models. A $599 Mac Mini handles all preprocessing, so the expensive cloud model only sees compressed, high-signal input. This alone reduces cloud API sessions by 30-40%.

**Thinking mode optimization:** Disabling thinking mode (`think: false`) on local classification/triage tasks yields 30x speedup with no accuracy loss — the model was wasting 500 tokens of reasoning to produce a 1-word answer.

### AXI TOON Format (from axi-agent-experience-interface-2026-04)

Agent eXperience Interface defines TOON (Terse Output, Optional Noise) — a structured output format for CLI tools consumed by AI agents:
- 40% token reduction verified across 915 benchmark runs
- Strips human-friendly formatting in favor of machine-parseable structure
- 10 design principles for agent-ergonomic tool interfaces
- See [[agent-cli-tools]] for full concept page

### Context+ MCP Code Intelligence (from contextplus-mcp-2026-04)

Tree-sitter-based MCP server provides structured code context instead of raw text:
- Reduces token usage by returning AST-level information
- RAG memory graph persists across sessions, avoiding re-reading codebases
- Obsidian-style bidirectional linking between code entities
- See [[mcp-protocol]] for MCP integration details

## Related Concepts

[[skill-registry]], [[memory-systems]], [[code-review-graph]], [[claude-md-best-practices]], [[local-llm-infrastructure]], [[agent-cli-tools]], [[vectorless-rag]]
