---
confidence: medium
created: '2026-04-16'
priority: reference
status: current
summary: TimesFM — Google Time-Series Foundation Model
tags:
- knowledge-management
- concept
title: Timesfm Google 2026 04
type: concept
updated: '2026-04-18'
---


# TimesFM — Google Time-Series Foundation Model

## Key Insights

- Google Research's pretrained time-series foundation model
- v2.5: 200M parameters with 16k context length
- Published at ICML 2024 — academically validated
- Zero-shot forecasting capability without domain-specific fine-tuning
- Directly applicable to quantitative trading and financial forecasting

## Technical Details

### Model Architecture
- 200M parameter foundation model for time-series
- 16,000 token context window for long-range forecasting
- Patch-based architecture adapted from vision transformers
- Pretrained on massive diverse time-series corpus

### Performance
- Zero-shot performance competitive with domain-specific models
- Strong on financial, weather, and infrastructure time-series
- ICML 2024 publication validates methodology

### Use Cases
- Financial market prediction and trading signals
- Demand forecasting
- Anomaly detection in time-series
- Infrastructure monitoring

### Integration
- Python API for batch and streaming inference
- Compatible with pandas, numpy workflows
- Fine-tuning support for domain adaptation

## Related Concepts

- [[quantitative-trading]] — direct application for trading signal generation
- [[open-source-ai-infra]] — major Google open-source release
