---
title: "Daily Research: Agentic Memory — 2026-04-18"
type: source
tags: [research, agent-memory, context-engineering, daily-research]
created: '2026-04-18'
updated: '2026-04-18'
confidence: high
status: current
priority: reference
summary: "Daily research log — Cloudflare Agent Memory, 5 new ArXiv papers, context engineering crystallizing, camp convergence"
---

# Daily Research: Agentic Memory — 2026-04-18

## Key Findings

### Cloudflare Agent Memory (Private Beta)
Cloudflare launched a managed agent memory service with opinionated API (ingest/remember/recall/list/forget). Explicitly rejects raw filesystem access approach. Addresses context rot in long-running agents. Validates memory as critical infrastructure.

### Context Engineering Crystallizing
- **outcomeops/context-engineering**: First reference implementation — 5 components (corpus, retrieval, injection, output, enforcement)
- **Augment Code guide**: Formal distinction: "Agent memory = external storage. Context engineering = what goes in context window."
- **TeleAI Awesome list**: Now has dedicated "Agentic Context Engineering" section
- The term is moving from buzzword to discipline

### Camp Convergence
The two camps (Memory Backends vs Context Substrates) are **merging**:
- Cloudflare combines managed memory backend WITH retrieval-based context engineering
- Augment Code establishes both layers are required
- memweave demonstrates Camp 1 tool with Camp 2 philosophy (files as source of truth)

### Market Validation
- AI agent memory market: **$6.27B (2026)**, projected **$28.45B by 2030** (35% CAGR)

## New Tools

| Name | Camp | Key Insight |
|------|------|-------------|
| Cloudflare Agent Memory | Camp 1 (managed) | Opinionated API, rejects raw filesystem |
| outcomeops/context-engineering | Camp 2 | Context engineering as code |
| volcengine/OpenViking | Hybrid | ByteDance open-source |
| memweave | Camp 1 (minimalist) | Markdown + SQLite, anti-vector-DB |
| vectorize-io/hindsight | Camp 1 | Cognee/Mem0 alternative |

## New ArXiv Papers

- **GAM**: Hierarchical graph-based agentic memory (Apr 15)
- **Retrieval-based memory**: Retrieval alone sufficient for conversational memory (Apr 14)
- **APEX-MEM**: Semi-structured memory formats (Apr 15)
- **ContextCurator**: RL-based context curation — hybrid Camp 1/Camp 2 (Apr 14)
- **AMA**: Multi-granular memory via multi-agent collaboration (Apr 16)

## Sources

- [Cloudflare Agent Memory](https://blog.cloudflare.com/introducing-agent-memory/)
- [outcomeops/context-engineering](https://github.com/outcomeops/context-engineering)
- [TeleAI Awesome-Agent-Memory](https://github.com/TeleAI-UAGI/Awesome-Agent-Memory)
- [memweave](https://github.com/sachinsharma9780/memweave)

## Related

[[context-substrate]], [[memory-systems]], [[cognee]], [[agentic-ai]]
