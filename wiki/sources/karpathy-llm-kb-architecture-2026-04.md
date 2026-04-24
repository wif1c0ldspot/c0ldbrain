---
title: Full Architecture of LLM Knowledge Base System
type: source
source_url: https://x.com//status/2039811786602607052
author: '@karpathy'
created: '2026-04-02'
confidence: high
status: current
tags:
- source
- knowledge-management
- architecture
- llm-wiki
summary: Complete architecture breakdown covering every stage from ingest to retrieval
priority: reference
updated: '2026-04-02'
compiled: true
---

## Summary

Detailed architecture of the LLM Knowledge Base system, covering every stage from raw content ingest to context retrieval for agent consumption.

## Architecture Layers

### 1. Ingest Layer (raw/)
- Raw content capture
- Minimal processing
- Preserves original format
- Timestamps preserved

### 2. Source Layer (sources/)
- Verbatim external content
- Single source per URL
- Full context preserved
- Source metadata attached

### 3. Concept Layer (concepts/)
- Synthesized knowledge
- Cross-referenced
- Pattern-extracted
- Timeless (not time-bound)

### 4. Link Layer
- Wikilinks between concepts
- Bidirectional where possible
- Graph structure emerges
- Hub-and-spoke pattern

## Data Flow

```
External Content → Raw Ingest → Source Extraction → Synthesis → Concept
      ↑                                                      ↓
      ←←←←←←←← Agent Reads & Writes ←←←←←←←←←←←←←←←←←←←←←←←
```

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Files over DB | LLM-native, versionable, human-readable |
| Verbatim over extract | Preserves nuance, enables reprocessing |
| Concepts over facts | Patterns transfer, facts decay |
| Links over tags | Richer relationships, discovery |

## Implementation Notes

- Obsidian as frontend viewer
- LLMs read/write markdown directly
- Minimal metadata overhead
- Focus on content quality

## Related Concepts

- [[llm-optimized-wiki]]
- [[context-substrate]]
- [[knowledge-lifecycle-decision-framework]]
- [[resolver-pattern]]
