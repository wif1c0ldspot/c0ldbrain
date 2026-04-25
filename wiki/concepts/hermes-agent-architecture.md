---
title: Hermes Agent Architecture
type: reference
tags: [hermes, ai-agents]
sources:
- hermes-agent-skills-hub-2026-04
- hermes-agent-practitioners-reference-2026
- axi-agent-experience-interface-2026-04
- claude-code-from-source-2026-04
- hwchase17-agent-harnesses-2026-04
created: '2026-04-06'
updated: '2026-04-15'
confidence: high
status: current
agents: [hermes]
priority: critical
summary: Hermes Agent running this system — tools, skills, memory, and wiki integration.
  Docker backend, terminal access, and knowledge base at ~/obsidian. Agent harnesses
  are the dominant pattern for building agents.
---


# Hermes Agent Architecture

## Summary

The system architecture, tools, skills, memory system, and wiki knowledge integration.

## System Details

| Setting | Value |
|---------|-------|
| Backend | Docker (default), Local for macOS-native tasks |
| Working Dir | ~/Projects/crypto-quant/ |
| Wiki Path | /Volumes/obsidian/C0ldbrain/ |
| Model | Claude Sonnet 4.5 (via OpenRouter) |

## Tools Available

| Category | Tools |
|----------|-------|
| Terminal | terminal, process |
| Files | read_file, write_file, patch, search_files |
| Code | execute_code |
| Web | browser_navigate, browser_snapshot, browser_vision, web_extract |
| Agent | clarify, delegate_task, cronjob, memory |
| Skills | skill_view, skills_list, skill_manage |
| Other | vision_analyze, text_to_speech |

## Skills Library

As of 2026-04-07: The official Skills Hub lists 643 skills across 4 registries (77 built-in, 45 optional, 521 community). See [[skill-registry]] for the full catalog.

Currently installed: 45+ skills covering:
- **Crypto-quant**: 11+ strategy modules, backtesting, live bot management
- **AI/Research**: arxiv, duckduckgo-search, blogwatcher, ml-paper-writing
- **Devops**: python-uv-packaging, webhook-subscriptions, bot-process-discovery
- **Software-dev**: code-review, test-driven-development, systematic-debugging, plan
- **Productivity**: daily-ai-research-workflow, google-workspace, obsidian, notion

Notable skills that could be installed (from the Hub):
- **obliteratus** — Remove guardrails from open LLMs via mechanistic interpretability
- **outlines/guidance** — Structured generation (JSON/XML/code guarantees)
- **axolotl** — YAML-based fine-tuning with LoRA/QLoRA, DPO/KTO/ORPO/GRPO
- **unsloth** — 2-5x faster fine-tuning, 50-80% less memory
- **grpo-rl-training** — GRPO/RL reasoning training
- **vllm** — High-throughput LLM serving with PagedAttention

External registries:
- Official Skills Hub: https://agentskills.io
- LobeHub: 505 community-contributed skills (largest registry)
- Anthropic: 16 skills (Claude-specific)

## How Knowledge Is Loaded

| Source | What It Is | Load Mechanism |
|--------|-----------|----------------|
| Skills | Procedural — HOW to do things | Auto-loaded by skill manager |
| Memory | Persistent facts — WHO/WHAT | Auto-injected every turn |
| Wiki | Declarative — WHAT is known | LLM reads via read_file() |

## How To Extend

- Add skills: `skill_manage()` to create/update in ~/.hermes/skills/
- Add wiki knowledge: drop sources into raw/ and compile
- Update memory: `memory` tool for persistent facts
- Schedule tasks: `cronjob` tool for recurring operations

## Agent Harnesses (from hwchase17-agent-harnesses-2026-04)

Agent harnesses are the dominant way to build agents today. A harness provides the scaffolding — tool management, context handling, memory, and state orchestration — that turns a raw LLM into a functional agent.

### Why Harnesses Matter

- Harnesses are **intimately tied to agent memory** — managing context is a core harness responsibility
- **Closed harnesses create lock-in** — using proprietary APIs means yielding control of your agent's memory
- Memory is critical for sticky agentic experiences and should be **open and owned by you**

### Evolution of Agent Building (2022-2026)

| Era | Pattern | Representative Tool |
|-----|---------|----------------------|
| 2022 (ChatGPT) | Simple RAG chains | LangChain |
| 2023 (Better models) | Complex flows | LangGraph |
| 2024-2026 (Current) | Scaffolding with harnesses | Claude Code, Deep Agents, Pi, Letta |

### Notable Agent Harnesses

| Harness | Focus | Link |
|---------|-------|------|
| **Claude Code** | Coding agent by Anthropic | https://code.claude.com/docs/en/overview |
| **Deep Agents** | Deep thinking agents (LangChain) | https://github.com/langchain-ai/deepagents |
| **Letta** | Stateful agents with advanced memory | https://www.letta.com |
| **Pi** | Agent harness with open protocol | https://github.com/badlogic/pi-mono |
| **OpenClaw** | Open protocol agent framework | https://docs.openclaw.ai/ |
| **OpenCode** | Open coding harness | https://opencode.ai/ |
| **Codex** | OpenAI coding harness | https://openai.com/codex/ |

### Harness Responsibility for Memory

Per Sarah Wooders: "Asking to plug memory into an agent harness is like asking to plug driving into a car."

Critical questions a harness must answer for memory:
- How are config files loaded into context?
- How is skill metadata shown to agents?
- Can agents modify their own system instructions?
- What survives context compaction?
- How is memory metadata presented?

## Related
- [[agent-orchestration-stacks]] — Paperclip + Hermes as two-layer orchestration + memory stack
- [[hermes-team-guide-nyk-builderz-2026-04]]
- [[hermes-ecosystem-nftcps-2026-04]] Concepts
- [[agent-meta-optimization]]
- [[agentic-ai]]
- [[ai-agents-handbook-2026]]
- [[autoagent-kevinrgu-2026-04]]
- [[axi-agent-experience-interface-2026-04]]
- [[bitter-lesson-agent-harnesses-gregpr07-2026-04]]
- [[browser-harness-browser-use]]
- [[career-ops-2026-04]]
- [[claude-code-from-source-2026-04]]
- [[claude-skills-67-polydao-2026-04]]
- [[design-md]]
- [[design-md-google-labs-2026-04]]
- [[evolving-programmatic-skill-networks-2026]]
- [[gbrain-agent-brain]]
- [[gbrain-garrytan-ayi-ainotes-2026-04]]
- [[hermes-agent]]
- [[hermes-agent-skills-hub-2026-04]]
- [[hermes-kanban-bridge]]
- [[hermes-kanban-gumbyender-2026-04]]
- [[honcho-hermes-lcm-stack-bayendor-2026-04]]
- [[hwchase17-agent-harnesses-2026-04]]
- [[knowledge-management-handbook-2026]]
- [[langflow-claude-code-integration]]
- [[model-routing]]
- [[multi-agent-systems]]
- [[paperclip-hermes-solo-ai-company-juliangoldieseo-2026-04]]
- [[polymarket-weather-hermes-agent-0xmovez-2026-04]]
- [[skill-composition-procedural-learning]]
- [[skillx-skill-kb-2026]]
- [[steps-compositional-generalization-2026]]

- [[hermes-multi-profile-team]] — 4-profile team architecture (orchestrator + research + writer + engineer)
- [[hermes-ecosystem-projects]] — 5 key community projects (CaMeL, Alpha, Skill Factory, Maestro, Icarus)
- [[honcho|related]] — Persistent memory layer for Hermes
- [[hermes-lcm|related]] — Measurement and control layer
- [[career-ops]]



[[karpathy-llm-wiki-agent]], [[ai-coding-agents]], [[skill-registry]], [[mcp-protocol]], [[hermes-agent-practitioners-reference-2026|extended-by]], [[agent-cli-tools]], [[claude-skills]], [[resolvers]]
