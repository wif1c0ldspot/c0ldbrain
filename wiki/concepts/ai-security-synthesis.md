---
title: "AI Security — Synthesis"
type: synthesis
tags: [ai-security, synthesis, prompt-injection, defense, red-teaming]
created: 2026-04-20
updated: 2026-04-20
confidence: high
status: current
priority: critical
summary: "Unified view of AI security landscape — prompt injection attack vectors, defense patterns, memory poisoning, and continuous red-teaming frameworks."
---

# AI Security — Synthesis

## The Threat Landscape

AI security breaks into three layers:

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 3: Application     │ RAG poisoning, tool misuse      │
│  Layer 2: Model           │ Jailbreaks, prompt injection    │
│  Layer 1: Infrastructure  │ Supply chain, training data     │
└─────────────────────────────────────────────────────────────┘
```

## Layer 1: Infrastructure Security

### Supply Chain Attacks
- **PyPI/Conda poisoning** — malicious packages in ML pipelines
- **Model weight tampering** — backdoored fine-tuned models
- **Dependency confusion** — internal packages hijacked

**Defense:** [[llm-supply-chain-attacks]], pip-audit, hash verification, uv lockfiles

## Layer 2: Model Security

### Prompt Injection
The dominant attack vector against LLM applications.

**Attack Types:**
| Type | Description | Severity |
|------|-------------|----------|
| Direct injection | User embeds malicious instructions in input | High |
| Indirect injection | Malicious content retrieved by RAG | Critical |
| Multi-turn injection | Gradual manipulation across conversation | High |
| Tool poisoning | Malicious tool descriptions hijack agent | Critical |

**Key Statistics:**
- **MINJA** — >95% injection success rate on state-of-the-art models
- **Agent systems especially vulnerable** — tool use expands attack surface
- **No complete defense exists** — only risk reduction

### Jailbreaks
Bypassing safety training to elicit harmful outputs.

**Techniques:**
- **G0DM0D3** — Parsimonious jailbreak, minimal tokens
- **Obfuscation** — encoding, translation, base64 wrapping
- **Persona adoption** — "DAN" (Do Anything Now), developer mode

**Defense:** [[defense-in-depth-llm]], output filtering, input sanitization

## Layer 3: Application Security

### RAG-Specific Attacks
- **Poisoned documents** — malicious content in knowledge base
- **Context manipulation** — controlling what the model "knows"
- **Citation fraud** — fake sources that appear legitimate

**Defense:** [[rag-security]], document validation, source authority checks

### Memory Poisoning
- **OWASP ASI06** — Memory Poisoning in the AI Security Top 10
- **Attack vector:** Corrupt agent's persistent memory to manipulate future behavior
- **Impact:** Long-term manipulation across sessions

**Defense:** [[memory-firewall]] — input validation, integrity checks, sandboxing

## Defense Patterns

### The Defense-in-Depth Stack

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 4: Output Guardrails │ Content filtering, PII scan   │
│  Layer 3: Tool Controls     │ Permission boundaries, audits │
│  Layer 2: Input Sanitization│ Prompt filtering, encoding    │
│  Layer 1: Model Hardening   │ Safety training, RLHF         │
└─────────────────────────────────────────────────────────────┘
```

### Continuous Red-Teaming
Security is not a one-time audit — it's continuous.

**Framework:** [[continuous-red-teaming]]
- Automated attack generation
- Regular penetration testing
- Adversarial simulation
- Feedback loop into defenses

### OWASP Top 10 for LLM Applications
The industry-standard vulnerability classification:

1. **LLM01: Prompt Injection** — Overcoming system prompts via crafted input
2. **LLM02: Insecure Output Handling** — Unvalidated LLM output to downstream
3. **LLM03: Training Data Poisoning** — Malicious data in training corpus
4. **LLM04: Model Denial of Service** — Resource exhaustion attacks
5. **LLM05: Supply Chain Vulnerabilities** — Compromised components
6. **LLM06: Sensitive Information Disclosure** — PII/secrets in output
7. **LLM07: Insecure Plugin Design** — Weak tool/MCP security
8. **LLM08: Excessive Agency** — Unrestricted tool access
9. **LLM09: Overreliance** — Trusting LLM output uncritically
10. **LLM10: Model Theft** — Extraction of model weights/IP

## Security Tooling

| Tool | Purpose | Status |
|------|---------|--------|
| G0DM0D3 | Jailbreak testing | Active |
| Promptmap | Automated injection testing | Active |
| Rebuff | Prompt injection detection | Active |
| LLM Guard | Input/output validation | Active |
| Vigil | Vector DB poisoning detection | Active |

## Key Insights

### From Recent Sources
- **Memory poisoning is emerging** — persistent memory = persistent attack surface
- **Tool use expands vulnerability** — every tool is a potential injection vector
- **No silver bullet** — defense requires layered approach
- **Red-teaming must be continuous** — attacks evolve, defenses must too

### Supply Chain Priority
- **Delayed update policies** — wait 14-30 days before applying critical updates
- **Hash verification** — lockfiles with pinned hashes
- **Audit trails** — track every dependency change

## Related Concepts

- [[prompt-injection-comprehensive-2026]] — Complete attack vector catalog
- [[prompt-injection-defense-tools]] — Defense tooling deep dive
- [[continuous-red-teaming]] — Ongoing security testing
- [[defense-in-depth-llm]] — Layered defense architecture
- [[memory-firewall]] — Memory poisoning defense
- [[rag-security]] — RAG-specific security patterns
- [[llm-supply-chain-attacks]] — Supply chain vulnerabilities
- [[owasp-top-10-for-llm]] — Standard vulnerability taxonomy
