---
title: "Systems Engineering: The Key To Building Agentic Software That Works"
type: source
tags: [ai-agents, systems-engineering, agent-architecture, infrastructure, source]
created: '2026-04-26'
updated: '2026-04-26'
confidence: high
status: current
priority: important
summary: "Ashpreet Bedi argues agentic software is systems engineering — five layers (agent, data, security, interface, infrastructure) must be designed together or the system fights itself."
source_url: https://www.ashpreetbedi.com/articles/systems-engineering
compiled: true
---

# Systems Engineering: The Key To Building Agentic Software That Works

**Author:** Ashpreet Bedi (Software Engineer at Agno, ex-Airbnb, ex-Facebook)
**Published:** April 14, 2026
**Source:** [ashpreetbedi.com](https://www.ashpreetbedi.com/articles/systems-engineering) | [X Post](https://x.com/ashpreetbedi/status/2041568919085854847)

## Core Thesis

Bell Labs discovered in the 1940s that **you can't optimize a system by optimizing individual components** — behavior emerges from interactions. They called this discipline systems engineering. The same principle applies to agentic software: coding agents lower the barrier to writing code, but they don't lower the requirements of production software.

**Agentic software is just regular software, with the business logic replaced by agents, and interfaces going from request/response to streaming across multiple surfaces.**

## The Five Layers

### 1. Agent Engineering
- Multi-agent logic and execution flow
- Model, system instructions, tool configurations, handoffs, context management, observability
- **Behavior should be deterministic where possible, observable where it isn't**
- See also: [[agent-architecture]], [[multi-agent-collaboration]]

### 2. Data Engineering
- Context is just data — apply data engineering principles
- Well-designed schemas, structured querying, databases for fast read/writes
- Object storage for long-term, workflows keeping knowledge up to date
- "The patterns are decades old. Use them."
- See also: [[rag]], [[memory-systems]], [[knowledge-management]]

### 3. Security Engineering
- JWT-backed permissions, RBAC, governance, data isolation, audit trails
- Read-only access is a tool configuration, NOT a prompt instruction
- Approval tiers: reads run freely, writes need user approval, sensitive ops need admin sign-off
- One user's context bleeding into another's is a data breach, not a bug
- See also: [[ai-security]], [[prompt-injection]]

### 4. Interface Engineering
- Multiple surfaces (REST API, Slack, MCP, terminal, Chat UI) each with own identity system
- Auth, policies, and access controls must hold consistently across every surface
- A Slack user ID ≠ your product's user ID; MCP client ≠ human user
- See also: [[mcp-protocol]], [[api-design]]

### 5. Infrastructure Engineering
- 95% identical to running any other service — reuse existing patterns
- The 5% different: longer timeouts (agent requests), SSE/WebSockets (streaming), scheduled tasks (proactive agents)
- Standard containers, Docker Compose, cloud deployment
- See also: [[agent-infrastructure]], [[developer-tools]]

## Practical Example: Dash (Agno)

Open-source self-learning data agent demonstrating all five layers:
- **Agent:** Leader + Analyst (read-only SQL) + Engineer (writable SQL). Permissions by config, not prompts
- **Interface:** REST API, Slack bot, web UI, CLI — same agents/tools/knowledge
- **Data:** Six context layers — table metadata, annotations, query patterns, institutional knowledge, learnings, runtime context
- **Security:** RBAC + JWT. Read-only is a PostgreSQL connection parameter. Eval suite tests boundaries
- **Infrastructure:** Python container, Docker Compose, one-command deploy

## Key Quotes

> "When you design one layer in isolation, you inherit constraints that cascade through the rest of the system. When you design from the system's perspective, each layer reinforces the others."

> "Query 100 is better than query 1, not because the model improved, but because the data layer got better."

> "Security is a system property tested across layers."
