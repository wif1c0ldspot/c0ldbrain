---
compiled: 2026-04-15
confidence: high
created: '2026-04-16'
priority: important
source_url: https://github.com/ForLoopCodes/contextplus
stars: 1.8k
status: current
summary: 1.8k star MCP server for code intelligence. Tree-sitter AST parsing, RAG
  memory graph, and Obsidian-style bidirectional linking for codebases.
tags:
- mcp-protocol
- token-optimization
- knowledge-management
- developer-tools
title: Context+ — MCP Code Intelligence Server
type: source
updated: '2026-04-18'
---


# Context+ — MCP Code Intelligence Server

## Key Insights

- MCP server providing deep code intelligence for AI coding agents
- Tree-sitter-based AST parsing for structural code understanding
- RAG memory graph that persists across sessions
- Obsidian-style bidirectional linking between code entities
- Directly reduces token usage by providing structured code context

## Technical Details

### Tree-sitter AST Integration
- Parses code into abstract syntax trees
- Provides agents with structural understanding, not just text
- Supports 40+ programming languages via Tree-sitter grammars
- Incremental parsing for real-time updates

### RAG Memory Graph
- Persistent graph of code entities and their relationships
- Functions, classes, modules, imports — all linked
- Survives across coding sessions
- Reduces need to re-read entire codebases

### Obsidian-Style Linking
- Bidirectional links between code entities (like wiki backlinks)
- `[[function_name]]` style references agents can follow
- Discover related code through link traversal
- Compatible with Obsidian graph visualization

### MCP Protocol
- Standard MCP server interface
- Compatible with Claude Code, Cursor, and any MCP-enabled agent
- Tools: search_code, get_definition, find_references, get_call_graph
- Reduces token waste by returning structured results instead of raw text

## Related Concepts

- [[mcp-protocol]] — implements MCP server interface
- [[token-optimization]] — structured code context reduces token usage
- [[llm-knowledge-bases]] — knowledge graph approach applied to codebases
- [[code-review-graph]] — similar Tree-sitter-based code indexing approach
