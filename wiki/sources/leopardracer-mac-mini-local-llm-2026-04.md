---
author: '@leopardracer'
confidence: high
created: '2026-04-16'
date: 2026-04-13
ingested: 2026-04-15
platform: X/Twitter
priority: reference
stats: 1.2M views, 1K likes, 4K bookmarks, 134 reposts, 48 replies
status: current
summary: How My $600 Mac Mini Runs a 35B AI Model
tags:
- local-llm
- mac-mini
- mmap
- model-routing
- gemma4
- qwen
- ollama
- ai-agent
title: 'Leopardracer: $600 Mac Mini Running 35B AI Model'
type: source
updated: '2026-04-18'
url: https://x.com/leopardracer/status/2043631410045452360
compiled: true
source_url: https://x.com/leopardracer/status/2043631410045452360
---


# How My $600 Mac Mini Runs a 35B AI Model

**Author:** @leopardracer
**Date:** April 13, 2026
**Platform:** X/Twitter

## Content

Comprehensive guide to running local LLMs on a Mac Mini M4 (16GB) as AI agent infrastructure. Covers three-tier model routing (Gemma 4 E2B/E4B + Qwen 35B via mmap), context compression, signal compression, memory consolidation, and a resilience chain for 24/7 uptime.

Key discoveries:
- mmap trick: 35B model on 16GB RAM at 17.3 tok/s, zero swap
- Gemma 4: 4.4x faster classification than Qwen, Apache 2.0 license, native multimodal
- Thinking mode disabled for classification: 30x speedup
- Three-tier routing saves 30-40% cloud API sessions
- Resilience chain with automatic cooldown tracking

## Key Resources

- Ollama 0.20+ (Gemma 4 support)
- llama.cpp (--mmap flag)
- Unsloth Qwen3.5-35B-A3B-UD-IQ3_XXS.gguf (13GB quantized)
- Apple "LLM in a Flash" paper (Dec 2023)
- Telegram channel: https://t.me/+ygATQAt9sUM1N2U6

## Reliability

High confidence. Author runs this in production 24/7. Specific numbers, specific hardware, specific commands. Benchmark methodology described. Pitfalls honestly documented.
