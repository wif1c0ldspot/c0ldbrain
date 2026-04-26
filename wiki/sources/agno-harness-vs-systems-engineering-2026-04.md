---
title: "Harness Engineering vs. Systems Engineering: The Mistake Killing Agentic Software"
type: source
tags: [ai-agents, systems-engineering, agent-architecture, harness-engineering, source]
created: '2026-04-26'
updated: '2026-04-26'
confidence: high
status: current
priority: important
summary: "Agno argues most 'AI engineers' are harness engineers optimizing tools, not systems. Agentic software needs the same 5 layers as regular software. Stop debating tools, start designing systems."
source_url: https://www.agno.com/blog/harness-engineering-vs-systems-engineering-the-mistake-killing-agentic-software
compiled: true
---

# Harness Engineering vs. Systems Engineering: The Mistake Killing Agentic Software

**Author:** Cosette Cressler (Agno)
**Published:** April 14, 2026
**Source:** [Agno Blog](https://www.agno.com/blog/harness-engineering-vs-systems-engineering-the-mistake-killing-agentic-software) | [X Post by @Suryanshti777](https://x.com/suryanshti777/status/2048055574185779638)

## Core Argument

Most "AI engineers" are **harness engineers** — they optimize the tool (model, prompt, framework) instead of optimizing for the outcome (the system). This produces duct-taped systems where each tool limitation becomes another patch.

**Harness engineer** optimizes the tool. **Systems engineer** optimizes for the outcome.

## The Harness-First Trap

Agent frameworks encourage:
- Filesystem for storage (can't isolate users)
- Broad bash access (security risk)
- Framework-specific boilerplate (locks in unconscious architectural decisions)

Each limitation forces a patch: database abstraction on filesystem, sandboxes on bash access. The harness grows more complex while the underlying system stays flawed.

## Systems Thinking Applied

The Bell Labs lesson (1940s): **optimizing individual parts does not produce an optimized system.** Call routing, reliability, capacity emerge from interactions.

Agentic software = regular software + agents as business logic. Same 5 layers apply:
- [[agent-architecture|Agent logic]] — deterministic where possible, observable where not
- [[rag|Data]] — proper databases, not filesystems
- [[ai-security|Security]] — in tool config, not prompts
- [[mcp-protocol|Interfaces]] — consistent auth across all surfaces
- [[agent-infrastructure|Infrastructure]] — standard DevOps + agent-specific tweaks

## Concrete Implications

| Area | Harness Approach | Systems Approach |
|------|-----------------|-----------------|
| Storage | Filesystem-backed memory | Database with user isolation |
| Security | "Don't write" in prompt | Read-only PostgreSQL connection |
| Interfaces | One surface, hard-coded | Multi-surface, consistent auth |
| Tools | Broad bash access | Well-scoped, permissioned tools |

## Key Quotes

> "Getting something running is not the same as having software that works—and the gap between the two is where production systems tend to fail."

> "Debates like MCP vs. CLI or REST vs. gRPC feel technical, but they're actually theological — arguments about which harness is holier."

> "You are not building a harness. You are building a system. Act like it."

## Related

- [[ashpreet-bedi-systems-engineering-agentic-2026-04]] — Companion piece by Ashpreet Bedi on same topic
- [[systems-engineering]] — Concept page on systems engineering for agentic software
- [[agent-architecture]] — Agent design patterns
- [[ai-security]] — Security for AI systems
