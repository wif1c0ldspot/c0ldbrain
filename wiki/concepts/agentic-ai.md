---
title: Agentic AI
type: concept
tags:
- agentic-ai
- ai-architecture
- autonomous-systems
- multi-agent
sources: [microsoft-autogen-2026-04, letta-agentic-ai-2026-04, activepieces-ai-agents-2026-04, db-gpt-ai-data-assistant-2026-04, personal-ai-infrastructure-2026-04, ml-road-agentic-ai-2026-04, ed-donner-agentic-ai-course-2026-04, panaversity-learn-agentic-ai-2026-04, goclaw-agent-gateway-2026-04, hwchase17-agent-harnesses-2026-04]
created: '2026-04-10'
updated: '2026-04-15'
confidence: high
status: current
agents:
- hermes
priority: important
summary: Agentic AI systems that act autonomously — frameworks, patterns, and
  production tools for building AI agents. Agent harnesses are the dominant pattern
  for production agents.
---

# Agentic AI

## Definition

Agentic AI refers to AI systems capable of autonomous decision-making, planning, and execution. Unlike passive LLMs that respond to prompts, agentic systems pursue goals, use tools, maintain state, and coordinate with other agents.

## Core Patterns

- **Single Agent** — One agent with tool use and memory
- **Multi-Agent** — Multiple agents collaborating on tasks
- **Human-in-the-Loop** — Agents with human oversight/approval
- **Hierarchical** — Manager agents delegating to specialist agents
- **Swarm** — Decentralized agent coordination

## Key Capabilities

- Tool use and function calling ([[mcp-protocol]])
- Persistent memory across sessions ([[memory-systems]])
- Planning and decomposition of complex tasks
- Code execution and self-modification
- Multi-agent communication and coordination

## Top GitHub Repositories (2026-04-10)

### Frameworks and Platforms

|| Repo | Stars | Focus |
|------|-------|-------|
| [[microsoft-autogen-2026-04]] | 56.9k | Multi-agent conversation framework by Microsoft |
| [[letta-agentic-ai-2026-04]] | 21.9k | Stateful agents with advanced memory (from MemGPT) |
| [[activepieces-ai-agents-2026-04]] | 21.6k | AI workflow automation with 400+ MCP integrations |
| [[db-gpt-ai-data-assistant-2026-04]] | 18.5k | Agentic AI data assistant with text-to-SQL |

### Infrastructure and Integration

|| Repo | Stars | Focus |
|------|-------|-------|
| [[personal-ai-infrastructure-2026-04]] | 11.2k | Personal AI infrastructure for human amplification |
| risingwavelabs/risingwave | — | Event streaming platform for agentic AI |
| grab/cursor-talk-to-figma-mcp | — | MCP integration between AI agents and Figma |
| memgraph/memgraph | — | Graph database for GraphRAG and agent memory |

### Education and Resources

|| Repo | Stars | Focus |
|------|-------|-------|
| [[ml-road-agentic-ai-2026-04]] | 4.7k | ML and agentic AI learning roadmap |
| [[ed-donner-agentic-ai-course-2026-04]] | 4.6k | Complete agentic AI engineering course |
| [[panaversity-learn-agentic-ai-2026-04]] | 4.1k | Agent-native cloud technologies curriculum |
| nibzard/awesome-agentic-patterns | — | Curated agentic AI patterns catalog |

## GoClaw Agent Gateway (from goclaw-agent-gateway-2026-04)

Multi-tenant AI agent gateway in Go (2.7k stars):
- 8-stage processing pipeline with pluggable middleware
- 3-tier memory: short-term, working, long-term (Knowledge Vault)
- 20+ LLM providers, 7 messaging channels
- Production reference architecture for agent gateways

## Agent Harness Ecosystem Evolution (from hwchase17-agent-harnesses-2026-04)

Agent harnesses have become the dominant pattern for building production agents. A harness provides the scaffolding that turns a raw LLM into a functional agent.

### Evolution Timeline (2022-2026)

| Era | Pattern | Representative Tools | Characteristics |
|-----|---------|----------------------|-----------------|
| **2022** (ChatGPT era) | Simple RAG chains | LangChain | Basic retrieval + generation |
| **2023** (Better models) | Complex flows | LangGraph | Multi-step workflows, state machines |
| **2024-2026** (Current) | Scaffolding with harnesses | Claude Code, Deep Agents, Letta, Pi | Full-featured agent platforms with integrated memory, tools, and state |

### Why Harnesses Dominated

- **Intimate tie to memory**: Managing context is a core harness responsibility, not a plugin
- **Lock-in concerns**: Closed harnesses (proprietary APIs) mean yielding control of agent's memory
- **Memory is in its infancy**: No well-established abstractions yet — harnesses provide structure
- **Tool integration via MCP**: Harnesses orchestrate multiple tools via standardized protocol

### Notable Agent Harnesses (2026)

| Harness | Owner | Focus | Notable Feature |
|---------|-------|-------|-----------------|
| **Claude Code** | Anthropic | Coding agent | Deep filesystem integration |
| **Deep Agents** | LangChain | Deep thinking agents | MCP-based extensibility |
| **Letta** | Letta AI | Stateful agents | Advanced memory management |
| **Pi** | Open Source | General-purpose | Open protocol |
| **OpenClaw** | OpenClaw | Enterprise-grade | Multi-tenant gateway |
| **OpenCode** | OpenCode.ai | Coding harness | Open alternative |
| **Codex** | OpenAI | Coding | Proprietary API |

### Harness Responsibility Checklist

Per Sarah Wooders, a robust harness must answer:

- **Config loading**: How are system instructions and config files loaded into context?
- **Skill discoverability**: How is tool/skill metadata presented to the agent?
- **Self-modification**: Can agents modify their own system instructions?
- **Compaction semantics**: What survives context compaction, what's lost?
- **Interaction storage**: Are interactions stored and made queryable?
- **Memory metadata**: How is memory metadata presented for relevance?
- **Filesystem exposure**: How much filesystem information is exposed?
- **Working directory**: How is the current working directory represented?

### Key Insight: Memory is Not a Plugin

"Ultimately, how a harness manages context and state in general is the foundation for agent memory." — Sarah Wooders

Memory is to a harness what driving is to a car — you can't bolt it on later; it's integral to the design.

## Related Concepts

- [[ai-coding-agents]] — AI agents for software development
- [[mcp-protocol]] — Tool integration standard for agents
- [[memory-systems]] — Persistent state management for agents
- [[hermes-agent-architecture]] — This agent's own architecture
- [[skill-registry]] — Agent capability discovery
- [[coral-multi-agent-discovery]] — Multi-agent orchestration
- [[hermes-atropos-environments]] — Training environments for agents

## Sources

- [[microsoft-autogen-2026-04]]
- [[letta-agentic-ai-2026-04]]
- [[activepieces-ai-agents-2026-04]]
- [[db-gpt-ai-data-assistant-2026-04]]
- [[personal-ai-infrastructure-2026-04]]
- [[ml-road-agentic-ai-2026-04]]
- [[ed-donner-agentic-ai-course-2026-04]]
- [[panaversity-learn-agentic-ai-2026-04]]
- [[goclaw-agent-gateway-2026-04]]

- [[agency-agents]]
- [[agent-architecture]]
- [[agent-infrastructure]]
- [[agent-memory-two-camps-witcheer-2026-04]]
- [[ai-engineering]]
- [[alibaba-gui-agent-web-control-2026-03]]
- [[aster-agentic-scaling]]
- [[autogenesis-self-evolving-agent-protocol-2026-04]]
- [[automation]]
- [[claude-35-evaluation-2025]]
- [[claude-caveman-token-strategy-2026-04]]
- [[claude-code-patterns]]
- [[claude-md]]
- [[claude-md-best-practices]]
- [[claude-skills]]
- [[completeness-principle]]
- [[context-substrate]]
- [[daily-research-agentic-memory-2026-04-18]]
- [[emergent-strategies]]
- [[escalation-protocol]]
- [[herakles-skill-chaining-2025]]
- [[hwchase17-agent-harnesses-2026-04]]
- [[karpathy-personal-kb-agents-2026-04]]
- [[karpathy-self-improving-second-brain-2026-04]]
- [[llm-knowledge-base-pattern]]
- [[llm-optimized-wiki]]
- [[personal-automation]]
- [[quantization-techniques]]
- [[resolver-pattern]]
- [[resolvers]]
- [[skill-composition-procedural-learning]]
- [[supersession-protocol]]
- [[token-optimization-and-efficiency]]
- [[user-sovereignty]]
- [[web-scraping]]
- [[weekly-synthesis-async-subagent-2026-04-17]]
- [[ai-security]]
- [[homeassistant-agent-setup]]