---
title: "LLM Wiki vs NotebookLM — Artem Zhutov Critique"
author: "@artemxtech"
date: 2026-04-20
source: "https://x.com/artemxtech/status/2045912259210485815"
tags: [source, knowledge-management, llm-wiki, notebooklm]
type: source
---

## Summary

Artem Zhutov (@artemxtech) ran a head-to-head comparison of Karpathy's LLM wiki pattern vs Google NotebookLM for personal knowledge management. Verdict: NotebookLM wins for personal use due to instant ingestion (embeddings vs full re-read), lower token cost, and built-in citations. LLM wikis shine only for deep research, team use, and competitive analysis.

## Key Points

- **Token cost problem**: LLM wiki requires re-reading full transcripts per query (~44K tokens/question). NotebookLM uses embeddings — ingestion is instant, queries are cheap.
- **Wiki lacks actionability**: Having a wiki doesn't improve decisions. Knowledge must become skills integrated into routines.
- **Skills > Storage**: Artem's 3-step framework: (1) Create skills from knowledge, (2) Integrate into daily routines, (3) Execute within workflows.
- **Dalio example**: Built a decision-making skill from Ray Dalio's 5-step process with daily reflection prompts and weekly reviews.
- **LLM wiki sweet spot**: PhD-level research, team wikis, competitive analysis — deep work where accuracy matters and cost is acceptable.
- **Personal knowledge**: For learning topics, LLM wiki is overkill. NotebookLM + Claude workflow is faster and cheaper.
- **Token era tightening**: Free tokens are ending. LLM wiki's heavy token usage is becoming unsustainable.

## Filing Decision

Filed under Knowledge Management per RESOLVER.md routing. Flat structure — no subdirectories. Concept page `notebooklm-vs-llm-wiki.md` captures the comparison. Related: `karpathy-llm-wiki-agent.md`, `karpathy.md`.


## Related Concepts
- [[llm-optimized-wiki]]
- [[hermes-multi-profile-team]]
- [[llm-optimized-wiki]]