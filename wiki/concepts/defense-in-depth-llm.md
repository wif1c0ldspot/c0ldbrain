---
confidence: medium
created: '2026-04-16'
priority: reference
status: current
summary: Key Facts
tags:
- ai-security
- infrastructure
- concept
title: Defense In Depth Llm
type: concept
updated: '2026-04-18'
---



## Key Facts
- [[ai-compliance-frameworks]] — NIST and ISO recommend defense-in-depth for AI systems
- No single control is sufficient against evolving LLM attack techniques
- Layers work synergistically — breaching one layer triggers the next

## Layer Architecture

```
┌─────────────────────────────────────────┐
│ Layer 5: Detection & Response          │
│   - Behavioral monitoring              │
│   - Anomaly detection on outputs        │
│   - Incident automated response         │
├─────────────────────────────────────────┤
│ Layer 4: Output Filtering              │
│   - Content moderation                  │
│   - PII/data leak prevention            │
│   - Response validation                 │
├─────────────────────────────────────────┤
│ Layer 3: Runtime Protection            │
│   - Prompt injection detection          │
│   - Input sanitization                  │
│   - Rate limiting                       │
├─────────────────────────────────────────┤
│ Layer 2: Access Control                │
│   - API authentication                  │
│   - Role-based permissions              │
│   - Model isolation                     │
├─────────────────────────────────────────┤
│ Layer 1: Foundation Controls           │
│   - Supply chain verification           │
│   - Training data provenance            │
│   - Model security assessment           │
└─────────────────────────────────────────┘
```

## Implementation Guidance
- **Layer 1**: Verify model sources, scan for [[llm-supply-chain-attacks]], audit training data
- **Layer 2**: Implement strict API auth, isolate model inference from production data
- **Layer 3**: Use [[llm-vulnerability-scanners]] at runtime, sanitize all user inputs
- **Layer 4**: Filter outputs for PII, enforce schema validation, content moderation
- **Layer 5**: Monitor for [[continuous-red-teaming]] triggers, automated incident response

## Related Concepts



[[prompt-injection-comprehensive-2026]], [[llm-supply-chain-attacks]], [[continuous-red-teaming]], [[llm-vulnerability-scanners]], [[rag-security]]

- [[ai-security-handbook-2026]]
- [[ai-security-synthesis]]
- [[magika]]
- [[multimodal-ai-security]]
- [[owasp-top-10-for-llm]]
- [[prompt-injection-attack-vectors]]
- [[prompt-injection-defense-guide]]
- [[prompt-injection-defense-tools]]
- [[prompt-injection-incidents]]