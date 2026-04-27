---
title: "Memory in Claude Managed Agents"
type: source
tags: [ai-agents, memory-systems, claude, agentic-ai, source]
created: '2026-04-27'
updated: '2026-04-27'
confidence: high
status: current
priority: important
summary: "Anthropic's Claude Managed Agents now uses filesystem-based memory stores — files persisted across sessions, synced between agents in real time."
source_url: https://x.com/rlancemartin/status/2047720067107033525
compiled: true
author: Lance Martin (@RLanceMartin)
engagement: "368 likes, 49 retweets, 115K views, 855 bookmarks"
---

# Memory in Claude Managed Agents

**Author:** Lance Martin (@RLanceMartin)
**Date:** 2026-04-24
**Platform:** X Article

## Key Points

- **Filesystem as memory:** Claude Managed Agents stores memories as files in `/mnt/memory/<store-name>/`, persisted across sessions via "memory stores"
- **Scaling intelligence improves memory:** Sonnet 3.5 treated memory as transcript (31 files, stuck in town). Opus 4.6 self-organized into directories with distilled learnings (3 gym badges)
- **General tools > specialized memory harnesses:** Filesystem approach outperforms custom memory tooling — @Letta_AI confirmed independently
- **Real-time multi-agent sync:** Multiple agents share same memory store with concurrency handling
- **Session log + memory store = context model:** Two-part context architecture — session log for current task, memory store for cross-session persistence

## Architecture

```
Session Container
├── Session Log (task context, lives outside context window)
└── /mnt/memory/<store-name>/ (persisted files)
    ├── Agent-organized directories
    ├── Learning files
    └── Export-friendly plain text
```

## Referenced Work

- CoALA paper (Sumers et al.) — cognitive science + OS model for agent memory
- memGPT (Wooders, Packer) — OS-inspired memory management
- Claude Plays Pokémon (Hershey) — filesystem memory evolution from Sonnet 3.5 → Opus 4.6
- Letta AI — filesystem vs specialized memory tools benchmark

## Connections

- [[memory-systems]] — broader landscape of AI memory approaches
- [[agentic-memory-research]] — research field overview
- [[claude-code]] — Anthropic's production agent harness
- [[agent-architecture]] — structural patterns for agent memory
- [[demand-paging-for-agent-memory]] — context window management patterns
