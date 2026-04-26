---
title: "Harness Engineering vs. Systems Engineering: The Mistake Killing Agentic Software"
author: Cosette Cressler (Agno)
source_url: https://www.agno.com/blog/harness-engineering-vs-systems-engineering-the-mistake-killing-agentic-software
x_url: https://x.com/suryanshti777/status/2048055574185779638
date: 2026-04-14
tags: [ai-agents, systems-engineering, agent-architecture, harness-engineering, source]
---

# Harness Engineering vs. Systems Engineering

**Author:** Cosette Cressler (Agno)
**Published:** April 14, 2026

## The Problem

A new job title is circulating: AI Engineer. But most "AI engineers" are building a pile of duct tape holding together a language model they don't own. Instead of designing cohesive systems, they wire up filesystem-backed memory, route bash commands through sandboxes, and stack abstraction on top of abstraction until the foundation collapses.

That is not engineering. It's harnessing.

## Harness vs. System

A harness engineer optimizes the tool. A systems engineer optimizes for the outcome.

The agentic ecosystem is dominated by harness engineering. Agent frameworks tell you to use the filesystem for storage, give agents broad bash access, and trust them to behave. Getting something running ≠ having software that works.

When you build harness-first, you hit walls immediately:
- Filesystems don't handle concurrent users → layer database abstraction
- Bash access introduces security risks → add per-request sandboxes
- Each tool limitation becomes another patch

The harness grows more complex, while the underlying system remains fundamentally flawed.

## Software Engineering IS Systems Engineering

Bell Labs (1940s): millions of components had to operate together at scale. They discovered optimizing individual parts does not produce an optimized system. They invented systems engineering.

We're making the same mistake 60 years later — optimizing model/prompt/tool while neglecting the system.

Agentic software = regular software + agents handling business logic. It still needs: agent logic, data, security, interfaces, infrastructure.

## Concrete Implications

**Storage:** Filesystem-backed memory can't safely isolate users. Context leaking = data breach, not a bug. Use a proper database with isolation, structured queries, decades of refinement.

**Security:** Read-only access is NOT a prompt instruction. It's a tool configuration, a PostgreSQL connection parameter. If security depends on the model behaving, you don't have real security.

**Interfaces:** One agent, many surfaces (REST, Slack, MCP, CLI). Each has different identity contexts. Slack user ID ≠ product user ID. MCP client ≠ human. Auth must be consistent across all surfaces.

## Stop Debating the Wrong Things

MCP vs. CLI, REST vs. gRPC — these are theological arguments about tools, not systems. From a systems perspective, the right tool choices follow naturally from understanding what the system actually needs.

You are not building a harness. You are building a system. Act like it.
