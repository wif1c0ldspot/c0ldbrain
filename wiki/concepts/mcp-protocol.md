---
title: MCP Protocol
type: concept
tags: [mcp-protocol, ai-agents, security]
sources:
- mempalace-github-2026-04
- markitdown-microsoft-2026-04
- contextplus-mcp-2026-04
- hwchase17-agent-harnesses-2026-04
- building-agents-mcp-production
created: '2026-04-06'
updated: '2026-04-15'
confidence: high
status: current
agents: [hermes, claude, codex]
priority: critical
summary: MCP protocol for AI agent tool connectivity and MemPalace's 19-tool server.
  Standard model-agnostic interface. Tool poisoning is critical security risk. Agent
  harnesses like Deep Agents use MCP for extensibility.
---


# MCP Protocol

## Summary

Model Context Protocol — standardized way for AI agents to connect to external tools. Any LLM can use any MCP server. MemPalace implements 19 MCP tools for Claude/Cursor integration.

## What Is It?

Standardized protocol for AI agent tool connectivity:
- One MCP server = one set of tools for the agent
- Agents can have multiple MCP servers
- Any LLM can use any MCP server (model-agnostic)
- Standard input/output: tools take parameters, return structured results

## Critical Security Risk: Tool Poisoning

- Malicious MCP server can leak SSH keys, API keys, secrets
- Agent reads ALL connected MCP servers
- Compromised server can poison agent context
- **Must audit MCP servers before adding them**

## Notable MCP Tools

| Project | Description | Trending |
|---------|-------------|----------|
| FastAPI-MCP | Build MCP servers with FastAPI | Yes |
| Deep Agents (LangChain) | Turn any LLM into deep thinking agent with MCP tools | Yes |
| MCP Server Builder | Build servers that give agents new capabilities | Yes |
| MarkItDown MCP | Microsoft file-to-Markdown converter with MCP server (109k stars) | Yes |
| Context+ | MCP server for code intelligence with Tree-sitter AST and RAG memory graph (1.8k stars) | Yes |

## Agent Harnesses and MCP (from hwchase17-agent-harnesses-2026-04)

Agent harnesses like Deep Agents use MCP protocol for extensibility. This creates a natural synergy:

- **Harnesses** provide the core scaffolding: memory management, context orchestration, state persistence
- **MCP servers** provide modular, pluggable tools that extend harness capabilities

This separation aligns with the insight that **memory is a harness responsibility, not a plugin** — while tools (via MCP) remain modular and pluggable.

Critical questions for harnesses integrating with MCP:
- How are MCP tool results represented in context and memory?
- What survives context compaction when multiple MCP servers are active?
- How is MCP tool metadata presented to the agent for discoverability?

## Related Concepts

- [[openchronicle]] — Local-first memory system with MCP endpoint for agents
- [[prompt-injection-comprehensive-2026]], [[ai-coding-agents]], [[token-optimization]], [[agent-cli-tools]]

- [[activepieces-ai-agents-2026-04]]
- [[agentic-ai]]
- [[ai-agents-handbook-2026]]
- [[autogenesis-self-evolving-agent-protocol-2026-04]]
- [[claude-code]]
- [[cli-vs-mcp-debate]]
- [[contextplus-mcp-2026-04]]
- [[coral-multi-agent-discovery]]
- [[design-md]]
- [[design-md-google-labs-2026-04]]
- [[function_name]]
- [[gbrain-agent-brain]]
- [[github-agent-repos-roundup-gittrend-2026-04]]
- [[github-ai-tools-roundup-2026-04]]
- [[goclaw-agent-gateway-2026-04]]
- [[hermes-agent-architecture]]
- [[hermes-agent-practitioners-reference-2026]]
- [[hermes-kanban-bridge]]
- [[hwchase17-agent-harnesses-2026-04]]
- [[knowledge-management-handbook-2026]]
- [[langflow-claude-code-integration]]
- [[letta-agentic-ai-2026-04]]
- [[markitdown-microsoft-2026-04]]
- [[memory-systems]]
- [[mempalace-github-2026-04]]
- [[microsoft-autogen-2026-04]]
- [[open-source-ai-infra]]
- [[openai-agents-sdk]]
- [[openchronicle-einsia-2026-04]]
- [[panaversity-learn-agentic-ai-2026-04]]
- [[context-engineering-handbook-2026]]
- [[rohit4verse-claude-code-architecture-2026-04]]
- [[simplemem-github-2026-04]]
- [[anthropic-adk-4layer-multiagent-framework-cyrilxbt-2026-04]] — ADK bidirectional MCP integration
- [[agent-development-kit]] — ADK toolkit
