---
confidence: high
created: '2026-04-11'
priority: important
sources:
- prompt-injection-comprehensive-2026
- defense-in-depth-llm
- llm-vulnerability-scanners
- ai-compliance-frameworks
- owasp-top-10-for-llm
- continuous-red-teaming
- rag-security
- llm-supply-chain-attacks
- multimodal-ai-security
- prompt-injection-defense-tools
- prompt-injection-attack-vectors
- prompt-injection-defense-guide
- prompt-injection-testing-tools
- prompt-injection-incidents
- deep-team-red-teaming
status: current
summary: Synthesized handbook of AI security for LLM systems, covering OWASP Top 10,
  attack vectors, defense-in-depth architecture, vulnerability scanners, red-teaming,
  and compliance frameworks.
tags:
- security
- handbook
title: AI Security Handbook — LLM Defense-in-Depth 2026
type: synthesis
updated: '2026-04-11'
---


# AI Security Handbook — LLM Defense-in-Depth 2026

## Definition

Securing Large Language Model deployments requires a layered defense strategy across the entire stack — from the raw input through LLM reasoning to output delivery and system-level API tool calls. As of 2026, **prompt injection remains the #1 critical vulnerability (OWASP LLM01)**, responsible for 78% of all LLM security incidents with an average cost of $2.3M per incident.

## History & Evolution

| Period | Milestone |
|--------|-----------|
| 2023 | First major prompt injection attacks; OWASP LLM Top 10 published |
| 2024 | RAG-specific injection vectors discovered; multimodal attacks (GPT-4V, LLaVA) |
| 2025 | OWASP LLM Top 10 updated (LLM01-LLM10); agentic tool-calling introduces new vectors; DeepTeam, Promptfoo emerge |
| 2026 | Supply-chain attacks surface; continuous red-teaming becomes standard; 6 major incidents reported (Microsoft Copilot, ChatGPT, Claude, Llama, Bard, Mistral) |

## Attack Vectors (6 Categories)

### 1. Direct Prompt Injection
User-crafted prompts that override system instructions. Techniques: DAN, role-play, context window hijacking.

### 2. Indirect/Data Poisoning
Malicious content injected into training data, RAG documents, or system prompts via third-party sources.

### 3. RAG-Specific Injections
Attack vectors exploiting retrieval pipelines: vector database poisoning, context window attacks, document-based injection.

### 4. Multimodal Attacks
Image/audio inputs containing adversarial perturbations (GPT-4V, Gemini, LLaVA). Hidden text in images bypasses text-only filters.

### 5. Tool/Plugin Abuse
LLM agent tool-calling exploited: unauthorized data access, recursive hijacking, excessive agency, goal theft.

### 6. System Prompt Leakage
Exposing internal instructions, API keys, or configuration data through carefully crafted queries.

## Defense-in-Depth Architecture (5 Layers)

| Layer | Controls | Tools |
|-------|----------|-------|
| 1. Input Validation | Pattern matching, sanitization, rate limiting | llm-guard, ShieldX (547+ rules) |
| 2. Prompt Engineering | System prompt hardening, role separation | Anthropic safety patterns |
| 3. Output Filtering | PII detection, harmful content detection | Rebuff.ai, Counterfit |
| 4. Architectural | Sandboxed tool execution, least privilege, API boundaries | AgentSecOps, sandbox |
| 5. Monitoring & Response | Continuous scanning, alerting, incident response | Garak, Promptfoo, DeepTeam |

## Scanner & Tool Landscape

### Vulnerability Scanners
| Tool | Type | Best For |
|------|------|----------|
| **Garak** (NVIDIA) | CLI | Comprehensive LLM probing, 5.0 |
| **Promptfoo** | Framework | CI/CD red-teaming platform, acquired by OpenAI |
| **DeepTeam** | SDK | 50+ tests, OWASP & MITRE ATLAS mapping |
| **llm-guard** | Library | Real-time input/output filtering |
| **Microsoft PyRIT** | SDK | Enterprise AI safety testing |

### Defense Tools
| Tool | TPR | Maturity |
|------|-----|----------|
| **ShieldX** | 91.9% | Active |
| **Promptfoo** | — | Production (19.7k stars) |
| **Prompt Siren** (Meta) | — | Research |
| **OASIS** | Deterministic | Prototype (regex-based) |

## Consensus & Best Practices

1. **Defense-in-depth is non-negotiable** — no single tool covers all vectors
2. **Garak + llm-guard + Promptfoo** = minimum viable scanning stack
3. **Deterministic > LLM-judgment** for input filtering (regex beats generative)
4. **Continuous red-teaming** must run in CI/CD, not just pre-deployment
5. **RAG systems need dedicated injection testing** — they extend the attack surface significantly
6. **Supply-chain security** increasingly critical as LLM dependencies grow
7. **OWASP Top 10 for LLMs + Agents** = baseline compliance framework

## Related Concepts
- [[prompt-injection-comprehensive-2026]] — Hub page for detailed sub-guides
- [[defense-in-depth-llm]] — Layer-by-layer defense architecture
- [[llm-vulnerability-scanners]] — Scanner comparison and integration patterns
- [[continuous-red-teaming]] — Ongoing security assessment methodology
- [[owasp-top-10-for-llm]] — OWASP compliance framework details
- [[rag-security]] — RAG-specific security considerations
- [[llm-supply-chain-attacks]] — Supply-chain threat landscape
- [[multimodal-ai-security]] — Multi-modal attack vectors
- [[ai-compliance-frameworks]] — AI regulatory compliance standards
- [[deep-team-red-teaming]] — DeepTeam red-teaming framework
- [[prompt-injection-attack-vectors]] — Detailed attack vector catalog
- [[prompt-injection-defense-guide]] — Implementation guide for defenses
- [[prompt-injection-testing-tools]] — Testing tool deep-dive
- [[prompt-injection-defense-tools]] — Defense tool survey
- [[prompt-injection-incidents]] — Real-world incident case studies
