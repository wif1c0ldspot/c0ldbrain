---
confidence: high
created: '2026-04-16'
priority: reference
sources:
- raw/github/deepteam.md
status: current
summary: Open-source LLM red teaming by confident-ai. 50+ tests, 20+ attacks, OWASP
  mapping.
tags:
- security
- red-teaming
- prompt-injection
- llm-attacks
- compliance
title: DeepTeam - LLM Red Teaming
type: concept
updated: 2026-04-10
---



# DeepTeam - LLM Red Teaming

## Summary

DeepTeam by confident-ai (DeepEval creators): 50+ vulnerability tests, 20+ adversarial attacks, 7 guardrails. Maps to OWASP Top 10 for LLMs 2025, OWASP Top 10 for Agents 2026, NIST AI RMF, MITRE ATLAS.

## Key Categories

| Category | Tests |
|----------|-------|
| Agentic | Goal Theft, Recursive Hijacking, Excessive Agency |
| Security | SQL Injection, SSRF, Tool Poisoning, BFLA, BOLA |
| Privacy | PII Leakage, Prompt Leakage |
| Safety | Illegal Activity, Unexpected Code Execution |

## Usage

`pip install -U deepteam` — works with ANY LLM via LLM-as-a-Judge.

## Related Concepts

[[owasp-top-10-for-llm]], [[llm-vulnerability-scanners]], [[continuous-red-teaming]], [[prompt-injection-comprehensive-2026]]
