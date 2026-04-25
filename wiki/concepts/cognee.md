---
title: Cognee — Graph-Vector Hybrid Memory Engine
type: concept
tags:
- memory-systems
- ai-agents
- knowledge-management
- concept
sources:
- agent-memory-cognee-akshay-2026-04
created: '2026-04-15'
updated: '2026-04-15'
confidence: high
status: current
agents:
- hermes
priority: important
summary: "Open-source knowledge engine combining vector search, knowledge graphs, and relational provenance for AI agent memory. Four API calls, embedded defaults (SQLite+LanceDB+Kuzu), production-swappable backends."
---

# Cognee — Graph-Vector Hybrid Memory Engine

## Summary

Open-source knowledge engine for AI agent memory that combines three storage paradigms (vector, graph, relational) under a single 4-call API. Default embedded stack (SQLite + LanceDB + Kuzu) requires no Docker or external services. Production backends (Postgres, Qdrant, Neo4j) swappable without code changes.

## Why It Exists

Agent memory requires three capabilities that no single store provides:
1. **Semantics** — "database" matches "PostgreSQL" (vector search)
2. **Relationships** — Alice works on Project Atlas which uses PostgreSQL (graph traversal)
3. **Provenance** — where did this fact come from, who has access (relational)

Flat vectors fail at multi-hop reasoning. Flat files fail at synonyms. Graphs alone miss semantic similarity. Cognee combines all three.

## Architecture

### API Surface (4 calls)
```python
await cognee.add("content")       # Ingest anything
await cognee.cognify()            # Build knowledge graph + embeddings
await cognee.memify()             # Self-improve memory
await cognee.search("query")      # Retrieve with reasoning
```

### Storage Stack
| Store | Purpose | Default | Production |
|-------|---------|---------|------------|
| Relational | Provenance, access control | SQLite | Postgres |
| Vector | Semantic similarity | LanceDB | Qdrant/Pinecone/pgvector |
| Graph | Entity relationships | Kuzu | Neo4j/FalkorDB/Neptune |

### cognify() Pipeline
1. Document classification (type, domain)
2. Permission checking (multi-tenant)
3. Paragraph-aware chunking (not fixed-size cuts)
4. Entity/relationship extraction via LLM
5. Deduplication via content hashing (same entity across 50 docs → single node, 50 edges)
6. Summary generation
7. Dual indexing (vector embeddings + graph edges)

Incremental by default — only new/updated files reprocessed.

### memify() — Self-Improving Memory
RL-inspired optimization pass over the knowledge graph:
- Strengthen paths that led to good retrieval
- Prune stale nodes (not recently accessed)
- Auto-tune edge weights based on real usage
- Add derived facts from implicit relationships
- Graph develops domain-specific relevance over time

### Search Modes
14 modes shipped. Key ones:
- `GRAPH_COMPLETION` — graph traversal with completion (multi-hop)
- `SUMMARIES` — summary-based retrieval
- `INSIGHTS` — insight extraction

### Agent Integration
```python
class CogneeMemoryAgent:
    async def ingest(text, dataset="main"):
        await cognee.add(text, dataset)
        await cognee.cognify([dataset])

    async def recall(query, session_id="default"):
        results = await cognee.search(
            query_text=query,
            query_type=SearchType.GRAPH_COMPLETION,
            session_id=session_id,
        )
        return results[0] if results else ""

    async def chat(user_input):
        context = await self.recall(user_input)
        messages = build_messages_with_context(context, user_input)
        reply = await llm.chat(messages)
        await cognee.add(f"User:{user_input}\nAssistant:{reply}", "conversations")
        await cognee.cognify(["conversations"])
        return reply
```

## Key Features
- **Session memory** — automatic pronoun resolution within session_id
- **Multi-tenancy** — per-dataset graph-level permissions (read/write/delete/share)
- **Dual representation** — every graph node has a corresponding embedding
- **No infrastructure** — `pip install cognee` + API key = running
- **Memory cycle** — ingest → extract → store → retrieve → respond → store again

## Comparison with [[memory-systems|Other Memory Systems]]

| System | Vectors | Graph | Relational | Self-Improving |
|--------|---------|-------|------------|----------------|
| Cognee | Yes | Yes | Yes | Yes (memify) |
| [[mempalace|MemPalace]] | Yes (ChromaDB) | Yes (KG) | Yes (SQLite) | No (manual) |
| Zep/Graphiti | Yes | Yes (Neo4j) | Partial | Partial |
| OpenClaw | No | No | No (markdown) | No |

## Related
- [[memory-systems]] — broader memory landscape
- [[vectorless-rag]] — alternative: no vectors, LLM reasoning over structure
- [[llm-knowledge-bases]] — knowledge management patterns
- [[agent-memory-cognee-akshay-2026-04]] — source article
- [[agent-memory-two-camps-witcheer-2026-04]]
- [[async-subagent-pattern]]
- [[context-substrate]]
- [[daily-research-agentic-memory-2026-04-18]]
- [[honcho]]
- [[knowledge-graphs]]
- [[openchronicle]]
- [[openchronicle-einsia-2026-04]]
