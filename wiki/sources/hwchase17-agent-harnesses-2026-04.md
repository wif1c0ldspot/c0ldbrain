---
compiled: 2026-04-15
confidence: high
created: '2026-04-16'
priority: important
source_url: https://x.com/hwchase17/status/2042978500567609738?s=46&t=CLd5pEAh4JLH9Y655r58aA
stars: 1.8M
status: current
summary: Harrison Chase on agent harnesses as the dominant pattern for building agents,
  their intimate tie to memory, closed harness lock-in, and memory being a core harness
  responsibility
tags:
- memory-systems
- agent-harnesses
- mcp-protocol
- agentic-ai
- context-management
title: Agent Harnesses and Memory (Harrison Chase)
type: source
updated: '2026-04-18'
---


# Agent Harnesses and Memory (Harrison Chase)

**Author:** Harrison Chase (@hwchase17)
**Date:** April 11, 2026
**Source:** https://x.com/hwchase17/status/2042978500567609738
**Views:** 1.8M | **Likes:** 3,728 | **Reposts:** 640

## Key Insights

1. **Agent harnesses are becoming the dominant way to build agents**, and they're not going anywhere
2. **Harnesses are intimately tied to agent memory** — managing context is a core harness responsibility
3. **Closed harnesses create lock-in** — using a closed harness (especially proprietary API) means yielding control of your agent's memory to a third party
4. **Memory is critical** for creating good and sticky agentic experiences
5. **Memory should be open** so you own your own memory
6. **Memory is in its infancy** — we're still figuring out best practices and abstractions

## The Evolution of Agent Development

The "best" way to build agentic systems has changed dramatically over the past three years:

1. **ChatGPT era (2022)**: Simple RAG chains (LangChain)
2. **Better models era**: More complex flows (LangGraph)
3. **Current era**: Scaffolding with agent harnesses

### Common Misconception

Some sentiment that models will absorb more and more scaffolding. This is not true. What has happened is that a lot of scaffolding needed in 2023 is no longer needed, but it's been replaced by other types of scaffolding.

## Agent Harnesses

### Harness Examples

- **Claude Code**: https://code.claude.com/docs/en/overview
- **Deep Agents**: https://github.com/langchain-ai/deepagents
- **Pi**: https://github.com/badlogic/pi-mono
- **OpenClaw**: https://docs.openclaw.ai/
- **OpenCode**: https://opencode.ai/
- **Codex**: https://openai.com/codex/
- **Letta Code**: https://www.letta.com/blog/letta-code

## Harnesses and Memory

### Sarah Wooders' Insight

Sarah Wooders wrote a critical blog on why "memory isn't a plugin (it's a harness)": https://x.com/sarahwooders/status/2040121230473457921

**Key point**: Asking to plug memory into an agent harness is like asking to plug driving into a car. Managing context, and therefore memory, is a **core capability and responsibility** of the agent harness.

### Memory as Context

Memory is just a form of context:
- **Short-term memory**: Messages in conversation, large tool call results (handled by harness)
- **Long-term memory**: Cross-session memory (needs to be updated and read by harness)

### Critical Memory Architecture Questions

Sarah Wooders lists these critical questions about how a harness manages memory:
- How is AGENTS.md or CLAUDE.md file loaded into context?
- How is skill metadata shown to agents?
- Can agent modify its own system instructions?
- What survives compaction, and what's lost?
- Are interactions stored and made queryable?
- How is memory metadata presented to agent?
- How is current working directory represented?
- How much filesystem information is exposed?

## Memory Is in Its Infancy

### Current Reality

Memory as a concept is still in its infancy. We don't have well-known or common abstractions for memory yet. Long-term memory is often not part of MVP. First you need to get an agent working generally, then you can worry about personalization.

### Future Possibility

If memory does become more known and best practices emerge, separate memory systems might start to make sense.

### Bottom Line from Sarah

"Ultimately, how a harness manages context and state in general is the foundation for agent memory."

## Technical Details

### Engagement Metrics

- 102 replies
- 640 reposts
- 3,728 likes
- 1.8M views
- 10,356 bookmarks

## Related Concepts

[[memory-systems]], [[hermes-agent-architecture]], [[mcp-protocol]], [[agentic-ai]]
