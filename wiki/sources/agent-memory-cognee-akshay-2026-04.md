---
title: Build Agents That Never Forget — Agent Memory Layers
type: source
tags:
- ai-agents
- memory-systems
- knowledge-management
- agentic-ai
- source
- social
- x
source_url: https://x.com/akshay_pachaar/status/2043745099792953508
sources: []
created: '2026-04-15'
updated: '2026-04-15'
confidence: high
status: current
agents:
- hermes
priority: important
summary: First-principles walkthrough of agent memory through 4 layers (list, markdown,
  vectors, graph-vector hybrid) introducing Cognee as open-source three-store knowledge
  engine.
compiled: true
---

# Build Agents That Never Forget — Akshay (@akshay_pachaar)

## Summary

Comprehensive walkthrough of AI agent memory systems progressing through 4 layers: Python lists (RAM-only), markdown files (persistent but keyword-limited), vector search (semantic but no relational reasoning), and graph-vector hybrids (full solution). Introduces [[cognee]] as an open-source knowledge engine combining vector search, knowledge graphs, and relational provenance in 4 API calls.

## Key Concepts

### The Memory Problem
- LLMs are stateless — every API call starts fresh
- 7 failure modes without memory: context amnesia, zero personalization, multi-step task failure, repeated mistakes, no knowledge accumulation, hallucination from gaps, identity collapse
- "Lost in the middle" effect: 30%+ accuracy drop when info sits in middle of long context
- Raw context length insufficient — need persistence, prioritization, salience

### Cognitive Science Framework (Lilian Weng 2023)
- Agent = LLM + Memory + Planning + Tool Use
- Three memory systems: Sensory (perceptual), Working (7±2 items), Long-term (durable, retrieval bottleneck)
- Long-term splits: Episodic (events), Semantic (facts), Procedural (skills)
- Memory consolidation: repeated events distilling into general knowledge

### The Four Layers

| Layer | Storage | Semantics | Relations | Limitation |
|-------|---------|-----------|-----------|------------|
| 1. Python List | No | No | No | RAM-only, unbounded growth |
| 2. Markdown Files | Yes | No | No | Keyword search, no synonyms |
| 3. Vector Search | Yes | Yes | No | Multi-hop reasoning fails |
| 4. Graph-Vector Hybrid | Yes | Yes | Yes | Full solution |

### Layer Details

**Layer 1 (List):** Append conversation history, re-send with every call. Hits context ceiling ~turn 200. Lost on restart.

**Layer 2 (Markdown):** Write to disk (human-readable, Git-friendly). Claude Code uses CLAUDE.md/MEMORY.md pattern. At scale (2000 facts = 500K+ tokens), keyword search can't handle synonyms, paraphrases, or connections. "Storage without intelligent retrieval is a library with no catalog."

**Layer 3 (Vectors):** Embeddings solve synonym problem. But multi-hop reasoning fails — "Was Alice's project affected by Tuesday's outage?" requires connecting Alice→Project Atlas→PostgreSQL→outage across 3 facts. The connecting fact mentions neither Alice nor Tuesday.

**Layer 4 (Graph-Vector Hybrid):** Need all three storage paradigms in one system.

### Cognee — Three Stores, One Engine

Open-source knowledge engine combining vector search + knowledge graphs + relational provenance.

**API:** 4 async calls — `add()`, `cognify()`, `memify()`, `search()`

**Default stack:** SQLite + LanceDB + Kuzu (embedded, file-based, no Docker)
**Production swap:** Postgres + Qdrant/Pinecone/pgvector + Neo4j/FalkorDB/Neptune

#### Three Stores
- Relational → provenance (source, timing, access control)
- Vector → semantics (meaning, similarity)
- Graph → relationships (connections, causation, org structure)

#### cognify() Pipeline
1. Document classification by type/domain
2. Permission checking (multi-tenant)
3. Paragraph-aware chunk extraction
4. Entity/relationship extraction via LLM with deduplication (content hashing)
5. Summary generation
6. Dual indexing (vector + graph)

Same entity across 50 docs → merged into single node with 50 edges. Incremental by default.

#### memify() — Self-Improving Memory
RL-inspired graph optimization:
- Strengthen useful retrieval paths
- Prune stale untouched nodes
- Auto-tune edge weights from usage
- Add derived facts (implicit relationships)

#### 14 Search Modes
Key ones: GRAPH_COMPLETION (graph traversal), SUMMARIES, INSIGHTS

### Agent Integration Pattern
```
ingest() → add + cognify
recall() → search with GRAPH_COMPLETION + session_id
chat() → recall + LLM + store conversation back
```
- Session memory: automatic pronoun resolution within session_id
- Multi-tenancy: per-dataset graph-level permissions

## Related Concepts
- [[memory-systems]] — broader memory landscape
- [[vectorless-rag]] — alternative to vector-based retrieval
- [[llm-knowledge-bases]] — knowledge management patterns
- [[cognee]] — the tool introduced in this source

## Stats
171K views, 3141 bookmarks, 1539 likes, 257 reposts (Apr 13, 2026)

## Links
- Cognee GitHub: https://github.com/topoteretes/cognee
- Miller 1956: https://pmc.ncbi.nlm.nih.gov/articles/PMC4486516/
- OpenClaw (markdown memory limitations reference)

## Author
Akshay (@akshay_pachaar) — Co-founder @dailydoseofds_, BITS Pilani, 3 Patents, ex-AI Engineer @ LightningAI
