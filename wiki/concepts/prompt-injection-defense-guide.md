---
confidence: high
created: '2026-04-10'
priority: critical
sources:
- llm-guard-sanitization-framework-source
- agentsecops-guardian-self-healing-source
status: current
summary: 'Defense-in-depth architecture: 5 layers — input validation, prompt engineering,
  output filtering, architectural controls, monitoring.'
tags:
- security
- prompt-injection
- defense-mechanisms
- compliance
title: Prompt Injection Defense Guide
type: concept
updated: '2026-04-26'
---

# Prompt Injection Defense Guide

## Defense-in-Depth Architecture

### Layer 1: Input Validation
- Strip invisible Unicode, normalize NFC (homoglyph defense)
- Pattern matching for instruction triggers ("ignore", "override", "reset")
- LLM-based classifier for intent scoring
- Canary tokens (honeypot instructions with fake credentials)
- **Tools**: `llm-guard` (15+ input scanners), custom regex

### Layer 2: System Prompt Engineering
- Enforce strict context adherence with explicit delimiters `[SYSTEM]`/`[USER]`
- Few-shot examples with malicious prompt handling
- Temperature=0 for safety-critical decisions
- Example: explicit rejection rules ("I cannot comply with that request")

### Layer 3: Output Filtering
- Regex scanning for credentials, PII, malicious URLs
- ML toxicity/bias detection, content moderation APIs
- Template enforcement (strict JSON/structured response formats)
- Groundedness checks against trusted sources
- **Tools**: `llm-guard` (12+ output scanners)

### Layer 4: Architectural Controls
- **Least Privilege**: minimal API tokens, restricted function calling, per-user credentials
- **Sandboxing**: isolated container/VM, no network egress, read-only FS
- **Human-in-the-Loop**: approval for high-risk ops, flagged reviews for critical decisions
- **Rate Limiting**: per-user/IP/session, exponential backoff on violations

### Layer 5: Monitoring & Response
- Audit logs: every prompt, response, tool call, retrieval
- Real-time anomaly detection + alerting
- Incident response playbook for prompt injection
- Automated quarantine of suspicious accounts

## Implementation Roadmap

| Week | Focus |
|------|-------|
| 1 | Assess: Garak scan, inventory RAG, deploy audit logging |
| 2 | Harden: sanitization, tool whitelisting, output filtering |
| 3 | Monitor: dashboards, alerts, response playbook, tabletop |
| 4 | Validate: Promptfoo red-team, pen test, re-scan with Garak |

**Ongoing**: Monthly Garak scans, Promptfoo CI/CD, KB audits, team training.

## ROI

- **Cost**: $0 licensing, 2-4 weeks engineering, <10% inference overhead
- **Saves**: $2.3M avg per prevented incident
- **Compliance**: EU AI Act, NIST AI RMF
- **Positive ROI** within 6-12 months for any org with 1+ LLM deployment

## Related Concepts

- [[ai-security-synthesis]] — Unified view of AI security landscape
- [[prompt-injection-comprehensive-2026]]
- [[prompt-injection-testing-tools]] — Garak, Promptfoo, llm-guard testing
- [[prompt-injection-defense-tools]] — 11 additional defense tools
- [[llm-vulnerability-scanners]] — Broader scanning
- [[defense-in-depth-llm]] — Layered architecture
- [[rag-security]] — RAG measures
- [[multimodal-ai-security]] — Multimodal patterns
- [[ai-compliance-frameworks]] — Regulatory compliance

- [[ai-security-handbook-2026]]
- [[prompt-injection-attack-vectors]]
- [[prompt-injection-incidents]]