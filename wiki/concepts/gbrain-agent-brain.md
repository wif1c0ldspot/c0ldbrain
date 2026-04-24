---
title: "GBrain — Production Agent Brain Architecture"
type: concept
tags: [ai-agents, knowledge-management, agent-architecture, skills-pattern]
created: 2026-04-20
updated: 2026-04-20
confidence: high
status: current
priority: important
summary: "Garry Tan's production-grade agent brain for OpenClaw/Hermes. Hybrid search + self-wiring knowledge graph + 26 skills + durable job queue (Minions). 9.5k stars."
---

# GBrain — Production Agent Brain Architecture

## Overview

GBrain is Garry Tan's (Y Combinator CEO) production-grade AI agent brain for OpenClaw and Hermes deployments. Running at production scale: 17,888 pages, 4,383 people, 723 companies, 21 autonomous cron jobs, built in 12 days.

**Key insight:** "Your AI agent is smart but forgetful. GBrain gives it a brain."

## Architecture

```
┌──────────────────┐    ┌───────────────┐    ┌──────────────────┐
│   Brain Repo     │    │    GBrain     │    │    AI Agent      │
│   (git)          │    │  (retrieval)  │    │  (read/write)    │
│                  │    │               │    │                  │
│  markdown files  │───>│  Postgres +   │<──>│  26 skills       │
│  = source of     │    │  pgvector     │    │  define HOW to   │
│    truth         │    │               │    │  use the brain   │
│                  │<───│  hybrid       │    │                  │
│  human can       │    │  search       │    │  RESOLVER.md     │
│  always read     │    │  (vector +    │    │  routes intent   │
│  & edit          │    │   keyword +   │    │  to skill        │
│                  │    │   RRF)        │    │                  │
└──────────────────┘    └───────────────┘    └──────────────────┘
```

**Three pillars:**
1. **Brain Repo** (git) — Markdown = source of truth, human-readable, version-controlled
2. **GBrain** (retrieval) — Postgres + pgvector, hybrid search
3. **AI Agent** (skills) — 26 skills define how to use the brain

## Performance Benchmarks

| Metric | Baseline | GBrain | Improvement |
|--------|----------|--------|-------------|
| Recall@5 | 83% | 95% | +12 pts |
| Precision@5 | 39% | 45% | +6 pts (+30 correct answers in top-5) |
| Graph-only F1 | 57.8% (grep) | 86.6% | +28.8 pts |

## Self-Wiring Knowledge Graph

Typed links extracted on every write — **zero LLM calls:**
- `attended` — person attended meeting
- `works_at` — employment relationship
- `invested_in` — investment relationship
- `founded` — company founder
- `advises` — advisory role

**Entity enrichment tiers:**
- **Tier 3** (stub): 1 mention → basic page
- **Tier 2** (social): 3+ mentions across sources → web + social enrichment
- **Tier 1** (full): Meeting or 8+ mentions → full pipeline

Auto-escalation: brain learns who matters without being told.

## The 26 Skills

### Always-On
| Skill | Purpose |
|-------|---------|
| **signal-detector** | Fires on every message. Parallel cheap model for entity capture |
| **brain-ops** | Brain-first lookup before external APIs |

### Content Ingestion
| Skill | Purpose |
|-------|---------|
| **ingest** | Thin router, detects input type |
| **idea-ingest** | Links/articles/tweets → brain pages |
| **media-ingest** | Video/audio/PDF/books/screenshots |
| **meeting-ingestion** | Transcripts → pages + attendee enrichment |

### Brain Operations
| Skill | Purpose |
|-------|---------|
| **enrich** | Tiered enrichment (Tier 1/2/3) |
| **query** | 3-layer search with synthesis and citations |
| **maintain** | Health: stale pages, orphans, dead links |
| **citation-fixer** | Scan/fix citation format |
| **repo-architecture** | Decision protocol: subject → directory |
| **publish** | Share as password-protected HTML |
| **data-research** | Structured data extraction via YAML recipes |

### Operational
| Skill | Purpose |
|-------|---------|
| **daily-task-manager** | Task lifecycle P0-P3 |
| **daily-task-prep** | Morning calendar + brain context |
| **cron-scheduler** | Schedule staggering, quiet hours |
| **reports** | Timestamped reports with keyword routing |
| **cross-modal-review** | Quality gate via second model |
| **webhook-transforms** | External events → brain pages |
| **skill-creator** | Create new skills with conformance |
| **minion-orchestrator** | Durable Postgres job queue |

### Identity & Setup
| Skill | Purpose |
|-------|---------|
| **soul-audit** | 6-phase interview → SOUL.md, USER.md, ACCESS_POLICY.md |
| **setup** | Auto-provision PGLite or Supabase |
| **migrate** | Universal migration from Obsidian, Notion, Logseq |
| **briefing** | Daily briefing with meeting context |

## Minions: Durable Job Queue

Postgres-native job queue for deterministic background work.

| Dimension | Minions | Sub-agents |
|-----------|---------|------------|
| Wall time | **753ms** | >10,000ms (timeout) |
| Token cost | **$0.00** | ~$0.03/run |
| Success rate | **100%** | 0% (couldn't spawn) |
| Memory/job | ~2 MB | ~80 MB |

**Routing rule:**
- **Deterministic** (same input → same steps) → Minions
- **Judgment** (requires assessment) → Sub-agents

Features: SIGKILL resilient, cascade cancel, fan-out, parent-child DAGs, progress streaming.

## Skillify: Skill Quality Control

10-item skill completeness checklist:
1. SKILL.md (contract)
2. Deterministic script
3. Unit tests
4. Integration tests
5. LLM evals
6. Resolver trigger
7. Resolver trigger eval
8. E2E smoke
9. Brain filing
10. Manifest coverage

**Key insight:** "Auto-generated skills are a liability the first time a behavior breaks. Skillify makes the black box legible."

## GStack Integration

- **GStack** = coding skills (ship, review, QA, investigate) — 70k+ stars
- **GBrain** = brain ops (memory, ingestion, enrichment)
- **Bridge**: `hosts/gbrain.ts` tells coding skills to check the brain first

## Installation

**Agent (recommended):** Paste `INSTALL_FOR_AGENTS.md` URL → agent clones, installs, configures. ~30 minutes.

**Standalone CLI:**
```bash
gbrain init          # PGLite, ready in 2 seconds
gbrain import ~/notes/
gbrain query "what themes show up?"
```

**MCP server:** 30+ tools via stdio for Claude Code, Cursor, Windsurf.

## Comparison to C0ldbrain

| Aspect | GBrain | C0ldbrain |
|--------|--------|-----------|
| Scale | 17,888 pages, production | ~200+ concepts, growing |
| Search | Hybrid (vector + keyword + RRF) | Semantic (MemPalace) |
| Graph | Self-wiring, typed links | Bidirectional wikilinks |
| Skills | 26 skills with Skillify | ~100+ skills |
| Job queue | Minions (Postgres) | Cron jobs |
| Installation | 30 min auto | Manual setup |

## Related
- [[gbrain-garrytan-ayi-ainotes-2026-04]] Concepts

- [[knowledge-management-synthesis]] — Paradigm comparison
- [[llm-knowledge-bases]] — LLM wiki pattern
- [[knowledge-layer]] — Two-layer architecture
- [[skills-pattern]] — Skills-based agent design
- [[hermes-agent-architecture]] — Hermes agent design
- [[mcp-protocol]] — MCP tool integration
- [[karpathy]] — Original LLM wiki inspiration
