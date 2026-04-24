---
title: "Claim-Based Memory"
type: concept
tags: [memory-systems, knowledge-graphs, agent-memory, claim-based, pckc]
created: 2026-04-21
updated: 2026-04-21
confidence: high
status: current
priority: high
summary: "Memory as typed claims with authority-based proofs instead of text summaries. Enables truth-filtering, contradiction detection, and temporal validity."
sources:
- chum-mem-pckc-2026-04
- cavemem-cross-agent-memory-2026-04
---

# Claim-Based Memory

## Definition

A memory architecture where each stored unit is an **atomic typed claim** carrying structured proof, rather than a text summary or embedding vector. This shifts the memory primitive from "what was said" to "what is true."

## The Problem It Solves

Traditional agent memory systems suffer from:
- **Hallucination pollution** — model-generated text stored alongside verified facts
- **Staleness** — old information persists without supersession tracking
- **Contradiction ambiguity** — conflicting information averaged rather than resolved
- **Authority blindness** — no distinction between user-confirmed facts and model inference

## The PCKC Model (chum-mem)

### Claim Types
`fact`, `decision`, `task`, `constraint`, `bug`, `fix`, `implementation_detail`, `open_question`

### Authority Classes
| Class | Source | Trust Level |
|-------|--------|-------------|
| `tool_verified` | Test results, command output | High |
| `user_confirmed` | User explicitly stated | High |
| `repository_derived` | Source code analysis | Medium |
| `test_verified` | Test suite outcomes | High |
| `session_derived` | Conversation context | Low |
| `model_inferred` | LLM reasoning | Lowest |

### Belief Gate
**Model-generated prose is NOT durable memory.** The belief gate enforces write-time filtering:
- `Reasoning` and `TurnContext` events are hard-rejected
- Only `tool_verified`, `user_confirmed`, `repository_derived`, `test_verified` survive
- Benchmark-verified: 0 reasoning leaks

### Supersession Engine
- Claims are not append-only
- Contradiction engine links conflicts with `contradicts` edges
- Supersession engine creates `supersedes` edges when higher-authority claims replace older ones
- Retrieval respects temporal validity: past `valid_to` hidden by default

## Compression Variant (cavemem)

An alternative approach: compress everything but preserve code/paths:
- Caveman grammar: ~75% fewer tokens
- Round-trip-guaranteed expansion
- Code blocks, URLs, paths, identifiers never touched

## Comparison

| Approach | Write Cost | Read Cost | Truth Quality | Storage |
|----------|-----------|-----------|---------------|---------|
| Summary-based | Low | Low | Low | Small |
| Embedding-based | Medium | Low | Medium | Medium |
| Claim-based (PCKC) | High | Medium | High | Medium |
| Compressed (cavemem) | Medium | Medium | Unknown | Small |

## Integration Potential

For [[mempalace]]:
- Add `authority_class` field to knowledge graph facts
- Implement belief gate for drawer writes
- Add supersession tracking to KG relationships

## Related Concepts

- [[memory-systems]] — broader landscape
- [[knowledge-graphs]] — graph-based claim storage
- [[memory-firewall]] — security filtering on writes
- [[context-compaction]] — storing less but higher quality
- [[demand-paging-for-agent-memory]] — lazy claim retrieval
