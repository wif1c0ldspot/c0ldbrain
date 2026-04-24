# C0ldbrain Wiki — Architecture Guide

> **TL;DR:** A staged-intake knowledge base with tiered memory retrieval. You drop links, the LLM fetches, compiles, and synthesizes into cross-linked concept pages. 40+ concepts across AI agents, security, and trading.

## Two-System Architecture

This wiki is a **knowledge base** (external reference), not agent memory. The agent manages its own memory separately.

### Hermes Agent Memory (Agent-Managed)

```
┌──────────────────────────────────────────────────────────────────────────┐
│  AGENT MEMORY (Hermes-Managed)                                          │
│  ──────────────────────────────────────────────────────────────────────────┘
│                                                                          │
│  Session: In-Memory       — Current conversation, tool results            │
│    • Auto-compression at token limit, auto-injected into context         │
│                                                                          │
│  Memory: SQLite           — Session history (~/.hermes/sessions/)         │
│    • Learned user preferences, cross-session task state                   │
│    • Access via: session_search(query) for "what did we discuss?"        │
└──────────────────────────────────────────────────────────────────────────┘
```

### C0ldbrain Knowledge Base (Human-Managed)

```
┌──────────────────────────────────────────────────────────────────────────┐
│  KNOWLEDGE BASE (C0ldbrain — External Reference)                        │
│  ──────────────────────────────────────────────────────────────────────────┘
│                                                                          │
│  Purpose: Human reference material, research synthesis, accumulated       │
│  wisdom. Agent QUERIES this when you ask "what do we know about X?"      │
│                                                                          │
│  Index: MemPalace          — Fast semantic search (auto-indexed from disk) │
│    • NOT agent memory, just a search index for the wiki                   │
│    • Use for: Discovery — "find concepts about X"                         │
│                                                                          │
│  Wiki: Disk (Source of Truth)                                           │
│    • 40+ concept pages, 53+ source pages in flat structure                │
│    • Human-readable markdown, version-controlled                          │
│    • Agent verifies Index findings here, cites with [[wikilinks]]        │
│                                                                          │
│  Synthesis: (On Demand)                                                 │
│    • Generated analysis, comparisons — expensive, use sparingly          │
│    • Triggered by: "compare X and Y", explicit synthesis request         │
└──────────────────────────────────────────────────────────────────────────┘
```

**Key Distinction:**
- **Session** (Hermes) = ephemeral, in-memory, current conversation
- **Memory** (Hermes) = persistent, SQLite, learned preferences
- **Index** (MemPalace) = search engine for the wiki, NOT agent memory
- **Wiki** (C0ldbrain) = external knowledge base, human-curated

## Current Structure

```
/Volumes/obsidian/C0ldbrain/
├── ABOUT.md              ← This file
├── SCHEMA.md             ← Conventions, frontmatter, tag taxonomy
├── MANIFEST.json         ← Source tracking and compilation status
├── watch_lists.json      ← Autonomous research topic definitions
│
├── _scripts/             ← LLM workflow definitions
│   ├── README.md         ← Agent master guide (read first)
│   ├── wiki_config.py    ← Path configuration
│   ├── compile.py        ← 5-phase Python compiler
│   ├── ingest.md         ← Stage source in raw/
│   ├── fetch_urls.md     ← Extract URLs to markdown
│   ├── compile.md        ← Master workflow guide
│   ├── synthesize.md     ← Merge scattered notes into Textbook
│   ├── ask.md            ← Query wiki with citations
│   ├── lint.md           ← Health audit
│   ├── graph_visualizer.md   ← Mermaid graph generator
│   ├── maint_auto.md         ← Automated maintenance
│   ├── merge.md              ← Deduplicate concept pages
│   ├── reflect.md            ← Cross-source pattern discovery
│   ├── output.md             ← Generate artifacts
│   ├── daily_digest.md       ← Daily briefing
│   ├── trend_watchers.md     ← Autonomous topic research
│   ├── feedback_loop.md      ← Self-correction from user corrections
│   ├── telegram_ingest.md    ← Handle Telegram messages
│   ├── wiki-hermes-integration.md
│   └── ingesters/            ← Per-source-type ingest rules
│       ├── article.md, github.md, social.md, podcast.md
│       ├── paper.md, newsletter.md, image.md, data.md
│       └── x-bookmarks-export.md
│
├── wiki/
│   ├── index.md          ← Master content catalog (by domain, priority, recency)
│   ├── log.md            ← Append-only audit trail
│   ├── concepts/         ← 30 synthesized knowledge articles (flat)
│   └── sources/          ← 20 source summary pages (1 per raw source)
│
└── raw/                  ← Staging area (empty when all compiled)
    └── notes/            ← Human-written notes (never deleted)
```

## How to Use It

| Command | What happens |
|---------|-------------|
| **Ingest [URL/file]** | Staged in raw/ with frontmatter, MANIFEST entry |
| **Compile the wiki** | 5-phase: Fetch → Compile → Maintain → Synthesize → Finalize |
| **Synthesize [topic]** | Merge scattered notes into authoritative Textbook article |
| **Lint the wiki** | Find contradictions, dead links, orphans, stale claims |
| **Ask about [topic]** | Query wiki with citations, never from memory |
| **Maintain the wiki** | Link rot, consolidation, pruning |

## Content Summary

- **40+ concept pages** across domains: Knowledge & Agents, Security, Hermes & Skills, Quant Trading
- **53+ source pages** — one per ingested raw source
- **0 uncompiled sources** — all raw files have been processed
- **536 MemPalace drawers** indexed from wiki (auto-sync via file hooks)
- **~350KB total** — structured for efficient retrieval

## Query Types & Retrieval Strategy

| Query Type | Example | Strategy | System Used |
|------------|---------|----------|-------------|
| **Session recall** | "What did we discuss?" | `session_search(query)` | Hermes Memory |
| **Discovery** | "Find concepts about X" | MemPalace search → verify in wiki | Index → Wiki |
| **Factual lookup** | "What is the RESOLVER?" | MemPalace find → wiki verify | Index → Wiki |
| **Deep dive** | "Tell me about emergence" | MemPalace → wiki full read | Index → Wiki |
| **Synthesis** | "Compare X and Y" | Gather → generate | Index → Wiki → Synthesis |

**System Legend:**
- **Session**: Hermes in-memory (current conversation)
- **Memory**: Hermes SQLite (`session_search` for history)
- **Index**: MemPalace search (wiki index)
- **Wiki**: C0ldbrain disk (source of truth)

**Always cite sources:** Use `[[wiki-slug]]` format for wiki content, `[Session: YYYY-MM-DD]` for agent session context.

## Page Standards

Every wiki page has:
- Frontmatter: title, type, tags, sources, updated, confidence, status, summary
- Structure: Summary → Key Facts → Tables → Related Concepts
- Cross-links via `[[wikilinks]]` — bidirectional enforced
- Confidence scoring: high (verified) / medium (likely) / low (speculative)

## Raw Folder (Staging)

`raw/` is a staging area — files are deleted after successful compilation.
- `raw/notes/` — only folder where humans write directly
- `raw/telegram/` — incoming links from Telegram (created on use)
- All other subdirectories are created as needed by ingest
