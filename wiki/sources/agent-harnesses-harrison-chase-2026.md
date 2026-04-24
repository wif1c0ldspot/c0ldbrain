---
author: Harrison Chase (@hwchase17)
confidence: medium
created: '2026-04-16'
date_added: 2026-04-12
priority: reference
status: compiled
summary: Agent Harnesses — Harrison Chase
tags:
- agentic-architecture
- agent-memory
- agent-harnesses
- open-source
- vendor-lock-in
title: Agent Harnesses Are How You Build Agents (And They're Not Going Anywhere)
type: source
updated: '2026-04-18'
url: https://x.com/hwchase17/status/2042978500567609738
compiled: true
---


# Agent Harnesses — Harrison Chase

## Key Claims

- Agent harnesses are the dominant pattern for building agents and are not going away
- Harnesses are intimately tied to agent memory
- Using a closed harness (especially behind a proprietary API) means yielding control of your agent's memory to a third party
- Memory creates incredible vendor lock-in
- Memory and harnesses should be open so you own your memory

## Evolution of Agentic Patterns

1. Simple RAG chains (LangChain era)
2. Complex flows (LangGraph era)
3. Agent harnesses (current era)

## Examples of Agent Harnesses

- Claude Code (512k lines of code — leaked)
- Deep Agents (LangChain)
- Pi / OpenClaw
- OpenCode
- Codex
- Letta Code

## Key Arguments

### Harnesses Are Not Going Away
Some sentiment that models will absorb scaffolding over time is wrong. The scaffolding needed in 2023 has been replaced by other types of scaffolding. An agent, by definition, is an LLM interacting with tools and other sources of data. There will always be a system around the LLM to facilitate that interaction.

Even web search built into OpenAI/Anthropic APIs is not "part of the model" — it's a lightweight harness behind the API orchestrating the model with tool calling.

### Memory Is a Harness Responsibility, Not a Plugin
Per Sarah Wooders: "Asking to plug memory into an agent harness is like asking to plug driving into a car."

Memory management questions the harness handles:
- How is AGENTS.md / CLAUDE.md loaded into context?
- How is skill metadata shown to the agent?
- Can the agent modify its own system instructions?
- What survives compaction, what's lost?
- Are interactions stored and made queryable?
- How is memory metadata presented?
- How is the current working directory represented?
- How much filesystem info is exposed?

Memory is still in its infancy — long-term memory is often not part of MVP. No well-known common abstractions exist yet.

"If you don't own your harness, you don't own your memory."

### Risks of Closed Harnesses

1. **Stateful APIs** (OpenAI Responses API, Anthropic server-side compaction): storing state on their server. Can't swap models and resume previous threads.
2. **Closed harnesses** (Claude Agent SDK / Claude Code not open source): interact with memory in unknown ways. Artifacts are non-transferable between harnesses.
3. **Unknown artifact shapes**: when harness memory management is opaque, you can't replicate or migrate it.

## Related Concepts

- Agent harness architecture
- Agent memory systems
- Context management
- Vendor lock-in
- Open vs closed source agent frameworks
- AGENTS.md / CLAUDE.md patterns

## Quotes

> "Memory is just a form of context. Short term memory (messages in the conversation, large tool call results) are handled by the harness. Long term memory (cross session memory) needs to be updated and read by the harness."

> "Ultimately, how the harness manages context and state in general is the foundation for agent memory." — Sarah Wooders
