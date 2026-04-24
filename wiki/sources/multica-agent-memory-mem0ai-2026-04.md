---
title: "How Memory Works in a Multi-Agent System: Inside Multica"
author: "@mem0ai"
date: 2026-04-19
source: "https://x.com/mem0ai/status/2045519377655890111"
type: source
tags: [multi-agent, memory-systems, relational-memory, agent-harness]
---

## Summary

Deep dive into Multica's memory architecture — a managed agents platform with 15,400+ GitHub stars. Uses pure relational (PostgreSQL + JSONB) instead of vector embeddings for agent memory. Six workspace-scoped tables, explicit skill-to-agent joins, point-in-time snapshots for dispatch.

## Key Points

- **Six tables, zero embeddings**: workspace.context, issue, agent_task_queue (JSONB snapshots), skill + agent_skill (join-based), comment, activity_log
- **Skills attached by join, not similarity**: `SELECT * FROM skill JOIN agent_skill` — no cosine similarity, no top-K
- **Cold inference via snapshots**: JSONB blob assembled at dispatch, daemon reads once, no DB roundtrips during inference
- **Workspace isolation**: every table has workspace_id with ON DELETE CASCADE — offboarding is one DELETE
- **Memory compounds**: skill library grows over time, each task resolution becomes a new/updated skill row

## Limitations Identified

1. No fuzzy recall — untagged skills invisible at dispatch
2. Snapshots go stale mid-task
3. Skill quality depends on team discipline
4. Snapshot size grows with library
5. No cross-workspace memory

## mem0's Take

PostgreSQL is the right harness (skills, tasks, state). But agent context needs a dedicated layer with fuzzy recall and contextual retrieval. The harness manages the scaffolding; the context layer would be the nervous system.

## Full Content

See [[multica-relational-agent-memory]] for concept analysis.

### Managed Agents Landscape

- **Claude Cowork**: Good but limits on shared state — copy-pasting context between sessions
- **Claude Managed Agents** (Anthropic): Better, but locked to Claude
- **Paperclip**: Enterprise-oriented — org charts, approval workflows, spend controls
- **Multica**: Open-source, vendor-neutral, lightweight

### Issue Assignment Flow

1. Human creates issue → row inserted with workspace_id
2. Issue assigned to agent/user
3. Backend assembles snapshot (workspace.context + issue + related issues + skills) → JSONB blob → agent_task_queue
4. Daemon polls via partial index, claims row, reads JSONB, spawns correct CLI
5. Agent streams updates → WebSocket fan-out
6. Resolution becomes new/updated skill row
