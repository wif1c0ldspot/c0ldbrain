---
confidence: high
created: '2026-04-06'
date: 2026-04-18
priority: critical
status: current
summary: Synthesis of Karpathy's LLM knowledge base pattern - file-native wiki that compounds context over time, inspired by his viral Obsidian setup
tags:
- knowledge-management
- llm-wiki
- context-substrate
- patterns
- karpathy
title: LLM Knowledge Base Pattern
type: concept
updated: '2026-04-18'
---

# LLM Knowledge Base Pattern

## Core Philosophy

The LLM Knowledge Base Pattern is a Camp 2 (Context Substrate) approach to persistent knowledge management. Unlike traditional PKM or vector-based retrieval, it emphasizes:

| Principle | Traditional PKM | LLM KB Pattern |
|-----------|-----------------|----------------|
| **Storage** | Database/notes | Plain markdown files |
| **Organization** | Manual by human | Agent-driven |
| **Retrieval** | Search & filters | Context injection |
| **Growth** | Human maintenance | Self-improving |
| **Source** | Extracted facts | Verbatim capture |

## Architecture Layers

### 1. Raw Layer (`raw/`)
Unprocessed source material:
- Bookmarks
- Web captures
- Transcripts
- Logs

### 2. Source Layer (`wiki/sources/`)
Verbatim external content:
- Individual URL captures
- Full context preserved
- Author attribution
- Timestamps

### 3. Concept Layer (`wiki/concepts/`)
Synthesized knowledge:
- Patterns extracted
- Cross-referenced
- Timeless principles
- Decision rationale

### 4. Link Layer (wikilinks)
Relationships between concepts:
- Bidirectional links
- Graph structure emerges
- Hub-and-spoke topology
- Discovery enabled

## Data Flow

```
External Content
       ↓
Raw Capture (raw/)
       ↓
Source Extraction (wiki/sources/) ← Individual verbatim captures
       ↓
Synthesis (wiki/concepts/) ← Pattern extraction, timeless knowledge
       ↓
Linking (wikilinks) ← Graph structure, discovery
       ↓
Agent Context ← LLM reads, works within, writes back
       ↓
Compounding Knowledge ← Each session enriches the wiki
```

## Key Implementations

### Karpathy's LLM Wiki
Primary inspiration - viral Obsidian-based setup:

- **Self-improving** — Agent organizes without manual editing
- **Zero friction** — Just add content, agent structures
- **Compounding** — Context grows session over session
- **Agent-native** — LLMs read/write markdown directly

Sources:
- [[karpathy-llm-knowledge-base-viral-2026-04]] — 7 key insights
- [[karpathy-self-improving-second-brain-2026-04]] — Zero manual editing
- [[karpathy-llm-kb-architecture-2026-04]] — Full architecture
- [[karpathy-personal-kb-agents-2026-04]] — Agent integration
- [[karpathy-llm-kb-pattern-2026-04]] — Core pattern

### OpenClaw Memory System
Production implementation with 358k stars:

- `MEMORY.md` — Long-term storage
- `YYYY-MM-DD.md` — Daily notes
- `DREAMS.md` — Consolidation summaries
- Dream cycle — Background refinement

### C0ldbrain Wiki (This Vault)
Built on these principles:
- [[context-substrate]] — Camp 2 accumulation problem
- [[knowledge-lifecycle-decision-framework]] — When to consolidate

## Design Decisions

### Why Files Over Databases

1. **LLM-native** — Can read/write directly
2. **Versionable** — Git for history
3. **Human-readable** — Inspect/edit manually
4. **Portable** — No lock-in
5. **Simple** — No infrastructure

### Why Verbatim Over Extraction

Extraction loses:
- Nuance
- Context
- Implicit relationships
- Future reprocessing potential

Verbatim preserves:
- Full meaning
- Original framing
- Flexibility to re-synthesize
- Audit trail

### Why Patterns Over Facts

Facts decay:
- "iPhone 14 price is $799" (outdated)
- "Python 3.9 has GIL issues" (resolved)

Patterns persist:
- "Mid-tier models outperform on bounded tasks" (transferable)
- "Cost/quality tradeoff is task-dependent" (principle)

## Implementation Guide

### Getting Started

1. **Choose tooling** — Obsidian, logseq, or plain files
2. **Create structure** — raw/, sources/, concepts/
3. **Capture verbatim** — Don't filter at ingest
4. **Let LLMs organize** — Agent structures content
5. **Link liberally** — Wikilinks create graph
6. **Iterate** — System improves over time

### Best Practices

| Practice | Rationale |
|----------|-----------|
| One source per URL | Verbatim, granular linking |
| Wikilinks over tags | Richer relationships |
| Frontmatter metadata | Structure without clutter |
| Timestamps | Track evolution |
| Confidence ratings | Quality signal |

### What to Capture

- Decisions and rationale
- Patterns discovered
- Preferences expressed
- Problems solved
- Progress made
- Failures analyzed

### What NOT to Capture

- Ephemeral state
- Repeated explanations
- Obvious derivations
- Temporary workarounds
- Context that doesn't compound

## Comparison to Vector Retrieval

| Aspect | Vector RAG | LLM KB Pattern |
|--------|-----------|-----------------|
| **Recall** | High | High |
| **Context** | Retrieved chunks | Compounding |
| **Updates** | Replace vectors | Evolving files |
| **Human inspection** | Difficult | Easy |
| **Agent modification** | Limited | Full |
| **Nuanced understanding** | Variable | Strong |

## Related Concepts

- [[context-substrate]] — Camp 2 memory paradigm
- [[memory-systems]] — Alternative approaches
- [[knowledge-management]] — General PKM
- [[resolver-pattern]] — Reference resolution
- [[agentic-ai]] — Autonomous agent integration
- [[llm-knowledge-bases]] — Implementations list

## Sources

- [[karpathy-llm-knowledge-base-viral-2026-04]]
- [[karpathy-self-improving-second-brain-2026-04]]
- [[karpathy-llm-kb-architecture-2026-04]]
- [[karpathy-personal-kb-agents-2026-04]]
- [[karpathy-llm-kb-pattern-2026-04]]
