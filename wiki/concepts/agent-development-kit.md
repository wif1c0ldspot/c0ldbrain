---
title: Agent Development Kit (ADK)
type: concept
tags: [ai-agents, agent-architecture, google-cloud, adk, developer-tools]
created: '2026-04-26'
updated: '2026-04-26'
confidence: high
status: current
priority: important
summary: "Open-source, code-first toolkit by Google/Anthropic for building, evaluating, and deploying AI agents. Part of the 4-layer agentic stack with MCP, A2A, and Agent Engine."
---

# Agent Development Kit (ADK)

Open-source, code-first toolkit for building, evaluating, and deploying AI agents. Developed jointly by Google and Anthropic.

## Core Components

| Component | Role | Key Detail |
|-----------|------|------------|
| LlmAgent | The brain/worker | Wraps LLM with name, model, instruction, tools |
| FunctionTool | Agent's skills | Python functions auto-converted to tool schemas |
| Runner | Execution engine | Manages sessions, runs agents (CLI or web) |
| AgentExecutor | Request processor | Execute/cancel methods for request lifecycle |
| Session & State | Memory | Session = conversation, State = data dictionary |

## MCP Integration (Bidirectional)

- **ADK as MCP Client:** Consume existing MCP servers directly
- **ADK as MCP Server:** Expose ADK tools to other MCP clients
- No rewriting needed — protocol translation handled by framework

## Deployment via Agent Engine

Single SDK call replaces entire infrastructure:
```python
agent_engines.create(agent=my_agent, requirements=[...])
```
Vertex AI handles: auto-scaling, regions, containers, logging, monitoring, tracing.

## Multi-Agent Patterns

- **Local agents:** Multiple agents in same process sharing sessions
- **Remote agents:** Deployed separately, communicate via A2A protocol
- **Coordinator pattern:** Organizer agent delegates to specialist workers

## Related

- [[mcp-protocol]] — Foundation protocol layer
- [[agent-architecture]] — General agent patterns
- [[multi-agent-collaboration]] — Multi-agent coordination
- [[anthropic-adk-4layer-multiagent-framework-cyrilxbt-2026-04]] — Source video
