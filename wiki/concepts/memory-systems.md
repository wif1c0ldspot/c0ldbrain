---
title: AI Memory Systems & Context Management
type: concept
tags: [memory-systems, ml-models, llm, cost]
sources:
- karpathy-llm-knowledge-base-viral-2026-04
- karpathy-self-improving-second-brain-2026-04
- karpathy-llm-kb-architecture-2026-04
- karpathy-personal-kb-agents-2026-04
- karpathy-llm-kb-pattern-2026-04
- mempalace-github-2026-04
- goclaw-agent-gateway-2026-04
- claude-code-from-source-2026-04
- rowboat-knowledge-graph-2026-04
- hwchase17-agent-harnesses-2026-04
- agent-memory-cognee-akshay-2026-04
- memvid-mp4-ai-memory-2026-04
- mlx-turboquant-local-power-2026-04
- turboquant-kv-cache-experiments-2026-04
- knowledge-graph-codebase-engine-2026-04
- multica-agent-memory-mem0ai-2026-04
- agent-memory-poisoning-security-2026-04
- simplemem-github-2026-04
- missing-memory-hierarchy-arxiv-2026-04
- million-token-illusion-oracle-converged-db-datachaz-2026-04rchy-arxiv-2026-04
- cloudflare-agent-memory-2026-04
- openviking-context-database-volcengine-2026-04
- memmachine-multi-tier-memory-2026-04
- atant-benchmark-critique-2026-04
- adam-privacy-attack-agent-memory-2026-04
- cavemem-cross-agent-memory-2026-04
- chum-mem-pckc-2026-04
- pomclaw-enterprise-agent-2026-04
- mem0-v2-0-redesign-2026-04
- mistake-notebook-learning-acl-2026
created: '2026-04-06'
updated: '2026-04-24'  # was: '2026-04-21'
confidence: high
status: current
agents: [hermes, claude, codex]
priority: critical
summary: How AI agents manage persistent memory and context. TurboQuant, MLX, Memvid,
  MemPalace, and KV cache optimization for instant, lossless queries. Memory is a core
  harness responsibility, not a plugin.
---


# AI Memory Systems & Context Management

## Summary

How AI agents manage persistent memory and context. Covers TurboQuant, MLX, Memvid, MemPalace, and Flash-MoE — alternatives to traditional RAG for local, instant queries.

## Key Technologies

### TurboQuant + MLX (Apple Silicon Super Power)

Combines Apple's MLX framework with TurboQuant compression:
- Pre-fill 256k KV cache with private documents or codebase
- Quantize and run on Apple's MLX framework
- Almost instantaneous, lossless document queries with total privacy
- >50% memory footprint reduction
- Qwen 3.5-27B runs on single RTX 5060 @ 3.15bit precision

### MemPalace (Hierarchical Memory Palace)

Memory system organizing conversations into a hierarchical "palace" (wings, rooms, closets, drawers):
- Mines conversations, code, notes into structured palace
- Stores everything lossless (no LLM summarization of originals)
- Semantic search across the structure
- 96.6% LongMemEval R@5, 100% with Haiku rerank
- 34% retrieval boost from structural organization
- MCP server with 19 tools for Claude/Cursor integration
- Knowledge graph with temporal validity (SQLite-backed)
- Specialist agents with persistent diaries
- AAAK: lossless compressed dialect, 30x token compression
- Compare with Zep/Graphiti: MemPalace is SQLite/free vs Neo4j/$25mo+

### Memvid (Vector DB Replacement)

Replaces vector databases with MP4 files:
- Packages embeddings into single portable file
- Uses video encoding logic for sub-millisecond retrieval
- Stores millions of text chunks
- Eliminates need for dedicated vector DB infrastructure

### Flash-MoE (Massive Model on Laptop)

397B parameters on a MacBook:
- Pure C and Metal inference engine
- Runs Qwen3.5-397B on consumer hardware
- No cloud, no GPU cluster needed

### Local Model Trends

|| Model | Hardware | Performance | Status ||
||-------|----------|-------------|--------||
|| Qwen3.5 27B (distill) | $600 16GB Mac Mini | Beats Claude Sonnet 4.5 | Active ||
|| Qwen3.5 397B | MacBook (Flash-MoE) | Full model on laptop | Experimental ||
|| Claude 4.6 Opus reasoning traces | — | Trained Qwen3.5 distill on | Active ||

### GoClaw 3-Tier Memory (from goclaw-agent-gateway-2026-04)

Production multi-tenant agent gateway (2.7k stars) implements a 3-tier memory architecture:
- **Short-term**: Conversation context within a session
- **Working**: Task-relevant information across sessions
- **Long-term**: Knowledge Vault for persistent organizational knowledge
- Written in Go, supports 20+ LLM providers and 7 messaging channels

### Rowboat Knowledge Graph Memory (from rowboat-knowledge-graph-2026-04)

AI coworker (12.4k stars) builds knowledge graphs from email and meetings:
- Automatic entity extraction and relationship mapping
- Outputs Obsidian-compatible vault with wikilinks
- Incremental updates as new data arrives
- Demonstrates LLM-compiled persistent memory pattern

## Memory is a Core Harness Responsibility (from hwchase17-agent-harnesses-2026-04)

### Agent Harnesses and Memory

Harrison Chase identifies agent harnesses as the dominant pattern for building agents, and they are intimately tied to memory management. **Memory is not a plugin — it's a core capability and responsibility of the agent harness.**

Sarah Wooders' key insight: "Asking to plug memory into an agent harness is like asking to plug driving into a car." Managing context (and therefore memory) is fundamental to how a harness functions.

### Critical Memory Architecture Questions

Sarah Wooders lists these essential questions about how a harness must manage memory:

| Question | Why It Matters |
|----------|----------------|
| How are config files (AGENTS.md, CLAUDE.md) loaded into context? | Affects how agent discovers its own capabilities |
| How is skill metadata shown to agents? | Determines tool discoverability and usage |
| Can agent modify its own system instructions? | Enables self-improvement and adaptation |
| What survives compaction, and what's lost? | Determines what knowledge persists across sessions |
| Are interactions stored and made queryable? | Enables learning from history and patterns |
| How is memory metadata presented to agent? | Affects memory retrieval and relevance |
| How is current working directory represented? | Context awareness for file-based tasks |
| How much filesystem information is exposed? | Security and capability boundaries |

### Memory as Context

Memory is fundamentally a form of context:
- **Short-term memory**: Messages in conversation, large tool call results (handled by harness)
- **Long-term memory**: Cross-session memory (needs to be updated and read by harness)

### Memory is in Its Infancy

Current state of memory systems:
- Memory as a concept is still in its infancy
- No well-known or common abstractions for memory yet
- Long-term memory is often not part of MVP — first get agent working, then worry about personalization
- If best practices emerge, separate memory systems might make sense in the future

Bottom line: "Ultimately, how a harness manages context and state in general is the foundation for agent memory."

## The Four Memory Layers (from agent-memory-cognee-akshay-2026-04)

A first-principles taxonomy of agent memory progression:

| Layer | Example | Persistence | Semantics | Relations |
|-------|---------|-------------|-----------|-----------|
| 1. In-memory list | `messages = []` | No | No | No |
| 2. Markdown files | CLAUDE.md, MEMORY.md | Yes | No | No |
| 3. Vector search | ChromaDB, LanceDB | Yes | Yes | No |
| 4. Graph-vector hybrid | Cognee, MemPalace | Yes | Yes | Yes |

Key insight: "Storage without intelligent retrieval is a library with no catalog." Vectors solve synonyms but fail at multi-hop reasoning (Alice→Project Atlas→PostgreSQL→outage). Graphs are needed for relational business knowledge.

### Cognee (Graph-Vector Hybrid Engine)

Open-source knowledge engine combining vector + graph + relational stores:
- 4 async calls: `add()`, `cognify()`, `memify()`, `search()`
- Default: SQLite + LanceDB + Kuzu (embedded, no Docker)
- Production: Postgres + Qdrant + Neo4j (swappable without code changes)
- `cognify()` builds knowledge graph with deduplication (same entity across N docs → single node)
- `memify()` runs RL-inspired self-improvement (strengthen useful paths, prune stale nodes)
- 14 search modes including GRAPH_COMPLETION for multi-hop queries
- Session memory with automatic pronoun resolution
- Multi-tenant graph-level permissions
- See [[cognee]] for full details

## The Two Camps: Memory Backends vs Context Substrates

Based on comprehensive analysis of 900+ GitHub repos tagged "agent-memory" and "context-management" (see [[agent-memory-two-camps-witcheer-2026-04]]):

### Camp 1: Memory Backends
Extract facts → store in vector/graph DBs → retrieve relevant facts. Optimizes for **recall accuracy**.

**Loop**: conversation happens → extract facts → store in DB → retrieve and inject next conversation

**Examples**: Mem0 (53.1k stars), MemPalace, Supermemory, Cognee, Honcho

### Camp 2: Context Substrates  
Structured, human-readable context files that agents read/write to. Optimizes for **compounding improvement** over time.

**Loop**: agent reads context → works within it → writes updates → richer context next session

**Examples**: OpenClaw (358k stars), Zep (rebranded to "context engineering"), TrustGraph, Thoth, MemSearch

**Key Distinction**: Camp 1 asks "what should the AI remember?" Camp 2 asks "what context should the AI work inside?"

See [[context-substrate]] for full deep-dive on Camp 2 architectures.



## New Research (Week of 2026-04-18)

### ArXiv Papers

| Paper | Date | Key Idea | Camp |
|-------|------|----------|------|
| GAM: Hierarchical Graph-based Agentic Memory | ~Apr 15 | Hierarchical graph + sliding window; separates real-time knowledge from noise | Camp 1 |
| Let Conversational Agents Remember with Just Retrieval | ~Apr 14 | Retrieval alone sufficient; RCR-router for multi-agent | Camp 1 |
| APEX-MEM: Agentic Semi-Structured Memory | ~Apr 15 | Semi-structured memory formats; compares RAG vs larger context windows | Camp 1/2 |
| Active Context Curation via RL (ContextCurator) | ~Apr 14 | **RL-based context curation** — policy model curates working memory for frozen TaskExecutor | Camp 2 hybrid |
| AMA: Adaptive Memory via Multi-Agent | ~Apr 16 | Multi-granular memory with structured semantic components | Camp 1 |

### ContextCurator — Notable

The ContextCurator paper introduces a **lightweight policy model** that actively curates what goes into the context window of a frozen TaskExecutor. This is a direct Camp 2 approach — treating context as something to be engineered, not stored. Directly applicable to Hermes' skill/context loading decisions.

### Market Data
- AI agent memory market: **$6.27B (2026)**, projected **$28.45B by 2030** (35% CAGR)


## Related
- [[2026-04-20-research]]
- [[2026-04-19-research]] Concepts
- [[knowledge-management-synthesis]] — Unified view of knowledge management paradigms
- [[gbrain-agent-brain]] — Production implementation at scale (17,888 pages)
- [[demand-paging-for-agent-memory]]
- [[active-inference-free-energy-principle]]
- [[agent-memory-cognee-akshay-2026-04]]
- [[agent-memory-poisoning-security-2026-04]]
- [[agent-orchestration-stacks]]
- [[agentic-ai]]
- [[agentic-memory-research]]
- [[ai-agents-handbook-2026]]
- [[apex-mem-acl-2026-2026-04]]
- [[arxiv-active-inference-papers-2026-03]]
- [[async-subagent-pattern]]
- [[autoagent-kevinrgu-2026-04]]
- [[autogenesis-self-evolving-agent-protocol-2026-04]]
- [[belief-gate]]
- [[brain-inspired-agent-architecture]]
- [[cavemem-cross-agent-memory-2026-04]]
- [[chum-mem-pckc-2026-04]]
- [[claim-based-memory]]
- [[claude-code-from-source-2026-04]]
- [[cloudflare-agent-memory]]
- [[cloudflare-agent-memory-2026-04]]
- [[coral-multi-agent-discovery]]
- [[daily-research-agentic-memory-2026-04-18]]
- [[daily-research-agentic-memory-2026-04-19]]
- [[emergent-agent-evolution-synthesis]]
- [[evomedagent-memory-agents-2026-04]]
- [[gbrain-garrytan-ayi-ainotes-2026-04]]
- [[goclaw-agent-gateway-2026-04]]
- [[hermes-agent-practitioners-reference-2026]]
- [[hermes-ecosystem-nftcps-2026-04]]
- [[hermes-team-guide-nyk-builderz-2026-04]]
- [[higmem-acl-2026-2026-04]]
- [[honcho-hermes-lcm-stack-bayendor-2026-04]]
- [[hwchase17-agent-harnesses-2026-04]]
- [[hypermem-hypergraph-memory-2026-04]]
- [[karpathy-llm-kb-pattern-2026-04]]
- [[karpathy-personal-kb-agents-2026-04]]
- [[karpathy-self-improving-second-brain-2026-04]]
- [[knowledge-lifecycle-decision-framework]]
- [[knowledge-management-handbook-2026]]
- [[langflow-claude-code-integration]]
- [[letta-agentic-ai-2026-04]]
- [[llm-knowledge-bases]]
- [[mem0-v2-0-redesign-2026-04]]
- [[memory-worth-governance-2026-04]]
- [[mempalace]]
- [[mempalace-github-2026-04]]
- [[memvid-mp4-ai-memory-2026-04]]
- [[million-token-illusion-oracle-converged-db-datachaz-2026-04]]
- [[missing-memory-hierarchy-arxiv-2026-04]]
- [[mistake-notebook-learning-acl-2026]]
- [[ml-models-handbook-2026]]
- [[openchronicle-einsia-2026-04]]
- [[openviking-context-database]]
- [[polymarket-weather-hermes-agent-0xmovez-2026-04]]
- [[pomclaw-enterprise-agent-2026-04]]
- [[predictive-coding-active-inference]]
- [[resolvers-garrytan-2026-04]]
- [[rowboat-knowledge-graph-2026-04]]
- [[simplemem-github-2026-04]]
- [[skill-composition-procedural-learning]]
- [[skill0-skill-internalization-2026]]
- [[smith-cognitive-memory-2025]]
- [[training-free-self-improvement]]
- [[turboquant-kv-cache-experiments-2026-04]]
- [[weekly-synthesis-2026-04-20]]
- [[agent-harness]]
[[context-substrate]], [[llm-knowledge-base-pattern]], [[quantitative-trading]], [[ai-coding-agents]], [[token-optimization]], [[mcp-protocol]], [[llm-wiki-v2-rohitg00|related]], [[vectorless-rag]], [[cognee]], [[multica-relational-agent-memory]], [[honcho|related]], [[openchronicle]]


## Demand Paging for Agent Memory (New — April 2026)

The "[[demand-paging-for-agent-memory]]" paradigm maps LLM context management to OS virtual memory:
- **Context window** = physical RAM (limited, fast)
- **External store** = disk (vast, slower)
- **Demand paging** = load context pages only when needed
- **Working set** = subset actively being used
- **Eviction policy** = LRU, LFU, relevance-based
- **Page fault** = retrieval call when evicted context is needed

The Pichay system (ArXiv 2603.09023) implements this as a transparent proxy. This is a **Camp 1.5 hybrid** — uses Camp 1 storage but thinks in Camp 2 terms.

## Memory Security (New — April 2026)

Memory poisoning is now a real threat (OWASP ASI06):
- **MINJA framework**: >95% injection success rate
- **Memory Firewall pattern**: Semantic drift detection, write gates, quarantine
- **OWASP Agent Memory Guard**: Reference implementation for ASI06

See [[memory-firewall]] for the defense architecture.

## Notable Entrants (April 2026)

- **Cloudflare Agent Memory** (Private Beta): Managed service with ingest/remember/recall/list/forget API. Validates agent memory as critical enterprise infrastructure.
- **SimpleMem** (3,259⭐): Efficient lifelong memory with MCP server. Cloud-hosted at mcp.simplemem.cloud.
- **TrustGraph** (1,994⭐): "Supabase for context graphs" — multi-model storage, semantic retrieval, portable context cores.

## New Research (Week of 2026-04-20)

### Hierarchical Memory Convergence

Multiple independent teams converging on OS-inspired hierarchical memory:

| System | Tiers | Key Result | Source |
|--------|-------|-----------|--------|
| [[memmachine-multi-tier-memory-2026-04\|MemMachine]] | 3 (short/episodic/profile) | 0.9169 LoCoMo, **80% fewer tokens** | ArXiv:2604.04853 |
| MemoryOS | 3 (short/mid/long-term) | **+49% F1** on LoCoMo | ArXiv:2506.06326 |
| GAM | Graph + topic networks | Hierarchical event progression | ArXiv:2604.12285 |
| Mnemosyne | Graph + decay + recall | **Highest LoCoMo temporal reasoning** | ArXiv:2510.08601 |
| RoMem | Temporal KG + rotation | 2-3x MRR on temporal reasoning | ArXiv:2604.11544 |
| MemGAS | Multi-granularity + GMM | Outperforms SOTA on 4 benchmarks | ArXiv:2505.19549 |

See [[hierarchical-memory-architectures]] for full analysis.

### Context Database — New Product Category

**[[openviking-context-database-volcengine-2026-04|OpenViking]]** (22,623★) from ByteDance/Volcengine positions as a "context database" — unifying memory + RAG + skills. First tool to combine all three. Created Jan 2026, extraordinary adoption.

### Benchmark Critique: ATANT

**[[atant-benchmark-critique-2026-04|ATANT]]** (ArXiv:2604.06710/2604.10981) defines 7 properties of true continuity and shows existing benchmarks cover a median of **1 of 7 properties**. 23% of LoCoMo unscorable. Don't trust single-number scores.

### Security: ADAM Privacy Attack

**[[adam-privacy-attack-agent-memory-2026-04|ADAM]]** (ArXiv:2604.09747) — **100% success rate** extracting sensitive data from agent memory. More severe than injection. Required: encryption at rest, access controls, audit logging.

### Context Engineering Formalized (5 papers)

| Paper | Key Contribution |
|-------|-----------------|
| CE Framework (2604.04258) | 5-role context package, 32%→55% first-pass acceptance |
| CE Discipline (2603.09619) | 5 quality criteria: relevance, sufficiency, isolation, economy, provenance |
| Tokalator (2604.08290) | VS Code extension for real-time context budget monitoring |
| HYVE (2604.05400) | Hybrid views reduce tokens 50-90% |
| DT-MDP-CE (2603.22083) | Digital-twin MDP for enterprise context engineering |

### RAG Alternatives

| Paper | Approach | Result |
|-------|----------|--------|
| CER (2506.06698) | Dynamic experience replay | 36.7% WebArena (+51% over GPT-4o) |
| CLEAR (2604.07487) | Generative context via contrastive learning | 72→81% AppWorld |
| XpandA (2505.20625) | Dynamic partitioning + shared memory | +20%, 1.5x speedup |
| PRECEPT (2602.07321) | Exact-match rules + Bayesian reliability | +41.1pp over Reflexion |
