---
title: "OpenChronicle"
type: concept
tags: [ai-agents, memory-systems, mcp-protocol, local-models, open-source, context-engineering]
created: '2026-04-23'
updated: '2026-04-23'
confidence: high
status: current
priority: important
summary: "Open-source, local-first memory system for AI agents. Captures macOS AX Tree context, converts to Markdown memory, exposes via MCP. Model-agnostic alternative to OpenAI Chronicle."
sources:
- openchronicle-einsia-2026-04
---

# OpenChronicle

## Overview

OpenChronicle is an **open-source, local-first memory system** for tool-capable AI agents. It captures structured context from macOS accessibility tree (AX Tree) events, compresses it into session-aware Markdown memory, and exposes it via an MCP endpoint for any compatible agent.

Created as an open alternative to OpenAI Chronicle, it prioritizes inspectability, model-agnosticism, and hackability over proprietary integration.

## Architecture

### Capture Pipeline

```
mac-ax-watcher events
    → S0 dispatcher (dedup · debounce · min-gap)
    → S1 parser (focused_element · visible_text · url)
    → capture-buffer (*.json)
    → Timeline normalizer (1-min verbatim blocks)
    → timeline_blocks
    → Session manager (idle 5m · app-switch 3m · max 2h)
    → S2 reducer
    → event-YYYY-MM-DD.md
    → Classifier
    → user-/project-/tool-/topic-/person-/org-*.md
    → SQLite FTS5 + Markdown
```

### Key Design Decisions

**AX Tree-first capture:** Structured text from macOS accessibility events is cheaper and more intent-rich than screenshot/OCR pipelines. Screenshots are a secondary signal for visual enrichment.

**Session-aware writing:** Instead of noisy per-snapshot logs, events are compressed into sessions with intelligent cutting rules (idle 5m, app-switch 3m, max 2h).

**Supersede-not-delete:** Memory history is preserved — updated entries supersede old ones rather than overwriting.

**Structured file taxonomy:**
- `user-*.md` — People and relationships
- `project-*.md` — Projects and workstreams
- `tool-*.md` — Tools and integrations
- `topic-*.md` — Topics and knowledge areas
- `person-*.md` — Individual profiles
- `org-*.md` — Organizations
- `event-YYYY-MM-DD.md` — Daily event logs

## Comparison with OpenAI Chronicle

| Dimension | OpenAI Chronicle | OpenChronicle |
|-----------|-----------------|---------------|
| Source | Closed | MIT open-source |
| Model choice | OpenAI-centric | Any LiteLLM-compatible |
| Agent compatibility | Product-specific | Any tool-capable agent |
| Primary capture | Screenshot/OCR-heavy | AX Tree first, screenshot-assisted |
| Storage | Local generated memories | Markdown + SQLite |
| Extensibility | Limited | Hackable parsers, memory logic |

## MCP Integration

OpenChronicle exposes an MCP endpoint at `http://127.0.0.1:8742/mcp`, making it immediately usable by:

- Claude Code / Claude Desktop
- Codex CLI
- opencode
- Any custom MCP client

This positions it as a **Camp 1 memory backend** (structured storage with retrieval) rather than a Camp 2 context substrate.

## Local-First Philosophy

- Memory stays on your machine
- No cloud dependency for core functionality
- SQLite FTS5 for fast local search
- Markdown on disk for human inspectability
- Supports both local (Ollama, LM Studio) and cloud (OpenAI, Anthropic) models

## Status & Limitations

- **v0.1.0 early alpha**
- **macOS 13+ only** — Uses macOS-specific AX APIs
- Requires Python 3.11+ and Xcode Command Line Tools
- Accessibility permission required
- 276 stars, actively developed (created 2026-04-21)

## Contributing Areas

1. **Better context parsers** — App-specific parsing for browsers, terminals, editors, Slack, Notion, Cursor, Linear, Figma
2. **Better memory management** — Session reduction, durable-fact extraction, compaction, merge logic, retrieval quality
3. **More agent integrations** — Additional MCP clients, IDE agents, coding assistants, desktop agents

## Related Concepts

- [[memory-systems]] — Broader memory systems landscape (Camp 1 vs Camp 2)
- [[context-substrate]] — Context-as-substrate paradigm (Camp 2 alternative)
- [[mcp-protocol]] — Model Context Protocol for agent tool integration
- [[cognee]] — Graph-based memory with vector hybrid
- [[honcho]] — Persistent memory and user-modeling layer
- [[mempalace]] — Hierarchical memory palace approach
- [[cli-vs-mcp-debate]] — CLI vs MCP tradeoffs for agent tool access

- [[openchronicle-einsia-2026-04]]
- [[million-token-illusion-oracle-converged-db-datachaz-2026-04]]