---
title: "Hermes Agent Ecosystem Projects (April 2026)"
type: concept
tags: [ai-agents, hermes, ecosystem, agent-architecture, security, multi-agent]
created: 2026-04-20
updated: 2026-04-20
confidence: high
status: current
priority: important
summary: "6 key community projects from the Hermes Atlas ecosystem — covering security (CaMeL), deployment (Alpha), auto-skill generation (Skill Factory), multi-agent coordination (Maestro), and model replacement (Icarus)."
---

# Hermes Agent Ecosystem Projects (April 2026)

## Overview

The Hermes Agent ecosystem exploded in 6 weeks, with community projects covering every production gap. 5 key projects from the Hermes Atlas ecosystem map, each built on the Hermes core loop and solving a different problem: security, deployment, skill growth, multi-agent coordination, and memory + training.

**Source:** @NFTCPS (51.6K views), via Hermes Atlas ecosystem map

## Ecosystem Coverage

| Gap | Project | Creator | Solution |
|-----|---------|---------|----------|
| **Security** | hermes-agent-camel | nativ3ai | CaMeL trust boundaries |
| **Deployment** | hermes-alpha | kaminocorp | Cloud bootstrap + autonomous operation |
| **Skill growth** | hermes-skill-factory | Romanescu11 | Auto-generate skills from workflows |
| **Multi-agent** | maestro | ReinaMacCredy | Local-first shared state conductor |
| **Memory + training** | icarus-plugin | esaradev | Self-memory + replacement model pipeline |

---

## 1. hermes-agent-camel — Security

**URL:** https://github.com/nativ3ai/hermes-agent-camel

CaMeL trust boundaries integrated into Hermes runtime. Distinguishes trusted control from untrusted data.

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│  1. Trusted Operator Plan    │ From real user turns only │
│  2. Untrusted Data Channel   │ Tool outputs + provenance │
│  3. Security Envelope        │ Per-turn compact metadata  │
│  4. Capability Gating        │ Side-effect tools checked  │
│  5. Provider Hygiene         │ Strip internal metadata    │
└─────────────────────────────────────────────────────────┘
```

### What It Blocks
- Indirect terminal exfiltration
- Indirect external messaging
- Indirect persistent-memory writes
- Indirect browser side-effects

### What It Allows
- Explicitly authorized terminal use
- Safe read-only list actions
- Trusted operator plan actions

### Runtime Modes
```bash
hermes --camel-guard on      # full enforcement
hermes --camel-guard monitor # log without blocking
hermes --camel-guard off     # legacy behavior
```

**Validation:** 205 tests passed, paper-aligned benchmark: all injection attempts blocked

### Research Provenance
- Based on Google Research CaMeL paper: https://arxiv.org/abs/2503.18813
- Research repo: https://github.com/google-research/camel-prompt-injection
- Adapted to Hermes-native runtime (not research reproduction)

---

## 2. hermes-alpha — Deployment + Autonomous Operation

**URL:** https://github.com/kaminocorp/hermes-alpha

Cloud-deployed Hermes with autonomous bug bounty hunting capability.

### The Experiment
"Can a stock AI agent — given nothing but a mission brief — bootstrap an autonomous bug bounty system from scratch?"

No custom tools. No purpose-built infrastructure. Just Linux terminal + git + mission.

### Architecture
```
Creator (You)
  └─ browser terminal / Telegram
       └─ Overseer (persistent, strategic — builds the system)
            └─ Hunter (ephemeral, tactical — finds the bugs)
                 └─ subagents (parallel analysis workers)
```

### Self-Improving Loop
- Overseer evolves Hunter's code, skills, strategy based on outcomes
- Hunter gets better at finding vulnerabilities
- Overseer gets better at improving Hunter
- **Validated by objective economic signal:** bounties paid or not

### A/B Test (Path B)
| Path | Approach | Question |
|------|----------|----------|
| A (Hermes Prime) | Purpose-built infrastructure | Does scaffolding accelerate results? |
| **B (Hermes Alpha)** | Stock agent + identity doc | Can agent bootstrap from first principles? |

---

## 3. hermes-skill-factory — Skill Growth

**URL:** https://github.com/Romanescu11/hermes-skill-factory

Meta-skill that watches workflows and auto-generates reusable skills.

### How It Works
1. Watches your workflows silently during every session
2. Detects repeated patterns
3. Proposes skill generation with one-click creation
4. Generates both SKILL.md (instructions) and plugin.py (slash command)

### Commands
| Command | Action |
|---------|--------|
| `/skill-factory propose` | Analyze session, propose top detected skill |
| `/skill-factory list` | List all generated skills this session |
| `/skill-factory status` | Show patterns being tracked |
| `/skill-factory queue` | Show detected patterns queued for proposal |
| `/skill-factory save <name>` | Save last proposal with custom name |

### What Gets Generated
- **SKILL.md** — Complete skill definition following Hermes native format
- **plugin.py** — Scaffolded slash command that triggers the skill

**Key insight:** "Every time you solve a problem with Hermes, you're performing a workflow worth repeating."

---

## 4. maestro — Multi-Agent Coordination

**URL:** https://github.com/ReinaMacCredy/maestro

Local-first conductor for multi-agent software engineering. Shared state on disk, not chat history.

### Core Concepts
| Concept | Purpose |
|---------|---------|
| Mission | Top-level unit of work (draft, approved, executing) |
| Milestone | Phase within mission (work phases or validation gates) |
| Feature | Concrete work assigned to agent type |
| Assertion | Validation target (passed, failed, blocked, waived) |
| Handoff | Persisted launch record + markdown brief |
| Memory | Corrections and learnings as reusable guidance |
| Principle | Behavioral rules injected into worker prompts |

### Architecture
```
Human operator
  └─ Maestro CLI + .maestro/ state
       ├─ Agent terminal A
       ├─ Agent terminal B
       └─ Mission Control (TUI)
```

### What It Is
- Shared state layer on disk (.maestro/)
- Mission-driven work decomposition
- Native handoff launches for fresh sessions
- Human operator bridges between terminals

### What It Is NOT
- Not a hosted orchestration service
- Not tied to single model vendor
- Not requiring database, queue, or network API

---

## 5. icarus-plugin — Memory + Model Training

**URL:** https://github.com/esaradev/icarus-plugin

Self-memory and model replacement pipeline for Hermes agents.

### Architecture
```
Hermes Agent
  └─ Icarus plugin
       ├─ hooks: auto-capture decisions, inject context
       ├─ tools: recall, write, search, train, switch
       └─ scoring: session quality, export weighting
            │
            ▼
       ~/my-vault/icarus/
       ├─ agent-decision-*.md
       ├─ daily/*.md
       └─ cold/ (archived)
            │
            ▼
       export-training.py → together.jsonl → Together AI
            │
            ▼
       fine-tuned replacement model
```

### What It Does
- **Auto-capture:** Decisions and context captured automatically
- **Tools:** recall, write, search, train, switch
- **Scoring:** Session quality, export weighting
- **Training pipeline:** Captured decisions → training data → fine-tuned model
- **Obsidian compatible:** Writes to vault, optional viewer

**Key insight:** "Agent 边干活边带徒弟" — agent works while training its replacement

---

## The Pattern

All 5 projects share:
- **Hermes core loop** as foundation DNA
- **Community layer** adding production capabilities
- **Each solves one gap** in the agent lifecycle

### The Complete Agent Stack
```
┌─────────────────────────────────────────────────────────┐
│  Security      │ CaMeL trust boundaries                 │
│  Deployment    │ Cloud bootstrap + autonomous operation │
│  Skills        │ Auto-generate from workflows           │
│  Coordination  │ Local-first shared state               │
│  Memory        │ Self-memory + replacement training     │
└─────────────────────────────────────────────────────────┘
```

## Relevance to C0ldbrain

### Direct Applications
1. **hermes-agent-camel** — Apply CaMeL boundaries to our agent for production safety
2. **hermes-skill-factory** — Auto-generate skills from repeated wiki/quant workflows
3. **maestro** — Shared state for wiki + crypto-quant multi-agent coordination
4. **icarus-plugin** — Capture decisions for training data + model replacement

### Ecosystem Timeline
6 weeks from start to full ecosystem coverage. Community velocity is "scary."

- [[hermes-kanban-bridge]] — Obsidian Kanban bridge for Hermes (GumbyEnder)

## Related
- [[hermes-ecosystem-nftcps-2026-04]] Concepts
- [[hermes-kanban-gumbyender-2026-04]]
- [[hermes-lcm]]

- [[hermes-agent-architecture]] — Base Hermes architecture
- [[hermes-multi-profile-team]] — Multi-agent team patterns
- [[skills-pattern]] — Skills-based agent design
- [[ai-security-synthesis]] — Security landscape
- [[gbrain-agent-brain]] — GBrain parallel approach (26 skills)
