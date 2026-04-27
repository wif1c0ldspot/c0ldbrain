---
type: daily-research
date: 2026-04-27
compiled: false
source: agentic-memory-research-cron
tags: [agentic-memory, daily-research]
---

# Agentic Memory Research — 2026-04-27

## Executive Summary

- **Stash** (312★, created Apr 24) launches as a Go-based persistent memory layer with an 8-stage consolidation pipeline and MCP server — fastest-growing new memory tool this week
- **auto-memory** (243★, created Apr 21) introduces zero-dependency progressive session recall for Copilot CLI — "page fault handler" mental model achieving 200x token savings
- **OpenViking v0.3.10** (released Apr 23) expands with new VLM providers, VikingDB cloud mode, and OpenClaw plugin ecosystem with ClawHub publishing
- **Hermes memory ecosystem emerging** — `hermes-local-memory` (19★) and `hermes-memory-skills` (17★) bring local-first SQLite memory and 3-phase dreaming consolidation to Hermes Agent
- **memtrace-public** (75★) builds bi-temporal, episodic knowledge graphs from AST for coding agents — structural approach via code analysis

## Findings

### 1. Stash — Cognitive Memory Layer (HIGH)
- **Source**: https://github.com/alash3al/stash
- **Stats**: 312★, created 2026-04-24, Go, Apache 2.0
- **Key Innovation**: 8-stage consolidation pipeline turning raw observations into structured knowledge: episodes → facts → relationships → causal links → goal tracking → failure patterns → hypothesis verification → confidence decay. Each stage processes only new data since last run.
- **Architecture**: Postgres + pgvector, MCP server, single binary, self-hosted, Docker Compose ready.
- **Integrations**: Claude Desktop, Cursor, Windsurf, Cline, Continue, OpenAI Agents, Ollama, OpenRouter — any MCP-compatible agent.
- **Camp**: Camp 1 (Memory Backend)
- **Relation**: The 8-stage pipeline is one of the most elaborate consolidation architectures seen. Directly comparable to MemPalace's room structure. The "patterns become wisdom" framing suggests emergent compression — relevant to C0ldbrain's compression spectrum concept.

### 2. auto-memory — Zero-Dependency Session Recall (HIGH)
- **Source**: https://github.com/dezgit2025/auto-memory
- **Stats**: 243★, created 2026-04-21, Python, MIT, ~1,900 LOC, zero dependencies
- **Key Innovation**: Read-only CLI that queries Copilot CLI's `session-store.db` (SQLite + FTS5) to inject ~50 tokens of recent context per prompt. Progressive tiered disclosure: Tier 1 cheap scan (~50 tokens) → Tier 2 focused recall (~200 tokens) → Tier 3 full session detail (~500 tokens).
- **Mental Model**: "Page fault handler" — context window = RAM, session-store = disk, auto-memory pulls exact facts from disk when needed. "Unlimited context recall."
- **Safety**: Read-only, schema-aware (fails fast on drift), WAL-safe with exponential backoff, telemetry ring buffer.
- **Camp**: Camp 2 (Context Substrate) — lightweight, IDE-integrated
- **Relation**: Novel proof that vector DBs aren't always necessary — SQLite FTS5 + progressive disclosure can be sufficient for coding agents. The "200x ROI" claim (50 tokens vs 10,000 for grep) challenges assumptions about retrieval cost. Connects to SCG-MEM thesis that vector stacks may be optional.

### 3. OpenViking v0.3.10 — Context Database Expansion (HIGH)
- **Source**: https://github.com/volcengine/OpenViking/releases/tag/v0.3.10
- **Stats**: 23,142★, released 2026-04-23, 46 commits
- **Key Updates**:
  - New VLM providers: Codex, Kimi, GLM with `vlm.timeout` config
  - VikingDB `volcengine.api_key` data plane mode — cloud VikingDB access via API key
  - `write()` `mode="create"` — create new text resource files with auto semantic/vector refresh
  - OpenClaw plugin ecosystem: ClawHub publishing, interactive setup wizard, `OPENCLAW_STATE_DIR` support
  - QueueFS SQLite backend — persistent queues, ack, stale message recovery
  - Locomo/VikingBot evaluation preflight checks
- **Camp**: Camp 2 (Context Substrate) / Infrastructure
- **Relation**: The OpenClaw plugin ecosystem (ClawHub) signals ByteDance is building a distribution platform for context tools. The VikingDB cloud bridge suggests "context database as a service" is coming. SQLite backend for QueueFS shows pragmatism — hybrid cloud+local.

### 4. Hermes Memory Ecosystem (HIGH)
- **hermes-local-memory**: https://github.com/smarzola/hermes-local-memory (19★, created Apr 25)
  - SQLite memory provider for Hermes Agent. Local-first, inspectable, agent-controlled.
  - Explicit tools (not opaque backend), deterministic retrieval, source-labeled context, conservative dry-run maintenance.
  - Inspired by Honcho (peers/cards/consolidation) but deliberately "boring engineering": one SQLite DB, explicit identity mapping, agent-generated patches.
  - **Status**: alpha
- **hermes-memory-skills**: https://github.com/nexus9888/hermes-memory-skills (17★, created Apr 25)
  - **Agent Dreaming**: 3-phase background consolidation (Light → Deep → REM) modeled on OpenClaw's dreaming metaphor. Light ingests transcripts, Deep scores on Novelty/Durability/Specificity/Reduction, REM extracts recurring patterns and proposes structural actions.
  - **Memory Lean Check**: Surgical trimmer validating wiki pointers, condensing verbose entries, removing stale/temporary entries, post-write integrity check.
- **Camp**: Camp 1 + Camp 2 hybrid
- **Relation**: Directly relevant to Hermes/MemPalace stack. The "dreaming" skill pattern is portable — could integrate with MemPalace's diary/consolidation workflow. The "lean check" pattern addresses a real problem: memory bloat. SQLite provider suggests users want lighter alternatives to full server setups.

### 5. memtrace — AST-Based Knowledge Graph (MEDIUM)
- **Source**: https://github.com/syncable-dev/memtrace-public
- **Stats**: 75★, created 2026-04-11, TypeScript/Node.js, Proprietary EULA
- **Key Innovation**: Bi-temporal, episodic, structural knowledge graph for coding agents — built from AST (Abstract Syntax Tree), not guesswork. Temporal features include evolution scoring and timeline replay.
- **Status**: Private beta, waitlist required. Core indexing and structural search stable; temporal features functional but rough.
- **Camp**: Camp 2 (Context Substrate) — coding-agent specific
- **Relation**: The AST-based approach is novel — most memory systems ingest text or embeddings; memtrace parses code structure directly. Bi-temporal modeling (valid time vs transaction time) is rare in agent memory. However, proprietary license limits adoption.

## Notable Repo Updates (existing tools)

| Repo | Stars | Last Push | Notes |
|------|-------|-----------|-------|
| mem0ai/mem0 | 54,201 | Apr 25 | Node SDK v3.0.2 released |
| supermemoryai/supermemory | 22,192 | Apr 27 | Active, search shortcut fix |
| volcengine/OpenViking | 23,142 | Apr 27 | v0.3.10 + active pushes |
| topoteretes/cognee | 16,762 | Apr 24 | v1.0.3 released |
| letta-ai/letta | 22,328 | Apr 12 | Quiet |
| getzep/zep | 4,492 | Apr 9 | Quiet |

## Pattern of the Day

**"Memory as Page Fault Handler"**: auto-memory's framing — context window = RAM, persistent store = disk, recall = page fault — elegantly captures a shift in how developers think about agent memory. Instead of "how much can we stuff into context?", the question becomes "how cheaply can we pull exactly what we need?" This aligns with the generative retrieval paradigm (SCG-MEM) and challenges the vector-database-default assumption. The 50-token recall barrier is a new benchmark.

## Integration Recommendations

1. **Stash's 8-stage pipeline** could inspire MemPalace consolidation room logic — the progression from episodes to wisdom maps well to drawer lifecycle
2. **auto-memory's progressive disclosure** is directly applicable to Hermes context injection — tier 1/2/3 recall based on prompt complexity
3. **OpenViking's ClawHub** pattern suggests MemPalace could benefit from a plugin/skills marketplace for memory tools
4. **Hermes memory skills** dreaming + lean check should be evaluated for MemPalace integration — the 3-phase consolidation and surgical trimmer solve real problems
5. **memtrace's AST approach** suggests code-specific memory might need different ingestion pipelines than text memory

## Sources
- https://github.com/alash3al/stash
- https://github.com/dezgit2025/auto-memory
- https://github.com/volcengine/OpenViking/releases/tag/v0.3.10
- https://github.com/smarzola/hermes-local-memory
- https://github.com/nexus9888/hermes-memory-skills
- https://github.com/syncable-dev/memtrace-public
