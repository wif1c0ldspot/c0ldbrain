---
title: "OpenAI Agents Python SDK — GitHub Repository"
author: "@openai"
date: 2026-04-19
source: "https://github.com/openai/openai-agents-python"
type: source
tags: [openai, agent-harness, multi-agent, python, framework]
stars: 22600
forks: 3600
language: python
---

## Summary

Official OpenAI Agents SDK — a lightweight, provider-agnostic framework for building multi-agent workflows. Supports OpenAI Responses/Chat APIs plus 100+ other LLMs. 22,600+ stars, 1,351 commits, active development (last commit: 2026-04-19).

## Core Concepts

1. **Agents** — LLMs configured with instructions, tools, guardrails, and handoffs
2. **Sandbox Agents** (v0.14.0+) — agents with container filesystem access for real work over long time horizons
3. **Agents as Tools / Handoffs** — delegate to other agents for specific tasks
4. **Tools** — functions, MCP, hosted tools for agent actions
5. **Guardrails** — configurable safety checks for input/output validation
6. **Human in the loop** — built-in mechanisms for involving humans across agent runs
7. **Sessions** — automatic conversation history management across agent runs
8. **Tracing** — built-in tracking for debugging and optimization
9. **Realtime Agents** — voice agents with `gpt-realtime-1.5`

## Key Architecture Decisions

- **Provider-agnostic**: Supports OpenAI APIs + 100+ other LLMs via any-llm/LiteLLM
- **Sandbox Agents**: Container-based environments for agents to inspect files, run commands, apply patches, carry workspace state
- **MCP integration**: Uses MCP Python SDK for tool calling
- **Python 3.10+**: Modern Python, uses uv for package management
- **JS/TS version available**: Separate `openai-agents-js` repository

## Dependencies

**Core:** Pydantic, Requests, MCP Python SDK, Griffe
**Optional:** websockets, SQLAlchemy, any-llm/LiteLLM
**Dev:** uv, ruff, mypy, Pyright, pytest, Coverage.py, MkDocs

## Sandbox Agent Example

```python
from agents import Runner
from agents.run import RunConfig
from agents.sandbox import Manifest, SandboxAgent, SandboxRunConfig
from agents.sandbox.entries import GitRepo
from agents.sandbox.sandboxes import UnixLocalSandboxClient

agent = SandboxAgent(
    name="Workspace Assistant",
    instructions="Inspect the sandbox workspace before answering.",
    default_manifest=Manifest(
        entries={
            "repo": GitRepo(repo="openai/openai-agents-python", ref="main"),
        }
    ),
)

result = Runner.run_sync(
    agent,
    "Inspect the repo README and summarize what this project does.",
    run_config=RunConfig(sandbox=SandboxRunConfig(client=UnixLocalSandboxClient())),
)
```

## Open Source Ecosystem

Committed to open source — extensible framework the community can expand. Complementary to existing tools (LangChain, CrewAI, etc.) rather than replacement.

## Related Concepts

See [[openai-agents-sdk]] for concept analysis.
