---
compiled: true
confidence: high
created: '2026-04-16'
priority: important
source_url: https://hermes-agent.nousresearch.com/docs/skills/
sources:
- hermes-agent-skills-hub-2026-04
status: current
summary: Official Hermes Agent Skills Hub catalog — 643 skills across 4 registries
  (77 built-in, 45 optional, 521 community).
tags:
- hermes
- ai-agents
- developer-tools
title: Hermes Agent Skills Hub
type: source
updated: '2026-04-26'
---


# Hermes Agent Skills Hub

**Source:** https://hermes-agent.nousresearch.com/docs/skills/
**Type:** Docusaurus documentation site (v3.9.2)
**Org:** Nous Research

## Summary

Official skills catalog for Hermes Agent, listing 643 skills across 4 registries and 16 categories. Includes built-in skills, optional installables, and community contributions from Anthropic and LobeHub.

## Key Statistics

| Stat | Value |
|------|-------|
| Total skills | 643 |
| Registries | 4 |
| Built-in | 77 |
| Optional | 45 |
| Community (Anthropic) | 16 |
| Community (LobeHub) | 505 |
| Categories | 16 |

## Category Breakdown

| Category | Count |
|----------|-------|
| Other | 348 |
| Software Dev | 69 |
| Creative (incl. popular-web-designs) | 54 |
| MLOps | 42 |
| Research | 37 |
| Translation | 24 |
| Productivity | 12 |
| Gaming | 11 |
| Social Media | 7 |
| Health | 7 |
| AI Agents | 6 |
| GitHub | 6 |
| Media | 6 |
| Security | 6 |
| Apple | 4 |
| Copywriting | 4 |

## Notable Built-in Tools

**LLM Safety/Mechanistic Interpretability:**
- obliteratus — Remove refusal behaviors from open-weight LLMs using mechanistic interpretability (diff-in-means, SVD, whitened SVD, LEACE, SAE decomposition). 9 CLI methods, 28 analysis modules, 116 model presets, tournament evaluation.

**Structured Generation:**
- outlines — Guarantee valid JSON/XML/code structure during generation, Pydantic models for type-safe outputs
- guidance — Microsoft constrained generation with regex and grammars

**Model Serving:**
- vllm — High-throughput LLM serving with PagedAttention and continuous batching
- llama-cpp — CPU/Apple Silicon/consumer GPU inference without CUDA
- tensorrt-llm — NVIDIA TensorRT optimized inference
- gguf — llama.cpp quantization (2-8 bit) for efficient local inference

**Fine-tuning:**
- axolotl — YAML-based fine-tuning with 100+ model support, LoRA/QLoRA, DPO/KTO/ORPO/GRPO
- trl — SFT, DPO, PPO/GRPO, reward model training
- unsloth — 2-5x faster fine-tuning, 50-80% less memory
- peft — LoRA/QLoRA and 25+ parameter-efficient methods
- grpo-rl-training — GRPO/RL training with TRL for reasoning

**External Resources:**
- Skills Hub: https://agentskills.io
- GitHub: https://github.com/NousResearch/hermes-agent
- Discord: https://discord.gg/NousResearch

## Key Insights

1. Skills ecosystem is much larger than local count suggests (643 total vs ~45 installed)
2. LobeHub contributes 505 of the 643 skills — community is dominant source
3. obliteratus is a significant tool for model surgery — mechanistic interpretability methods to excise guardrails while preserving reasoning
4. Structured generation has two major implementations: outlines (dottxt.ai) and guidance (Microsoft Research)
5. Platform targeting exists: some skills are macOS-only (Apple), some Linux+macOS

## Related Concepts

- [[hermes-agent-architecture]]
- [[ai-coding-agents]]
- [[skill-registry]]
