---
confidence: medium
created: '2026-04-16'
priority: important
status: current
summary: Overview
tags:
- agent-architecture
- context-management
- routing
- ai-systems
title: Resolvers
type: meta
updated: '2026-04-18'
---


## Overview

A resolver is a routing table for context in agent systems. It's a mapping mechanism that determines which document, skill, or resource to load when a specific task type or context appears. The core principle: when task type X appears, load document Y first.

Resolvers are invisible when they work and catastrophic when they don't. They represent the governance layer that transforms a collection of skills into a coherent, compounding intelligence system.

## Core Concept

**Definition**: A resolver maps task types to resources (documents, skills, directories) that should be loaded to handle that task effectively.

**Anatomy of a resolver**:
```
Task Pattern → Resource to Load
"Is it a person?" → /people/ directory
"A company?" → /companies/ directory  
"A policy analysis?" → /civic/ directory
```

**Key insight from Garry Tan**: 200 lines of well-structured resolver logic can replace 20,000 lines of crammed context while dramatically improving performance.

## Why Resolvers Matter

### The Problem: Context Drowning

When you cram everything into system prompts:
- Model attention degrades
- Responses slow down
- Precision drops
- The AI literally tells you to stop

### The Solution: Just-in-Time Context

Instead of omniscience by proximity, provide the right book at the right moment. Load context on demand based on the specific task at hand.

## Types of Resolvers

### 1. Skill Resolver (AGENTS.md)
Maps user intents to skill files.
```
"Who is this person?" → brain-ops skill
"Ingest this PDF" → pdf-ingest skill
"Check my calendar" → google-calendar skill
```

### 2. Filing Resolver (RESOLVER.md)
Maps content types to storage locations.
```
Person → people/
Company → companies/
Policy analysis → civic/
Meeting transcript → meetings/
```

### 3. Context Resolver (within skills)
Sub-routing within individual skills.
```
Executive assistant skill:
  "email triage" → triage submodule
  "scheduling" → calendar submodule
  "signatures" → signature tracking submodule
```

## Common Failure Modes

### 1. Misfiling
Skills with hardcoded paths bypass the resolver, filing content incorrectly. Example: political analysis filed in `sources/` instead of `civic/`.

**Fix**: Mandate that every brain-writing skill reads `RESOLVER.md` and `filing-rules.md` before creating any page.

### 2. Invisible Skills
Skills exist but aren't registered in the resolver. Like having a surgeon on staff but not in the hospital directory.

**Fix**: `check-resolvable` meta-skill - audits that every skill has a path from the resolver.

### 3. Context Rot
Resolvers decay over time:
- Day 1: Perfect
- Day 30: New skills not registered
- Day 60: Trigger descriptions don't match user phrasing
- Day 90: Resolver is a historical document

**Fix**: Trigger evals + periodic self-healing via RLM (reinforcement learning from task dispatch patterns).

## Implementation Patterns

### Trigger Evals
Test suite that verifies routing works correctly:
```
Input: "check my signatures"
Expected: executive-assistant (signature section)

Input: "who is Pedro Franceschi"
Expected: brain-ops → search

Input: "save this article"
Expected: idea-ingest + RESOLVER.md
```

Failure modes to catch:
- **False negative**: Skill should fire but doesn't
- **False positive**: Wrong skill fires (triggers overlap)

### Check-Resolvable Meta-Skill
Walks the chain: AGENTS.md → skill file → code → finds dead links.

First run on Garry Tan's system: 6 unreachable skills out of 40+ (15% dark capabilities).

### Self-Healing Resolvers
RLM-based system that:
- Observes every task dispatch
- Tracks which skills fire, which don't
- Identifies tasks with no match
- Rewrites resolver based on evidence

Claude Code's AutoDream is a primitive version (memory consolidation during idle time).

## Resolvers as Management

Viewed through an organizational lens:

| Component | Management Analog |
|-----------|-------------------|
| Skills | Employees with capabilities |
| Resolver | Org chart + escalation logic |
| Filing rules | Internal process documentation |
| Check-resolvable | Audit and compliance |
| Trigger evals | Performance reviews |

The problem with most agent systems: they're organizations with no management layer. Just talented employees with vague hopes of coordination.

## Best Practices

1. **Load right context at right moment** - Don't cram
2. **Mandate resolver consultation** - Don't trust individual filing logic
3. **Test routing, not just output** - Trigger evals catch routing failures
4. **Audit reachability weekly** - Run check-resolvable regularly
5. **Document misfiling patterns** - Catalog common errors to prevent recurrence
6. **Make it learn from traffic** - Self-healing is the endgame

## Open Source Implementations

- **GBrain** (github.com/garrytan/gbrain): Ships with resolver pattern built-in
- **GStack** (github.com/garrytan/gstack): Coding layer with fat skills
- Compatible with: OpenClaw, Hermes Agent

## Related Concepts

- [[agent-architecture]]
- [[context-engineering]]
- [[skills-pattern]]
- [[agent-skills-systems]]
- [[agentic-ai]]
- [[agent-meta-optimization]]
- [[resolvers]]

## Key Sources

- [[resolvers-garrytan-2026-04]] - Garry Tan's original article

- [[ai-coding-agents]]
- [[gstack-garrytan-2026-04]]
- [[hermes-agent-architecture]]
- [[llm-knowledge-bases]]