---
title: "NotebookLM vs LLM Wiki for Knowledge Management"
type: concept
tags: [knowledge-management, llm-wiki, notebooklm, ai-agents, skills-based-knowledge]
created: 2026-04-20
updated: 2026-04-20
confidence: medium
status: current
priority: reference
summary: "Comparison of LLM-maintained wikis vs embedding-based tools (NotebookLM) for personal knowledge management. Key insight: convert knowledge to skills, not just storage."
---

# NotebookLM vs LLM Wiki for Knowledge Management

## Overview

Two paradigms for AI-assisted knowledge management: **LLM wikis** (Karpathy pattern — Claude reads, summarizes, maintains structured wiki) vs **embedding-based tools** (Google NotebookLM — sources ingested as embeddings, queried via RAG). Different tradeoffs for different use cases.

## The Comparison (per @artemxtech)

| Dimension | LLM Wiki (Karpathy) | NotebookLM |
|-----------|---------------------|------------|
| Ingestion | ~20 min for 19 sources (parallel) | Instant (embedding) |
| Query cost | ~44K tokens/question | Fraction of tokens |
| Citations | Must re-read sources | Built-in |
| Maintenance | Ongoing wiki upkeep | None — sources stay raw |
| Depth | Deep synthesis, PhD-level | Surface-level, fast answers |
| Best for | Team, competitive analysis | Personal learning, FOMO |

## Key Insight: Skills > Storage

The wiki stores knowledge. But knowledge without application is worthless. Artem's 3-step framework:

1. **Create skills** — Extract frameworks from sources into actionable skills
2. **Integrate into routines** — Embed skills in daily/weekly workflows
3. **Execute** — Run skills within routines (not just ask questions about them)

Example: Dalio's 5-step decision process → daily template with reflection prompts + weekly review loop.

## When to Use Each

### LLM Wiki (deep work)
- PhD-level research requiring high accuracy
- Team wikis with shared knowledge base
- Competitive analysis across many sources
- When you can afford 30 min per source ingestion
- Need full source access for nuanced answers

### NotebookLM (fast learning)
- Personal knowledge — learning a topic quickly
- Staying current (21 videos on AI agents)
- Reducing FOMO across many sources
- Token budget constrained
- No maintenance overhead

## Related Concepts

- [[knowledge-management-synthesis]] — Unified view of RAG vs compiled vs synthesized paradigms
- [[karpathy-llm-wiki-agent]] — The original LLM wiki pattern this critiques
- [[karpathy]] — Creator of the LLM wiki approach
- [[knowledge-management]] — Broader domain
