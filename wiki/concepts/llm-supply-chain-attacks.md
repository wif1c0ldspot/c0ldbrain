---
confidence: medium
created: '2026-04-16'
priority: reference
status: current
summary: Key Facts
tags:
- infrastructure
- concept
title: Llm Supply Chain Attacks
type: concept
updated: '2026-04-18'
---



## Key Facts
- [[defense-in-depth-llm]] — Layer 1 foundation controls must address supply chain risks
- Attack surface spans: training data → model weights → fine-tuning → serving infrastructure
- High-impact: compromised base model affects all downstream applications

## Attack Vectors

| Vector | Stage | Impact | Detection |
|--------|-------|--------|-----------|
| Poisoned training data | Pre-training | Subtle behavior backdoors | Statistical analysis |
| Compromised fine-tuning | Post-training | Targeted misbehavior | Output analysis |
| Malicious model weights | Distribution | Arbitrary code execution | Weight auditing |
| Dependency attacks | Serving | Runtime exploitation | SBOM scanning |
| API proxy hijacking | Runtime | Data interception | Network monitoring |
| Dataset contamination | Curation | Knowledge poisoning | Data provenance |

## Mitigation Strategies
- **SBOM for AI**: Track all model dependencies, libraries, and fine-tuning data sources
- **Model signing**: Cryptographic verification of model weights before deployment
- **Data provenance**: Document training data sources with [[ai-compliance-frameworks]] requirements
- **Continuous monitoring**: Use [[llm-vulnerability-scanners]] to detect emergent vulnerabilities
- **Red team supply chain**: [[continuous-red-teaming]] must include dependency analysis

## Emerging Threats
- **Fine-tuned backdoors**: Adversarially fine-tuned models that appear normal but respond to trigger phrases
- **LoRA/adapter attacks**: Malicious adapters that override base model safety when loaded
- **Embedding space attacks**: Manipulating the embedding space to cause specific misclassifications

## Related Concepts




[[rag-security]], [[continuous-red-teaming]], [[llm-vulnerability-scanners]], [[ai-compliance-frameworks]]
