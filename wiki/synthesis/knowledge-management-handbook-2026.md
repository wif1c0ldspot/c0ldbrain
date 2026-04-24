---
confidence: high
created: '2026-04-14'
priority: important
sources:
- llm-knowledge-bases
- karpathy-llm-wiki-agent
- memory-systems
- llm-wiki-v2-rohitg00
- code-review-graph
status: current
summary: 'Synthesized handbook of LLM-maintained knowledge management: from flat wikis
  through structured knowledge bases to autonomous self-evolving systems with memory
  lifecycle, crystallization, and hybrid search.'
tags:
- knowledge-management
- memory-systems
- knowledge-graph
- crystallization
title: Knowledge Management Handbook — LLM-Maintained Knowledge Systems 2026
type: synthesis
updated: '2026-04-14'
---


# Knowledge Management Handbook — LLM-Maintained Knowledge Systems 2026

## Definition

**LLM-maintained knowledge management** is the practice of using large language models to autonomously build, compile, organize, and evolve personal or organizational knowledge bases. The LLM acts as a tireless research librarian — reading raw source material, writing interlinked encyclopedia-style articles, maintaining backlinks, running integrity checks, and filing outputs back into the knowledge base. Unlike traditional RAG (Retrieval-Augmented Generation), which queries a static vector index, LLM-maintained wikis produce human-readable, self-improving articles that compound in value over time.

The core insight: **the LLM organizes, not you**. Humans contribute sources and ask questions; the LLM handles all curation, linking, categorization, and maintenance.

## History & Evolution

| Period | Milestone                      | Key Innovation                                                                         |
| ------ | ------------------------------ | -------------------------------------------------------------------------------------- |
| 2023   | First wiki-as-code experiments | Manual markdown wikis with LLM-assisted authoring                                      |
| 2024   | Karpathy's raw → wiki pipeline | Three-layer architecture (raw/, wiki/, scripts/); LLM as compiler                      |
| 2025   | Autonomous wiki agents         | GitHub Actions running 4h cycles (yologdev/karpathy-llm-wiki); no human in loop        |
| 2025   | Memory lifecycle patterns      | Confidence scoring, supersession, forgetting curves from cognitive science             |
| 2026   | LLM Wiki v2 (rohitg00)         | Knowledge graph, hybrid search, consolidation tiers, crystallization, multi-agent sync |
| 2026   | Infrastructure convergence     | Memvid (vector DB → MP4), MemPalace (hierarchical palace), Flash-MoE (397B on laptop)  |

The trajectory moves through three clear stages:

1. **Flat wikis** — interlinked markdown pages with manual upkeep
2. **Structured knowledge bases** — LLM-compiled articles with typed relationships and quality scoring
3. **Autonomous self-evolving systems** — event-driven agents that ingest, consolidate, crystallize, and self-correct without human intervention

## Core Methods

### 1. The raw + wiki Pattern (Karpathy Foundation)

Three-layer architecture that decouples source material from compiled knowledge:

```
raw/     → Source material (articles, papers, repos, transcripts, datasets)
wiki/    → LLM-compiled knowledge (interlinked markdown, categorized by concept)
scripts/ → Ingestion, query, and maintenance tools
```

The LLM reads from `raw/`, writes encyclopedia-style articles into `wiki/`, and maintains an `index.md` as the human-readable catalog. Key principles:

- **Backlinks are mandatory** — no new page without bidirectional links
- **Two-tier structure** — source summaries AND concept articles
- **Manifest tracking** — decouples ingestion from compilation
- **Batch mode** — ingest many sources, compile all at once
- **Outputs file back** — analyses, slides, charts get filed into the wiki

### 2. Memory Lifecycle

The original pattern treats all wiki content as equally valid forever. Production systems add:

- **Confidence scoring** — every fact carries a score based on source count, recency, contradictions. Strengthens with reinforcement, decays over time.
- **Supersession** — contradicting info explicitly supersedes old entries. Linked, timestamped; old preserved but marked stale.
- **Forgetting** — Ebbinghaus forgetting curve applied to knowledge. Facts not accessed or reinforced gradually deprioritize (not deleted). Architecture decisions decay slowly; transient bugs decay fast.
- **Consolidation tiers** — mirrors human memory architecture:

| Tier           | Characteristics                         | Example                           |
| -------------- | --------------------------------------- | --------------------------------- |
| **Working**    | Ephemeral, high-detail, short-lived     | Current debugging session         |
| **Episodic**   | Event-linked, medium duration           | "The outage on March 12"          |
| **Semantic**   | Abstracted, high-confidence, long-lived | "Service X depends on Redis 7.2+" |
| **Procedural** | Compressed into reusable patterns       | "How to deploy service X"         |

The LLM promotes information up through tiers as evidence accumulates.

### 3. Knowledge Graphs

Flat wikilinks break down beyond ~50 pages. Typed relationships carry semantic weight that keyword search misses:

- **Entity extraction** on ingest — people, projects, libraries, concepts, files, decisions
- **Typed relationships** — "uses", "depends on", "contradicts", "caused", "fixed", "supersedes"
- **Graph traversal for queries** — walk edges to find downstream connections keyword search misses
- Graph augments pages: **pages for reading, graph for navigation and discovery**

Related: [[code-review-graph]] applies this principle to codebases via Tree-sitter structural maps, achieving 8.2x average token reduction.

### 4. Hybrid Search

The `index.md` works as primary search to ~100–200 pages. Beyond that:

| Layer               | Method                               | Strength             |
| ------------------- | ------------------------------------ | -------------------- |
| **BM25**            | Keyword + stemming/synonym expansion | Exact term recall    |
| **Vector search**   | Semantic similarity embeddings       | Conceptual matching  |
| **Graph traversal** | Entity-aware edge walking            | Relational discovery |

Fused with **reciprocal rank fusion**. Keep `index.md` as human-readable catalog, not primary search mechanism.

### 5. Crystallization

Automatically distill completed work chains (research, debugging, analysis sessions) into structured digests:

```
question → findings → entities → lessons
```

Digests become first-class wiki pages. **Explorations are sources** — just like articles and papers. This closes the loop: sessions don't evaporate; they feed back into the knowledge base.

### 6. Event-Driven Automation

Hooks that keep the wiki healthy without manual intervention:

| Event | Action |
|-------|--------|
| New source | Auto-ingest, extract entities, update graph, update index |
| Session start | Load relevant context from wiki based on recent activity |
| Session end | Compress session into observations, file insights |
| Query | Check if answer worth filing back (quality score > threshold) |
| Memory write | Check for contradictions, trigger supersession |
| Schedule | Periodic lint, consolidation, retention decay |

## Tools & Ecosystem

### Approach Comparison

| Approach                           | Originator             | Key Innovation                                                                               | Scale       | Automation          | Status        |
| ---------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------- | ----------- | ------------------- | ------------- |
| **Karpathy v1**                    | Andrej Karpathy        | raw → wiki pipeline, backlinks, lint passes                                                  | ~100 pages  | Manual + scripts    | Foundation    |
| **Karpathy Wiki Agent** (yologdev) | yologdev               | 4-phase autonomous pipeline (Assess → Plan → Build → Communicate) on 4h GitHub Actions cycle | ~100 pages  | Fully autonomous    | Active        |
| **LLM Wiki v2**                    | rohitg00 (Rohit Gupta) | Memory lifecycle, knowledge graph, hybrid search, crystallization, multi-agent sync          | 100s+ pages | Event-driven        | Active, 373★  |
| **Hermes Wiki**                    | Hermes Agent           | Cron-driven synthesis handbooks, concept/source pages, schema-driven                         | Growing     | Cron + manual       | Active        |
| **MemPalace**                      | mempalace-github       | Hierarchical palace (wings/rooms/drawers), 96.6% LongMemEval R@5, AAAK 30x compression       | Large       | MCP server + agents | Active        |
| **Memvid**                         | Memvid project         | Vector DB replaced by MP4 files, sub-ms retrieval, millions of chunks                        | Large       | API-driven          | Experimental  |
| **GitNexus**                       | —                      | Full knowledge graph engine for codebases, maps every dependency/call chain                  | Codebases   | Automated           | Active, 40K+★ |

### Supporting Infrastructure

| Tool | Purpose | Note |
|------|---------|------|
| **MarkItDown** (Microsoft) | Converts any document to Markdown for LLM ingestion | Open-source, active |
| **TurboQuant + MLX** | Pre-fill 256K KV cache with private docs on Apple Silicon | Instant, lossless, private |
| **Flash-MoE** | Pure C + Metal inference; 397B params on MacBook | No cloud needed |
| **8 AI Agents for Obsidian** | PhD researcher replaces Notion + notes with 8 AI agents | Active |

## Architecture Patterns

### Consolidation Tiers

Knowledge flows upward through tiers as confidence accumulates:

```
Working Memory (ephemeral)
    ↓ reinforce
Episodic Memory (event-linked)
    ↓ generalize
Semantic Memory (abstracted facts)
    ↓ compress
Procedural Memory (reusable patterns)
```

Each tier is more compressed, more confident, and longer-lived. The LLM promotes information automatically.

### Confidence Decay

Every fact carries a confidence score influenced by:

- **Source count** — more sources = higher confidence
- **Recency** — newer sources weigh more
- **Contradictions** — conflicting evidence lowers confidence
- **Reinforcement** — repeated access or citation strengthens confidence
- **Domain decay rate** — architecture decisions decay slowly; transient bugs decay fast

### Supersession Protocol

When contradicting information arrives:

1. New claim extracted with timestamp and source authority
2. Old claim marked `[STALE: superseded by [[page#section]] on YYYY-MM-DD]`
3. Both preserved — old is not deleted, just deprioritized
4. Confidence of old drops; confidence of new starts high
5. Downstream pages that reference old claim get flagged for review

### Quality & Self-Correction

- **Score everything** — LLM-written content gets a quality score (structure, citations, consistency). Below threshold → flagged for rewrite.
- **Self-healing lint** — auto-fixes orphan pages, stale claims, broken cross-references.
- **Contradiction resolution** — propose which claim is more likely correct based on recency, authority, supporting observations.

### Multi-Agent Collaboration

For teams or multi-agent setups:

- **Mesh sync** — multiple agents merge observations; last-write-wins with timestamp + manual override
- **Shared vs. private scoping** — private observations roll up into shared knowledge when promoted
- **Work coordination** — lightweight tracking of who's working on what

## Conflicting Views

### RAG vs. LLM-Authored Wikis

| Dimension         | RAG (Vector DB)                         | LLM Wiki                                         |
| ----------------- | --------------------------------------- | ------------------------------------------------ |
| Coherence         | Chunking artifacts                      | Full human-readable articles                     |
| Maintenance       | Static index, manual updates            | Self-improving through lint/consolidation passes |
| Human access      | Black box (embedding vectors)           | Direct markdown files in Obsidian                |
| Compounding value | None — each query is isolated           | Each query enriches the wiki                     |
| Infrastructure    | Vector DB, embeddings pipeline, hosting | Just markdown files                              |
| Scale ceiling     | Handles millions of chunks              | Hybrid search needed past ~100 pages             |

**Consensus:** RAG wins at massive scale (millions of documents). LLM wikis win at personal/team scale (<10K pages) where coherence, human readability, and compounding value matter. The hybrid approach (LLM wiki + vector search for the raw tier) captures both advantages.

### Flat vs. Structured Knowledge

Karpathy's original design uses flat pages with wikilinks. LLM Wiki v2 argues typed relationships and knowledge graphs are essential past 50 pages. Both are correct — flat is sufficient for MVPs; structure becomes necessary at scale. The implementation spectrum below reflects this.

## Implementation Spectrum

| Level | Addition | When to Add |
|-------|----------|-------------|
| **MVP** | raw + wiki + index.md + schema | Start here (Karpathy original) |
| **Lifecycle** | Confidence scoring, supersession, retention decay | When wiki starts aging |
| **Structure** | Entity extraction, typed relationships, knowledge graph | When pages > 50 |
| **Automation** | Auto-ingest, auto-lint, context injection hooks | When manual ops slow you down |
| **Scale** | Hybrid search, consolidation tiers, quality scoring | At 100s+ pages |
| **Collaboration** | Mesh sync, shared/private scoping, work coordination | When multiple agents contribute |

## Best Practices

1. **The schema is the real product** — a well-crafted schema document turns a generic LLM into a disciplined knowledge worker. Co-evolve it over time. Transfer it to others.
2. **Start flat, add structure incrementally** — don't over-engineer on day one. Add knowledge graph, hybrid search, and lifecycle management only when the flat wiki starts creaking.
3. **Never delete, always supersede** — preserve old knowledge, mark it stale. This maintains audit trail and enables rollback.
4. **Explorations are first-class sources** — debugging sessions, research rabbit holes, and analysis chains should crystallize back into the wiki as structured digests.
5. **Event-driven over scheduled** — hooks that fire on ingestion, query, and contradiction are more responsive than periodic cron jobs. Use both for defense in depth.
6. **Lint religiously** — automated lint passes find orphans, contradictions, missing connections, and stale claims. Run them on every change or on schedule.
7. **Backlinks are non-negotiable** — every new page must link to and be linked from related concepts. This is the connective tissue that makes wikis more than folders of files.
8. **Batch ingestion, not trickle** — accumulate sources, then compile all at once. This gives the LLM cross-source context for better synthesis.
9. **Privacy on ingest** — auto-strip API keys, tokens, passwords, PII before content enters the wiki. Filter at the boundary.
10. **Confidence decay is domain-specific** — architecture decisions should decay slowly (months); bug reports and transient states should decay fast (days).

## Related Concepts

- [[llm-knowledge-bases]] — Core LLM wiki architecture and RAG comparison
- [[karpathy-llm-wiki-agent]] — Autonomous 4-phase pipeline on GitHub Actions
- [[memory-systems]] — TurboQuant, MLX, MemPalace, Memvid, Flash-MoE for AI memory
- [[llm-wiki-v2-rohitg00]] — Extended pattern with lifecycle, graph, hybrid search, crystallization
- [[code-review-graph]] — Tree-sitter knowledge graph for codebases (8.2x token reduction)
- [[ai-coding-agents]] — Coding agent tools and benchmarks
- [[token-optimization]] — Context window management, caching, prompt distillation
- [[mcp-protocol]] — Model Context Protocol for standardized tool/resource access
- [[hermes-agent-architecture]] — Hermes Agent design, skills, and autonomous workflows
