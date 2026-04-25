---
title: Agent Harness
type: concept
tags: [ai-agents, architecture, coding-agents, harness-engineering]
created: 2026-04-18
updated: 2026-04-24
confidence: high
status: current
priority: important
summary: "Scaffolding that turns raw LLM into functional agent — memory, tools, state management, and deterministic control systems"
---

# Agent Harness

The scaffolding that transforms a raw LLM into a functional agent. Provides:
- Memory/context management
- Tool integration
- State tracking
- Configuration loading
- Deterministic constraints on stochastic LLM output

## Common Harnesses
- OpenAI Agents SDK
- Claude Code
- Letta
- OpenClaw
- Deep Agents
- Browser Harness (browser-use)

## Design Patterns
See [[harness-design]] for detailed harness architecture patterns including:
- GAN-inspired multi-agent systems (planner/generator/evaluator)
- Progressive disclosure and R.P.I. framework
- Context reset strategies for long-running sessions

## Harness Engineering Framework

Term coined by Mitchell Hashimoto (HashiCorp), 2026. The third pillar of AI engineering after Prompt and Context Engineering.

> **Definition:** Every piece of infrastructure other than the LLM that enables an agent to actually deliver results.

### R.E.S.T Framework

Four core objectives for production-grade agents:

| Objective | Key Requirements |
|-----------|------------------|
| **Reliability** | Fault recovery, operation idempotency, behavioral consistency |
| **Efficiency** | Resource control (token/API budgets), low latency, high throughput |
| **Security** | Least privilege, sandboxed execution, I/O filtering |
| **Traceability** | End-to-end tracing, explainable decisions, auditable state |

### PPAF Agent Cycle

Production agents operate on a continuous loop:
1. **Perception** — Observe world state (inputs, tool outputs, history)
2. **Planning** — Update goals, decompose tasks, decide next move
3. **Action** — Execute operations (internal memory updates or external tool calls)
4. **Feedback/Reflection** — Observe results, feed back into next cycle

### REPL Harness Architecture

Deterministic shell wrapping the non-deterministic LLM "brain":

```
Read → Context Manager → structured prompts (Perception)
Eval → Call Interceptor → tool routing + monitoring (Planning/Action)
Print → Feedback Assembler → observation injection (Feedback)
Loop → drives PPAF cycle continuously
```

### 6 Design Principles

1. **Design for Failure** — Exceptions are the norm. Every component needs fault tolerance, retries, graceful degradation.
2. **Contract-First** — Define all interactions through explicit schemas, APIs, events.
3. **Secure by Default** — Least privilege, zero trust, defense-in-depth. Not a bolt-on.
4. **Separation of Concerns** — Decouple deciding what to do (planning) from how to do it (execution).
5. **Everything is Measurable** — Without measurement, no path to optimization.
6. **Data-Driven Evolution** — Every run is a learning opportunity. Closed loop of data → label → feedback.

### Token Transformation Pipeline

5-step pipeline to pack maximum signal into finite context:
1. **Collection** ‒ Aggregate user requests, short-term memory, long-term retrievals
2. **Ranking** ‒ Score by recency and semantic relevance
3. **Compression** ‒ Summarize high-volume, low-density content
4. **Budgeting** ‒ Allocate token limits per information category
5. **Assembly** ‒ Piece together final prompt with structured templates

> Offload attention management to engineering. Don't hope the model "figures out" what to focus on.

### Sandbox Levels

| Level | Technology | Use Case |
|-------|-----------|----------|
| L1 | Process isolation (chroot, namespaces) | Trusted internal tools |
| L2 | Containers (Docker) | **Default** for most tool execution |
| L3 | MicroVMs (Firecracker) | Multi-tenant, untrusted code |
| L4 | Full VMs (KVM/QEMU) | Maximum security, highest cost |

### State Separation Principle

**Rule:** Treat the LLM as a stateless compute unit ("CPU"). All cross-turn state — user sessions, task progress, memory — offloaded to an external Context State Manager controlled by the Harness.

**Anti-pattern:** Forcing the LLM to maintain complex state via prompt engineering leads to chaotic, unpredictable, untraceable behavior.

### Spec Coding

As AI becomes the primary engine of productivity, human engineers shift from line-by-line coding to:
- Architecting blueprints
- Defining rules and constraints
- Signing off on final output

The engineer evolves from creator of code to guardian of the creation process.

## The Bitter Lesson of Harnesses

Gregor Zunic's evolution on harness design (2026-04):
1. **First lesson:** Don't wrap the LLM in abstractions. Maximal action space.
2. **Second lesson:** Don't wrap its tools either. Every `click()`, `type()`, `scroll()` is a constraint.
3. **Result:** Give raw protocol access (CDP for browsers). Let the agent write what it needs mid-task.

The agent writes missing functions on the fly — not from first principles, but like fixing a missing import. Error recovery is emergent: the model has seen thousands of crash recovery patterns in training data.

~600 lines of harness code is sufficient when the agent can self-edit.

See [[bitter-lesson-agent-harnesses-gregpr07-2026-04]] for full article.

## Sources
- [[harness-engineering-trae-ai-2026-04]] — TRAE's definitive guide: R.E.S.T, PPAF, REPL, 6 principles
- [[bitter-lesson-agent-harnesses-gregpr07-2026-04]] — "Bitter lesson" philosophy, raw CDP access
- [[browser-harness-browser-use]]
- [[anthropic-harness-design-long-running-apps]] — Anthropic's multi-agent harness
- [[thealexker-harness-optimization-guide-2026-04]] — Optimization techniques
- [[agent-harnesses-harrison-chase-2026]] — Harrison Chase's overview
- [[hwchase17-agent-harnesses-2026-04]] — hwchase17 harness patterns
- [[claude-code-agent-design-space-arxiv-2026-04]] — arXiv research synthesis

## Related Concepts
- [[multica-relational-agent-memory]] — pure relational agent memory pattern (SQL + JSONB, no embeddings)
- [[openai-agents-sdk]] — OpenAI's official agent harness (sandbox agents, handoffs, tracing)
- [[agent-orchestration-stacks]] — multi-agent orchestration patterns
- [[brain-inspired-agent-architecture]] — brain-module mapping for agent design

- [[agent-memory-poisoning-security-2026-04]]
- [[browser-automation]]
- [[claude-code]]
- [[langflow-claude-code-integration]]
- [[memory-firewall]]
- [[multica-platform]]
- [[openviking-context-database-volcengine-2026-04]]
- [[rohit4verse-claude-code-architecture-2026-04]]
- [[agent-skills-osmani-github-2026-04]]