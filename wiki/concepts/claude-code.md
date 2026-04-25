---
confidence: high
created: '2026-04-16'
priority: important
sources:
- rohit4verse-claude-code-architecture-2026-04
- hwchase17-agent-harnesses-2026-04
- jarvis-obsidian-claude-code-cyrilxbt-2026-04
status: current
summary: Anthropic's production agent harness with 55 directories and 331 modules.
  Features async generator loops, tool concurrency classification, four-layer architecture
  (Model/Context/Harness/Infrastructure), and enterprise multi-tenancy.
tags:
- coding-agents
- ai-agents
- claude-code
- agent-architecture
- infrastructure
- developer-tools
title: Claude Code
type: concept
updated: '2026-04-24'
---


# Claude Code

Anthropic's production-grade agent harness for software engineering. Open-sourced with 55 directories and 331 modules of TypeScript, representing the most battle-tested agent architecture in production.

## Summary

Claude Code is not just a coding agent — it is a complete agent **infrastructure** stack. While most frameworks focus on the three-layer model (Model Weights, Context, Harness), Claude Code introduces a critical fourth layer: **Infrastructure** (multi-tenancy, RBAC, resource isolation, distributed coordination).

## Four-Layer Architecture

```
┌──────────────────────────────────────────────────────────────────────────┐
│  CLAUDE CODE ARCHITECTURE                                                │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Layer 1: Model Weights                                                  │
│    └── Frozen intelligence (Claude API)                                   │
│                                                                          │
│  Layer 2: Context                                                        │
│    ├── Conversation history                                               │
│    ├── Four compaction strategies (micro → snip → auto → collapse)      │
│    └── System prompt with cache boundary optimization                      │
│                                                                          │
│  Layer 3: Harness                                                        │
│    ├── Async generator agent loop (query.ts: 1,729 lines)                 │
│    ├── 45+ tools with concurrency classification                           │
│    ├── Streaming tool executor (mid-stream execution)                      │
│    ├── 823-line retry system with per-error recovery                       │
│    └── Tool result budgeting                                               │
│                                                                          │
│  Layer 4: Infrastructure ⭐                                             │
│    ├── CLAUDE.md hierarchy (enterprise → project → user → local)         │
│    ├── Git worktree isolation for sub-agents                               │
│    ├── File-based task coordination with locking                           │
│    ├── Permission pipeline (7 stages)                                      │
│    └── Multi-tenancy, RBAC, distributed coordination                       │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

## Core Technical Innovations

### 1. Async Generator Agent Loop

Located in `query.ts` (1,729 lines of TypeScript). The critical decision:

```typescript
async function* agentLoop(...)
```

**Benefits over while-loop:**
| Feature | Async Generator | While Loop |
|---------|----------------|------------|
| Streaming | Native (yields StreamEvent) | Requires bolt-on |
| Cancellation | Stop calling `.next()` | Abort mechanism needed |
| Composability | Universal interface (UI, sub-agents, tests) | Single caller |
| Backpressure | Pauses when consumer stops | Buffers in memory |
| Error Recovery | First-class in loop states | Outer try-catch |

**Five Phases:**
1. **Setup**: Apply budgets, run compaction, validate tokens
2. **Model Invocation**: Streaming call through dependency injection
3. **Error Recovery**: Handle prompt-too-long, max_output_tokens, overflow
4. **Tool Execution**: Streaming executor runs tools
5. **Continuation Decision**: Check stop_reason, maxTurns, hooks

### 2. Tool Concurrency Classification

Claude Code classifies 45+ tools by concurrency behavior:

| Type | Tools | Execution |
|------|-------|-----------|
| **Read-only** | Glob, Grep, Read, WebFetch | 10x parallel |
| **Write** | Edit, Write, Bash (mutating) | Serial |

**Streaming Tool Executor**: Starts tool execution mid-stream, hiding 2-5s latency per turn.

### 3. Context Compaction Hierarchy

Four strategies ordered by cost (cheapest first):

| Strategy | When | Cost |
|----------|------|------|
| **Microcompact** | Every turn | Near zero |
| **Snip Compact** | Approaching limits | Fast (no model) |
| **Auto Compact** | Snip insufficient | Model call |
| **Context Collapse** | Hours-long sessions | Expensive |

**Protected Tail**: Recent messages never summarized, maintaining full fidelity on current plan.

### 4. CLAUDE.md Hierarchy

Four-level instruction system for multi-tenancy:

```
/etc/claude-code/CLAUDE.md     ← Enterprise (MDM)
./.claude/CLAUDE.md            ← Project
~/.claude/CLAUDE.md            ← User
./CLAUDE.local.md              ← Local (private)
```

Features `@include` directive for composition. Higher levels override lower ones.

### 5. Error Recovery System

823-line retry system (`services/api/withRetry.ts`) with specific recovery per error class:

| Error | Recovery |
|-------|----------|
| 429 Rate Limited | Check Retry-After; <20s retry, >20s cooldown |
| 529 Overloaded | Track consecutive; 3x → switch models |
| 400 Context Overflow | Parse tokens, recalculate budget, retry |
| Network | Disable keep-alive, new connection |

**Backoff**: `delay = min(500ms × 2^attempt, 32s) + random(0, 0.25 × baseDelay)`

### 6. Sub-Agent Worktree Isolation

```
getOrCreateWorktree(repoRoot, slug)
    → Create branch: worktree-<slug>
    → Symlink node_modules (prevent bloat)
    → Copy CLAUDE.md, settings
    → Isolated execution, changes merge when verified
```

**Three Spawn Backends:**
- In-process (fastest, shared memory)
- Tmux pane (terminal visibility)
- Remote (full machine isolation)

## System Prompt Cache Optimization

The system prompt is a structured array with `SYSTEM_PROMPT_DYNAMIC_BOUNDARY`:

- **Above boundary** (~80%): Static, cached globally at API level
- **Below boundary**: Memoized (per session) or volatile (per turn)

**Impact**: Determines whether agent costs $0.02 or $0.20 per session at scale.

## Permission System: Seven Stages

| Stage | Action |
|-------|--------|
| 1 | Tool call requested |
| 2 | Check tool-level rules (glob patterns) |
| 3 | Check permission mode (default/acceptEdits/readOnly/bypass) |
| 4 | PreToolUse hooks |
| 5 | Execute tool |
| 6 | PostToolUse hooks |
| 7 | Return result |

**Hooks** enable custom guardrails: Slack notifications, security scans, linters.

## Extensibility: Four Mechanisms

All require **zero source modifications**:

1. **Skills**: Markdown files with YAML frontmatter
2. **Hooks**: Event-driven (PreToolUse, PostToolUse, SessionStart, etc.)
3. **MCP**: Model Context Protocol for external systems
4. **Plugins**: Directories of skills/agents/hooks/config

## Key Statistics

| Metric | Value |
|--------|-------|
| Directories | 55 |
| Modules | 331 |
| query.ts | 1,729 lines |
| withRetry.ts | 823 lines |
| Built-in tools | 45+ |
| Compaction strategies | 4 |
| Permission stages | 7 |
| CLAUDE.md levels | 4 |

## Comparison to Other Harnesses

| Feature | Claude Code | Typical Framework |
|---------|-------------|-------------------|
| Agent loop | Async generator | While loop |
| Tool execution | Concurrent classification | Sequential or naive parallel |
| Streaming | Mid-stream tool execution | Post-generation |
| Context management | 4-tier compaction | Truncation or crash |
| Multi-tenancy | CLAUDE.md hierarchy | None |
| Sub-agents | Worktree isolation | None |
| Error recovery | Per-class state machine | Generic retry |

## References

- **Source Analysis:** [[rohit4verse-claude-code-architecture-2026-04]]
- **Harness Theory:** [[hwchase17-agent-harnesses-2026-04]]
- **Claude Code Repository:** https://github.com/anthropics/claude-code

## Related Concepts

- [[agent-harness]] — Agent harness patterns
- [[agent-architecture]] — Multi-layer frameworks
- [[agent-infrastructure]] — Layer 4 concerns
- [[async-generators]] — Streaming patterns
- [[context-compaction]] — Context window strategies
- [[tool-orchestration]] — Concurrent execution
- [[mcp-protocol]] — Model Context Protocol
- [[ai-coding-agents]] — Coding agent landscape

- [[claude-caveman-prompting-strategy-2026-04]]
- [[claude-caveman-token-strategy-2026-04]]
- [[claude-code-opus-planning-2026-04]]
- [[claude-code-patterns]]
- [[claude-code-skill-graphs-2026-04]]
- [[coral-human-agent-society-2026-04]]
- [[coral-multi-agent-discovery]]
- [[github-ai-tools-roundup-2026-04]]
- [[gstack-garrytan-2026-04]]
- [[harness-design]]
- [[jarvis-obsidian-claude-code-cyrilxbt-2026-04]]
- [[karpathy-wiki-self-evolving-claude-2026-04-06]]
- [[langflow-claude-code-integration]]
- [[multica-platform]]
- [[mac-mini-35b-local-ai-agent-2026-04]]
- [[agency-agents]]
- [[infrastructure-handbook-2026]]
- [[agent-skills-osmani-github-2026-04]]