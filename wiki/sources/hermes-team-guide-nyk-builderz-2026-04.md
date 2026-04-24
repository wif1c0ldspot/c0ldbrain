---
title: "Hermes 4-Profile Team Guide — @nyk_builderz"
author: "@nyk_builderz (Nyk)"
date: 2026-04-20
source: "https://x.com/nyk_builderz/status/2044472463279710344"
tags: [source, ai-agents, hermes, multi-agent, agent-architecture]
type: source
---

## Summary

Comprehensive guide for running a 4-profile Hermes team that stays coherent past day 30. Key insight: single agent with multiple roles collapses into same voice within 2 weeks. Fix = isolated profiles + operator layer (handoff contracts, memory KPI, policy gates, gateway messaging). Documents 4 failure modes and their patches.

## Key Points

- **Profiles isolate 7 things**: config, sessions, memory, skills, personality, cron state, gateway state
- **4-role split**: Orchestrator (Hermes), Research (Alan), Writer (Mira), Engineer (Turing)
- **Handoff contracts**: 4-field contracts (input shape, output shape, failure action, verification gate)
- **Memory KPI**: Track stale_notes per profile, brain-resolve at >15%
- **Policy gates**: Per-role permissions (safe/review/critical risk classes)
- **4 day-30 failures**: Profile drift, handoff rot, SOUL.md bloat, cron collision
- **Key principle**: "Profiles are the feature. Boundaries are the moat."

## Filing Decision

Filed under AI Agents & Architecture per RESOLVER.md. Flat structure. Concept: `hermes-multi-profile-team.md`.


## Related Concepts
- [[hermes-agent-architecture]]
- [[memory-systems]]
- [[company-context-brain]]
- [[hermes-multi-profile-team]]