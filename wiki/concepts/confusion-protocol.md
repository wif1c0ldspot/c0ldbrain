---
confidence: high
created: 2026-04-17
priority: reference
related_concepts:
- - - gstack
- - - resolvers
- - - ask-for-help
- - - decision-under-uncertainty
sources:
- - - gstack-garrytan-2026-04
status: current
summary: Confusion Protocol
tags:
- decision-making
- ambiguity
- architecture
- coding-methodology
- gstack
- safety
title: Confusion Protocol
type: concept
updated: 2026-04-17
---


# Confusion Protocol

A decision-making safety protocol for AI coding agents when encountering high-stakes ambiguity. Originated in Garry Tan's [gstack](https://github.com/garrytan/gstack) framework.

## Core Principle

> When you encounter high-stakes ambiguity during coding: **STOP**. Name the ambiguity in one sentence. Present 2-3 options with tradeoffs. Ask the user. Do not guess on architectural or data model decisions.

## When to Invoke

The Confusion Protocol applies when:

1. **Two plausible architectures** or data models for the same requirement
2. **A request that contradicts existing patterns** and you're unsure which to follow
3. **A destructive operation** where the scope is unclear
4. **Missing context** that would change your approach significantly

## When NOT to Apply

- Routine coding tasks
- Small features with clear implementation paths
- Obvious changes that follow existing patterns
- Low-stakes decisions with easily reversible outcomes

## The Protocol Steps

### Step 1: STOP

Immediately halt autonomous action. Do not proceed with implementation.

### Step 2: Name the Ambiguity

Articulate the core uncertainty in exactly one sentence.

**Good examples:**
- "Should we denormalize the user data for read performance or keep it normalized for consistency?"
- "The request asks for a synchronous API but our existing patterns are all async."

**Bad examples:**
- "I'm not sure what to do here." (Too vague)
- "There are many ways to implement this feature." (Doesn't name the specific ambiguity)

### Step 3: Present 2-3 Options

For each option, provide:
- **The approach** (what would be done)
- **Tradeoffs** (pros and cons)
- **Completeness score** (X/10)

**Example:**

| Option | Approach | Tradeoffs | Completeness |
|--------|----------|-----------|--------------|
| A | Keep normalized schema | Consistency wins, may have N+1 query issues | 7/10 |
| B | Denormalize with triggers | Better read perf, complexity in write path | 8/10 |
| C | Hybrid with materialized views | Best of both, more infra to maintain | 9/10 |

### Step 4: Ask the User

Present the analysis and wait for direction. Never proceed without user input on high-stakes architectural decisions.

## Why It Matters

### The Cost of Wrong Guesses

| Decision Type | Cost of Wrong Guess |
|---------------|---------------------|
| Data model | Days to weeks of migration |
| API contract | Breaking changes, versioning complexity |
| Architecture pattern | Technical debt accumulation |
| Security boundary | Potential vulnerability |

### Agent Safety

The Confusion Protocol prevents:
- **Overconfidence in ambiguous situations**
- **Pattern misapplication**
- **Destructive operations with unclear scope**
- **Architectural decisions made without sufficient context**

## Integration with Other Frameworks

### In gstack

The Confusion Protocol is one of several safety mechanisms in gstack's decision-making hierarchy:

1. **User Sovereignty** — User always decides when models recommend changes
2. **Confusion Protocol** — Stop and ask on high-stakes ambiguity
3. **6 Decision Principles** — Auto-decide routine questions using completeness, DRY, pragmatism

### In Resolvers

The Confusion Protocol can be seen as a **trigger condition** for the resolver pattern:

```
IF high_stakes_ambiguity_detected:
    TRIGGER confusion_protocol
    RESOLVE via human_decision
ELSE:
    PROCEED with autonomous_execution
```

## Related Concepts

- [[user-sovereignty]] — User has final say on model recommendations
- [[resolver-pattern]] — Routing table for intelligence
- [[completeness-principle]] — Boil the lake, do the complete thing
- [[escalation-protocol]] — When to stop and ask for help

## References

- [[gstack-garrytan-2026-04]] — Source of the Confusion Protocol
- Garry Tan's gstack README: https://github.com/garrytan/gstack

- [[confusion-protocol]]