---
confidence: high
created: '2026-04-10'
priority: reference
sources:
- garak-vulnerability-scanner-source
- promptfoo-red-teaming-platform-source
- academic-papers-2025-2026-source
status: current
summary: Garak (NVIDIA scanner v5.0), Promptfoo (red team platform v3.0, acquired
  by OpenAI), llm-guard (real-time sanitizer v2.0), AgentSecOps Guardian (self-healing,
  early).
tags:
- security
- prompt-injection
- red-teaming
- developer-tools
title: Prompt Injection Testing Tools
type: concept
updated: '2026-04-26'
---


# Prompt Injection Testing Tools

## Tool Comparison

| Tool | Type | Multimodal | RAG | CI/CD | Maturity |
|------|------|------------|-----|-------|----------|
| **Garak** (NVIDIA) | 200+ probe scanner | ✅ v5.0 | ✅ | ✅ | High |
| **Promptfoo** (OpenAI) | Red team platform | ❌ | ✅ | ✅ | High |
| **llm-guard** (ProtectAI) | Real-time sanitizer | ✅ v2.0 | ❌ | ✅ | High |
| **AgentSecOps Guardian** | Self-healing auto-patch | ❌ | ❌ | ✅ | Low (early) |

## Tool Details

### Garak (NVIDIA) — Find vulnerabilities
- 200+ probes across injection, hallucination, toxicity, jailbreaks
- v5.0 added multimodal (image/audio) injection tests, RAG probes
- `pip install garak` → `garak --target_type openai --probes promptinject`
- Output: FAIL/PASS per probe with detailed logs
- Best for: comprehensive scanning, CI/CD, research

### Promptfoo (OpenAI) — Continuous red-teaming
- Declarative YAML configs, PR annotations with remediation
- 300k+ community threat intel, multi-model comparison
- `npm install -g promptfoo` → `promptfoo redteam run`
- Best for: developer-friendly CI/CD, enterprise, continuous monitoring

### llm-guard (ProtectAI) — Block attacks in real-time
- 15+ input scanners + 12 output scanners
- <10ms latency (vs 50-200ms for others)
- Focus: real-time middleware, not attack generation
- Best for: production middleware, low-latency requirements

### AgentSecOps Guardian — Self-healing (experimental)
- Closed-loop: monitor → detect → auto-patch → deploy → verify
- Mistral AI Hackathon winner 2026 — wait for v1.5+ for production

## Recommendation

**Garak + llm-guard** for comprehensive coverage (Garak finds vulns, llm-guard blocks them). Add Promptfoo for continuous monitoring. All open source, $0 licensing.

## Related Concepts

- [[prompt-injection-attack-vectors]] — What these tools test for
- [[prompt-injection-defense-guide]] — What these tools enforce
- [[prompt-injection-defense-tools]] — 11 additional tools (ShieldX, OASIS, Buzur)
- [[deep-team-red-teaming]] — 50+ vuln tests, OWASP mapping
- [[continuous-red-teaming]] — Ongoing security assessment
- [[llm-vulnerability-scanners]] — Broader scanning

- [[ai-security-handbook-2026]]
- [[prompt-injection-comprehensive-2026]]
- [[prompt-injection-incidents]]