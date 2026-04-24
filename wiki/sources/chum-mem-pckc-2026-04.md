---
title: "chum-mem — PCKC Proof-Carrying Knowledge Compiler"
type: source
tags: [memory-systems, knowledge-graphs, agent-memory, pckc, claim-based-memory]
created: 2026-04-21
updated: 2026-04-21
confidence: high
status: current
url: https://github.com/sly-codechum/chum-mem
stars: 29
language: Rust
---

# chum-mem — Proof-Carrying Knowledge Compiler

Better memory for AI agents. (Karpathy + Graphify + PCKC)

## The PCKC Model

Redefines three units of AI memory:

| Unit | Standard RAG | PCKC |
|------|-------------|------|
| **Memory** | Text chunks / summaries | **Claim** — atomic typed assertion |
| **Trust** | "Source: file X" | **Proof** — structured evidence with authority classification |
| **Context** | Top-K similar text | **Compiled minimal proof set** — smallest set of current-valid claims |

## Claim Types

Memory units are typed **claims**: `fact`, `decision`, `task`, `constraint`, `bug`, `fix`, `implementation_detail`, `open_question`

## Authority Classification

Each claim carries **proof** with:
- `authority_class`: tool_verified, user_confirmed, repository_derived, session_derived, model_inferred
- `verification_status`: verified, unverified, refuted, superseded
- `proof_type`, `source_ref`, `excerpt`

## Belief Gate

**Model-generated prose is NOT durable memory.** The belief gate enforces this:
- `Reasoning` and `TurnContext` events are hard-rejected before text analysis
- `AgentMessage` goes through standard classifier — rejected unless user-confirmed
- Only four authority classes survive: `tool_verified`, `user_confirmed`, `repository_derived`, `test_verified`
- Benchmark-verified: 0 reasoning leaks, 0 model-derived durable claims

## Supersession and Contradiction

Claims are not append-only:
- **Contradiction engine** — links conflicting claims with `contradicts` edges
- **Supersession engine** — creates `supersedes` edges when higher-authority claims replace older ones
- Retrieval respects temporal validity: past `valid_to` or `superseded_by` hidden by default

## Three-Way Hybrid Search

Retrieval merges three signals:
1. Vector similarity (semantic)
2. FTS5 keyword matching (structural)
3. Graph traversal (relational)

## Camp Classification

**Camp 1 Enhanced** — Memory backend with strong truth-filtering. The authority model and belief gate add a "trust layer" to Camp 1 systems.

## Related Concepts

- [[memory-systems]] — broader landscape
- [[knowledge-graphs]] — graph-based memory
- [[memory-firewall]] — security filtering on memory writes
- [[context-compaction]] — storing less but higher quality
