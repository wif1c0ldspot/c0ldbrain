---
title: 'OpenChronicle: Open-source, local-first memory for any tool-capable LLM agent'
author: Einsia
date: 2026-04-23
source: https://github.com/Einsia/OpenChronicle
type: source
tags:
- ai-agents
- memory-systems
- mcp-protocol
- local-models
- open-source
confidence: high
status: current
stars: 276
forks: 4
language: Python
license: MIT
summary: Open-source alternative to OpenAI Chronicle. macOS AX Tree-first context
  capture → Markdown + SQLite memory. MCP endpoint for any tool-capable agent. Model-agnostic,
  local-first, MIT-licensed.
priority: important
updated: '2026-04-24'
created: '2026-04-24'
compiled: true
---

## Summary

OpenChronicle is an open-source, local-first memory system for AI agents. It captures structured context from macOS accessibility tree events, converts it into persistent Markdown memory, and exposes it via an MCP endpoint. It is model-agnostic (Ollama, LM Studio, OpenAI, Anthropic, LiteLLM) and designed as a general memory layer for any tool-capable agent — not tied to one protocol or provider.

## Key Points

- **276 stars, 4 forks** — Created 2026-04-21, actively updated (v0.1.0 early alpha)
- **Local-first** — Memory stays on your machine (Markdown + SQLite)
- **Model-agnostic** — Works with any LiteLLM-compatible provider
- **AX Tree-first capture** — Structured text from macOS accessibility events, not screenshot/OCR
- **Session-aware** — Idle 5m / app-switch 3m / max 2h session cutting rules
- **MCP endpoint** — `http://127.0.0.1:8742/mcp` for Claude Code, Codex, opencode, etc.
- **Structured memory files** — user-, project-, tool-, topic-, person-, org-, daily event-*.md
- **Supersede-not-delete** — History preserved, updated entries supersede old ones
- **macOS 13+ only** — Requires Python 3.11+ and Xcode Command Line Tools

## OpenChronicle vs OpenAI Chronicle

| Dimension | OpenAI Chronicle | OpenChronicle |
|-----------|-----------------|---------------|
| Source | Closed | MIT open-source |
| Model choice | OpenAI-centric | Your choice |
| Agent compatibility | Product-specific | Any tool-capable agent |
| Primary capture | Screenshot/OCR-heavy | AX Tree first, screenshot-assisted |
| Storage | Local generated memories | Markdown + SQLite on your machine |
| Extensibility | Limited | Hackable parsers, memory logic, integrations |

## Pipeline Architecture

1. **mac-ax-watcher** captures macOS accessibility events
2. **S0 dispatcher** deduplicates, debounces, enforces min-gap
3. **S1 parser** extracts focused_element, visible_text, URL
4. **capture-buffer** (.json) holds raw captures
5. **Timeline normalizer** creates 1-minute verbatim blocks
6. **Session manager** cuts sessions (idle 5m, app-switch 3m, max 2h)
7. **S2 reducer** compresses into event-YYYY-MM-DD.md
8. **Classifier** routes to user-/project-/tool-/topic-/person-/org-*.md
9. **SQLite FTS5** indexes everything for fast retrieval

## Integration Paths

- Claude Code / Claude Desktop
- Codex CLI
- opencode
- Custom local agents via MCP

## Documentation

- `docs/architecture.md` — End-to-end pipeline
- `docs/config.md` — Configuration and model setup
- `docs/capture.md` — Event-driven capture and AX details
- `docs/timeline.md` — Normalization and anti-hallucination design
- `docs/session.md` — Session cutting rules
- `docs/writer.md` — Reducer, classifier, retry model
- `docs/mcp.md` — Tool surface and integrations
- `docs/memory-format.md` — File layout and supersede semantics

## Related Concepts

- [[openchronicle]] — Main concept page for OpenChronicle architecture and patterns
- [[memory-systems]] — Broader memory systems landscape
- [[context-substrate]] — Context-as-substrate paradigm
- [[mcp-protocol]] — Model Context Protocol for agent tool integration
- [[cognee]] — Graph-based memory alternative
- [[honcho]] — Persistent memory and user-modeling layer
- [[mempalace]] — Hierarchical memory palace approach
