---
title: Financial LLMs
type: concept
tags: [quantitative-trading, financial-llm, sentiment-analysis, open-source]
created: 2026-04-24
updated: 2026-04-24
confidence: high
status: current
priority: important
summary: "Large language models specialized for finance — sentiment analysis, robo-advisory, trading signals. Open-source alternatives to BloombergGPT."
---

# Financial LLMs

Large language models fine-tuned for financial domain tasks: sentiment analysis, relation extraction, headline classification, named-entity recognition, robo-advisory, and trading signal generation.

## Key Differentiator vs General LLMs

Finance is highly dynamic. Models need weekly/monthly updates with new market data. Full retraining is prohibitively expensive ($3M for BloombergGPT). Lightweight adaptation (LoRA) reduces this to <$300 per fine-tuning.

## Major Projects

### FinGPT (AI4Finance Foundation)
- Open-source, MIT license
- 5-layer architecture: Data Source → Data Engineering → LLMs → Tasks → Applications
- LoRA fine-tuning on open-source base models (Llama-2, Falcon, Qwen, etc.)
- Beats GPT-4 on financial sentiment analysis (0.882 vs 0.833 F1)
- FinGPT-Forecaster: AI robo-advisor for stock movement prediction
- 6 papers at IJCAI 2023, NeurIPS 2023, ICAIF 2023, AAAI 2025
- See [[fingpt-ai4finance-2026-04]]

### BloombergGPT (Bloomberg)
- Proprietary, 50B parameters
- $3M training cost, 53 days on 512 A100s
- Mixed finance + general data
- No RLHF, no open API
- Privileged data access

## Core Tasks

| Task | Description | Key Datasets |
|------|-------------|-------------|
| Sentiment Analysis | Classify financial text as positive/negative/neutral | FPB, FiQA-SA, TFNS, NWGI |
| Relation Extraction | Extract financial entity relationships | FinRED |
| Headline Classification | Price movement from headlines | fingpt-headline |
| Named-Entity Recognition | Extract orgs, persons, locations | fingpt-ner |
| Q&A | Financial question answering | fingpt-fiqa_qa |
| Stock Prediction | Predict price movement from news | FinGPT-Forecaster |

## Fine-Tuning Approaches

1. **LoRA** (Low-Rank Adaptation) — Preferred for FinGPT. <$300 per run, single GPU. Adapts base model without modifying weights.
2. **QLoRA** — 4-bit quantized LoRA. Even cheaper (~$4.15) but lower accuracy.
3. **Full fine-tuning** — BloombergGPT approach. Prohibitively expensive for frequent updates.
4. **RLHF** — Enables personalization (risk tolerance, investing habits). Missing in BloombergGPT.

## Cost Comparison

| Approach | Cost | Hardware | Frequency |
|----------|------|----------|-----------|
| BloombergGPT (full retrain) | $2.67M | 512× A100 | Annual |
| FinGPT LoRA | $17.25 | 1× RTX 3090 | Weekly |
| FinGPT QLoRA | $4.15 | 1× RTX 3090 | Daily |

## Relevance to Quant Trading

Financial LLMs provide signal extraction capabilities:
- **Sentiment signals** from news, tweets, filings
- **Event detection** from headlines
- **Entity extraction** for relationship mapping
- **Price prediction** from multi-source news aggregation

Integration pattern: LLM generates sentiment/features → quant model uses as alpha factors → backtesting pipeline validates.

## Sources
- [[fingpt-ai4finance-2026-04]] — FinGPT repo, full architecture and benchmarks

## Related Concepts
- [[crypto-quant-trading]]
- [[crypto-quant-factor-research]]
- [[crypto-quant-strategy-optimization]]
