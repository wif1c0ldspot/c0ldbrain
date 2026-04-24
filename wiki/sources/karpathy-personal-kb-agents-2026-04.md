---
title: "Building Personal Knowledge Base for Agents"
type: source
source_url: "https://x.com//status/2039844072748204246"
author: "@karpathy"
created: '2026-04-02'
confidence: high
status: current
tags: [source, knowledge-management, agents, llm-wiki]
summary: "Using LLMs to build personal knowledge bases that serve as context for AI agents"
---

## Summary

Discussion of using LLMs to build personal knowledge bases specifically designed to serve as context for AI agents in multi-session workflows.

## Core Concept

Personal knowledge base that:
1. **Captures** — Everything worth remembering
2. **Structures** — Organizes for both human and AI
3. **Retrieves** — Surfaces relevant context on demand
4. **Compounds** — Gets smarter over time

## Agent Integration

### Context Provision
- Agents read wiki before working
- Wiki provides background, decisions, patterns
- Reduces repeated explanations

### Memory Externalization
- Internal model knowledge → External storage
- Enables agent continuity
- Survives session boundaries

### Collaborative Building
- Human and agent both contribute
- Agent documents decisions
- Human corrects/extends

## Technical Considerations

### What to Store
- Decisions and rationale
- Patterns discovered
- Preferences expressed
- Progress made
- Problems solved

### What NOT to Store
- Ephemeral state
- Repeated explanations
- Obvious derivations
- Temporary workarounds

### Storage Format
- Markdown preferred
- Wikilinks for relationships
- Frontmatter for metadata
- Verbatim capture over summary

## Related Concepts

- [[llm-knowledge-bases]]
- [[agentic-ai]]
- [[context-substrate]]
- [[memory-systems]]
