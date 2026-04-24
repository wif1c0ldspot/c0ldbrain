---
confidence: medium
created: '2026-04-16'
date: 2026-04-17
priority: reference
source_type: synthesis
status: current
summary: Summary
tags:
- synthesis
- agentic-ai
- ai-agents
- async-patterns
title: 'Weekly Synthesis: Async Subagent Pattern'
type: source
updated: '2026-04-18'
---


## Summary

Weekly synthesis documenting the emerging distinction between Camp 1 (Memory Backend) and Camp 2 (Context Substrate) as LangChain introduces async subagent patterns.

## Key Insights

### The Two Camps Distinction

**Camp 1 (Memory Backends)**: Mem0, Supermemory - Focus on storage and retrieval of memories
**Camp 2 (Context Substrates)**: Cognee, Zep (Graphiti), LangChain Deep Agents - Focus on context management during execution

### Emerging Pattern: Async Task Execution

Async task execution requires **both camps**:
- **Camp 1** for persistent memory across tasks
- **Camp 2** for task-scoped context isolation

### Integration Opportunity

Hermes already implements Camp 2 patterns via [[delegate_task]]. Could strengthen Camp 1 integration with [[mempalace]] enhancements.

## Related Sources

- [[agent-memory-two-camps-witcheer-2026-04]]
- [[daily-research-agentic-memory-2026-04-17]]
- [[langflow-claude-code-integration]]

## Related Concepts

- [[async-subagent-pattern]]
- [[agentic-ai]]
- [[context-substrate]]
- [[knowledge-layer]]
- [[hermes-agent-architecture]]

---

*Synthesized: 2026-04-17*
