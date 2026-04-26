---
title: "Agent Harness"
type: concept
tags:
- ai-agents
- agent-harness
- context-engineering
- orchestration
sources:
- akshay-agent-harness-anatomy-2026-04
created: '2026-04-25'
updated: '2026-04-25'
confidence: high
status: current
priority: critical
summary: "The complete software infrastructure wrapping an LLM: orchestration loop, tools, memory, context management, state persistence, error handling, and guardrails. Formalized 2026."
---

# Agent Harness

The agent harness is the complete software infrastructure that transforms a stateless LLM into a capable agent. As LangChain's Vivek Trivedy puts it: "If you're not the model, you're the harness."

The harness is distinct from the "agent" — the agent is emergent behavior; the harness is the machinery producing it. Beren Millidge's analogy: a raw LLM is a CPU with no RAM, disk, or I/O. The context window is RAM, external databases are disk, tools are device drivers, and the harness is the operating system.

## Three Levels of Engineering

1. **Prompt engineering** — crafts instructions the model receives
2. **Context engineering** — manages what the model sees and when
3. **Harness engineering** — encompasses both plus tool orchestration, state persistence, error recovery, verification loops, safety enforcement, lifecycle management

## 12 Components of a Production Harness

1. **Orchestration Loop** — Thought-Action-Observation (TAO) / ReAct cycle
2. **Tools** — schemas injected into context; registration, validation, sandboxed execution
3. **Memory** — short-term (context window), long-term (vector/graph DBs), episodic
4. **Context Management** — assembly, truncation, prioritization of context window
5. **State Persistence** — checkpointing agent state across sessions
6. **Error Handling** — retries, fallbacks, graceful degradation
7. **Verification Loops** — self-check results before returning to user
8. **Guardrails** — safety enforcement, output filtering, scope limiting
9. **Lifecycle Management** — agent initialization, execution, termination
10. **Logging/Observability** — tracing, metrics, debugging
11. **Planning** — task decomposition, multi-step reasoning
12. **Communication** — inter-agent messaging, user interaction

## Key Players

- **Anthropic**: Claude Code SDK described as "the agent harness that powers Claude Code"
- **OpenAI**: Codex team explicitly equates "agent" and "harness" for non-model infrastructure
- **LangChain**: Jumped from outside top 30 to rank 5 on TerminalBench 2.0 by changing only harness infrastructure

## Related
- [[agent-memory-poisoning-security-2026-04]]
- [[agent-orchestration-stacks]]
- [[bitter-lesson-agent-harnesses-gregpr07-2026-04]]
- [[brain-inspired-agent-architecture]]
- [[browser-automation]]
- [[browser-harness-browser-use]]
- [[claude-code]]
- [[harness-design]]
- [[harness-engineering-trae-ai-2026-04]]
- [[langflow-claude-code-integration]]
- [[memory-firewall]]
- [[multica-platform]]
- [[multica-relational-agent-memory]]
- [[openai-agents-sdk]]
- [[openviking-context-database-volcengine-2026-04]]
- [[rohit4verse-claude-code-architecture-2026-04]]

- [[akshay-agent-harness-anatomy-2026-04]]
- [[agent-architecture]]
- [[context-engineering]]
- [[tool-orchestration]]
- [[memory-systems]]
- [[agent-harness]]
