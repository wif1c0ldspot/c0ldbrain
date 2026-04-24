---
confidence: medium
created: '2026-04-16'
date: 2026-04-17
priority: reference
source_type: daily-research
status: current
summary: Summary
tags:
- research
- agentic-ai
- knowledge-management
- ai-agents
title: 'Daily Research: Agentic Memory Tools - 2026-04-17'
type: source
updated: '2026-04-18'
---


## Summary

Daily research compilation tracking major developments in agentic memory tools and AI agent architectures. Key updates include Mem0 v3.0 TypeScript SDK release, LangChain async subagent patterns, and Cognee v1.0.1 launch. Documents the emerging distinction between Camp 1 (Memory Backends) and Camp 2 (Context Substrates).

## Key Findings

### Major Tool Updates

| Tool | Version | Stars | Camp | Key Update |
|------|---------|-------|------|------------|
| Mem0 | v3.0.0 | 53,314 | Camp 1 (Backend) | TypeScript SDK released 2026-04-16 |
| Cognee | v1.0.1 | 16,107 | Camp 2 (Substrate) | Knowledge graph engine released 2026-04-15 |
| Supermemory | - | 21,896 | Camp 1 (Backend) | Memory API with temporal awareness |
| Zep | - | 4,444 | Camp 2 (Substrate) | Graphiti graph memory |

### Pattern of the Day: Async/Background Agent Execution

**Problem**: Traditional inline subagents create deadlocks - supervisor waits, can't receive user input, can't coordinate parallel work.

**Solution**: Async subagent pattern with:
1. Non-blocking task launch (returns task ID immediately)
2. Background execution with independent state
3. Polling/checking mechanisms for results
4. Continued supervisor responsiveness

**Implications for Memory**:
- Subagents need isolated memory contexts
- Supervisor needs memory of ongoing tasks
- Cross-agent memory sharing becomes important
- "Walnut container" pattern for task isolation

### Camp Classification

**Camp 1 (Memory Backends)**: Mem0, Supermemory - Focus on storage and retrieval of memories
**Camp 2 (Context Substrates)**: Cognee, Zep (Graphiti), LangChain Deep Agents - Focus on context management during execution

### Integration Recommendations

**High Priority**:
1. Monitor Mem0 v3.0 TypeScript SDK - API changes may affect MCP integration
2. Study LangChain async pattern - Hermes delegate_task already implements this
3. Evaluate Cognee graph approach - Could complement MemPalace's vector-only approach

**Medium Priority**:
4. Track Camp 1 vs Camp 2 evolution - MemPalace currently Camp 1, consider Camp 2 features
5. LongMemEval/LoCoMo benchmarks - Add evaluation capability

## Research Questions

- How does MemPalace's "wing-room-drawer" taxonomy compare to Cognee's graph approach?
- Can we add graph relationships to MemPalace without losing simplicity?
- Should Hermes implement async task memory (tracking delegate_task history)?

## Sources

- GitHub API: github.com/mem0ai/mem0, github.com/getzep/zep, github.com/supermemoryai/supermemory, github.com/topoteretes/cognee
- LangChain Blog: blog.langchain.com/running-subagents-in-the-background
- Agent Protocol Spec: github.com/langchain-ai/agent-protocol

---

*Research conducted: 2026-04-17*
