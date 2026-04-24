---
compiled: 2026-04-15
confidence: high
created: '2026-04-16'
priority: 2
source_url: https://github.com/nextlevelbuilder/goclaw
stars: 2.7k
status: current
summary: 2.7k star multi-tenant AI agent gateway in Go. 8-stage pipeline, 3-tier memory,
  Knowledge Vault, 20+ LLM providers, 7 messaging channels.
tags:
- ai-agents
- mcp-protocol
- memory-systems
- infrastructure
- open-source
title: GoClaw — Multi-Tenant AI Agent Gateway
type: source
updated: '2026-04-18'
---


# GoClaw — Multi-Tenant AI Agent Gateway

## Key Insights

- Production-grade multi-tenant AI agent gateway written in Go
- 8-stage processing pipeline with pluggable middleware
- 3-tier memory architecture: short-term, working, long-term with Knowledge Vault
- Supports 20+ LLM providers and 7 messaging channels out of the box
- Significant architecture for understanding how production agent gateways work

## Technical Details

### 8-Stage Pipeline
1. Input parsing and validation
2. Context enrichment
3. Memory retrieval (3-tier)
4. LLM provider routing
5. Prompt construction
6. Model inference
7. Response processing
8. Memory storage and indexing

### 3-Tier Memory Architecture
- **Short-term**: Conversation context within a session
- **Working**: Task-relevant information across sessions
- **Long-term**: Knowledge Vault for persistent organizational knowledge

### Multi-Tenant Design
- Isolated tenant contexts and memory spaces
- Per-tenant LLM provider configuration
- Billing and usage tracking per tenant
- Role-based access control

### Integrations
- **LLM Providers**: 20+ including OpenAI, Anthropic, Google, local models
- **Messaging Channels**: 7 channels (Slack, Discord, Telegram, Web, API, etc.)
- **Knowledge Vault**: Persistent vector + graph storage

## Related Concepts

- [[agentic-ai]] — multi-agent gateway architecture
- [[mcp-protocol]] — tool connectivity compatible
- [[memory-systems]] — 3-tier memory with Knowledge Vault
