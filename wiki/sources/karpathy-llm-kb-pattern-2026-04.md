---
title: "LLM Knowledge Bases Pattern"
type: source
source_url: "https://x.com//status/2039805659525644595"
author: "@karpathy"
created: '2026-04-02'
confidence: high
status: current
tags: [source, knowledge-management, patterns, llm-wiki]
summary: "Core pattern for using LLMs to build personal knowledge bases - the foundational thread"
---

## Summary

The original thread introducing Karpathy's LLM Knowledge Base pattern. Describes using LLMs to maintain a personal wiki that captures and structures knowledge over time.

## The Pattern

### Premise
LLMs are good at:
- Reading and understanding text
- Synthesizing information
- Finding patterns
- Making connections

A personal wiki can leverage these capabilities to:
- Automatically organize information
- Link related concepts
- Surface relevant knowledge
- Build on previous work

### Implementation

1. **Capture everything** — Store raw, don't filter
2. **Let LLMs organize** — Agent structures content
3. **Link liberally** — Wikilinks create graph
4. **Iterate** — System improves over time

### Benefits

- **Low friction** — Just add content
- **High value** — Rich context for agents
- **Self-improving** — Gets better automatically
- **Human-readable** — Can inspect/edit directly

### Comparison to Traditional PKM

| Traditional PKM | LLM-Based PKM |
|-----------------|---------------|
| Human organizes | Agent organizes |
| Manual linking | Automatic linking |
| Active maintenance | Passive improvement |
| Search-based retrieval | Context injection |

## Viral Impact

This pattern inspired:
- OpenClaw memory system
- Various wiki implementations
- Agent memory frameworks
- C0ldbrain (this vault)

## Related Concepts

- [[karpathy]]
- [[llm-knowledge-bases]]
- [[context-substrate]]
- [[memory-systems]]
