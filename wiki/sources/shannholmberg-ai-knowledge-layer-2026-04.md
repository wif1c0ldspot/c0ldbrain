---
author: Shann Holmberg (@shannholmberg)
confidence: high
created: '2026-04-16'
engagement: 219K views, 1.5K bookmarks, 543 likes
priority: reference
published: 2026-04-14
source_url: https://x.com/shannholmberg/status/2044111115878326444
status: current
summary: Two-layer AI knowledge system (Knowledge Base Layer + Brand Foundation) that
  makes agents smarter. 20-minute setup, open source framework (LLM Wikid), compounding
  knowledge base approach vs RAG.
tags:
- knowledge-management
- ai-agents
- llm-wiki
- personal-knowledge-base
- content-creation
- karpathy
title: AI Knowledge Layer (and why your agents are useless without it)
type: source
updated: 2026-04-17
compiled: true
---


# AI Knowledge Layer (and why your agents are useless without it)

**Author:** Shann Holmberg (@shannholmberg)  
**Published:** 2026-04-14  
**Engagement:** 219K views, 1.5K bookmarks, 543 likes, 65 reposts, 12 replies

## Key Insights

### The Problem: Agents Don't Know You

Karpathy's observation: agents start every conversation from zero. You re-explain your business, voice, goals, context. Output is generic because input has no memory.

> "Your agents don't know you. Every conversation starts from zero."

### The Solution: Two-Layer Knowledge System

```
+-------------------------------------------------------+
|                    YOUR AGENTS                         |
|  (writer, researcher, strategist, analyst)             |
+---------------------------+---------------------------+
      |  reads from                  |  reads from
      v                              v
+------------------+   +-------------------+
|  KNOWLEDGE BASE  |   | BRAND FOUNDATION  |
|  LAYER (KBL)     |   | (BF)              |
|                  |   |                   |
|  dynamic         |   |  static           |
|  agent-maintained|   |  human-edited     |
|  grows over time |   |  your voice, your |
|  wiki pages,     |   |  rules, your      |
|  sources, index  |   |  positioning      |
+--------+---------+   +-------------------+
      |
compiles from
      |
+--------+---------+
|     raw/ inbox    |
|  tweets, articles |
|  bookmarks, PDFs  |
|  notes, ideas     |
+-------------------+
```

#### Layer 1: Knowledge Base Layer (KBL) - Dynamic
- You dump raw sources into folder: tweets, articles, bookmarks, PDFs, notes, voice memos
- AI agent reads all, classifies by type, builds structured wiki pages with cross-references
- Maintains master index with one-line summaries
- Every question gets filed back as new page
- **Wiki gets richer over time**

#### Layer 2: Brand Foundation (BF) - Static
- **Only you edit** this layer
- Your voice rules, visual style, positioning, audience definition
- Words you never use (banned phrases)
- Agents read before producing, never rewrite it
- **Anchor that keeps everything sounding like you**

### Why Not RAG?

| Approach | How It Works | Performance |
|----------|--------------|-------------|
| **RAG** | Re-derives answers at query time by chunking and searching | Baseline |
| **Knowledge Layer** | Compiles once, cross-references, keeps current | **71.5x fewer tokens** (Graphify data) |

Karpathy found compiled approach outperforms RAG at ~100 articles for Q&A.

### Evolution of Knowledge Retrieval

1. **One-shot RAG** (2020-2023)
2. **Agentic RAG with multi-hop retrieval** (2023-2024)
3. **Context engineering** (2025+) - agent builds its own context from multiple sources

**The knowledge layer is infrastructure for phase 3.**

### Real-World Results

Shann's implementation:
- **230+ structured wiki pages** from personal data
- **15 themed source pages, 14 concept pages, 11 entity pages**
- **100+ cross-links** between them
- **197 bookmarks** processed via X API
- **81 images downloaded and analyzed**
- **49 videos transcribed**

### The 5 Levels of AI Marketing

| Level | Description | Knowledge Layer |
|-------|-------------|-----------------|
| 1 | Custom prompts | None |
| 2 | Manual skills | Thin |
| 3 | Skills + Brand Foundation | BF only |
| **4** | **Agents reading from compiled knowledge** | **KBL + BF** |
| 5 | Autonomous agent teams | Full compounding |

**Most people at Level 1-2. Knowledge layer gets you to 4-5.**

### Directory Structure (LLM Wikid Framework)

```
my-wiki/
  raw/
    clippings/          # Obsidian Web Clipper drops here
    ideas/              # Notes, brainstorms
    bookmarks/          # Saved tweets, threads
    articles/           # Your published content
    papers/             # PDFs, research
    x-archive/          # Twitter export
    assets/images/      # Downloaded media
  wiki/
    index.md            # Master index with TLDRs
    log.md              # Append-only changelog
    concepts/           # Ideas, frameworks
    entities/           # People, companies, tools
    sources/            # One summary per raw source
    outputs/            # Filed answers to queries
    sops/               # Repeatable processes
    syntheses/          # Cross-cutting analysis
  templates/            # Page type starters
  CLAUDE.md             # Schema that controls everything
```

### Key Operations

| Command | Purpose |
|---------|---------|
| `/wiki-ingest` | Process raw/ into wiki pages |
| `/wiki-query` | Ask questions, get cited answers |
| `/wiki-explore` | Browse and validate pages |
| `/wiki-lint` | Catch contradictions, stale content |

### Quality Controls

1. **Bias checks** - Forces counter-arguments and data gaps on every page
2. **Validation gate** - Every AI page starts `explored: false`, only human marks confirmed
3. **Confidence levels** - High/medium/low/uncertain tags on every page

### The Compounding Loop

> "Every question you ask makes the system richer. Every source you add creates new connections. Your curiosity feeds back into the quality of answers you get."

### Business Model Opportunity

Setting up knowledge layers as a service:
- **$1,500-3,000** setup fee
- **$300-500/month** retainer
- **10 clients = $56,800 year one**

### Setup: 20 Minutes

1. **Clone repo** (2 min): `git clone https://github.com/shannhk/llm-wikid.git`
2. **Run agent** (3 min): Agent reads CLAUDE.md, scaffolds structure
3. **Fill raw/** (10 min): X archive, bookmarks, notes, ideas
4. **Run ingest** (5 min): `/wiki-ingest` processes everything

### The Window

Karpathy's post: 99,000+ bookmarks  
Graphify: 27,000+ bookmarks (48 hours)  

> "Most people will bookmark this, think 'that's cool,' and never set it up. The ones who spend 20 minutes today will have a compounding knowledge base by next month."

## Source Reference

- **URL:** https://x.com/shannholmberg/status/2044111115878326444
- **Framework:** https://github.com/shannhk/llm-wikid
- **Type:** X Article / Implementation Guide
- **Related:** Karpathy's LLM Knowledge Bases post

## Related Concepts

- [[karpathy-llm-knowledge-bases]] — Original inspiration
- [[llm-optimized-wiki]] — Your wiki architecture
- [[langflow-claude-code-integration]] — Agent implementation
- [[c0ldbrain-wiki]] — Your existing knowledge base
- [[context-engineering]] — Third phase of knowledge retrieval
- [[personal-knowledge-management]] — PKM systems
- [[ai-content-creation]] — Content workflows
- [[brand-foundation]] — Static layer concept
- [[knowledge-base-layer]] — Dynamic layer concept
