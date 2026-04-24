---
title: GBrain — Garry Tan's Agent Brain System
author: '@AYi_AInotes (link), Garry Tan (creator)'
date: 2026-04-20
source: https://github.com/garrytan/gbrain
tags:
- source
- ai-agents
- knowledge-management
- agent-architecture
type: source
priority: important
updated: '2026-04-24'
created: '2026-04-24'
confidence: high
status: current
summary: Auto-generated placeholder for GBrain — Garry Tan's Agent Brain System
compiled: true
---

## Summary

GBrain is Garry Tan's (Y Combinator CEO) production-grade AI agent brain for OpenClaw/Hermes. 17,888 pages, 4,383 people, 723 companies, 21 autonomous cron jobs, built in 12 days. Hybrid search + self-wiring knowledge graph. Recall@5: 95%, Graph-only F1: 86.6%. 26 skills including signal detection, brain-first lookups, tiered enrichment, and a durable Postgres job queue (Minions).

## Key Points

- **Production scale**: 17,888 pages, 4,383 people, 723 companies, 21 cron jobs
- **Self-wiring graph**: Typed links extracted on every write (zero LLM calls)
- **Hybrid search**: Vector + keyword + Reciprocal Rank Fusion
- **Benchmarks**: Recall@5 83%→95%, Precision@5 39%→45%, Graph F1 86.6%
- **26 skills**: signal-detector, brain-ops, ingest, enrich, query, maintain, minions, skillify
- **Minions**: Postgres-native job queue — 753ms, $0 tokens, 100% success, SIGKILL resilient
- **Skillify**: 10-item skill completeness checklist (SKILL.md + tests + evals + resolver)
- **Installation**: ~30 minutes via agent, 2 seconds standalone
- **MCP**: 30+ tools via stdio

## Filing Decision

Filed under AI Agents & Architecture per RESOLVER.md. Flat structure. Concept: `gbrain-agent-brain.md`.
