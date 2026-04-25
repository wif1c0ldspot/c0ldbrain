---
title: Local LLM Infrastructure & Model Routing
type: concept
tags:
- local-llm
- mac-mini
- mmap
- model-routing
- gemma4
- qwen
- ollama
- llama-cpp
- ai-agent
sources:
- leopardracer-mac-mini-local-llm-2026-04
- mac-mini-35b-local-ai-agent-2026-04
created: '2026-04-15'
updated: '2026-04-15'
confidence: high
status: current
agents:
- ollama
- llama-cpp
- gemma4
- qwen
priority: important
summary: Running local LLMs on consumer hardware ($599 Mac Mini M4, 16GB). Three-tier
  model routing, mmap trick for oversized models, Gemma 4 vs Qwen benchmarks, context
  compression, and resilience chain for AI agent uptime.
---

# Local LLM Infrastructure & Model Routing

## Summary

Production-grade local LLM setup on a $599 Mac Mini M4 (16GB RAM). Three-tier model routing system (fast/primary/heavy) running alongside cloud Claude for AI agent preprocessing, context compression, and fallback. 30-40% reduction in cloud API usage.

## Three-Tier Architecture

| Tier | Model | Params | Purpose | Speed |
|------|-------|--------|---------|-------|
| Fast | Gemma 4 E2B | 2.3B effective | Message triage, classification | <2s/msg |
| Primary | Gemma 4 E4B | 4.5B effective | Context compression, summaries | Moderate |
| Heavy | Qwen 3.5 35B-A3B | 35B total / 3B active | Signal compression, Claude fallback | 17.3 tok/s |

**Principle:** Different tools for different jobs. A 2B model handles classification fine. Summarization needs 4.5B+. Complex preprocessing and fallback need 35B.

## Use Cases for Local Models

- **Message triage:** Classify every message (question/request/idea/greeting/FYI) + urgency
- **Context compression:** 500-word message → 30 words before cloud API sees it
- **Signal compression:** Full day of automation signals → dense summary (15x token savings for Opus planning)
- **Email preprocessing:** Triage before deciding on full Claude session
- **Memory consolidation:** Cluster and merge daily agent notes
- **Fallback:** Handle operational tasks when cloud API is down/rate-limited

## The mmap Trick

Key insight: MoE models (like Qwen 35B-A3B) have most parameters idle per token. `--mmap` flag in llama.cpp lets OS page in only needed weights from SSD:

- Shared layers (attention, embeddings): 4-6GB resident in RAM
- Expert weights: paged from NVMe on demand, 90% untouched
- Result: 17.3 tok/s on 16GB machine with 35B model, zero swap
- Apple's "LLM in a Flash" paper (Dec 2023) describes this approach

**Without mmap:** Ollama loaded 26GB → system froze, 4.3M swapouts, timeout.
**With mmap:** Same model, same hardware → 17.3 tok/s, 81% memory free.

## Gemma 4 vs Qwen 3.5

Gemma 4 benchmarks made the swap worthwhile:
- Classification: 4.4x faster (8.5s → 1.9s)
- Summarization: 1.8x faster
- Apache 2.0 license (no usage restrictions — critical for 24/7 production)
- Native vision + audio on E2B/E4B (Qwen was text-only)
- Accuracy tradeoff: 70% vs 80% — mostly gray areas, fixable with prompting

Migration: 2 constants changed, 3 files updated. Old models kept as rollback.

## Critical Optimizations

1. **Disable thinking mode for fast tasks:** `think: false` in Ollama API. 30x speedup for classification (30s → 1s, same accuracy)
2. **OLLAMA_MAX_LOADED_MODELS=1:** Critical on 16GB. Without it, Ollama loads both models and system dies.
3. **--n-gpu-layers 0 with mmap:** Let OS manage paging, don't offload to GPU layers. Unified memory makes this moot.
4. **Context windows:** 4K for classification, 32K for summarization, 16K for heavy tier. KV cache lives in RAM.

## Resilience Chain

```
Claude Sonnet → retry → Haiku → Local 35B → Local Primary → OpenRouter → Queue
```

Tracks cooldowns per model. Skips tiers known to fail. Local fallback responses marked `[Local Fallback]`.

## Setup Recipe

**Fast + Primary (Ollama):**
```bash
brew install ollama
ollama pull gemma4:e2b
ollama pull gemma4:e4b
export OLLAMA_FLASH_ATTENTION=1
export OLLAMA_KV_CACHE_TYPE=q8_0
export OLLAMA_KEEP_ALIVE=10m
export OLLAMA_MAX_LOADED_MODELS=1
```

**Heavy (llama.cpp):**
```bash
brew install llama.cpp
llama-server --model Qwen3.5-35B-A3B-UD-IQ3_XXS.gguf \
  --port 8081 --ctx-size 16384 --n-gpu-layers 0 --mmap \
  --flash-attn on --threads 8
```

Both coexist: Ollama on port 11434, llama.cpp on 8081.

## Safety Rules

- Messages mentioning money, deployment, publishing → bypass local, straight to Claude
- Messages under 20 chars skip triage (ambiguous)
- Always test benchmarks before swapping production models

## Additional Notes (from mac-mini-35b-local-ai-agent-2026-04)

This source confirmed and expanded on several points:

- **MoE on 16GB is production-viable:** The mmap approach is not just a demo trick — it runs 24/7 as AI agent infrastructure. The key insight is that MoE models naturally suit this because only 3B of 35B params are active per token.
- **Ollama + llama.cpp coexistence:** Running Ollama (port 11434) for smaller models and llama.cpp (port 8081) for the heavy tier is a stable production pattern. Each tool plays to its strength.
- **Thinking mode trap:** Disabling thinking mode (`think: false`) for fast classification tasks is the single biggest optimization in the whole setup — 30x speedup with same accuracy. This applies broadly to any local model doing classification/triage.
- **Safety bypass rules:** Messages mentioning money, deployment, or publishing bypass local processing entirely and go straight to Claude. This is a critical pattern for any hybrid local/cloud system.

## Related Concepts

- [[ai-coding-agents]] — cloud agent ecosystem
- [[token-optimization-and-efficiency]] — token reduction strategies
- [[model-routing]] — Hermes model routing

- [[apple-silicon-ai]]
- [[edge-ai]]
- [[local-397b-model-macbook-2026-03]]
- [[mac-mini-35b-local-ai-agent-2026-04]]
- [[mlx-turboquant-local-power-2026-04]]
- [[privacy-first-ai]]
- [[token-optimization]]
- [[leopardracer-mac-mini-local-llm-2026-04]]