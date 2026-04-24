---
title: Building agents that reach production systems with MCP
type: source
tags:
- agents
- mcp
- production
- claude
- anthropic
- agent-infrastructure
source_url: https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
sources: []
created: '2026-04-22'
updated: '2026-04-23'
confidence: high
status: current
agents:
- hermes
priority: medium
summary: "Anthropic's guide to connecting production agents to external systems via MCP, covering server design patterns, context efficiency, and skills integration."
---

# Building agents that reach production systems with MCP

## Summary

Anthropic's official guide (April 2026) on why production agents converge on MCP over direct API calls or CLIs. Covers server design patterns (intent-grouped tools, code orchestration, rich semantics), client context-efficiency techniques (tool search, programmatic calling), and how skills complement MCP servers. MCP SDKs now exceed 300M monthly downloads.

## Key Details

### Three integration paths compared
- **Direct API calls**: Fine for 1:1 agent-service pairs. Scales poorly (M×N integration problem) — bespoke auth, descriptions, edge cases per pair.
- **CLI**: Fast, lightweight, common layer. Limited to local/sandboxed environments with filesystem+shell. Fails on mobile/web/cloud-hosted agents.
- **MCP**: Protocol-level common layer. Standardized auth, discovery, rich semantics. One remote server reaches any compatible client (Claude, ChatGPT, Cursor, VS Code) in any deployment environment.

### MCP adoption metrics
- MCP SDKs: 300M+ monthly downloads (up from 100M at start of 2026)
- 200+ MCP servers in Anthropic directory
- Millions use MCP with Claude daily
- Powers: Claude Cowork, Claude Managed Agents, channels in Claude Code

### Building effective MCP servers

**1. Build remote servers for maximum reach**
- Only configuration that runs across web, mobile, and cloud-hosted agents
- Every major client optimized to consume remote servers

**2. Group tools around intent, not endpoints**
- Fewer, well-described tools outperform exhaustive API mirrors
- Example: `create_issue_from_thread` beats `get_thread` + `parse_messages` + `create_issue` + `link_attachment`
- Reference: [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)

**3. Design for code orchestration when surface is large**
- For services with hundreds of operations (Cloudflare, AWS, K8s), expose thin tool surface that accepts code
- Agent writes script → server runs in sandbox → only result returns
- Cloudflare MCP server: 2 tools (search + execute) cover ~2,500 endpoints in ~1K tokens

**4. Ship rich semantics where they help**
- **MCP Apps**: First official protocol extension. Tools return interactive UI (charts, forms, dashboards) rendered inline. Higher adoption/retention than text-only servers.
- **Elicitation**: Server pauses mid-tool call to ask user input
  - *Form mode*: Client renders native form for missing params, confirmations, disambiguation
  - *URL mode*: Hands user to browser for OAuth, payments, sensitive credentials
- **Standardized auth**: OAuth with CIMD (Client ID Metadata Documents) for fast first-time auth and fewer re-auth prompts
- **Vaults** (Claude Managed Agents): Register OAuth tokens once, reference by ID at session creation. Platform injects credentials into each MCP connection and refreshes automatically

### Making MCP clients context-efficient

**Tool search**
- Defers loading all tools into context. Agent searches catalog at runtime, pulls relevant tools when needed
- Cuts tool-definition tokens by 85%+ while maintaining high selection accuracy

**Programmatic tool calling**
- Processes tool results in code-execution sandbox instead of returning raw to model
- Agent loops, filters, aggregates across calls in code; only final output reaches context
- Reduces token usage by ~37% on complex multi-step workflows

### Pairing MCP servers with skills

**Skills + MCP are complementary**
- MCP = access to tools/data from external systems
- Skills = procedural knowledge of how to use those tools
- Two patterns:
  1. **Bundle as plugin**: Skills + MCP servers + hooks + LSP + subagents in one distribution. Example: data plugin for Cowork (10 skills + 8 MCP servers for Snowflake, Databricks, BigQuery, Hex, etc.)
  2. **Distribute skills from MCP server**: Provider publishes skill alongside MCP server. Canva, Notion, Sentry do this today. Community working on extension to deliver skills directly from servers for portability across clients

### The compounding layer
- Mature integrations ship all three: API (foundation), CLI (local-first), MCP (cloud-based agents)
- MCP is the compounding layer — same server gets more capable as more clients adopt spec and extensions land

## Related Links
- [MCP SDKs](https://modelcontextprotocol.io/docs/sdk)
- [Claude Cowork](https://claude.com/product/cowork)
- [Claude Managed Agents](https://claude.com/blog/claude-managed-agents)
- [Channels in Claude Code](https://code.claude.com/docs/en/channels)
- [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [Cloudflare MCP server](https://github.com/cloudflare/mcp)
- [Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use)

## Notes
- Directly relevant to Hermes MCP skill and native-mcp configuration
- Tool search + programmatic calling patterns could significantly reduce token usage in Hermes tool-calling loops
- Vaults pattern aligns with Hermes' credential management needs for cloud-hosted deployments
- Plugin model (skills + MCP bundled) matches Hermes' skill architecture
