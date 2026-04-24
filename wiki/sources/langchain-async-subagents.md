---
author: LangChain Team
confidence: medium
created: '2026-04-16'
date: 2026-04-17
priority: reference
reliability: high
source_type: blog
status: current
summary: Running Subagents in the Background
tags:
- langchain
- agents
- async
- subagents
- orchestration
title: 'LangChain: Running Subagents in the Background'
type: concept
updated: '2026-04-18'
url: https://blog.langchain.com/running-subagents-in-the-background
---


# Running Subagents in the Background

## Key Takeaways

- Traditional inline subagents create deadlocks in complex workflows
- Async subagent pattern enables non-blocking task execution
- Built on Agent Protocol specification
- Management tools: `start_async_task`, `check_task_status`, `get_task_result`

## Core Problem

Traditional pattern breaks down with longer, complex tasks:
1. Agents perform better with smaller tasks
2. Supervisor organizes work into subtasks
3. But inline execution blocks supervisor

## Async Pattern Benefits

- Supervisor stays responsive to user input
- Parallel subagent coordination possible
- Subagent results can inform other subagents
- Independent state management per subagent

## Technical Details

```typescript
// Subagent definition
export const researcher = createAgent({
  // agent configuration
});

// Supervisor with async tools
export const agent = createDeepAgent({
  subagents: {
    "researcher": "./agents.ts:researcher"
  }
});
```

## Relation to Hermes

Hermes `delegate_task` implements similar pattern:
- Isolated subagent contexts
- Background execution
- Polling for results
- Supervisor maintains responsiveness

## Camp Classification

This is a **Camp 2 (Context Substrate)** pattern - about how agents maintain and share context during execution, not about storage backends.

## Links
- Full article: https://blog.langchain.com/running-subagents-in-the-background
- Agent Protocol: https://github.com/langchain-ai/agent-protocol
