---
title: "SimpleMem: Efficient Lifelong Memory for LLM Agents"
type: source
tags: [memory-systems, tools, mcp, github, open-source]
created: '2026-04-19'
updated: '2026-04-19'
confidence: high
status: current
priority: medium
summary: "SimpleMem — efficient lifelong memory framework with MCP server. 3,259 stars. Text + multimodal (Omni-SimpleMem). Cloud-hosted at mcp.simplemem.cloud."
source_url: "https://github.com/aiming-lab/SimpleMem"
sources:
- simplemem-github-2026-04
---

# SimpleMem: Efficient Lifelong Memory for LLM Agents

**GitHub**: github.com/aiming-lab/SimpleMem
**Stars**: 3,259 | **Forks**: 328
**MCP Server**: mcp.simplemem.cloud

## What It Is

A family of efficient memory frameworks based on **semantic lossless compression**:
- **SimpleMem**: Text-based memory for LLM agents
- **Omni-SimpleMem**: Multimodal (text, image, audio, video)

## Key Features

1. **Semantic Lossless Compression**: Consistently outperforms baselines in accuracy, retrieval efficiency, and inference cost
2. **MCP Server**: Cloud-hosted, implements Streamable HTTP transport (MCP 2025-03-26 spec)
3. **Integrations**: LM Studio, Cherry Studio, Cursor, Claude Desktop
4. **PyPI Package**: `pip install simplemem`

## MCP Server Details

- Hosted at mcp.simplemem.cloud
- OpenRouter API key required for creation
- Personal memory server instance
- Streamable HTTP MCP protocol

## Camp Classification

**Camp 1 (Memory Backend)**: Focus on storage and retrieval with compression optimization.

## Related Concepts

- [[memory-systems]] — Hub for agent memory patterns
- [[mcp-protocol]] — MCP integration pattern

## Sources

- [GitHub: aiming-lab/SimpleMem](https://github.com/aiming-lab/SimpleMem)
- [SimpleMem MCP Server](https://mcp.simplemem.cloud/)
- [OpenReview: SimpleMem](https://openreview.net/forum?id=dbZAi4hmwg)
- [PyPI: simplemem](https://pypi.org/project/simplemem/)
