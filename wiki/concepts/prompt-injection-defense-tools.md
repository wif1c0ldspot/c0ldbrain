---
confidence: medium
created: '2026-04-16'
priority: reference
status: current
summary: Prompt Injection Defense Tools
tags:
- ai-security
- concept
title: Prompt Injection Defense Tools
type: concept
updated: '2026-04-18'
---



# Prompt Injection Defense Tools

## Summary

Survey of tools defending against prompt injection — from single-dev projects to major lab releases.

## Key Tools

| Tool | Stars | Focus | Maturity |
|------|-------|-------|----------|
| ShieldX | 5 | 547+ rules, 10-layer, 91.9% TPR | Active |
| Promptfoo | 19.7k | Red teaming platform, CI/CD | Production |
| Prompt Siren (Meta) | 47 | Research workbench, state machine | Research |
| OASIS | 2 | OpenClaw Slack plugin, deterministic | Prototype |
| LochBot | 0 | 31 patterns, client-side checker | Tool |
| AgentSec Sandbox | 0 | 565 test cases, 11 defenses | Research |
| Sec-Ops Guard | 1 | 49 hooks, 28 MCP tools | Prototype |
| Buzur | 0 | Web search collective defense | Prototype |
| Text2SQL Security | 0 | 6-layer Text2SQL defense | Project |
| OpenEnv Defense | 0 | Agent robustness testing | Experiment |
| GuardRails | 19 | Ruby Rails scanner (not LLM) | Archived |

## Key Findings

1. No silver bullet — defense-in-depth required
2. ShieldX (91.9% TPR) and Promptfoo lead in measurable results
3. Deterministic beats LLM judgment (OASIS uses regex)
4. Buzur's collective defense model = immune system for AI
5. AgentSec Sandbox provides first standardized benchmark

## Related Concepts



[[rag-security]], [[llm-vulnerability-scanners]], [[continuous-red-teaming]], [[owasp-top-10-for-llm]], [[defense-in-depth-llm]]
