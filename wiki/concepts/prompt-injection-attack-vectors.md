---
confidence: high
created: '2026-04-10'
priority: critical
sources:
- owasp-top10-llm-2025-source
- rag-specific-injection-vulnerabilities-source
- multimodal-injection-emerging-threats-source
- academic-papers-2025-2026-source
- incident-case-studies-2025-2026-source
status: current
summary: '6 attack vectors: direct, indirect, RAG-specific, multimodal, tool abuse,
  system prompt leakage. 78% of incidents, avg cost $2.3M.'
tags:
- security
- prompt-injection
- llm-attacks
- defense-mechanisms
title: Prompt Injection Attack Vectors (2026)
type: concept
updated: '2026-04-26'
---

# Prompt Injection Attack Vectors (2026)

## Key Facts

- **OWASP LLM01:2025**: #1 critical vulnerability
- **Incident rate**: 78% of LLM incidents involve prompt injection
- **RAG/indirect**: 45% of attacks (up from 20% in 2025)
- **Multimodal**: 30%+ false negative detection rate
- **Avg incident cost**: $2.3M

---

## 1. Direct Injection

User prompt directly alters behavior:
- Instruction override, role-playing/jailbreaking (DAN)
- Encoding obfuscation (base64, hex, zero-width chars)
- Unicode homoglyphs
- Defense: input sanitization, system prompt hardening, output validation

## 2. Indirect Injection

External content (documents, websites, API responses) contains hidden instructions that influence model when retrieved.
- Sources: RAG knowledge bases, web search, uploads, DB results
- Impact: data exfiltration, context poisoning, cross-session contamination
- Defense: document sanitization, retrieval validation, provenance tracking, periodic KB audits

## 3. RAG-Specific

| Vulnerability | Mitigation |
|---------------|-----------|
| Context poisoning (malicious doc in vector DB) | Sanitize pre-embedding |
| Metadata injection (EXIF, title fields) | Strip all metadata |
| Chunk-splitting (instruction split across docs) | Cross-chunk pattern detection |
| Cross-user contamination (shared vector store) | Per-user isolation |
| Retrieval manipulation (poisoned embeddings) | Anomaly detection |

**Case**: Microsoft Copilot (Aug 2025) — SharePoint document poisoning → fabricated customer data.

## 4. Multimodal

Hidden instructions in non-text media bypass text-only filters:
- **Images**: steganography (LSB, frequency domain), EXIF metadata, OCR-able text with camouflage, adversarial perturbations
- **Audio**: subliminal messages, fast speech compression, hidden in lyrics
- **Video**: frame sequencing, caption manipulation, cross-modal conflicts
- **Detection**: `zsteg` for steganalysis, OCR + sanitization, metadata stripping, STT output filtering
- **Challenge**: 57-68% accuracy, 50-2000ms/scan latency
- **Case**: ChatGPT Vision (Jan 2026) — hidden OCR text in screenshot triggered system override

## 5. Tool & Function Call Abuse

Injection induces unauthorized tool execution (DB queries, emails, file ops, CI/CD, cloud provisioning, payments).
- Defense: tool whitelisting, parameter validation, human approval for high-risk ops, audit logging

**Case**: Mistral Small (Apr 2026) — 10,000+ records exfiltrated via DB tool abuse.

## 6. System Prompt Leakage

Extracting hidden system prompts via repeated queries, role-play as developer mode, encoding (base64, rot13), format switching.
- Impact: proprietary guardrails exposed, competitive intelligence loss
- Defense: no API access to system prompt, rate limiting, anomaly detection

**Case**: Anthropic Claude (Jan 2026) — ~80% of system prompt extracted via repeated queries.

## Related Concepts

- [[prompt-injection-defense-guide]] — 5-layer defense architecture
- [[prompt-injection-testing-tools]] — Garak, Promptfoo, llm-guard
- [[prompt-injection-defense-tools]] — 11 defense tools survey
- [[rag-security]] — RAG-specific risks
- [[multimodal-ai-security]] — Image/audio/video vectors
- [[defense-in-depth-llm]] — Layered defense
- [[owasp-top-10-for-llm]] — OWASP standards

- [[ai-security-handbook-2026]]
- [[prompt-injection-comprehensive-2026]]
- [[prompt-injection-incidents]]