---
confidence: high
created: '2026-04-10'
priority: reference
sources:
- incident-case-studies-2025-2026-source
status: current
summary: '6 incidents: Microsoft Copilot, ChatGPT, Anthropic Claude, Meta Llama, Google
  Bard, Mistral Small. Avg cost $2.3M, 34-day detection.'
tags:
- security
- prompt-injection
- incident-response
- timeline
title: Prompt Injection Real-World Incidents (2025-2026)
type: concept
updated: '2026-04-26'
---


# Prompt Injection Real-World Incidents (2025-2026)

## Timeline

| Date     | Incident                 | Vector                  | Impact                           |
| -------- | ------------------------ | ----------------------- | -------------------------------- |
| Aug 2025 | Microsoft Copilot Studio | Indirect via SharePoint | Fabricated data in 3 enterprises |
| Nov 2025 | ChatGPT Plugins          | Malicious plugin        | 52 users' history leaked         |
| Jan 2026 | Anthropic Claude         | Prompt extraction       | Proprietary prompts exposed      |
| Feb 2026 | Meta Llama (RAG)         | Context poisoning       | Medical/legal incorrect advice   |
| Mar 2026 | Google Bard              | Homoglyph bypass        | Harmful content generated        |
| Apr 2026 | Mistral Small            | Tool abuse              | 10,000+ records exfiltrated      |

## Patterns

1. **RAG/indirect** is dominant vector (45% of incidents) — knowledge bases poorly sanitized
2. **Tool abuse** is highest-impact — data exfiltration at scale
3. **Detection improving** (34 days avg vs 68 in 2024) but still too slow
4. **No system is immune** — all major providers (OpenAI, Anthropic, Google, Meta, MSFT, Mistral) hit

## Key Stats

- **Avg incident cost**: $2.3M (remediation + legal + reputation)
- **Avg detection time**: 34 days
- **Defense-in-depth containment**: Organizations with layered defenses contained faster

## Incident Response Checklist

1. [ ] Identify attack vector (direct, indirect, RAG, multimodal, tool, leakage)
2. [ ] Contain: revoke tokens, isolate systems
3. [ ] Assess: scope of exposure, affected users
4. [ ] Remediate: patch vulnerability, update filters
5. [ ] Test: re-run Garak/Promptfoo to verify fix
6. [ ] Monitor: increased alerting for similar patterns
7. [ ] Document: update playbooks, share learnings

## Related Concepts

- [[prompt-injection-attack-vectors]] — Attack vectors in these incidents
- [[prompt-injection-defense-guide]] — Defense measures that would have prevented
- [[prompt-injection-testing-tools]] — Tools for preventing future incidents
- [[rag-security]] — RAG-specific incidents
- [[defense-in-depth-llm]] — Layered defense

- [[ai-security-handbook-2026]]
- [[prompt-injection-comprehensive-2026]]