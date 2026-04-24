---
author: Rohit (@rohit4verse)
confidence: high
created: '2026-04-16'
engagement: 557K views, 3.4K bookmarks, 1K likes
priority: reference
published: 2026-04-07
source_url: https://x.com/rohit4verse/status/2041548810804211936
status: current
summary: Deep architectural analysis of Claude Code's source revealing a four-layer
  framework (Model, Context, Harness, Infrastructure) with async generators, tool
  concurrency, streaming execution, and enterprise multi-tenancy.
tags:
- coding-agents
- ai-agents
- claude-code
- agent-architecture
- infrastructure
title: How I built harness for my agent using Claude Code leaks
type: source
updated: 2026-04-17
compiled: true
---


# How I built harness for my agent using Claude Code leaks

**Author:** Rohit (@rohit4verse)  
**Published:** 2026-04-07  
**Engagement:** 557K views, 3.4K bookmarks, 1K likes, 125 reposts, 27 replies

## Key Insights

### The Four-Layer Framework

Rohit argues the industry-standard three-layer model (Model Weights, Context, Harness) is incomplete. Claude Code operates on **four layers**:

| Layer | Purpose | Example |
|-------|---------|---------|
| **Model Weights** | Frozen intelligence | Claude API calls |
| **Context** | Runtime input | Conversation history |
| **Harness** | Agent environment | Tools, loops, error handling |
| **Infrastructure** | Multi-tenancy, coordination | RBAC, worktree isolation, state persistence |

> "Most teams talk about the first three because they are interesting to think about. The fourth is where products die."

### Core Technical Decisions

**Async Generator Agent Loop**
- Located in `query.ts`: 1,729 lines
- `async function* agentLoop(...)` enables streaming, cancellation, composability, backpressure
- Five phases per iteration: Setup → Model Invocation → Error Recovery → Tool Execution → Continuation Decision

**Tool Concurrency Classification**
- Read-only tools (Glob, Grep, Read): 10x parallel
- Write tools (Edit, Write, Bash): serial execution
- Streaming executor starts tool calls mid-stream, hiding 2-5s latency

**System Prompt Cache Optimization**
- `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` splits static (~80%, cached globally) from dynamic content
- Determines whether agent costs $0.02 or $0.20 per session at scale

**Four Compaction Strategies** (cheapest first):
1. **Microcompact**: Cache unchanged tool results
2. **Snip Compact**: Remove old messages, preserve "protected tail"
3. **Auto Compact**: Model-based summarization
4. **Context Collapse**: Multi-phase compression for hour-long sessions

**CLAUDE.md Hierarchy** (RBAC for agents):
- Enterprise (`/etc/claude-code/`): Org-wide via MDM
- Project (`.claude/`): Project conventions
- User (`~/.claude/`): Personal preferences
- Local (`CLAUDE.local.md`): Private overrides

**Error Recovery as First-Class State**
- 823-line retry system (`withRetry.ts`)
- Specific recovery per error class: 429 (rate limit), 529 (overloaded), 400 (context overflow), network errors
- Exponential backoff: `delay = min(500ms × 2^attempt, 32s) + random(0, 0.25 × baseDelay)`

**Sub-Agent Architecture**
- Git worktree isolation: each agent gets own branch
- Three spawn backends: in-process, tmux pane, remote
- File-based locking for task coordination

## Source Reference

- **URL:** https://x.com/rohit4verse/status/2041548810804211936
- **Type:** X Article / Twitter Thread
- **Length:** ~15,000 characters
- **Codebase Analyzed:** 55 directories, 331 modules

## Related Concepts

- [[claude-code]] — Claude Code agent analysis
- [[langflow-claude-code-integration]] — Implementation guide for Langflow
- [[agent-harness]] — Agent harness patterns
- [[agent-architecture]] — Multi-layer frameworks
- [[agent-infrastructure]] — Layer 4: multi-tenancy, RBAC, coordination
- [[swe-agent]] — Princeton NLP's environment optimization research
- [[async-generators]] — Streaming agent loop patterns
- [[context-compaction]] — Context window management strategies
- [[tool-orchestration]] — Concurrent vs serial tool execution
- [[claude-md]] — Hierarchical instruction system
- [[mcp-protocol]] — Model Context Protocol mentioned as extensibility mechanism
