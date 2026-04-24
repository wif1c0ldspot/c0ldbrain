---
confidence: high
created: '2026-04-16'
priority: reference
sources:
- raw/github/karpathy-llm-wiki-yologdev.md
status: current
summary: Autonomous agent every 4h on GitHub Actions. 4-phase pipeline with auto-revert.
tags:
- ai-agents
- knowledge-management
- autonomous-optimization
title: Karpathy LLM Wiki - Autonomous Agent
type: concept
updated: 2026-04-10
---



# Karpathy LLM Wiki - Autonomous Agent

## Summary

yologdev/karpathy-llm-wiki: autonomous agent runs every 4h via GitHub Actions. Reads vision, plans, builds, communicates — no human in the loop.

## 4-Phase Pipeline

| Phase | Purpose |
|-------|---------|
| ASSESS | Read vision, check build, map gaps |
| PLAN | Set max 3 tasks |
| BUILD | Implement, test, auto-revert on failure |
| COMMUNICATE | Journal, learnings |

## Security

Random nonces, content sanitization, author allowlist, auto-revert on failure.

## Critiques
- [[notebooklm-vs-llm-wiki]] — @artemxtech comparison: NotebookLM wins for personal use due to embedding-based ingestion and lower token cost

## Related Concepts

[[llm-knowledge-bases]], [[hermes-agent-architecture]], [[ai-coding-agents]], [[llm-wiki-v2-rohitg00|extended-by]] — LLM Wiki v2 extends Karpathy's original pattern with memory lifecycle, knowledge graph, hybrid search
