---
title: AI Coding Agents
type: concept
tags: [ai-agents, developer-tools, claude-code, cursor]
sources:
- claude-caveman-prompting-strategy-2026-04
- claude-code-skill-graphs-2026-04
- claude-code-opus-planning-2026-04
- noisyb0y1-claude-code-thread-2026-04
- google-engineer-claude-code-automation-2026-04
- claude-code-from-source-2026-04
- agent-skills-osmani-2026-04
- cli-anything-hkuds-2026-04
created: '2026-04-06'
updated: '2026-04-15'
confidence: high
status: current
agents: [hermes, claude, codex]
priority: critical
summary: 'The ecosystem of AI coding agents: Claude Code, Cursor, and their supporting
 tools. Agent architecture, skill systems, CLAUDE.md, and development methodologies.'
---


# AI Coding Agents

## Summary

The ecosystem of AI coding agents — Claude Code, Cursor, and their supporting tools. Covers agent architecture, skill systems, CLAUDE.md context files, and development methodologies.

## Core Patterns

### CLAUDE.md (Context File)

Created by Claude Code team lead (@bcherny). Place at project root:
- Teaches agent about the codebase
- Contains past mistakes, conventions, rules
- Claude reads it every session
- Result: agent learns from context instead of re-learning

### Superpowers (40.9K Stars)

Full development methodology for AI coding agents:
- Most people fire up Claude Code / Codex and code blindly
- Superpowers adds structured planning, review, and iteration
- 40.9K stars indicates massive community adoption

### Skill Graphs

Modular capabilities agents load on-demand:
- Each skill is a SKILL.md with YAML frontmatter (name, description, triggers)
- Skills include references, templates, and scripts
- Shareable across projects and agents
- Discoverable after extended Claude Code usage

### /model opusplan

Claude Code setting: uses Opus for planning, Sonnet for execution. Maximum efficiency.

## Agent Design Philosophy

> The model already knows how to be an agent. Your job is to get out of the way.

An agent is just a loop:
1. Model sees context + available capabilities
2. Model decides: act or respond
3. If act: execute capability, add result, continue
4. If respond: return to user

Key principles:
- Most agents need only 3–5 capabilities
- Start simple, add complexity only when usage reveals the need
- Capabilities enable, knowledge informs, constraints focus
- Trust the model — don't over-engineer

## Notable Agent Tools

| Tool               | Category                   | Description                                                      |                                                          |     |
| ------------------ | -------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------- | --- |
| Claude Code        | Coding agent               | Leading AI coding agent, skill-based, CLAUDE.md context          |                                                          |     |
| Cursor             | IDE                        | Built-in AI agent capabilities                                   |                                                          |     |
| GitNexus           | Code graph                 | Knowledge graph for codebases                                    |                                                          |     |
| Alibaba Page Agent | GUI                        | Controls webpages with natural language (pure JS)                |                                                          |     |
| OpenClaw           | Agent                      | Self-hosted persistent agent with memory and skills              |                                                          |     |
| VisionClaw         | Multimodal                 | Real-time agent on Meta glasses, sees/hears/acts via Gemini Live |                                                          |     |
|                    | Deep Agents (LangChain)    | Framework                                                        | Turns any LLM into deep thinking agent with MCP tools    |     |
|                    | Agent Skills (Addy Osmani) | Commands                                                         | 7 slash commands for AI coding agents (15.6k stars)      |     |
|                    | CLI-Anything               | Wrappers                                                         | Agent-native CLI wrappers with CLI-Hub (30.7k stars)     |     |
|                    | AXI                        | Design                                                           | 10 principles for agent-ergonomic CLI tools, TOON format |     |


## Automation Insights (from google-engineer-claude-code-automation-2026-04)

A Google engineer (11 years exp) demonstrated a practical 3-step automation system with Claude Code:

1. **Classification loop** (15-min cycle): dotnet app polls GitLab API → Claude reads issues → auto-responds if not dev-ready
2. **Autonomous execution:** Subagent implements features → pushes branch → creates PR
3. **PR workflow automation:** Monitors PR comments → implements review feedback

**Results:** 8h/day → 2-3h/day. 80% automation, same code quality.

**Key tools in the stack:**
- Karpathy CLAUDE.md (4 principles: Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution)
- Everything Claude Code (153K+ GitHub stars, 30+ agents, 180+ skills)
- **Critical warning:** Don't load all agents at once — 27 agents + 64 skills simultaneously burns context limits

This pattern (classify → execute → review) is directly applicable to Hermes agent workflows.

## Claude Code Internals (from claude-code-from-source-2026-04)

18-chapter book reverse-engineering Claude Code's architecture:
- Agent loop: observe context → decide action → execute tool → integrate result
- Tool pipeline with sequential and parallel invocation
- Multi-agent orchestration for complex task delegation
- File-based memory using CLAUDE.md for session persistence
- Essential reference for understanding production coding agent internals

## Agent Skills & CLI Wrappers (from agent-skills-osmani-2026-04, cli-anything-hkuds-2026-04)

Addy Osmani's 7 slash commands (15.6k stars) provide structured agent workflows:
- `/plan`, `/debug`, `/review`, `/refactor`, `/test`, `/document`, `/ship`
- Production-tested, chainable commands for the full development lifecycle

CLI-Anything (30.7k stars) wraps any CLI tool into agent-native interfaces:
- CLI-Hub package manager with 30+ community harnesses
- Makes git, docker, k8s, cloud CLIs agent-friendly
- See [[agent-cli-tools]] for full concept

## Related Concepts

- [[agent-skills-systems]] — lifecycle-organized skills with anti-rationalization + verification
- [[career-ops]] — Job search pipeline via Claude Code

[[hermes-agent-architecture]], [[skill-registry]], [[token-optimization]], [[llm-knowledge-bases]], [[claude-md-best-practices]], [[local-llm-infrastructure]], [[agent-cli-tools]], [[resolvers]]

- [[agent-meta-optimization]]
- [[agent-skills-osmani-2026-04]]
- [[agentic-ai]]
- [[ai-agents-handbook-2026]]
- [[architecture-diagram-generator-2026-04]]
- [[autoagent-kevinrgu-2026-04]]
- [[axi-agent-experience-interface-2026-04]]
- [[bitter-lesson-agent-harnesses-gregpr07-2026-04]]
- [[browser-automation]]
- [[career-ops-2026-04]]
- [[claude-code]]
- [[claude-code-from-source-2026-04]]
- [[cli-anything-hkuds-2026-04]]
- [[code-review-graph]]
- [[coral-multi-agent-discovery]]
- [[design-md]]
- [[design-md-google-labs-2026-04]]
- [[developer-tools]]
- [[google-engineer-claude-code-automation-2026-04]]
- [[hermes-agent-skills-hub-2026-04]]
- [[karpathy-llm-wiki-agent]]
- [[knowledge-management-handbook-2026]]
- [[langflow-claude-code-integration]]
- [[mac-mini-35b-local-ai-agent-2026-04]]
- [[mcp-protocol]]
- [[memory-systems]]
- [[mempalace-github-2026-04]]
- [[multica-kimi-k26-agent-teams-multicaai-2026-04]]
- [[multica-platform]]
- [[multica-relational-agent-memory]]
- [[jarvis-obsidian-claude-code-cyrilxbt-2026-04]]