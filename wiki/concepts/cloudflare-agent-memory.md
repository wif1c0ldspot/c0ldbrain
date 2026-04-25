---
title: Cloudflare Agent Memory
type: concept
tags:
- agent-memory
- context-engineering
- cloudflare
- infrastructure
- camp-2
created: 2026-04-22
updated: 2026-04-22
confidence: high
status: current
priority: important
summary: Cloudflare's managed Agent Memory service — infrastructure-grade memory with
  multi-channel retrieval, compaction lifecycle, and SOC 2 Type 2 certification
---

# Cloudflare Agent Memory

## Overview

Cloudflare entered the agent memory market (April 17, 2026) with a managed service built on Durable Objects + Vectorize + Workers AI. This is significant as the first major infrastructure provider offering agent memory as a managed service.

## Architecture

### Multi-Stage Pipeline
1. **Deterministic ID generation** — stable identifiers across sessions
2. **Parallel extraction** — full pass + detail pass simultaneously
3. **Verification** — 8-check pipeline for data quality
4. **Classification** — facts / events / instructions / tasks
5. **Supersession chains** — temporal validity tracking
6. **5-channel parallel retrieval**:
   - FTS (full-text search)
   - Fact-key lookup
   - Raw message retrieval
   - Direct vector search
   - HyDE (Hypothetical Document Embedding) vector search
7. **RRF fusion** — Reciprocal Rank Fusion of all channels
8. **Synthesis** — final context assembly

### Models Used
- Llama 4 Scout for extraction/classification
- Nemotron 3 for synthesis

### Infrastructure
- Built on Cloudflare's Durable Objects + Vectorize + Workers AI
- Designed around context compaction lifecycle
- Explicitly designed to NOT give agents raw filesystem access

## Camp Classification

**Camp 2 (Context Substrate)** — Cloudflare's approach is fundamentally about context lifecycle management during compaction. Memory is a service that preserves knowledge when context is pruned, then surfaces it on demand. Their opinionated API deliberately keeps storage strategy out of the agent's context.

## Why It Matters

1. First **major cloud provider** offering agent memory as managed infrastructure
2. Brings **SOC 2 Type 2** and **HIPAA-ready** compliance to agent memory
3. **5-channel retrieval with RRF fusion** is the most sophisticated retrieval pipeline seen in a production memory service
4. Positions memory as a **cloud primitive** alongside compute and storage

## Related Concepts

- [[context-compaction]] — Cloudflare's design centers on compaction lifecycle
- [[context-substrate]] — Cloudflare is squarely in the substrate camp
- [[memory-systems]] — broader memory system landscape
- [[harness-design]] — memory as part of agent harness architecture

## Sources

- [Cloudflare Blog: Introducing Agent Memory](https://blog.cloudflare.com/introducing-agent-memory/) (2026-04-17)

- [[cloudflare-agent-memory]]
- [[context-engineering-handbook-2026]]
- [[infrastructure-handbook-2026]]