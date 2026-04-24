---
title: LLM Knowledge Bases & Second Brains
type: concept
tags: [knowledge-management, llm, obsidian, ai-agents]
sources:
- karpathy-llm-knowledge-base-viral-2026-04
- karpathy-self-improving-second-brain-2026-04
- karpathy-llm-kb-architecture-2026-04
- karpathy-personal-kb-agents-2026-04
- karpathy-llm-kb-pattern-2026-04
- rowboat-knowledge-graph-2026-04
- pageindex-vectorless-rag-2026-04
- markitdown-microsoft-2026-04
created: '2026-04-06'
updated: '2026-04-15'
confidence: high
status: current
agents: [hermes, claude, codex]
priority: critical
summary: LLMs build, compile, and maintain personal knowledge bases as structured
 markdown wikis. Replaces RAG with LLM-authored articles that compound in value.
---


# LLM Knowledge Bases & Second Brains

## Summary

The pattern of using LLMs to build, compile, and maintain personal knowledge bases as structured markdown wikis in Obsidian. Replaces RAG with LLM-authored articles that compound in value over time.

## Core Architecture (Karpathy's Pattern)

Three-layer system:

```
raw/ -> Source material (articles, papers, repos, transcripts, datasets)
wiki/ -> LLM-compiled knowledge (interlinked markdown files, categorized)
scripts/ -> Ingestion, query, and maintenance tools
```

The LLM acts as research librarian: reads raw materials, writes encyclopedia-style articles, creates backlinks, categorizes by concept, and maintains an index. Humans rarely touch the wiki directly.

## Why This Beats RAG at Small Scale

| Feature | RAG (Vector DB) | LLM Wiki |
|---------|-----------------|----------|
| Coherence | Chunking artifacts | Full human-readable articles |
| Maintenance | Static index | Self-improving through lint passes |
| Human access | Black box | Direct markdown files |
| Compounding value | None | Each query enriches the wiki |
| Infrastructure | Vector DB, embeddings | Just markdown files |

## Key Principles

1. The LLM organizes, not you
2. Backlinks are mandatory — no new page without bidirectional links
3. Two-tier structure: source summaries AND concept articles
4. Manifest tracking decouples ingestion from compilation
5. Batch mode — ingest many, compile all at once
6. Lint passes find contradictions, orphans, and missing connections
7. Outputs (analyses, slides, charts) get filed back into the wiki

## Notable Projects

|| Project | Description | Status ||
||---------|-------------|--------||
|| GitNexus | Full knowledge graph engine for codebases — maps every dependency, call chain, execution flow | Active, 40K+ stars ||
|| MarkItDown (Microsoft) | Converts any document to Markdown for LLM use. 109k stars. MCP server available. | Active, open-source ||
|| Memvid | Replaces vector databases with MP4 files — portable, sub-ms retrieval | Experimental ||
|| 8 AI Agents for Obsidian | PhD researcher replaced Notion + note-taking + inbox with 8 AI agents managing Obsidian | Active ||
|| Rowboat | AI coworker building knowledge graphs from email/meetings. Obsidian-compatible vault output. 12.4k stars. | Active ||
|| PageIndex | Vectorless RAG using LLM reasoning + tree index. 98.7% FinanceBench accuracy. 25.2k stars. | Active ||

## Vectorless RAG Alternative (from pageindex-vectorless-rag-2026-04)

PageIndex introduces a paradigm shift: replacing vector embeddings entirely with LLM reasoning over tree-structured document indices. Achieves 98.7% on FinanceBench without any vector database. See [[vectorless-rag]] for full concept page.

## Related Concepts

- [[knowledge-management-synthesis]] — Unified view of RAG vs compiled vs synthesized paradigms
- [[gbrain-agent-brain]] — Production agent brain (Garry Tan, 9.5k stars)
- [[code-review-graph]], [[ai-coding-agents]], [[memory-systems]], [[token-optimization]], [[llm-wiki-v2-rohitg00|extended-by]], [[vectorless-rag]], [[resolvers]]
