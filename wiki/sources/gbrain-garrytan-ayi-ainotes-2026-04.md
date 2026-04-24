---
title: GBrain — Garry's Opinionated OpenClaw/Hermes Agent Brain
date: 2026-04-20
type: source
compiled: true
tags:
- source
- hermes
- agent
- memory
- agent-brain
source: raw/social/gbrain-garrytan-ayi-ainotes-2026-04.md
priority: reference
updated: '2026-04-24'
created: '2026-04-24'
confidence: high
status: current
summary: Auto-generated placeholder for GBrain — Garry's Opinionated OpenClaw/Hermes
  Agent Brain
---

---
title: "GBrain — Garry's Opinionated OpenClaw/Hermes Agent Brain"
author: "@AYi_AInotes (source link), Garry Tan (creator)"
date_fetched: 2026-04-20
source_tweet: "https://x.com/ayi_ainotes/status/2045825589366362562"
source_repo: "https://github.com/garrytan/gbrain"
---

## Tweet Content

@AYi_AInotes: "看 INSTALL_FOR_AGENTS.md，复制命令到 OpenClaw 就行" (Read INSTALL_FOR_AGENTS.md, copy commands to OpenClaw)

Links to: GitHub - garrytan/gbrain: Garry's Opinionated OpenClaw/Hermes Agent Brain

## Repository Overview

GBrain: Production brain powering Garry Tan's (President/CEO of Y Combinator) OpenClaw and Hermes deployments.

- **Scale**: 17,888 pages, 4,383 people, 723 companies
- **Autonomous**: 21 cron jobs running autonomously
- **Built**: 12 days
- **Performance**: Recall@5 95%, Precision@5 45%, Graph-only F1: 86.6%

## Key Features

### Hybrid Search + Knowledge Graph
- Vector search + keyword search + Reciprocal Rank Fusion
- Self-wiring knowledge graph — zero LLM calls for relationship extraction
- Typed links: attended, works_at, invested_in, founded, advises
- Backlink-boosted ranking

### 26 Skills
- Signal-detector: parallel cheap model for entity capture
- Brain-ops: brain-first lookup before external APIs
- Content ingestion: meetings, emails, tweets, voice calls
- Enrichment: tiered person/company page creation
- Minion-orchestrator: durable Postgres job queue
- Skillify: 10-item skill completeness checklist

### Minions (Postgres Job Queue)
- 753ms wall time vs >10s gateway timeout
- $0 token cost vs ~$0.03 per run
- 100% success vs 0% spawn failure
- SIGKILL resilient, cascade cancel, fan-out

### Architecture
- Brain Repo (git) → GBrain (retrieval) → AI Agent (skills)
- Markdown = source of truth
- Human can always read & edit
- Hybrid search: vector + keyword + RRF

## Installation

Agent installation: paste `INSTALL_FOR_AGENTS.md` URL into agent. ~30 minutes.
Standalone CLI: `gbrain init` → ready in 2 seconds (PGLite, no server)
MCP server: 30+ tools via stdio

## GStack Integration

- GStack = coding skills (ship, review, QA)
- GBrain = brain ops (memory, ingestion, enrichment)
- Bridge: `hosts/gbrain.ts`


---

## Related Concepts
- [[hermes-agent-architecture]]
- [[gbrain-agent-brain]]
- [[memory-systems]]
