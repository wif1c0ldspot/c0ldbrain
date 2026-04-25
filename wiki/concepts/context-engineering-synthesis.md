---
title: "Context Engineering — Synthesis"
type: synthesis
tags: [context-engineering, ai-agents, memory, synthesis]
created: 2026-04-20
updated: 2026-04-20
confidence: high
status: current
priority: critical
summary: "Unified view of context engineering — from substrate to compaction to organizational synthesis. How agents build, maintain, and utilize context."
---

# Context Engineering — Synthesis

## What is Context Engineering?

Context engineering is the discipline of designing, managing, and optimizing the information environment that AI agents operate within. It has evolved from simple prompt engineering to complex multi-layer context architectures.

**Evolution:**
```
2020-2023: Prompt engineering (one-shot context)
    ↓
2023-2024: RAG + agentic retrieval (dynamic context)
    ↓
2025+: Context engineering (agent builds its own context)
```

## The Context Stack

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 4: Synthesis       │ Company brain, multi-source synthesis │
│  Layer 3: Compiled        │ Wiki concepts, structured knowledge   │
│  Layer 2: Retrieved       │ Vector search, document chunks        │
│  Layer 1: Working Memory  │ Context window, active session        │
│  Layer 0: Substrate       │ Hardware, KV cache, quantization      │
└─────────────────────────────────────────────────────────────┘
```

## Layer 0: Context Substrate

The hardware and software foundation for context management.

**Key Technologies:**
- **TurboQuant + MLX** — 256K KV cache with quantization on Apple Silicon
- **Flash-MoE** — Flash Attention + Mixture of Experts
- **GGUF/llama.cpp** — Local inference with extended context

**Pattern:** [[context-substrate]] — Hardware abstraction layer for context

## Layer 1: Working Memory

The immediate context window — what the model sees right now.

**Challenge:** Fixed-size window (4K-2M tokens depending on model)

**Management Techniques:**
- **Context compaction** — Summarization, compression, selective retention
- **Demand paging** — OS virtual memory analogy for context loading
- **Hierarchical attention** — Different attention patterns for different context depths

**Patterns:** [[context-compaction]], [[demand-paging-for-agent-memory]]

## Layer 2: Retrieved Context

Dynamic retrieval from external stores at query time.

**Technologies:**
- **Vector RAG** — Embeddings + similarity search
- **Vectorless RAG (PageIndex)** — Tree-structured indices, LLM reasoning
- **Graph RAG** — Knowledge graph traversal for multi-hop retrieval

**Tradeoff:** Flexibility vs coherence — chunks may lose context

## Layer 3: Compiled Context

Pre-processed, structured knowledge that agents maintain.

**Pattern:** LLM Wiki (Karpathy)
- LLM reads sources → writes encyclopedia-style articles
- Bidirectional wikilinks create navigable knowledge graph
- Compounding value — each query enriches the wiki

**Benefits:** Coherence, cross-references, human-readable

## Layer 4: Synthesized Context

Continuously updated, multi-source organizational understanding.

**Pattern:** Company Context Brain
- Resolves conflicts between sources
- Tracks entity identity across tools
- Monitors information decay
- Surfaces as filesystem for any agent to read

**Key insight:** Access ≠ Understanding. Retrieval finds; synthesis knows.

## The Two Camps

The field has bifurcated into two philosophical approaches:

### Camp 1: Maximize Context Window
**Belief:** Bigger context = better performance
**Approach:** Extend window to millions of tokens, fit everything
**Tools:** Long-context models (Claude 3, Gemini 1.5)

### Camp 2: Optimize Context Efficiency
**Belief:** Quality of context > quantity
**Approach:** Smart selection, compaction, synthesis
**Tools:** RAG, wikis, context graphs, demand paging

**Reality:** Most practical systems are **Camp 1.5** — extended windows with smart management.

## Context Engineering Discipline (April 2026)

Formalized as a discipline with five sub-fields:

| Sub-field | Focus |
|-----------|-------|
| Context Assembly | How context is gathered from sources |
| Context Compaction | How to fit more into limited windows |
| Context Retrieval | How to find relevant information |
| Context Governance | Security, privacy, access control |
| Context Evaluation | Measuring context quality |

**Sources:** Taskade Field Guide, Supermemory, ContextGraph, Swirl AI, Toolhalla

## Key Tradeoffs

| Approach | Pros | Cons |
|----------|------|------|
| Big context | Simple, no retrieval complexity | Expensive, attention dilution |
| RAG | Cheap, scalable | Fragmented, no synthesis |
| Wiki | Coherent, compounding | Expensive queries, maintenance |
| Synthesis | Always current, conflict-resolved | Complex, requires continuous operation |

## Practical Recommendations

1. **Start with Camp 1** — Use long-context models for simple cases
2. **Add Camp 2** — Layer RAG/wikis as complexity grows
3. **Synthesize** — For organizational context, build continuous synthesis
4. **Measure** — Track context quality, not just quantity

## Related
- [[weekly-synthesis-2026-04-20]] Concepts
- [[atant-benchmark-critique-2026-04]]
- [[cli-vs-mcp-debate]]
- [[context-constitution]]
- [[context-engineering]]
- [[context-management]]
- [[genericagent-contextual-density-2026-04]]
- [[hierarchical-memory-architectures]]
- [[mem0-v2-0-redesign-2026-04]]
- [[memmachine-multi-tier-memory-2026-04]]
- [[openviking-context-database]]
- [[openviking-context-database-volcengine-2026-04]]
- [[prompt-engineering]]
- [[context-engineering-handbook-2026]]

- [[context-substrate]] — Hardware/software foundation
- [[context-compaction]] — Working memory optimization
- [[demand-paging-for-agent-memory]] — OS memory analogy
- [[company-context-brain]] — Organizational synthesis
- [[llm-knowledge-bases]] — Compiled knowledge pattern
- [[vectorless-rag]] — Alternative retrieval
- [[knowledge-management-synthesis]] — Knowledge paradigms overview


## Context Engineering Goes Mainstream (Update 2026-04-21)

**HuggingFace published a context engineering course** (github.com/huggingface/context-course). This signals that context engineering is no longer a niche discipline — it's becoming a standard part of AI engineering education.

The course focuses on context engineering with code agents, aligning with the "agent builds its own context" paradigm from the 2025+ era.
