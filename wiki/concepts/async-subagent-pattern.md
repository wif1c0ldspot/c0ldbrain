---
camp: 2
category: pattern
confidence: medium
created: '2026-04-16'
date: 2026-04-17
priority: reference
status: emerging
summary: Async Subagent Pattern
tags:
- agents
- memory
- context
- orchestration
- langchain
title: Async Subagent Pattern
type: concept
updated: '2026-04-18'
---


# Async Subagent Pattern

## Overview

The Async Subagent Pattern enables supervisor agents to launch long-running subtasks without blocking, maintaining responsiveness to user input and ability to coordinate multiple parallel workstreams.

## Problem Statement

Traditional inline subagents create deadlocks:
- Supervisor waits for subagent completion
- Cannot receive user input during execution  
- Cannot coordinate parallel workstreams
- Single point of failure

## Solution Architecture

```
┌───────────────────────────────────────────────────────────────┐
│                    SUPERVISOR AGENT                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │ Task Manager │  │   User Input   │  │ Coordination │    │
│  └───┬──────────┘  └──────────────┘  └──────────────┘    │
│       │                                              │
│       │ start_async_task()                          │
│       │                                              │
└────────┼───────────────────────────────────────────────────────┘
        │
        │ launches (non-blocking)
        ▼
┌───────────────────────────────────────────────────────────────┐
│                    SUBAGENT A (Background)               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │    State     │  │    Memory     │  │  Execution   │    │
│  │   (isolated) │  │   (isolated)  │  │   Context    │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└───────────────────────────────────────────────────────────────┘
```

## Management Tools

| Tool | Function |
|------|----------|
| `start_async_task` | Launch task, return task ID immediately |
| `check_task_status` | Poll for completion status |
| `get_task_result` | Retrieve final output |

## Memory Implications

1. **Subagent Isolation**: Each subagent maintains independent state and memory
2. **Supervisor Context**: Supervisor must track active tasks in working memory
3. **Cross-Agent Memory**: Results may need to propagate between agents
4. **Walnut Container Pattern**: Task-scoped memory isolation

## Implementation in Hermes

Hermes `delegate_task` already implements async subagent pattern:
- Tasks run in isolated contexts
- Background execution with polling
- Results retrieved when complete
- Supervisor remains responsive

## Sources
- [[langchain-async-subagents]]
- Agent Protocol Specification: https://github.com/langchain-ai/agent-protocol

## Related Concepts
- [[context-substrate]]
- [[context-substrate]]
- [[agent-orchestration-stacks]]

## See Also
- [[memory-systems]]
- [[cognee]]
