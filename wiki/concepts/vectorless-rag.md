---
title: Vectorless RAG & Reasoning-Based Retrieval
type: concept
tags: [rag, knowledge-management, ml-models, benchmarking]
sources: [pageindex-vectorless-rag-2026-04]
created: '2026-04-15'
updated: '2026-04-15'
confidence: high
status: current
priority: important
summary: RAG without vector embeddings. Uses LLM reasoning over structured indices (trees, graphs) to retrieve information. PageIndex achieves 98.7% FinanceBench accuracy.
---

# Vectorless RAG & Reasoning-Based Retrieval

## Summary

An emerging paradigm that replaces vector embeddings and similarity search with LLM reasoning over structured document indices. Achieves higher accuracy than traditional RAG by leveraging the LLM's own reasoning capability to navigate document structure.

## Core Idea

Traditional RAG: chunk documents → embed chunks → similarity search → retrieve top-k → pass to LLM

Vectorless RAG: structure documents into tree/graph → LLM reasons through structure → retrieves precise information

The key insight: instead of using embeddings as an approximate retrieval layer, let the LLM itself decide where information lives by navigating a structured index.

## PageIndex (25.2k stars)

The leading implementation of vectorless RAG:
- Tree-structured document index with hierarchical navigation
- LLM performs multi-step reasoning at each tree level to prune branches
- 98.7% accuracy on FinanceBench (financial document QA)
- No vector database, no embeddings pipeline, no similarity search
- API-compatible with existing RAG systems for easy migration

## Advantages Over Vector RAG

| Feature | Vector RAG | Vectorless RAG |
|---------|-----------|----------------|
| Infrastructure | Vector DB + embedding model | Just structured index |
| Accuracy | Chunk boundary artifacts | Full document reasoning |
| Numerical QA | Weak (embedding loss) | Strong (reasoning-based) |
| Setup complexity | Embedding pipeline + DB | Tree construction only |
| Cost | Embedding + search + generation | Multi-step reasoning calls |

## When to Use

- High-accuracy requirements (financial, legal, medical)
- Document collections with complex structure
- When numerical precision matters
- When infrastructure simplicity is preferred

## Related Concepts

- [[llm-knowledge-bases]] — alternative retrieval approach for knowledge bases
- [[rag-security]] — different security profile than vector-based RAG
- [[token-optimization]] — tree navigation reduces unnecessary context loading

## Sources

- [[pageindex-vectorless-rag-2026-04]]

- [[agent-memory-cognee-akshay-2026-04]]
- [[cognee]]
- [[context-engineering-synthesis]]
- [[knowledge-management-synthesis]]
- [[memory-systems]]
- [[ml-models-handbook-2026]]