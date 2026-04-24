---
compiled: 2026-04-15
confidence: high
created: '2026-04-16'
priority: 2
source_url: https://github.com/VectifyAI/PageIndex
stars: 25.2k
status: current
summary: 25.2k star vectorless RAG using LLM reasoning + tree index. Achieves 98.7%
  accuracy on FinanceBench without vector embeddings.
tags:
- rag
- knowledge-management
- ml-models
- benchmarking
- open-source
title: PageIndex — Vectorless RAG via LLM Reasoning
type: source
updated: '2026-04-18'
---


# PageIndex — Vectorless RAG via LLM Reasoning

## Key Insights

- Replaces vector embeddings entirely with LLM reasoning and tree-structured indices
- Achieves 98.7% accuracy on FinanceBench — top performance without vector search
- 25.2k stars: one of the most popular RAG alternatives in 2026
- Paradigm shift: reasoning over structure beats embedding similarity

## Technical Details

### Vectorless Approach
- No vector database, no embeddings, no similarity search
- Uses LLM reasoning to navigate document structure
- Tree index provides hierarchical document organization
- LLM performs multi-step reasoning to locate and extract relevant information

### Tree Index Structure
- Hierarchical document decomposition (sections, paragraphs, sentences)
- LLM navigates tree top-down, pruning irrelevant branches
- Each navigation step is a lightweight LLM call
- Total cost comparable to embedding-based RAG but with higher accuracy

### FinanceBench Results
- 98.7% accuracy on FinanceBench benchmark
- Outperforms vector-based RAG systems
- Particularly strong on numerical reasoning and financial extraction
- No domain-specific fine-tuning required

### Architecture
- Document ingestion: automatic tree construction
- Query time: LLM-guided tree traversal
- Supports PDFs, web pages, structured documents
- API-compatible with existing RAG pipelines

## Related Concepts

- [[llm-knowledge-bases]] — alternative to vector-based knowledge retrieval
- [[rag-security]] — new RAG paradigm with different security profile
- [[token-optimization]] — tree-based navigation reduces unnecessary context
