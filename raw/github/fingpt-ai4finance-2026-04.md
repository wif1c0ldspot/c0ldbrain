---
title: "FinGPT"
author: "AI4Finance-Foundation"
date: 2026-04-24
source: "https://github.com/AI4Finance-Foundation/FinGPT"
fetched: 2026-04-24
type: raw
---

# FinGPT: Open-Source Financial Large Language Models

Let us not expect Wall Street to open-source LLMs or open APIs, due to FinTech institutes' internal regulations and policies.

## Why FinGPT?

1). Finance is highly dynamic. BloombergGPT trained an LLM using a mixture of finance data and general-purpose data, which took about 53 days, at a cost of around $3M. It is costly to retrain an LLM model like BloombergGPT every month or every week, thus lightweight adaptation is highly favorable. FinGPT can be fine-tuned swiftly to incorporate new data (the cost falls significantly, less than $300 per fine-tuning).

2). Democratizing Internet-scale financial data is critical, say allowing timely updates of the model (monthly or weekly updates) using an automatic data curation pipeline. BloombergGPT has privileged data access and APIs, while FinGPT presents a more accessible alternative. It prioritizes lightweight adaptation, leveraging the best available open-source LLMs.

3). The key technology is "RLHF (Reinforcement learning from human feedback)", which is missing in BloombergGPT. RLHF enables an LLM model to learn individual preferences (risk-aversion level, investing habits, personalized robo-advisor, etc.), which is the "secret" ingredient of ChatGPT and GPT4.

## FinGPT-Forecaster

AI Robo-Advisor milestone. Enter ticker symbol, prediction date, number of past weeks for market news retrieval, and whether to add latest basic financials. Returns a well-rounded analysis and prediction for next week's stock price movement.

## Benchmark Results (Financial Sentiment Analysis)

| Model | FPB | FiQA-SA | TFNS | NWGI | Cost |
|-------|-----|---------|------|------|------|
| FinGPT v3.3 (llama2-13b LoRA) | **0.882** | 0.874 | **0.903** | **0.643** | $17.25 (RTX 3090) |
| OpenAI Fine-tune | 0.878 | **0.887** | 0.883 | - | - |
| GPT-4 | 0.833 | 0.630 | 0.808 | - | - |
| BloombergGPT | 0.511 | 0.751 | - | - | $2.67M |

## Five-Layer FinGPT Framework

1. **Data Source Layer** — Real-time market data capture, temporal sensitivity
2. **Data Engineering Layer** — Real-time NLP data processing, low signal-to-noise handling
3. **LLMs Layer** — LoRA fine-tuning on open-source base models, mitigating dynamic nature
4. **Task Layer** — Sentiment analysis, relation extraction, headline classification, NER, Q&A
5. **Application Layer** — Robo-advisor, trading, financial analysis demos

## Instruction Tuning Datasets

| Dataset | Train Rows | Task |
|---------|-----------|------|
| fingpt-sentiment-train | 76.8K | Sentiment Analysis |
| fingpt-finred | 27.6K | Financial Relation Extraction |
| fingpt-headline | 82.2K | Financial Headline Analysis |
| fingpt-ner | 511 | Financial Named-Entity Recognition |
| fingpt-fiqa_qa | 17.1K | Financial Q&A |
| fingpt-fineval | 1.06K | Chinese Multiple-Choice Questions |

## Multi-Task Models (LoRA)

- fingpt-mt_llama2-7b_lora
- fingpt-mt_falcon-7b_lora
- fingpt-mt_bloom-7b1_lora
- fingpt-mt_mpt-7b_lora
- fingpt-mt_chatglm2-6b_lora
- fingpt-mt_qwen-7b_lora
- fingpt-sentiment_llama2-13b_lora
- fingpt-forecaster_dow30_llama2-7b_lora

## Open-Source Base Models Tested

Llama-2, Falcon, MPT, Bloom, ChatGLM2, Qwen, InternLM

## Key Papers

- FinGPT: Open-Source Financial Large Language Models (IJCAI 2023)
- Instruct-FinGPT: Financial Sentiment Analysis by Instruction Tuning (IJCAI 2023)
- FinGPT-RAG: Enhancing Financial Sentiment Analysis via Retrieval Augmented LLMs (ICAIF 2023)
- FinGPT: Instruction Tuning Benchmark for Open-Source LLMs in Financial Datasets (NeurIPS 2023)
- FinGPT: Data-centric FinGPT: Democratizing Internet-scale Data (NeurIPS 2023)
- FinGPT: Enhancing Sentiment-based Stock Movement Prediction (AAAI 2025)

## Cloud LLM Providers

| Provider | Model | Context Length |
|----------|-------|---------------|
| OpenAI | GPT-3.5-turbo | 16K |
| MiniMax | MiniMax-M2.7 | 204K |
| FinGPT (local) | Llama-2-13B LoRA | 4K |

## License

MIT License. Academic purposes. Not financial advice.
