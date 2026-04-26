---
title: Harness Engineering
type: concept
tags: [ai-agents, systems-engineering, anti-pattern]
created: '2026-04-26'
updated: '2026-04-26'
confidence: high
status: current
priority: important
summary: "Anti-pattern where engineers optimize tools (model, prompt, framework) instead of system outcomes. Results in duct-taped systems that collapse in production."
---

# Harness Engineering

The anti-pattern opposite of [[systems-engineering]]. Instead of optimizing for outcomes, harness engineers optimize the tool — the model, the prompt, or the framework.

## Symptoms

- Filesystem-backed memory that can't isolate users
- Broad bash access given to agents
- Security enforced through prompt instructions
- Framework-specific boilerplate locking in unconscious architectural decisions
- Each tool limitation patched with another abstraction layer

## Why It Fails

The harness grows more complex with each patch, while the underlying system remains fundamentally flawed. Getting something running ≠ having software that works.

## The Fix

Adopt [[systems-engineering]] — design the full system (agent, data, security, interfaces, infrastructure) as a cohesive whole. Each layer should reinforce the others.

## Sources

- [[agno-harness-vs-systems-engineering-2026-04]] — Agno blog, April 2026

## Related
- [[harness-engineering]]
