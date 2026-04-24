---
title: Honcho
type: concept
tags:
- memory-systems
- ai-agents
- knowledge-management
- hermes
sources:
- honcho-hermes-lcm-stack-bayendor-2026-04
updated: 2026-04-22
confidence: high
status: current
priority: important
summary: Open-source persistent memory and user-modeling layer for AI agents. Dual-peer
  architecture (user peer + AI peer) with hybrid recall, async writeback, and cross-session
  continuity. Not a chat buffer — a structured memory system.
created: '2026-04-24'
---

# Honcho

## What It Is

Honcho is an open-source persistent memory and user-modeling layer for AI agents. It sits between the agent execution layer and the user, providing structured, durable memory that survives across sessions.

Unlike temporary chat buffers or simple message history, Honcho is designed as a **memory system** that actively learns and writes back stable facts.

## Key Features

### Dual-Peer Architecture

Honcho models both sides of the agent-user relationship:

| Peer | What It Learns |
|------|---------------|
| **User peer** | Preferences, goals, communication style |
| **AI peer** | Agent's own knowledge representation |

This means the system tracks both who it is talking to and what the agent itself has learned.

### Core Capabilities

1. **Prompt-time context injection** — Relevant memory injected at inference time
2. **Cross-session continuity** — Memory persists between conversations
3. **Durable writeback** — Agent learnings are written back to memory store

### Configuration (Production Setup)

| Setting | Value | Purpose |
|---------|-------|---------|
| baseUrl | http://localhost:8000 | Self-hosted endpoint |
| recallMode | hybrid | Combines multiple retrieval strategies |
| writeFrequency | async | Non-blocking memory writes |
| sessionStrategy | per-directory | Context scoped by working directory |
| dialecticReasoningLevel | low | Minimal dialectic overhead |
| dialecticDynamic | true | Adaptive reasoning adjustment |
| messageMaxChars | 25000 | Large context window per message |

## How It Works

```
User Input
   ↓
Hermes Agent (execution)
   ↓
Honcho Memory Layer
   ├── Injects relevant context from user peer
   ├── Injects agent knowledge from AI peer
   └── Writes back new facts asynchronously
   ↓
Response
```

## How It Differs

| Approach | What It Is | Limitation |
|----------|-----------|------------|
| Chat history | Message list | Forgetful, no synthesis |
| RAG | Document retrieval | Static, no user model |
| **Honcho** | Dual-peer memory system | Requires integration layer |

## Applications

- **Agent continuity**: User preferences persist across sessions
- **Team contexts**: Different memory per project/directory
- **Self-improving agents**: AI peer accumulates operational knowledge
- **Production deployments**: Observable, measurable memory layer

## Challenges

- Requires self-hosted infrastructure (no managed SaaS mentioned)
- Async writeback means temporary inconsistency windows
- 25k message limit may constrain very large context operations
- Integration burden: must wire into agent harness manually

## Key Quotes

> "Honcho is not a temporary chat buffer. It is the layer that remembers what should still matter later."

> "That means the system can keep track of both who it is talking to and what the agent itself has learned."

## Related Concepts

- [[hermes-lcm|related]] — Measurement and control layer that pairs with Honcho
- [[hermes-agent-architecture|depends-on]] — Execution layer Honcho integrates with
- [[memory-systems|extends]] — Broader memory system taxonomy
- [[cognee|related]] — Graph-vector hybrid memory alternative
- [[mempalace|related]] — Hierarchical memory palace approach
- [[context-substrate|related]] — Camp 2 context engineering alternative

## Sources

- [[honcho-hermes-lcm-stack-bayendor-2026-04]] — Production stack walkthrough by david bayendor
- https://github.com/plastic-labs/honcho
