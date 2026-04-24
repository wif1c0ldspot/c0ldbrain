---
title: 'Autogenesis: A Self-Evolving Agent Protocol'
type: source
source_url: https://arxiv.org/abs/2604.15034
author: Wentao Zhang
created: '2026-04-16'
confidence: high
status: current
tags:
- source
- agent-protocols
- meta-optimization
- self-evolving
- arxiv
summary: Autogenesis Protocol (AGP) for self-evolving multi-agent systems - models
  prompts, agents, tools, environments, and memory as protocol-registered resources
  with lifecycle management and closed-loop evolution
priority: reference
updated: '2026-04-16'
compiled: true
---

## Metadata

| Field | Value |
|-------|-------|
| **arXiv ID** | 2604.15034 |
| **Published** | 2026-04-16 |
| **Author** | Wentao Zhang |
| **Category** | cs.AI |
| **PDF** | [arxiv.org/pdf/2604.15034](https://arxiv.org/pdf/2604.15034v1) |
| **HTML** | [arxiv.org/html/2604.15034](https://arxiv.org/html/2604.15034v1) |

## Summary

Introduces **Autogenesis Protocol (AGP)**, a self-evolution protocol for LLM-based agent systems that decouples *what evolves* from *how evolution occurs*. Addresses limitations of existing agent protocols (A2A, MCP) that under-specify cross-entity lifecycle management, context management, version tracking, and evolution-safe update interfaces.

## Key Contributions

### Two-Layer Architecture

#### Layer 1: Resource Substrate Protocol Layer (RSPL)
Models five entity types as protocol-registered resources with explicit state, lifecycle, and versioned interfaces:

| Resource Type | Description |
|---------------|-------------|
| **Prompt** | Agent system instructions and templates |
| **Agent** | Individual reasoning units |
| **Tool** | External capabilities and APIs |
| **Environment** | Execution contexts |
| **Memory** | Persistent state and outputs |

#### Layer 2: Self Evolution Protocol Layer (SEPL)
Specifies closed-loop operator interface for:

1. **Propose** — Suggest improvements to resources
2. **Assess** — Evaluate proposed changes
3. **Commit** — Apply improvements
4. **Audit** — Track lineage, enable rollback

### Autogenesis System (AGS)

Implements AGP as a multi-agent system that:
- Dynamically instantiates protocol-registered resources during execution
- Retrieves and refines resources based on task requirements
- Maintains auditable evolution history

## Key Problems Addressed

| Problem | Existing (A2A/MCP) | AGP Solution |
|---------|-------------------|--------------|
| **Monolithic composition** | Encouraged by under-specification | Decoupled resource types |
| **Brittle glue code** | Hard-coded integrations | Protocol-registered interfaces |
| **No version tracking** | Stateless interfaces | Versioned resources with lineage |
| **No evolution safety** | No rollback | SEPL commit/rollback primitives |
| **No lifecycle management** | Implicit lifecycles | Explicit state transitions |

## Evaluation

Tested on benchmarks requiring:
- Long-horizon planning
- Tool use across heterogeneous resources
- Dynamic resource management

**Results**: Consistent improvements over strong baselines.

## Relationship to C0ldbrain

### Alignment with [[agent-meta-optimization]]

AGP directly addresses the meta-optimization problem:
- **Self-improving agents** that evolve their own prompts and tools
- **Versioned resources** enabling safe experimentation
- **Closed-loop evaluation** for continuous improvement

### Alignment with [[mcp-protocol]]

AGP extends MCP's tool-interaction model:
- MCP: Agent ↔ Tool interactions
- AGP: Agent ↔ Prompt ↔ Tool ↔ Environment ↔ Memory lifecycle
- AGP adds versioning and evolution that MCP lacks

### Alignment with [[memory-systems]]

Memory is modeled as a first-class protocol resource:
- Explicit lifecycle states
- Versioned interfaces
- Evolution-safe updates
- Integrated with agent reasoning

### Alignment with [[llm-knowledge-base-pattern]]

AGP's resource substrate resembles wiki organization:
- Prompts ↔ Concepts (synthesized knowledge)
- Memory ↔ Sources (verbatim capture)
- Tools ↔ Skills (agent capabilities)
- Environment ↔ Wiki structure

### Gap: Decoupling AGP from AGS

The paper presents both protocol (AGP) and system (AGS) together. The protocol layer is the more valuable contribution — abstracting AGP to work with any agent framework (Hermes, Claude Code, Codex) would extend its reach.

## Implementation Considerations

### For C0ldbrain

| Concept | AGP Mapping | Implementation |
|---------|-------------|----------------|
| **Wiki sources** | Memory resources | Current already fits |
| **Wiki concepts** | Prompt resources | Knowledge as prompts |
| **Skills** | Tool resources | Skill registry = tool registration |
| **Agents** | Agent resources | Hermes, Claude, Codex |
| **Sessions** | Environment resources | Chat contexts = environments |

### For Hermes Agent

AGP could enhance:
- **Versioned skills** — Track skill evolution with rollback
- **Memory versioning** — Evolving knowledge with lineage
- **Prompt templates** — Versioned system instructions
- **Multi-agent coordination** — Resource sharing across agents

## Full Abstract

> Recent advances in LLM based agent systems have shown promise in tackling complex, long horizon tasks. However, existing agent protocols (e.g., A2A and MCP) under specify cross entity lifecycle and context management, version tracking, and evolution safe update interfaces, which encourages monolithic compositions and brittle glue code. We introduce Autogenesis Protocol (AGP), a self evolution protocol that decouples what evolves from how evolution occurs. Its Resource Substrate Protocol Layer (RSPL) models prompts, agents, tools, environments, and memory as protocol registered resources with explicit state, lifecycle, and versioned interfaces. Its Self Evolution Protocol Layer (SEPL) specifies a closed loop operator interface for proposing, assessing, and committing improvements with auditable lineage and rollback. Building on AGP, we present Autogenesis System (AGS), a self-evolving multi-agent system that dynamically instantiates, retrieves, and refines protocol-registered resources during execution. We evaluate AGS on multiple challenging benchmarks that require long horizon planning and tool use across heterogeneous resources. The results demonstrate consistent improvements over strong baselines, supporting the effectiveness of agent resource management and closed loop self evolution.

## Related Concepts

- [[agent-meta-optimization]] — Self-evolving agent frameworks
- [[agentic-ai]] — Agent protocol ecosystem
- [[mcp-protocol]] — Agent-tool interaction protocol (AGP extends this)
- [[memory-systems]] — Memory as first-class resource
- [[llm-knowledge-base-pattern]] — Resource organization patterns
- [[skill-registry]] — Tool registration and management
- [[prompt-engineering]] — Prompt templates as resources
