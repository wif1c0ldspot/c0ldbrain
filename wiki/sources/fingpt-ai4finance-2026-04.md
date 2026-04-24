---
title: "FinGPT: Open-Source Financial Large Language Models"
author: "AI4Finance-Foundation (Hongyang Yang, Xiao-Yang Liu)"
date: 2026-04-24
type: source
compiled: true
tags: [source, financial-llm, sentiment-analysis, LoRA, robo-advisor, open-source, quant-finance]
source_url: https://github.com/AI4Finance-Foundation/FinGPT
confidence: high
status: current
priority: important
summary: "Open-source financial LLM framework. 5-layer architecture. LoRA fine-tuning <$300. Beats GPT-4 on financial sentiment. Forecaster for robo-advisory. 6 papers at IJCAI/NeurIPS/ICAIF/AAAI."
---

# FinGPT: Open-Source Financial Large Language Models

**Author:** AI4Finance-Foundation (Hongyang Yang, Xiao-Yang Liu)  
**Source:** https://github.com/AI4Finance-Foundation/FinGPT  
**License:** MIT

## Summary

Open-source financial large language model framework by AI4Finance Foundation. Key differentiator from BloombergGPT: lightweight LoRA adaptation instead of full retraining, reducing cost from $3M to <$300 per fine-tuning. Achieves state-of-the-art on financial sentiment analysis benchmarks, beating GPT-4 and BloombergGPT.

## Key Takeaways

1. **Cost advantage over BloombergGPT.** BloombergGPT: $3M, 53 days, 512 A100s. FinGPT: <$300, single RTX 3090, LoRA fine-tuning. Finance is highly dynamic — lightweight adaptation is critical for weekly/monthly updates.

2. **Five-layer architecture:**
   - Data Source Layer (real-time market data)
   - Data Engineering Layer (NLP processing, signal extraction)
   - LLMs Layer (LoRA fine-tuning on open-source bases)
   - Task Layer (sentiment, NER, relation extraction, headline classification, Q&A)
   - Application Layer (robo-advisor, trading demos)

3. **Beats GPT-4 on financial sentiment.** FinGPT v3.3 (llama2-13b LoRA): 0.882 F1 on FPB vs GPT-4 at 0.833. Cost: $17.25 on RTX 3090.

4. **FinGPT-Forecaster.** AI robo-advisor: enter ticker + date → well-rounded company analysis + next-week stock movement prediction. Demo on HuggingFace.

5. **Instruction tuning datasets.** 76.8K sentiment, 27.6K relation extraction, 82.2K headline, 511 NER, 17.1K Q&A. All on HuggingFace.

6. **Multi-model support.** Tested on Llama-2, Falcon, MPT, Bloom, ChatGLM2, Qwen, InternLM as base models. LoRA adapters published for each.

7. **RLHF for personalization.** Enables learning individual preferences (risk level, investing habits). Key differentiator vs BloombergGPT which lacks RLHF.

## Benchmark Highlights

| Model | FPB F1 | FiQA-SA F1 | Cost | Hardware |
|-------|--------|------------|------|----------|
| FinGPT v3.3 | **0.882** | 0.874 | $17.25 | 1× RTX 3090 |
| GPT-4 | 0.833 | 0.630 | API | API |
| BloombergGPT | 0.511 | 0.751 | $2.67M | 512× A100 |

## Key Publications

- NeurIPS 2023 (2 papers): Instruction tuning benchmark + data-centric FinGPT
- IJCAI 2023 (2 papers): Open-source FinLLM + instruction tuning for sentiment
- ICAIF 2023: RAG-enhanced financial sentiment analysis
- AAAI 2025: Sentiment-based stock movement prediction

## Related Concepts
- [[financial-llms]]
- [[crypto-quant-trading]]
- [[crypto-quant-factor-research]]
- [[sentiment-analysis-finance]]

## Related Sources
- [[crypto-quant-data-download-and-optimization]]
