---
title: "Anthropic's 4-Layer Multi-Agent Framework: ADK + MCP + A2A + Agent Engine"
type: source
tags: [ai-agents, agent-architecture, multi-agent, mcp-protocol, a2a, adk, anthropic, google-cloud, source]
created: '2026-04-26'
updated: '2026-04-26'
confidence: high
status: current
priority: important
summary: "CyrilXBT recaps Anthropic/Google presentation on production-grade multi-agent systems: 4-layer stack (LlmAgent → Runner → MCP → Agent Engine), ADK toolkit, A2A protocol for inter-agent communication, and Vertex AI deployment."
source_url: https://x.com/cyrilXBT/status/2048262079925154192
compiled: true
---

# Anthropic's 4-Layer Multi-Agent Framework

**Source:** Video by @CyrilXBT (April 26, 2026) — 30 min presentation
**Presenter:** Ivan Nardini (AI/ML Developer Advocate, Google Cloud AI)
**Original event:** Google/Anthropic joint presentation
**Engagement:** 984 likes, 98 RTs, 96K views

## The Problem Statement

Building AI agents is **powerful but complex**. Three pain points:

1. **Fragmented landscape** — How do we achieve faster development and iteration?
2. **Hard to integrate** — How do we manage dependencies, delegate effectively, and avoid hard-to-debug workflows between agents?
3. **Lack of ops & governance** — How do we reliably deploy, scale, monitor, and govern an ecosystem of agents?

## The 4-Layer Agentic Stack

### Layer 1: LlmAgent (The Brain)

The core agent building block. A wrapper around LLMs with:

| Parameter | Purpose |
|-----------|---------|
| `name` | Agent identifier |
| `model` | Underlying LLM (Claude, Gemini, open models) |
| `instruction` | System prompt / behavioral guidelines |
| `tools` | Available capabilities (Python functions) |

**Key principle:** ADK auto-handles schema generation for the LLM — write Python functions, the framework converts them to tool schemas automatically.

### Layer 2: Tools + Runner (Execution)

**FunctionTool:** Python functions exposed as agent capabilities. ADK generates JSON schemas automatically — no manual schema writing.

**Runner:** The execution engine:
- Runs the agent (via `ADK run` CLI or `ADK web` interface)
- Manages session state (conversation history)
- Handles execute/cancel lifecycle

**Session & State:**
- Session = conversation boundary
- State = dictionary for passing data within a session
- Enables intra-agent memory and inter-agent communication via shared state

### Layer 3: MCP (Model Context Protocol)

**Bidirectional ADK ↔ MCP integration:**

| Direction | Pattern | Use Case |
|-----------|---------|----------|
| ADK → MCP | ADK agent as MCP client | Consume existing MCP servers without rewriting tools |
| MCP → ADK | ADK tools as MCP server | Expose ADK tools to non-ADK MCP clients |

Example: Calendar Service Agent connects to external MCP Calendar Service, fetches tools dynamically, configures Claude 3.7 Sonnet with calendar management capabilities.

```python
async def create_calendar_service_agent():
    # Connect to external MCP Calendar Service
    tools = await MCPClient.fetch_tools("calendar-mcp-service")
    agent = LlmAgent(
        name="calendar_service",
        model="claude-3.7-sonnet",
        instruction="Manage calendar events...",
        tools=tools
    )
```

### Layer 4: Agent Engine (Deployment)

Vertex AI Agent Engine handles production deployment:

**Without Agent Engine:**
- Build FastAPI/Django server for HTTP API
- Docker container + GCP config manually
- User manages all ops (scaling, regions, vulnerabilities)
- Manual logging/monitoring/tracing

**With Agent Engine:**
- `agent_engines.create()` via Vertex AI SDK
- Deployed to tenant project with auto-scaling
- Built-in Cloud Logging, Monitoring, Tracing
- Integrated Vertex AI Gen AI Evaluation

```python
remote_app = agent_engine.create_agent(
    agent_id="birthday-planner",
    agent=birthday_planner_agent,
    requirements=["google-cloud-aiplatform[adk]==1.93.0", "anthropic[vertex]==0.51.0"],
    display_name="BirthdayPlannerAgent",
    description="Plans birthday events"
)
```

## Multi-Agent Architecture Demo: Event Management System

The demo builds a 3-agent event planning system:

```
CODE_WITH_CLAUDE/
├── birthday_planner_agent/
│   ├── agent.py              # Single agent
│   └── .env
├── event_management_local_agent_system/
│   ├── agents/
│   │   ├── birthday_planner.py   # Planner agent
│   │   ├── calendar_service.py   # Calendar agent (MCP)
│   │   └── event_organizer.py    # Organizer agent
│   └── tools/
│       └── agent.py
├── event_management_remote_agent_system/
│   ├── deploy_agents.py      # Deployment script
│   └── call_remote_agent.py  # A2A remote calls
```

**Agent topology:**
1. **BirthdayPlannerAgent** — Plans events (worker)
2. **Calendar Service Agent** — Manages calendar via MCP tools
3. **Event Organizer** — Coordinates and delegates to other agents

**Deployment flow:**
1. HTTP POST to MCP Calendar Service → fetch tools
2. Initialize Calendar Service Agent with MCP tools
3. Define Organizer Agent
4. Deploy to Vertex AI Agent Engine (us-central1)
5. Worker agents deployed individually with dependency management

## A2A (Agent-to-Agent Protocol)

Referenced on presenter's laptop (A2A sticker) and in the remote agent system. Enables:
- Agents communicating across different vendors/platforms
- Remote agent calls via `call_remote_agent.py`
- Standardized capability discovery and task management

## Key Dependencies (from deployment)

- `google-cloud-aiplatform[adk, agent_engines]==1.93.0`
- `anthropic[vertex]==0.51.0`
- `fastmcp==2.3.4`
- `pydantic==2.11.4`
- `cloudpickle==3.1.1`

## Key Takeaways

1. **Agentic stack = MCP + ADK** — Protocol layer + Development layer
2. **Production = Agent Engine** — One SDK call replaces entire DevOps pipeline
3. **Multi-agent = Local + Remote** — ADK handles both local agent systems and remote A2A communication
4. **MCP is bidirectional** — ADK can both consume and expose MCP tools
5. **Schema generation is automatic** — Write Python functions, ADK handles the rest

## Related Concepts

- [[agent-architecture]] — Agent design patterns
- [[multi-agent-collaboration]] — Multi-agent coordination
- [[mcp-protocol]] — Model Context Protocol
- [[systems-engineering]] — Systems thinking for agents
- [[agno-harness-vs-systems-engineering-2026-04]] — Complementary systems perspective
- [[ashpreet-bedi-systems-engineering-agentic-2026-04]] — 5-layer systems engineering framework
