---
title: "Multica Relational Agent Memory Pattern"
type: concept
tags: [ai-agents, memory-systems, multi-agent, relational-memory, agent-harness, postgresql]
created: '2026-04-19'
updated: '2026-04-19'
confidence: medium
status: current
priority: important
summary: "Pure relational (SQL + JSONB) memory for multi-agent systems. No vector embeddings. Explicit skill-to-agent joins, point-in-time snapshots for cold inference, workspace-scoped isolation."
sources:
- multica-agent-memory-mem0ai-2026-04
---

# Multica Relational Agent Memory Pattern

## Summary

A multi-agent memory architecture that uses pure relational storage (PostgreSQL + JSONB) instead of vector embeddings. Multica (15,400+ GitHub stars) demonstrates that curated, explicit skill attachment beats similarity-based retrieval for coding agent harnesses.

## Key Concepts

### Six-Table Schema (all workspace-scoped)

1. **workspace.context (TEXT)** — workspace-wide prompt every agent inherits
2. **issue** — task unit with context_refs (JSONB), acceptance_criteria, related issues
3. **agent_task_queue.context (JSONB)** — point-in-time snapshot assembled at dispatch. Daemon reads once, no DB roundtrips during inference
4. **skill + skill_file + agent_skill** — capabilities attached to agents via join table
5. **comment** — threaded working memory during task execution
6. **activity_log** — append-only audit trail of every state transition

### Core Design Decisions

- **Explicit > Similarity**: Skills attached to agents via `agent_skill` join table. Query is a simple SQL join, not cosine similarity
- **Snapshots > Live Queries**: JSONB snapshot assembled at dispatch, handed off. Database stays cold during inference
- **Workspace Isolation**: Every table has `workspace_id` with `ON DELETE CASCADE`. Offboarding = one DELETE
- **Memory Compounds**: Task resolutions become new/updated skill rows. Library grows with team activity

### Cold Inference Pattern

```
Dispatch: Assemble workspace context + issue + skills → JSONB blob
Execution: Daemon reads blob once, spawns CLI, no DB during inference
Completion: Agent streams updates → WebSocket + DB writes
Resolution: Output becomes new skill → available next task
```

## When to Use

- **Coding agent harnesses** — curated skill libraries, exact runbook retrieval
- **Multi-agent orchestration** — explicit task routing, not fuzzy matching
- **Regulated environments** — full audit trail, workspace isolation, cascading deletes

## When NOT to Use

- **Chat assistants** — need fuzzy recall, contextual retrieval, semantic search
- **Research synthesis** — needs cross-workspace memory, similarity matching
- **Knowledge-heavy workflows** — skill libraries too large for explicit attachment

## Relationship to Vector Memory

Not a replacement — complementary layers:
- **Relational harness** (PostgreSQL): Skills, tasks, state, audit. The scaffolding
- **Context layer** (mem0 / vector store): Agent context, prior decisions, learned patterns, working relationships. The nervous system

Optimal: harness in PostgreSQL + context in vector store, bridged at dispatch.

## Implementation

### Stack
- PostgreSQL with JSONB support
- Partial index on `agent_task_queue(status)` for polling
- WebSocket for real-time fan-out

### Schema Pattern
```sql
CREATE TABLE agent_task_queue (
  id UUID PRIMARY KEY,
  workspace_id UUID NOT NULL REFERENCES workspace(id) ON DELETE CASCADE,
  context JSONB,  -- snapshot blob
  status TEXT DEFAULT 'queued'
);
CREATE INDEX idx_agent_task_queue_pending ON agent_task_queue(status) WHERE status = 'queued';
```

## Limitations

1. **No fuzzy recall** — untagged skills invisible at dispatch
2. **Snapshot staleness** — agents miss new comments mid-task
3. **Discipline-dependent** — skills library rots without write-ups
4. **Unbounded snapshots** — 200 skills = 200 summaries per blob
5. **Siloed workspaces** — Team A's solution can't help Team B

## Related Concepts

- [[multica-platform]] — the full platform overview (agents, autopilot, skills)
- [[agent-harness]] — scaffolding patterns for agent systems
- [[memory-systems]] — memory architectures across agent types
- [[coral-multi-agent-discovery]] — autonomous multi-agent evolution
- [[ai-coding-agents]] — coding agent ecosystem and tools
