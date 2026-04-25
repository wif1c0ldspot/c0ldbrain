---
title: Demand Paging for Agent Memory
type: concept
tags:
- memory-systems
- context-engineering
- agent-architecture
- systems-design
created: '2026-04-19'
updated: '2026-04-19'
confidence: medium
status: emerging
priority: important
summary: Reframing agent memory management through OS virtual memory concepts — demand
  paging, working sets, eviction policies.
sources:
- missing-memory-hierarchy-arxiv-2026-04
---

# Demand Paging for Agent Memory

## Overview

An emerging paradigm that maps LLM context management to **operating system virtual memory** concepts. First rigorously formalized in "The Missing Memory Hierarchy" (ArXiv 2603.09023, March 2026).

## Core Analogy

| OS Concept | Agent Memory Equivalent |
|------------|------------------------|
| Physical RAM | Context window (limited, fast) |
| Disk/Storage | External memory store (vast, slower) |
| Demand paging | Load context pages only when needed |
| Working set | Subset of context actively being used |
| Eviction policy | What to drop when context fills up (LRU, LFU, relevance) |
| Page fault | Retrieval call when needed context was evicted |

## Implementation: Pichay

A transparent proxy between the agent and the LLM:
- Manages context windows programmatically
- Implements working set tracking
- Supports multiple eviction policies
- Handles "page faults" (retrieval calls) transparently

## Why This Matters

Every production agent system implicitly does demand paging. This framing makes it:
1. **Explicit** — named and formalized
2. **Rigorous** — borrowing decades of OS research
3. **Optimizable** — eviction policies can be tuned per workload

## Camp Classification

**Camp 1.5 Hybrid**: Uses Camp 1 storage techniques but thinks in Camp 2 terms (what context should the agent work inside?).

## Related Concepts

- [[memory-systems]] — Hub for agent memory patterns
- [[context-substrate]] — Context-as-substrate paradigm
- [[context-compaction]] — Complementary compression technique
- [[cloudflare-agent-memory-2026-04]] — Enterprise implementation

## Open Questions

- What eviction policies work best for different agent workloads?
- How does this interact with context compaction?
- Can working set prediction improve retrieval latency?

- [[cavemem-cross-agent-memory-2026-04]]
- [[claim-based-memory]]
- [[context-engineering]]
- [[context-engineering-synthesis]]
- [[daily-research-agentic-memory-2026-04-19]]
- [[hierarchical-memory-architectures]]
- [[higmem-acl-2026-2026-04]]
- [[memmachine-multi-tier-memory-2026-04]]
- [[memory-firewall]]
- [[memory-worth-governance-2026-04]]