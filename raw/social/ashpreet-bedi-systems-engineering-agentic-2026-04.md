---
title: "Systems Engineering: The Key To Building Agentic Software That Works"
author: Ashpreet Bedi
source_url: https://www.ashpreetbedi.com/articles/systems-engineering
x_url: https://x.com/ashpreetbedi/status/2041568919085854847
date: 2026-04-14
tags: [ai-agents, systems-engineering, agent-architecture, infrastructure, source]
---

# Systems Engineering: The Key To Building Agentic Software That Works

**Author:** Ashpreet Bedi (Software Engineer at Agno, ex-Airbnb, ex-Facebook)
**Published:** April 14, 2026

## Core Thesis

In the early 1940s, Bell Labs was building the national telephone network — the most complex technical system in the world. Millions of switches, cables, relays, and operators had to work together. The engineers discovered an 80-year-old lesson: **you can't optimize a system by optimizing individual components.** The behavior of the whole (call routing, reliability, capacity, cost) emerged from how the parts interacted. They needed a discipline focused on the interactions between components.

They called it **systems engineering**.

Coding agents have lowered the barrier to writing code, but they haven't lowered the requirements of production software. Software engineering is, and has always been, systems engineering — and agentic software is no different.

## The Five Layers of Agentic Software

### 1. Agent Engineering
Your agent or multi-agent logic and execution flow. Model, system instructions, tool configurations, handoffs, context management, observability. This is where you define what your agent does, how it runs, and how it responds. Your agent's behavior should be **deterministic where possible and observable where it isn't**.

### 2. Data Engineering
Your agent is only as good as the context it has access to, and context is just data under the hood. Call it memory, storage, knowledge — your Agent's data should be managed with data engineering principles. Well-designed schemas, structured querying, databases for fast read/writes, object storage for long-term storage, and workflows that keep your knowledge and memory up to date. **The patterns are decades old. Use them.**

### 3. Security Engineering
Auth, RBAC, governance, data isolation, audit trails. Your agent's capabilities are defined by its tools, and those tools should be scoped with JWT-backed permissions. Read-only access IS NOT a prompt instruction — it's a tool configuration. Actions should have approval tiers: reads run freely, writes need user approval, sensitive operations need admin sign-off. Most actions should be logged and queryable for the life of the product. **One user's context bleeding into another's is a data breach, not a "bug".**

### 4. Interface Engineering
How users and other agents reach your agent. REST API, Slack, MCP server, terminal, Chat UI. In the old world, you had one API and one client. Now you have multiple surfaces, each with its own identity system. A Slack user ID is not your product's user ID. An MCP client authenticating as another agent is not a human user. Interface engineering is about making sure your auth, policies, and access controls hold consistently across every surface.

### 5. Infrastructure Engineering
How you run and scale your software. Containers, cloud deployment, horizontal scaling. 95% of this is identical to running any other service. The 5% that's different: agent requests take longer (increase load balancer timeouts), responses stream (plan for SSE or WebSockets), and the best agents are proactive (scheduled tasks, background execution).

## Key Insight

The key unlock for AI engineers is realizing that **agentic software is just regular software, with the business logic replaced by agents, and interfaces going from request/response to streaming across multiple surfaces.**

When you design one layer in isolation, you inherit constraints that cascade through the rest of the system. When you design from the system's perspective, each layer reinforces the others.

## Practical Example: Dash

Dash is an open-source, self-learning data agent by Agno that demonstrates all five layers:

- **Agent:** Three agents — Leader routes to Analyst (read-only SQL) and Engineer (writable SQL). Same interface, different permissions by configuration, not prompts.
- **Interface:** REST API, Slack bot, web UI, CLI. All hit same agents, same tools, same knowledge.
- **Data:** Six layers of context — table metadata, human annotations, query patterns, institutional knowledge, learnings, runtime context. Curated knowledge in PostgreSQL + discovered learnings auto-saved.
- **Security:** RBAC with JWT. Queries scoped to user_id. Eval suite tests boundaries directly. Read-only is a PostgreSQL connection parameter, not a prompt.
- **Infrastructure:** Standard Python container, Docker Compose, one-command cloud deployment, SSE streaming.

## TLDR

Agentic software is just software. The agent replaces business logic. Everything else is systems engineering. Five layers: agent, data, security, interface, infrastructure. Each layer affects the others. Design them together and the system compounds. Design them in isolation and you spend your time patching around constraints that shouldn't exist.
