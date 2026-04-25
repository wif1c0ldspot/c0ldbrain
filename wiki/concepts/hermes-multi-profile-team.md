---
title: "Hermes Multi-Profile Team Architecture"
type: concept
tags: [ai-agents, hermes, multi-agent, agent-architecture, operations]
created: 2026-04-20
updated: 2026-04-20
confidence: high
status: current
priority: important
summary: "Running coherent multi-agent teams using Hermes profiles — 4-role split (orchestrator, research, writer, engineer) with handoff contracts, memory KPIs, and per-role policy gates."
---

# Hermes Multi-Profile Team Architecture

## Overview

A pattern for running coherent multi-agent teams using Hermes profiles. Single agent with multiple roles collapses into "same voice" within 14 days due to shared memory and tone. The fix: **isolated profiles** that separate 7 dimensions of state (config, sessions, memory, skills, personality, cron, gateway).

**Key principle:** "Profiles are the feature. Boundaries are the moat."

## The Problem: Single-Agent Collapse

When one agent carries 5 roles:
- Memory accumulates cross-role noise
- Tone/style bleeds between tasks
- 14 days → "same voice" for all outputs
- Not a prompting problem — an isolation problem

## The 4-Profile Team

| Profile | Role | SOUL.md Style | Risk Class |
|---------|------|---------------|------------|
| **Hermes** | Orchestrator | Structured, decisive | Critical |
| **Alan** | Research | Source-first, skeptical, uncertainty-aware | Safe |
| **Mira** | Writer | Clear, audience-aware | Safe |
| **Turing** | Engineer | Precise, test-oriented | Review |

### Why This Split Works

Mirrors real work:
- Orchestrator never has to be good writer
- Writer never has to debug
- Engineer never has to convince anyone
- Each role's memory stays on-topic → cleaner every week

## What Profiles Isolate

Each profile isolates 7 dimensions of state:

```
┌─────────────────────────────────────────────────────────┐
│  Profile Isolation                                      │
├─────────────────────────────────────────────────────────┤
│  1. Configuration    │ config.yaml, .env                │
│  2. Sessions         │ conversation history             │
│  3. Memory           │ persistent memory store          │
│  4. Skills           │ available skills/commands         │
│  5. Personality      │ SOUL.md identity                 │
│  6. Cron state       │ scheduled jobs                   │
│  7. Gateway state    │ messaging integration            │
└─────────────────────────────────────────────────────────┘
```

## 7-Step Build

1. **Start from working Hermes** — Base installation healthy
2. **Create specialist profiles** — `hermes profile create alan --clone`
3. **Verify on disk** — `ls ~/.hermes/profiles/` shows alan/, mira/, turing/
4. **Write real SOUL.md per role** — Identity, not just name change
5. **Keep project context in AGENTS.md** — SOUL.md = who; AGENTS.md = what
6. **Add team reference file** — `~/.hermes/team-agents.md`
7. **Run profiles separately** — `hermes -p alan`

## The Operator Layer (Day 2-30)

### Handoff Contracts

File: `~/.hermes/team/handoffs/<from>-to-<to>.md`

```
┌─────────────────────────────────────────────────────────┐
│  Handoff Contract Fields                                │
├─────────────────────────────────────────────────────────┤
│  Input shape     │ What receiving profile expects       │
│  Output shape    │ What receiving profile returns       │
│  Failure action  │ block / require-human-review / retry │
│  Verification    │ One assertion before handoff completes│
└─────────────────────────────────────────────────────────┘
```

Example: Alan → Mira
- Input: ranked claims with source URLs (not raw transcripts)
- Output: drafted section with change log (not finished article)
- Gate: every claim carries a source URL

### Memory KPI per Profile

```bash
for p in alan mira turing; do
  hermes -p $p memory-kpi --json | jq '.source_backed_pct, .stale_notes, .contradiction_notes'
done
```

**Key metric:** `stale_notes`. When >15% of total notes → schedule brain-resolve pass.

### Policy Gates per Role

| Profile | Can | Cannot |
|---------|-----|--------|
| Alan | Read web/repo, write research/ | Run shell, write outside sandbox |
| Mira | Read research, write drafts/ | Read secrets, execute code |
| Turing | Read repo, sandboxed tests, feature branch | Merge to main |
| Hermes | Approve merges, widen permissions, spend above budget | — |

Encode in `config.yaml` under `policy:` block.

### Gateway Messaging

Turn local profiles into operational control surface:

- Alan → research findings channel
- Mira → drafts channel
- Turing → test results + PR links
- Hermes → synthesis + human approval requests

## The 4 Day-30 Failures

### Failure 1: Profile Drift
**Symptom:** SOUL.md edits accumulate, profiles slowly become each other.
**Cause:** New responsibilities creep in without approval.
**Patch:** Diff SOUL.md weekly against day-one version. Log any additions.

### Failure 2: Handoff Rot
**Symptom:** Contracts exist but nobody enforces them.
**Cause:** Alan starts sending raw transcripts, Mira asks Turing "just check this."
**Patch:** Wire contracts into harness. Block non-conforming handoffs.

### Failure 3: SOUL.md Bloat
**Symptom:** Each SOUL.md grows to 2kb+ of special cases.
**Cause:** Edge cases pile up, original identity lost.
**Patch:** Cap SOUL.md at 400 words. Extra goes to AGENTS.md or reference files.

### Failure 4: Cron Collision
**Symptom:** Profiles collide at 3am because nobody coordinated.
**Cause:** Each profile adds cron independently.
**Patch:** Shared `~/.hermes/team/cron.md` listing all scheduled tasks with times.

## Team-Agents.md Template

```markdown
# ~/.hermes/team-agents.md

## roster
- **hermes** (orchestrator): plans, routes, approves, synthesizes
- **alan** (research): source-first, skeptical, uncertainty-tagged
- **mira** (writer): clarity, structure, audience-aware
- **turing** (engineer): implementation, tests, reproducibility

## when to use which profile
- starting new project → hermes
- validating claim → alan
- drafting external-facing → mira
- writing/debugging code → turing

## handoff rules
- alan → mira: ranked claims with source urls. no raw transcripts.
- mira → hermes: drafted section + change log. not finished article.
- turing → hermes: feature branch + passing tests + diff summary.
- hermes → any: scoped task with acceptance criteria and failure action.

## policy ceilings
- alan: read-only outside research/
- mira: read research/, write drafts/
- turing: read repo, write feature branch, run sandboxed tests
- hermes: only profile allowed to approve merges, widen permissions

## cron schedule
- mon 6am — alan: weekly research digest
- tue 6am — mira: draft refresh from alan's digest
- wed 6am — turing: test sweep + flaky test report
- thu 6am — hermes: weekly synthesis + handoff audit
```

## Guardrails

1. No SOUL.md edit without logged reason
2. No handoff accepted without declared input shape
3. No role widened without orchestrator approval
4. No cron added without checking shared schedule

## Applicability to C0ldbrain

This pattern applies directly:
- Current setup: Single Hermes agent = research + coding + wiki
- Opportunity: Split into Alan (wiki/research) + Turing (coding) + Hermes (orchestrator)
- Would reduce context pollution between wiki and crypto-quant work

## Related
- [[hermes-team-guide-nyk-builderz-2026-04]] Concepts
- [[hermes-ecosystem-projects]]
- [[llm-wiki-vs-notebooklm-artemxtech-2026-04]]

- [[hermes-agent-architecture]] — Base Hermes architecture
- [[skills-pattern]] — Skills-based agent design
- [[gbrain-agent-brain]] — GBrain's 26-skill system (parallel approach)
- [[knowledge-management-synthesis]] — Knowledge paradigms
- [[coral-multi-agent-discovery]] — Multi-agent co-evolution
