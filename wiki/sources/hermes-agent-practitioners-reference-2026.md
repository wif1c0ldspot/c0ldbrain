---
confidence: high
created: '2026-04-16'
priority: reference
sources:
- raw/articles/hermes-agent-practitioners-reference-2026.md
status: current
summary: Comprehensive 12,000-word practitioner's reference to Hermes Agent by Blake
  Crosley — 19+ providers, 15+ messaging platforms, skills system, persistent memory,
  cron, MCP integration.
tags:
- hermes-agent
- ai-agents
- configuration
- tools
- mcp-protocol
- memory-systems
title: 'Hermes Agent: The Practitioner''s Reference (2026)'
type: source
updated: '2026-04-14'
compiled: true
source_url: https://blakecrosley.com/guides/hermes
---


# Hermes Agent: The Practitioner's Reference (2026)

**Source URL:** https://blakecrosley.com/guides/hermes  
**Author:** Blake Crosley  
**Ingested:** 2026-04-14

## Summary

Comprehensive practitioner's reference guide to Hermes Agent by Nous Research. Covers provider authentication (19+ providers, 3 auth paths), configuration hierarchy, CLI commands, slash commands, tools/toolsets, skills system, persistent memory, SOUL.md personality, messaging gateway (15+ platforms), cron scheduling, MCP integration, context compression, and architecture internals.

## Key Facts

- **Three auth paths:** API key in .env, OAuth via `hermes model`, or custom endpoint in config.yaml
- **19+ providers:** Nous Portal, OpenRouter, Anthropic, GitHub Copilot, z.ai/GLM, Kimi, MiniMax, Alibaba, DeepSeek, Hugging Face, Google/Gemini, xAI/Grok, plus any OpenAI-compatible endpoint
- **Local LLM support:** Ollama, vLLM, SGLang, llama.cpp, LM Studio templates included
- **47 tools / 20 toolsets** in full registry
- **Messaging gateway:** 15+ platforms — Telegram, Discord, Slack, WhatsApp, Signal, Email, Home Assistant, Mattermost, Matrix, DingTalk, Feishu, WeCom, BlueBubbles, Webhook
- **Skills system:** Progressive disclosure (list → view → file), agent-managed skill creation, skill hub with security scanning
- **Memory:** MEMORY.md (2,200 chars) + USER.md (1,375 chars), frozen snapshot injection, 8 external memory providers
- **Cron:** Agent-level scheduled tasks, deliver to any platform
- **MCP:** Both client and server support
- **Context compression:** Automatic with configurable threshold, separate summarizer LLM
- **Fallback model:** Auto-switch on provider failure, once per session
- **Profiles:** Multiple isolated Hermes instances with separate config/memory/sessions
- **Terminal backends:** local, docker, ssh, singularity, modal, daytona
- **OpenClaw migration:** `hermes claw migrate` imports 30+ categories

## Gotchas

- Auxiliary model fallback: vision/web/compression fail silently if only Anthropic configured without OpenRouter key
- Ollama default context length (4096) too low for agent use — must raise to 16k-32k
- vLLM requires `--enable-auto-tool-choice` and `--tool-call-parser` for tool calling
- llama.cpp requires `--jinja` flag for tool calling support
- SGLang default max_tokens is 128 — must override

## Related Concepts

- [[hermes-agent-architecture|extended-by]] — Internal architecture details of Hermes
- [[llm-knowledge-bases|uses]] — Knowledge base integration
- [[mcp-protocol|uses]] — MCP client/server support
- [[memory-systems|uses]] — Persistent memory architecture
