---
confidence: medium
created: '2026-04-16'
priority: reference
status: current
summary: Key Facts
tags:
- ai-security
- concept
title: Continuous Red Teaming
type: concept
updated: '2026-04-18'
---



## Key Facts
- [[llm-vulnerability-scanners]] — Automated scanning tools complement manual red teaming
- [[ai-compliance-frameworks]] — NIST AI RMF recommends continuous security testing as a core practice
- Shift from point-in-time audits → ongoing adversarial testing cycles
- Covers: prompt injection, jailbreaking, data extraction, output manipulation, and multi-modal attacks

## Red Teaming Methodology
1. **Reconnaissance** — Map system architecture, available endpoints, input/output channels
2. **Threat Modeling** — Identify attack surfaces based on [[llm-supply-chain-attacks]] patterns
3. **Attack Execution** — Automated fuzzing + manual creative attacks
4. **Analysis & Reporting** — Categorize findings by severity, map to [[owasp-top-10-for-llm]]
5. **Remediation** — Deploy [[defense-in-depth-llm]] controls, re-test

## Testing Categories

| Category | Techniques | Tools |
|----------|-----------|-------|
| Prompt Injection | Direct/indirect injection, framing attacks | garak, promptfoo |
| Jailbreaking | DAN, multi-turn escalation, role-play | llm-guard, promptfoo |
| Data Extraction | Training data regurgitation, API probing | custom scripts |
| Multi-Modal | Image-based injection, audio attacks | vision-specific tools |

## Automation Pipeline
- Schedule: Run red team suites daily/weekly on staging
- Monitor: Track new [[llm-vulnerability-scanners]] and exploit techniques
- Alert: Auto-flag novel attack vectors to security team
- Report: Generate compliance evidence for [[ai-compliance-frameworks]]

## Related Concepts


[[rag-security]], [[prompt-injection-defense-tools]], [[llm-vulnerability-scanners]], [[defense-in-depth-llm]], [[multimodal-ai-security]]

- [[ai-security-handbook-2026]]
- [[ai-security-synthesis]]
- [[clearwing]]
- [[deep-team-red-teaming]]
- [[prompt-injection-comprehensive-2026]]
- [[prompt-injection-testing-tools]]