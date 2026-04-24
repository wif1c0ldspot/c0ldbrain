---
title: MemPalace GitHub Repository
type: source
tags:
- memory-systems
- mcp-protocol
- source
- github
source_url: https://github.com/milla-jovovich/mempalace
sources:
- raw/github/mempalace.md
created: '2026-04-07'
updated: '2026-04-07'
confidence: high
status: current
agents:
- hermes
priority: important
summary: MemPalace GitHub repo — hierarchical AI memory system with MCP integration,
  96.6% LongMemEval score, lossless storage.
---

# MemPalace GitHub Repository

## Summary

MemPalace (github.com/milla-jovovich/mempalace) is an AI memory system that organizes conversations and data into a hierarchical "palace" structure. Features MCP server integration and runs entirely local.

## Source

- https://github.com/milla-jovovich/mempalace

## Key Claims & Metrics

- 96.6% LongMemEval R@5 score (zero API calls)
- 100% with Haiku rerank
- 34% retrieval boost from structural organization
- 30x AAAK token compression dialect
- Runs entirely local, no cloud

## Architecture

### Hierarchical Structure
- Mine conversations, code, notes into palace (wings, rooms, closets, drawers)
- Stores everything lossless — no LLM summarization of originals
- Semantic search across the structure

### MCP Integration
- MCP server with 19 tools for Claude/Cursor integration
- Auto-save hooks for Claude Code

### Knowledge Graph
- SQLite-backed knowledge graph with temporal validity
- Specialist agents with persistent diaries

### AAAK Dialect
- Lossless compressed dialect
- 30x compression ratio
- Works with any LLM

## Install & Usage
- `pip install mempalace`
- `mempalace init`, `mempalace mine`, `mempalace search`

## Notes
- Benchmarks published, tests included
- Compare with Zep/Graphiti: MemPalace is SQLite/free vs Neo4j/$25mo+

## Related Concepts

- [[memory-systems]] — Core AI memory pattern
- [[mcp-protocol]] — MCP server integration
- [[ai-coding-agents]] — Claude Code integration
