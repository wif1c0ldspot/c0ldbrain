# LLM Agent Master Guide

> **READ THIS FIRST.** This defines how you, the LLM agent, interact with the wiki.

## 1. Two-System Architecture

You manage **two separate systems**:

### Hermes Agent Memory (Built-in, Agent-Managed)
```
┌──────────────────────────────────────────────────────────────────────────┐
│  AGENT MEMORY (Hermes-Managed)                                          │
│                                                                          │
│  Session: In-Memory      — Current conversation, tool results             │
│    • Auto-compression at token limit                                     │
│    • Access: Auto-injected into context                                  │
│                                                                          │
│  Memory: SQLite          — Session history (~/.hermes/sessions/)          │
│    • Learned user preferences, cross-session task state                  │
│    • Access: session_search(query) for "what did we discuss?"            │
└──────────────────────────────────────────────────────────────────────────┘
```

### C0ldbrain Knowledge Base (Wiki on Disk, Human-Managed)
```
┌──────────────────────────────────────────────────────────────────────────┐
│  KNOWLEDGE BASE (C0ldbrain Wiki)                                        │
│                                                                          │
│  Index: MemPalace Search — Fast semantic search (NOT agent memory)       │
│    • Auto-indexed from disk, just a search index                          │
│                                                                          │
│  Wiki: Disk (Source of Truth) — 40+ concepts, 53+ sources                 │
│    • Human-readable markdown, version-controlled                          │
│    • ALWAYS verify Index findings here, cite with [[wikilinks]]          │
│                                                                          │
│  Synthesis: (On Demand) — Expensive, use sparingly                       │
└──────────────────────────────────────────────────────────────────────────┘
```

**Key Distinction:**
- **Session** = your built-in in-memory context (ephemeral, task-focused)
- **Memory** = your SQLite store for history (`session_search`)
- **Index** = MemPalace search engine for the wiki (external)
- **Wiki** = C0ldbrain knowledge base (external reference, queried on demand)

### Memory Types
- **Skills:** How to do things (Auto-loaded)
- **Agent Memory:** Your built-in session context and SQLite (ephemeral, task-focused)
- **Wiki (Knowledge Base):** What is known (Read via tiered retrieval when asked)

## 2. Query Classification (MANDATORY)

**Critical:** L1/L2/L3 tiers refer to the **Knowledge Base** (C0ldbrain wiki), NOT your agent memory. You manage your own L1/L2 separately.

Before retrieving, classify the query type:

| Type | Trigger | Action | System |
|------|---------|--------|--------|
| `session_recall` | "What did we discuss?" | `session_search(query)` | Memory |
| `discovery` | "Find concepts about X" | MemPalace search → wiki verify | Index → Wiki |
| `factual_lookup` | "What is X?" | MemPalace find → wiki verify | Index → Wiki |
| `deep_dive` | "Tell me about X..." | MemPalace find → wiki full read | Index → Wiki |
| `synthesis` | "Compare X and Y" | Gather → generate | Index → Wiki → Synthesis |

**Session recall** goes to your built-in Hermes memory (`session_search`), NOT the knowledge base.

**System Legend:**
- **Session**: In-memory context (current conversation)
- **Memory**: SQLite history (`session_search` tool)
- **Index**: MemPalace search (wiki index)
- **Wiki**: C0ldbrain disk (source of truth)

## 3. Capabilities

### Markdown workflows in `_scripts/`:

| File | Trigger | Purpose |
|------|---------|---------|
| `ingest.md` | "ingest [URL/file]" | Stage sources in `raw/` with frontmatter |
| `fetch_urls.md` | (Auto-triggered by /compile) | Extract URLs into readable markdown |
| `compile.md` | "compile the wiki" | 5-phase master flow: Fetch→Compile→Maintain→Synthesize→Finalize |
| `synthesize.md` | "synthesize [topic]" | Merge scattered notes into a Textbook |
| `ask.md` | "ask about [topic]" | Query wiki + cite sources |
| `lint.md` | "lint the wiki" | Find contradictions, dead links, orphans, stale claims |
| `graph_visualizer.md` | "graph the wiki" | Mermaid knowledge graph → outputs/mermaid/wiki-graph.mmd |
| `maint_auto.md` | "maintain the wiki" | Link rot, consolidation, pruning |
| `merge.md` | "merge these" | Deduplicate similar concepts |
| `output.md` | "create [slides/chart]" | Generate artifacts (slides, charts, analyses) |
| `daily_digest.md` | "daily digest" | Generate daily briefing report |
| `trend_watchers.md` | "trend watchers" | Autonomous topic research |
| `feedback_loop.md` | "that's wrong" | Self-correction from user corrections |
| `telegram_ingest.md` | (Auto from Telegram) | Handle incoming Telegram links/notes |
| `reflect.md` | "reflect on wiki" | Cross-source pattern discovery, gaps, contradictions |

### Python health pipeline:

| File | Trigger | Purpose |
|------|---------|---------|
| `build_dashboard_data.py` | "health", "status", weekly cron | Scan wiki, build graph from wikilinks, extract metrics → `outputs/dashboard/wiki-data.json` |
| `generate_health_report.py` | After data pipeline | Generate `outputs/dashboard/health.md` with health score (0-100), broken links, orphans, stale content, pending files, recommendations. Also outputs Telegram summary. |
| `auto_fix.py` | "fix wiki", or after health check | Auto-repair: broken links, noise files, missing summaries, missing tags, orphan backlinks, whitespace, MANIFEST sync, date normalization. Add `--apply --cron` for non-interactive. |

## 4. Workflow Execution Order

### For Session Recall (Your Memory)
```
User asks: "What did we discuss?"
    │
    ▼
Use your built-in Hermes session history (NOT MemPalace)
    │
    ▼
Return: Recent conversation topics, decisions, task state
```

### For Knowledge Queries (Wiki Tiered Retrieval)
```
User asks: "What do we know about X?"
    │
    ▼
Classify query type (discovery | factual_lookup | deep_dive | synthesis)
    │
    ▼
Execute tiered retrieval:
  • Index (MemPalace): Fast search for "find concepts about X"
  • L2 (Wiki Disk): Verify authoritative content, cite [[wikilink]]
  • L3 (Synthesis): Only for explicit comparison/analysis
    │
    ▼
Return: Content with [[wikilink]] citations
```

### For Wiki Compilation

1. **Read MANIFEST.json** → Check for `pending_fetch`.
2. **If URLs exist:** Run `_scripts/fetch_urls.md` (Browser/snapshot → save to `raw/downloads/`).
3. **Run compile:** Read raw → Write `wiki/sources/` → Create concept pages → Backlink audit.
4. **Update Index:** Add to `wiki/index.md` → Log to `wiki/log.md`.
5. **MemPalace sync:** File hooks auto-index new content (no manual action needed).

## 5. Page Structure Standards

Every wiki page MUST have this frontmatter:
```yaml
---
title: Concept Name
type: concept | source | analysis
tags: [controlled-vocab-tag, secondary-tag]
sources: [source-slug-1, source-slug-2]
confidence: high | medium | low
status: current | deprecated
updated: YYYY-MM-DD
summary: "One-line machine-readable summary"
---
```
Required fields: title, type, tags, updated
Recommended: sources, confidence, status, summary, priority
Priority values: critical, important, reference
Tag vocab: ai-agents, llm, memory-systems, token-optimization, mcp-protocol, open-source, knowledge-management, hermes, quantitative-trading, crypto-quant, developer-tools, ml-models, cost, autonomous-optimization, meta-agents, benchmarking, infrastructure, local-models, security

# Title
## Summary
[2-3 sentences]
## Key Facts
- [Fact]
## Tables/Tools
[Comparison tables]
## Related Concepts
- [[link]] — relationship
```

## 6. LLM Decision Rules

- **Confidence:** If `confidence: high`, cite as fact. If `low`, flag as "claim".
- **Contradictions:** If Source A and Source B disagree, flag: `> ⚠️ CONFLICT: ...`.
- **Tables:** Always output data in tables when comparing tools, dates, or metrics.
- **Links:** NEVER add a new page without adding `[[wikilinks]]` to existing pages.
- **Retrieval:** Classify query first. Session recall → Hermes memory. Factual queries → tiered knowledge base retrieval.
- **Citations:** Always cite `[[wiki-slug]]` for wiki content, `[Session: date]` for your session context.
- **Separation:** Your agent memory (L1/L2) is SEPARATE from the C0ldbrain knowledge base.

## 7. Where to Save Files

- `wiki/concepts/` → Synthesized knowledge (one per topic).
- `wiki/sources/` → Summary of one raw file.
- `raw/downloads/` → Extracted content from URLs.
- `outputs/dashboard/` → Health reports (health.md), data (wiki-data.json), inline Mermaid graphs (.md with ```mermaid blocks)
- `outputs/analyses/` → Lint reports, synthesis reports, answers (markdown)
- `outputs/slides/` → Marp presentations
- `outputs/charts/` → ASCII charts, visualizations

**Important for Obsidian users:**
- Mermaid diagrams use inline code blocks in .md files, NOT standalone .mmd files. Obsidian renders them natively.
- Save graph output to `outputs/dashboard/wiki-graph.md` with a ` ```mermaid ` code block.
- Never create standalone .mmd files — they are useless without a wrapper markdown file.
- Diagram output belongs in `outputs/dashboard/`, NOT in `wiki/`. The wiki folder is for knowledge content only.

## 8. Logging

After every operation, append to `wiki/log.md`:
```
## [DATE] <agent> <operation> | <result>
Sources: [list]
```

Supported operations: `ingest`, `fetch`, `compile`, `ask`, `reflect`, `lint`, `merge`, `synthesize`, `output`, `graph`, `maintain`, `digest`, `migrate`, `query` (L1/L2/L3)

## 9. Cron Jobs & Automation

| Cron Job | Schedule | Action | Output |
|----------|----------|--------|--------|
| **Daily Digest** | 8pm daily | Your session diary + relevant wiki queries | Telegram briefing |
| **Health Check** | Weekly | Scan wiki index, validate against disk | health.md report |
| **Trend Watch** | Every 6h | Search for topic updates, compile if new | Update concept pages |

**Important:** Daily digest uses YOUR session diary (Hermes memory), not MemPalace search.

