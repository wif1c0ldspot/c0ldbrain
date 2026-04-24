---
title: "The Missing Memory Hierarchy: Demand Paging for LLM Context"
type: source
tags: [memory-systems, research, context-engineering, arxiv, demand-paging]
created: '2026-04-19'
updated: '2026-04-19'
confidence: high
status: current
priority: high
summary: "ArXiv paper introducing Pichay — a demand paging system for LLM context windows. Maps agent memory to OS virtual memory concepts."
source_url: "https://arxiv.org/abs/2603.09023"
sources:
- arxiv-2603-09023
---

# The Missing Memory Hierarchy: Demand Paging for LLM Context

**Paper**: arxiv.org/abs/2603.09023
**Published**: March 2026
**Key Contribution**: First rigorous systems-level framing of agent memory management

## Core Insight

LLM context management maps structurally (not merely metaphorically) to **virtual memory** in operating systems:

| OS Concept | Agent Memory Equivalent |
|------------|------------------------|
| Physical RAM | Context window (limited, fast) |
| Disk/Storage | External memory store (vast, slower) |
| Demand paging | Load context pages only when needed |
| Working set | Subset of context actively being used |
| Eviction policy | What to drop when context fills up |
| Page fault | Retrieval call when needed context was evicted |

## The Pichay System

A transparent proxy between the agent and the LLM that:
- Manages context windows programmatically
- Implements working set tracking
- Supports multiple eviction policies (LRU, LFU, relevance-based)
- Handles "page faults" (retrieval calls) transparently

## Why This Matters

Every production agent system implicitly does demand paging. This paper makes it:
1. **Explicit** — named and formalized
2. **Rigorous** — borrowing decades of OS research
3. **Optimizable** — eviction policies can be tuned

## Camp Classification

**Camp 1.5 Hybrid**: Uses Camp 1 storage techniques but thinks in Camp 2 terms (what context should the agent work inside?). The systems-level framing bridges both camps.

## Related Concepts

- [[memory-systems]] — Hub for agent memory patterns
- [[context-substrate]] — Context-as-substrate paradigm
- [[context-compaction]] — Complementary technique

## Sources

- [ArXiv: The Missing Memory Hierarchy](https://arxiv.org/abs/2603.09023)
- [Hacker News Discussion](https://news.ycombinator.com/item?id=47458096)
- [Working Memory Compression Analysis](https://notes.muthu.co/2026/03/working-memory-compression-and-context-distillation-in-long-horizon-agents/)
