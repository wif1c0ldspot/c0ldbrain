---
title: "RAG Security"
type: concept
tags: [security, prompt-injection, rag, defense-mechanisms, owasp]
created: 2026-04-09
updated: 2026-04-18
confidence: high
priority: critical
status: current
summary: "Securing Retrieval-Augmented Generation systems against injection and manipulation attacks."
---


## Key Facts
- [[defense-in-depth-llm]] — RAG introduces unique attack surfaces across retrieval and generation
- [[llm-vulnerability-scanners]] — Must scan both retrieved documents and generated responses
- Indirect prompt injection via retrieved documents is the primary threat vector

## RAG Attack Surface

```
User Query → [Input Layer] → Retriever → [Document Injection Risk]
                                    ↓
                            Retrieved Context
                                    ↓
                              [Context Injection]
                                    ↓
                            LLM Generation
                                    ↓
                             [Output Filtering]
                                    ↓
                              Response
```

## Vulnerability Categories

| Category | Attack | Mitigation |
|----------|--------|------------|
| Indirect Injection | Malicious content in retrieved docs | Context sanitization, source filtering |
| Data Exfiltration | Queries leaked via retrieved content | Retriever access controls, output scanning |
| Context Poisoning | Polluting vector DB with crafted docs | [[llm-supply-chain-attacks]] controls on data |
| Retrieval Hijacking | Forcing specific doc retrieval | Query validation, embedding monitoring |
| Prompt Leaking | Retrieved docs contain prompt escapes | Input/output [[defense-in-depth-llm]] layers |

## Defense Architecture
- **Retrieval layer**: Source authentication, document signing, embedding space monitoring
- **Context layer**: Sanitize retrieved text, enforce token limits, detect injection patterns
- **Generation layer**: Apply the same [[defense-in-depth-llm]] protections as non-RAG systems
- **Output layer**: [[llm-vulnerability-scanners]] on generated responses, PII filtering

## Compliance Impact
- [[ai-compliance-frameworks]] increasingly cover RAG-specific risks
- Retrieved content provenance must be documented per regulations
- [[continuous-red-teaming]] must test indirect injection via document corpus

## Related Concepts



[[prompt-injection-comprehensive-2026]], [[defense-in-depth-llm]], [[llm-supply-chain-attacks]], [[continuous-red-teaming]], [[llm-vulnerability-scanners]]

- [[ai-security-handbook-2026]]
- [[ai-security-synthesis]]
- [[multimodal-ai-security]]
- [[owasp-top-10-for-llm]]
- [[pageindex-vectorless-rag-2026-04]]
- [[prompt-injection-attack-vectors]]
- [[prompt-injection-defense-guide]]
- [[prompt-injection-defense-tools]]
- [[prompt-injection-incidents]]
- [[rag]]
- [[vectorless-rag]]