---
author: Gabriel Lespérance (@gablesperance) / Alex L. Zhang, Tim Kraska, Omar Khattab
  (MIT/Stanford)
confidence: medium
created: '2026-04-16'
date_added: 2026-04-12
paper_url: https://arxiv.org/abs/2512.24601v1
priority: reference
status: compiled
summary: Recursive Language Models (RLMs)
tags:
- rlm
- recursive-language-models
- agent-architecture
- dspy
- context-management
- inference-scaling
title: Recursive Language Models (RLMs) — Predict RLM by Trampoline AI
type: article
updated: '2026-04-18'
url: https://x.com/gablesperance/status/2042950334469787975
---


# Recursive Language Models (RLMs)

## What Is an RLM?

A Recursive Language Model replaces a standard LM call (`gpt.completion(msg)`) with `rlm.completion(msg)`. Under the hood, the LM writes Python code in a REPL environment to interact with a potentially massive context, sub-calling itself or other LMs for intermediate computation. The user sees the same API — infinite context is the illusion.

Paper: "Recursive Language Models" by Alex L. Zhang, Tim Kraska, Omar Khattab (MIT CSAIL, Stanford NLP, Oct 2025).

## Key Claims (Lespérance's Article)

- "I think I might bet the company on it" — Gabriel Lespérance on RLMs
- RLM = LM + Deno sandbox running Python + calls itself
- Python sandbox concept credited to Simon Willison (`@simonw`)
- The code is the "reasoning substrate" — like algebra for a mathematician
- Small models with REPL outperform bigger models without one
- When base models improve, RLM improves for free — no rewiring, no harness rethinking
- Bitter lesson playing out in real time
- Applications: documents, contracts, repositories, videos, deep research, massive corpora

## The predict-rlm Library

Production-focused port of RLMs by Trampoline AI. Allows LM to call sub-LM with DSPy signatures.

**Features:**
- Fully multimodal (images, docs, audio, video)
- First-class file I/O
- Async tool calling in WASM sandbox
- Structured sub-LM calls with Pydantic
- Composable skills
- Coding agent integration via `npx skills add`
- `uv add predict-rlm`

**Example:**
```python
class AnalyzeImages(dspy.Signature):
    images: list[File] = dspy.InputField()
    query: str = dspy.InputField()
    answer: str = dspy.OutputField()

rlm = PredictRLM(AnalyzeImages, lm="openai/gpt-5.4", sub_lm="openai/gpt-5.1")
result = rlm(images=[File(path="page.png")], query="Extract all visible text.")
```

## Paper Results (Alex Zhang)

- RLM(GPT-5-mini) outperforms GPT-5 on OOLONG benchmark (hardest long-context task) by 2x correct answers
- RLM(GPT-5-mini) is cheaper per query than GPT-5 on average
- No performance degradation at 10M+ tokens at inference time
- Outperforms ReAct + test-time indexing and prompt retrieval on Deep Research tasks

## Context Rot Problem

Context rot: as token count increases, model's ability to accurately recall decreases. Happens in long conversations, bloated Claude Code histories. RLM solves this by programmatically interacting with context through the REPL — root LM stays within comfortable operating range.

## Architecture

1. User calls `rlm.completion(query)`
2. Root LM (depth=0) interacts with Python REPL environment containing the full context
3. Root LM writes code to read/write context cells
4. Root LM can spawn sub-LM calls (depth=1) to process chunks
5. Sub-LMs can spawn their own sub-LMs (recursive)
6. Root LM aggregates results and returns final answer

## RLM vs Harness

- Harnesses (Claude Code, agents): LM mechanically emits each sub-agent call
- RLMs: single line of code can represent 1M sub-calls — expresses structure of computation
- Harnesses encode control flow in scaffolding; RLMs encode it in the code the LM writes
- No context rot — root LM only sees what it needs
- Bitter lesson proof: performance scales with base model improvements automatically

## Related Concepts

- [[recursive-language-models]] — full concept page
- DSPy signatures (Omar Khattab)
- Agent harnesses (Harrison Chase's article)
- Context engineering (Anthropic)
- Inference-time scaling
- ReAct agents
- Program of thought
