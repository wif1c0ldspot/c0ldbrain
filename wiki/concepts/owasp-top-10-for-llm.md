---
confidence: medium
created: '2026-04-16'
priority: reference
status: current
summary: OWASP Top 10 for LLM Applications
tags:
- ai-security
- infrastructure
- concept
title: Owasp Top 10 For Llm
type: concept
updated: '2026-04-18'
---




# OWASP Top 10 for LLM Applications

## Key Facts
- [[ai-compliance-frameworks]] — The OWASP Top 10 is referenced by major compliance frameworks as a baseline
- [[llm-vulnerability-scanners]] — Most scanners map findings to OWASP categories
- Published by OWASP — a globally recognized open community for application security
- Maintained through community research and real-world incident analysis

## The OWASP LLM Top 10

| Rank | Risk Category | Description |
|------|--------------|-------------|
| 1 | Prompt Injection (LLM01) | Manipulating LLM input to produce unintended behavior |
| 2 | Insecure Output Handling (LLM02) | Treating LLM output as trusted without validation |
| 3 | Training Data Poisoning (LLM03) | Corrupting training data to compromise model behavior |
| 4 | Model Denial of Service (LLM04) | Resource exhaustion through excessive/complex LLM calls |
| 5 | Supply Chain Vulnerabilities (LLM05) | Compromised models, plugins, or dependencies |
| 6 | Sensitive Information Disclosure (LLM06) | Unintended exposure of confidential data in outputs |
| 7 | Insecure Plugin Design (LLM07) | Plugins with excessive privileges or poor input validation |
| 8 | Excessive Agency (LLM08) | LLMs taking unauthorized actions via connected systems |
| 9 | Overreliance (LLM09) | Users making decisions based on incorrect LLM output |
| 10 | Model Theft (LLM10) | Unauthorized access to proprietary model weights/architecture |

## Most Critical for Our Wiki
- **LLM01 (Prompt Injection)**: Core threat across all concepts — see [[defense-in-depth-llm]], [[rag-security]], [[multimodal-ai-security]]
- **LLM05 (Supply Chain)**: See [[llm-supply-chain-attacks]] for deep dive
- **LLM02 (Insecure Output)**: Handled by Layer 4 in our defense architecture
- **LLM03 (Poisoning)**: Covered by data provenance controls

## Testing Alignment
- [[continuous-red-teaming]] exercises map directly to OWASP categories
- [[llm-vulnerability-scanners]] report findings in OWASP Top 10 format
- Compliance audits reference OWASP as industry benchmark per [[ai-compliance-frameworks]]

## Related Concepts



[[prompt-injection-defense-tools]], [[llm-vulnerability-scanners]], [[defense-in-depth-llm]], [[continuous-red-teaming]]

- [[ai-security-handbook-2026]]
- [[ai-security-synthesis]]
- [[clearwing]]
- [[deep-team-red-teaming]]
- [[prompt-injection-attack-vectors]]
- [[prompt-injection-comprehensive-2026]]
- [[infrastructure-handbook-2026]]