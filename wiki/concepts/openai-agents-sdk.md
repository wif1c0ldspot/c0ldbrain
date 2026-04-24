---
title: "OpenAI Agents SDK"
type: concept
tags: [ai-agents, agent-harness, multi-agent, openai, python, framework, tool-calling]
created: '2026-04-19'
updated: '2026-04-19'
confidence: high
status: current
priority: important
summary: "Official OpenAI agent harness — lightweight, provider-agnostic multi-agent framework. Sandbox agents, handoffs, guardrails, tracing, MCP tools."
sources:
- openai-agents-python-sdk-github-2026-04
---

# OpenAI Agents SDK

## Summary

OpenAI's official agent harness — a lightweight, provider-agnostic Python framework for building multi-agent workflows. 22,600+ GitHub stars. Supports OpenAI APIs + 100+ other LLMs. Key differentiator: Sandbox Agents for container-based long-running work.

## Key Concepts

### Agent Primitives

| Primitive | Purpose |
|-----------|---------|
| **Agent** | LLM + instructions + tools + guardrails + handoffs |
| **Sandbox Agent** | Agent with container filesystem access (v0.14.0+) |
| **Handoff** | Delegate task to specialized agent |
| **Tool** | Function, MCP, or hosted tool for actions |
| **Guardrail** | Input/output safety validation |
| **Session** | Conversation history management |
| **Trace** | Execution tracking for debugging |

### Sandbox Agents

New in v0.14.0. Agents that operate in a container environment:
- Inspect files, run commands, apply patches
- Carry workspace state across long tasks
- Configurable via `Manifest` (git repos, local dirs, etc.)
- Use `UnixLocalSandboxClient` or remote sandbox providers

This is a significant evolution — agents that can do real work over extended time horizons, not just single-turn interactions.

### Provider-Agnostic Design

- Supports OpenAI Responses API and Chat Completions API
- 100+ other LLMs via any-llm and LiteLLM integrations
- MCP (Model Context Protocol) for tool calling standardization

### Tracing & Observability

Built-in tracing lets you view, debug, and optimize agent workflows. First-class support for multi-agent orchestration debugging.

## Architecture

```
Agent (config)
├── Instructions (system prompt)
├── Tools
│   ├── Function tools
│   ├── MCP tools
│   ├── Hosted tools
│   └── Agent-as-tool (handoff)
├── Guardrails (input/output)
├── Handoffs (delegate to other agents)
└── Sandbox (optional, container-based)
```

### Execution Model

```python
Runner.run_sync(agent, user_input, run_config=RunConfig(...))
# or
Runner.run_streamed(agent, user_input, run_config=RunConfig(...))
```

## When to Use

- **OpenAI-centric workflows** — tight integration with OpenAI APIs
- **Multi-agent orchestration** — built-in handoffs and agent-as-tool
- **Long-running tasks** — Sandbox Agents with container persistence
- **Production deployments** — tracing, guardrails, human-in-the-loop

## When NOT to Use

- **Pure local/offline** — designed around API-based models
- **Deep customization** — simpler but less flexible than raw API
- **Non-Python** — JS/TS version exists but separate codebase

## Comparison to Other Harnesses

| Feature | OpenAI Agents SDK | Claude Code | LangChain Agents | CrewAI |
|---------|-------------------|-------------|------------------|--------|
| Multi-agent | ✅ Handoffs | ✅ Subagents | ⚠️ Chains | ✅ Crews |
| Sandbox | ✅ v0.14.0+ | ✅ Local FS | ❌ | ❌ |
| Tracing | ✅ Built-in | ⚠️ Partial | ✅ LangSmith | ⚠️ Partial |
| Provider-agnostic | ✅ 100+ LLMs | ❌ Claude | ✅ Many | ✅ Many |
| Guardrails | ✅ Built-in | ❌ Manual | ⚠️ External | ⚠️ External |
| Human-in-loop | ✅ Built-in | ✅ Manual | ⚠️ External | ⚠️ External |
| MCP | ✅ Native | ✅ Native | ⚠️ Partial | ❌ |

## Implementation Notes

- **uv for packaging** — matches user's preference
- **Python 3.10+ required** — modern async/await
- **Optional voice support** — `openai-agents[voice]` for realtime agents
- **Optional Redis sessions** — `openai-agents[redis]` for persistence

## Limitations

1. **OpenAI bias** — provider-agnostic but OpenAI APIs are first-class
2. **Sandbox maturity** — container-based agents are new (v0.14.0)
3. **No built-in memory layer** — sessions handle history but no long-term memory
4. **Separate JS/TS codebase** — Python and JS versions diverge

## Related Concepts

- [[agent-harness]] — general harness patterns
- [[multica-relational-agent-memory]] — relational memory for multi-agent systems
- [[mcp-protocol]] — tool calling standard
- [[ai-coding-agents]] — coding agent ecosystem
