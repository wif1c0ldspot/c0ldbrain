---
title: "Resolvers: The Routing Table for Intelligence"
type: source
tags:
- ai-agents
- agent-architecture
- resolvers
- source
- x
source_url: https://x.com/garrytan/status/2044479509874020852
sources:
- agent-resolvers
created: '2026-04-15'
updated: '2026-04-17'
confidence: high
status: current
agents:
- hermes
priority: important
summary: "Garry Tan's article on resolvers as the routing table for agent intelligence - replacing 20,000 lines of context with 200 lines of routing logic."
---

# Resolvers: The Routing Table for Intelligence

**Author:** Garry Tan (@garrytan)  
**Published:** 2026-04-15  
**Engagement:** 41 replies, 122 reposts, 914 likes, 2.5K bookmarks, 189.9K views

## Summary

A resolver is a routing table for context. When task type X appears, load document Y first. This single pattern replaced 20,000 lines of crammed context with 200 lines of routing logic, dramatically improving agent performance.

## Key Insights

### The Problem: Context Drowning
- Garry's CLAUDE.md was 20,000 lines of accumulated patterns, quirks, and conventions
- Model attention degraded; responses got slower and less precise
- Claude Code itself advised cutting it back
- The fix: 200 lines of numbered decision tree with pointers to documents

### Three Layers of Resolvers
1. **Skill Resolver (AGENTS.md)** - maps task types to skill files
2. **Filing Resolver (RESOLVER.md)** - maps content types to directories
3. **Context Resolver** - sub-routing within each skill

### The Invisible Skill Problem
- Only 3 out of 13 brain-writing skills referenced the resolver
- 10 had hardcoded paths leading to misfiling
- Created `check-resolvable` meta-skill to find unreachable capabilities
- First run found 6 unreachable skills (15% of capabilities were "dark")

### Context Rot
- Resolvers decay over time (Day 1: perfect → Day 90: historical document)
- Skills get built by sub-agents but resolver doesn't get updated
- Solution: Trigger evals (test suite of 50 sample inputs with expected outputs)
- Future: RLM (reinforcement learning model) to auto-rewrite resolver based on traffic

### Resolver Pattern Checklist
- Load right context at right moment (don't cram)
- Mandate every skill consults the resolver
- Test routing, not just output (trigger evals)
- Audit reachability weekly (check-resolvable)
- Make resolver learn from its own traffic (endgame)

## Resources Mentioned
- **GBrain:** github.com/garrytan/gbrain (open-sourced resolver pattern)
- **GStack:** github.com/garrytan/gstack (fat skills in markdown)
- **OpenClaw/Hermes Agent:** The conductor/harness layer

## Related Concepts
- [[agent-meta-optimization]]
- [[ai-coding-agents]]
- [[memory-systems]]
- [[skill-registry]]
- [[karpathy-llm-wiki-agent]]
