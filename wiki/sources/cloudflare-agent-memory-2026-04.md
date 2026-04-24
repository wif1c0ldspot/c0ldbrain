---
title: "Cloudflare Agent Memory (Private Beta)"
type: source
tags: [memory-systems, context-engineering, cloudflare, agent-infrastructure, enterprise]
created: '2026-04-19'
updated: '2026-04-19'
confidence: high
status: current
priority: high
summary: "Cloudflare announces Agent Memory — a managed service for persistent agent memory with ingest/remember/recall/list/forget API. Private beta, April 2026."
source_url: "https://blog.cloudflare.com/introducing-agent-memory/"
sources:
- cloudflare-agent-memory-2026-04
---

# Cloudflare Agent Memory (Private Beta)

**Announced**: April 17-18, 2026 (Cloudflare Agents Week)
**Status**: Private Beta
**Access**: Workers binding + REST API

## What It Is

A managed service that extracts information from agent conversations and makes it available when needed — without filling up the context window.

## API Operations

| Operation | Description |
|-----------|-------------|
| `ingest` | Bulk process a conversation to extract memories |
| `remember` | Explicitly store something important |
| `recall` | Retrieve relevant memories for current context |
| `list` | See what memories are stored |
| `forget` | Mark a memory as no longer important or true |

## Design Philosophy

Cloudflare's approach is **opinionated**:
- No raw filesystem access — structured profiles addressed by name
- Retrieval-first: optimized for recall during conversation, not storage
- Managed infrastructure — no self-hosting required
- Integrated with Workers ecosystem (but REST API for external use)

## Why It Matters

- **Enterprise validation**: Cloudflare entering this space confirms agent memory as critical infrastructure
- **Opinionated API**: The ingest/remember/recall/list/forget pattern may become a de facto standard
- **Managed service model**: Competes with Mem0, Zep on convenience — differentiator is Cloudflare's edge network

## Camp Classification

**Hybrid (Camp 1 + Camp 2)**: Uses Camp 1 storage techniques (extract, store, retrieve) but with Camp 2 philosophy (structured profiles, not raw facts). The "forget" operation is particularly notable — Camp 1 systems rarely support memory deletion.

## Related Concepts

- [[memory-systems]] — Hub for agent memory patterns
- [[context-substrate]] — Camp 2 paradigm this complements
- [[context-engineering]] — The broader discipline

## Sources

- [Cloudflare Blog: Introducing Agent Memory](https://blog.cloudflare.com/introducing-agent-memory/)
- [The Register: Cloudflare can remember it for you wholesale](https://www.theregister.com/2026/04/18/cloudflare_agent_memory/)
- [Cloudflare Docs: Memory](https://developers.cloudflare.com/agents/concepts/memory/)
