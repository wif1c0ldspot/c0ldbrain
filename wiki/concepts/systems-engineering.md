---
title: Systems Engineering
type: concept
tags: [systems-engineering, agent-architecture, infrastructure, ai-agents]
created: '2026-04-26'
updated: '2026-04-26'
confidence: high
status: current
priority: important
summary: "Discipline of designing systems where behavior emerges from component interactions, not individual optimization. Originated at Bell Labs (1940s). Applied to agentic software as 5 layers."
---

# Systems Engineering

Systems engineering is the discipline of making parts work together. Originated at Bell Labs in the 1940s when engineers realized you can't optimize a system by optimizing individual components — behavior emerges from interactions.

## Core Principle

The behavior of the whole (routing, reliability, capacity, cost) emerges from how parts interact. This is true whether you're building telephone networks or agentic software.

## Five Layers of Agentic Software

| Layer | Concern | Key Pattern |
|-------|---------|-------------|
| Agent Engineering | Execution flow, tools, context, observability | Deterministic where possible, observable where not |
| Data Engineering | Context as data, schemas, storage, knowledge | Decades-old data patterns applied to agent memory |
| Security Engineering | Auth, RBAC, isolation, audit trails | Permissions in tool config, not prompts |
| Interface Engineering | Multi-surface identity, consistent access controls | Same agents across all surfaces |
| Infrastructure Engineering | Containers, scaling, deployment, streaming | 95% standard DevOps, 5% agent-specific |

## Key Insights

1. **Agentic software is regular software** with business logic replaced by agents, interfaces going from request/response to streaming across multiple surfaces
2. **Design layers together** — isolation creates cascading constraints
3. **Security is a system property** tested across layers, not bolted onto one
4. **Data compounds** — query 100 > query 1 because the data layer improved, not the model

## Related Concepts

- [[agent-architecture]] — Agent design patterns
- [[multi-agent-collaboration]] — Multi-agent coordination
- [[ai-security]] — Security for AI systems
- [[mcp-protocol]] — Tool communication protocol
- [[agent-infrastructure]] — Running agents in production
- [[ashpreet-bedi-systems-engineering-agentic-2026-04]] — Source article

## Harness Engineering (Anti-Pattern)

The opposite of systems engineering. Harness engineers optimize tools (model, prompt, framework) instead of outcomes. Symptoms:
- Filesystem-backed memory instead of databases
- Broad bash access instead of scoped tools
- Security via prompt instructions instead of tool configuration
- Framework boilerplate that locks in unconscious decisions

Each tool limitation becomes another patch. The harness grows complex while the system stays flawed.

See [[agno-harness-vs-systems-engineering-2026-04]] for the full argument.

## Sources

- [[anthropic-adk-4layer-multiagent-framework-cyrilxbt-2026-04]] — ADK 4-layer framework (production systems engineering)

- [[ashpreet-bedi-systems-engineering-agentic-2026-04]] — Ashpreet Bedi, April 2026
- [[agno-harness-vs-systems-engineering-2026-04]] — Cosette Cressler (Agno), April 2026

- [[harness-engineering]]