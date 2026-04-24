---
compiled: 2026-04-15
confidence: high
created: '2026-04-16'
priority: important
source_url: https://x.com/leopardracer/status/2043631410045452360
status: current
summary: 'Production guide: running 35B MoE model on $599 Mac Mini M4 (16GB) via llama.cpp
  mmap. Three-tier model routing (Gemma 4 E2B/E4B + Qwen 35B), context compression
  saving 15x tokens, and resilience chain for 24/7 AI agent uptime.'
tags:
- local-models
- ai-agents
- infrastructure
- developer-tools
- cost
title: $600 Mac Mini Running 35B AI Model — Local AI Agent Infrastructure
type: source
updated: '2026-04-18'
---


# $600 Mac Mini Running 35B AI Model — Local AI Agent Infrastructure

**Author:** @leopardracer
**Platform:** X/Twitter
**Stats:** 1.2M views, 1K likes, 4K bookmarks, 134 reposts

## Key Insights

### Three-Tier Model Routing

| Tier | Model | Purpose | Speed |
|------|-------|---------|-------|
| Fast | Gemma 4 E2B (2.3B effective) | Message triage, classification | <2 sec/msg |
| Primary | Gemma 4 E4B (4.5B effective) | Context compression, summaries, email preprocessing | Moderate |
| Heavy | Qwen 3.5 35B-A3B (via llama.cpp mmap) | Signal compression, Claude fallback, memory consolidation | 17.3 tok/s |

Result: 30-40% fewer Claude sessions. Different tools for different jobs.

### The mmap Trick (Critical)

- Qwen 3.5 35B-A3B is MoE: 35B params total, only 3B active per token
- Ollama tried loading 26GB into 16GB RAM — system froze, 4.3M swapouts
- llama.cpp with `--mmap`: OS memory-maps model file, pages in only needed weights
- Result: 17.3 tok/s, 81% memory free, zero swap
- Shared layers (4-6GB) stay in RAM, expert weights paged from SSD on demand
- Based on Apple "LLM in a Flash" paper (Dec 2023)

### Context Compression

- 500-word messages compressed to 30 words before Claude sees them
- Full day of automation signals → dense summary (15x token savings for Opus planning)
- Memory consolidation: cluster and merge daily agent notes

### Resilience Chain

```
Claude Sonnet → retry → Haiku → Local 35B → Local Primary → OpenRouter → Queue
```

Tracks cooldowns per model. Skips tiers known to fail.

## Technical Details

### Setup Commands

**Gemma 4 (recommended for fast/primary tiers):**
```bash
brew install ollama
ollama pull gemma4:e2b
ollama pull gemma4:e4b
ollama pull nomic-embed-text

export OLLAMA_FLASH_ATTENTION=1
export OLLAMA_KV_CACHE_TYPE=q8_0
export OLLAMA_KEEP_ALIVE=10m
export OLLAMA_MAX_LOADED_MODELS=1
```

**35B Heavy Tier:**
```bash
brew install llama.cpp
# Download Qwen 35B (13GB quantized) from Unsloth
llama-server --model Qwen3.5-35B-A3B-UD-IQ3_XXS.gguf \
  --port 8081 --ctx-size 16384 --n-gpu-layers 0 --mmap \
  --flash-attn on --threads 8
```

### Critical Pitfalls

- `OLLAMA_MAX_LOADED_MODELS=1` is critical on 16GB — without it system dies
- `--n-gpu-layers 0` with mmap lets OS manage paging (unified memory anyway)
- Ollama (port 11434) + llama.cpp (port 8081) coexist fine
- `think: false` in Ollama API → 30x faster classification, same accuracy
- Safety: messages mentioning money/deployment/publishing bypass local triage → straight to Claude
- Very short messages (<20 chars) skip triage — "yes" is ambiguous

### Gemma 4 vs Qwen Benchmarks

- Classification: 8.5s (Qwen) → 1.9s (Gemma 4) — 4.4x faster
- Summarization: ~50s → ~28s — 1.8x faster
- Accuracy: 70% (Gemma) vs 80% (Qwen) — mostly gray areas, fixable with prompting
- Gemma E2B/E4B have native vision + audio (Qwen was text-only)
- Apache 2.0 license (no usage restrictions — critical for 24/7 production)
- Swap: 2 constants changed, 3 files updated. Old models kept as rollback.

## Related Concepts

- [[local-llm-infrastructure]] — full concept page on this setup
- [[token-optimization]] — context compression strategies
- [[ai-coding-agents]] — cloud agent ecosystem
