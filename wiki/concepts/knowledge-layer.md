---
confidence: high
created: 2026-04-17
priority: reference
related_concepts:
- - - knowledge-base-layer
- - - brand-foundation
- - - context-engineering
- - - llm-optimized-wiki
- - - rag-vs-compiled-knowledge
sources:
- - - shannholmberg-ai-knowledge-layer-2026-04
- - - karpathy-llm-knowledge-bases-2026-04
status: current
summary: AI Knowledge Layer
tags:
- ai-agents
- knowledge-management
- llm-architecture
- context-engineering
- personal-knowledge-base
title: AI Knowledge Layer
type: concept
updated: 2026-04-17
---


# AI Knowledge Layer

Infrastructure that sits between you and your agents—what they read before they do anything. Without it, they guess. With it, they know.

## Core Problem

Agents start every conversation from zero. You re-explain your business, voice, goals, context. Output is generic because input has no memory.

> "Your agents don't know you. Every conversation starts from zero."
> — Shann Holmberg

## Two-Layer Architecture

The AI Knowledge Layer consists of two complementary systems:

### Layer 1: Knowledge Base Layer (KBL)

**Dynamic, agent-maintained, grows over time**

- Raw sources dumped into `raw/` folder: tweets, articles, bookmarks, PDFs, notes, voice memos
- AI agent reads all, classifies by type
- Builds structured wiki pages with cross-references
- Maintains master index with one-line summaries for fast scanning
- **Every question gets filed back as new page**
- Wiki gets richer over time through compounding

```
raw/ → agent processes → wiki/ (structured, cross-linked)
```

### Layer 2: Brand Foundation (BF)

**Static, human-edited, anchors voice**

- **Only you edit** this layer
- Voice rules (tone, style, phrases to avoid)
- Visual style guide
- Positioning and audience definition
- Banned words/phrases that flag as AI-generated
- Agents read before producing but **never rewrite it**
- Keeps everything sounding like you

## KBL vs RAG Performance

| Metric | RAG | Knowledge Layer |
|--------|-----|-----------------|
| Approach | Re-derive at query time | Compile once, keep current |
| Token Efficiency | Baseline | **71.5x fewer tokens** |
| Cross-References | Limited | Automatic |
| Query Speed | Slower | Faster (pre-compiled) |
| Break-Even Point | Always baseline | ~100 articles |

Source: Graphify analysis, Karpathy observations

## Evolution of Knowledge Systems

```
2020-2023: One-shot RAG
    ↓
2023-2024: Agentic RAG with multi-hop retrieval
    ↓
2025+: Context engineering (agent builds its own context)
```

**The knowledge layer is infrastructure for the third phase.**

## Directory Structure

```
my-wiki/
  raw/                    # Messy inbox
    clippings/            # Obsidian Web Clipper
    ideas/                # Notes, brainstorms
    bookmarks/            # Saved content
    articles/             # Your content
    papers/               # PDFs, research
    x-archive/            # Social exports
    assets/images/        # Downloaded media
  
  wiki/                   # Compiled knowledge
    index.md              # Master index with TLDRs
    log.md                # Changelog
    concepts/             # Ideas, frameworks
    entities/             # People, companies
    sources/              # Summarized sources
    outputs/              # Query answers
    sops/                 # Processes
    syntheses/            # Cross-cutting analysis
  
  templates/              # Page starters
  CLAUDE.md               # Schema controlling everything
```

## Core Operations

| Command | Function | Frequency |
|---------|----------|-----------|
| `/wiki-ingest` | Process raw/ → wiki/ | Daily/scheduled |
| `/wiki-query` | Ask questions, get cited answers | On demand |
| `/wiki-explore` | Browse and validate pages | Weekly |
| `/wiki-lint` | Catch contradictions, stale content | Weekly |

## Quality Controls

1. **Bias Checks** - Forces counter-arguments on every page
2. **Validation Gate** - AI pages start `explored: false`, human marks confirmed
3. **Confidence Levels** - High/medium/low/uncertain tags
4. **Cross-References** - Automatic linking between related concepts

## The Compounding Effect

> "Every question you ask makes the system richer. Every source you add creates new connections. Your curiosity feeds back into the quality of answers you get."

**The loop:**
1. Add sources to `raw/`
2. Run `/wiki-ingest` → structured pages created
3. Query with `/wiki-query` → cited answers
4. Answer filed back as new page
5. Next query richer than last

## The 5 Levels of AI

| Level | Knowledge Layer State |
|-------|----------------------|
| 1. Custom prompts | None |
| 2. Manual skills | Thin |
| 3. Skills + BF | Static layer only |
| **4. Agents + compiled knowledge** | **KBL + BF working together** |
| 5. Autonomous teams | Full compounding |

## Implementation Options

- **LLM Wikid** (Shann Holmberg): github.com/shannhk/llm-wikid
- **C0ldbrain** (Your system): Custom implementation with Hermes agent
- **Graphify**: Commercial implementation with 71.5x token efficiency

## Business Applications

### Content Creators
- Personal brand voice encoded
- Content performance tracking
- Distribution intelligence compounding

### Companies
- Shared brain across team
- Role-tuned agents reading same knowledge
- No information falls through cracks

### Services Opportunity
- Setup: $1,500-3,000
- Retainer: $300-500/month
- 10 clients → $56,800 year one

## References
## References
- [[shannholmberg-ai-knowledge-layer-2026-04]] — Original article
- [[karpathy-personal-kb-agents-2026-04]] — Inspiration source
- [[llm-optimized-wiki]] — Your implementation
- [[knowledge-management-synthesis]] — Unified paradigm comparison
- [[gbrain-agent-brain]] — Production implementation (Garry Tan)

## Related
- [[active-inference-free-energy-principle]]
- [[ai-content-creation]]
- [[arxiv-active-inference-papers-2026-03]]
- [[brain-inspired-agent-architecture]]
- [[brand-foundation]]
- [[knowledge-base-layer]]
- [[weekly-synthesis-async-subagent-2026-04-17]]
