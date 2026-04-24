---
title: Catalinx Agent Team — Feasible Deployment Plan (Revised)
created: 2026-04-22
status: draft
version: 2.0
company: Catalinx (3 engineers, mobile apps)
stack: GCP + Cloudflare
priority: reference
updated: '2026-04-22'
confidence: medium
summary: Auto-generated placeholder for Catalinx Agent Team — Feasible Deployment
  Plan (Revised)
---

# Catalinx Agent Team — Feasible Deployment Plan

**Version:** 2.0 (Feasibility-Adjusted)  
**Status:** Draft — Requires Approval  
**Key Change:** Scaled down 5x — from 30 agents to 6, 12 weeks to 24 weeks

---

## Executive Summary

The original plan was **3-5x overambitious** for a 3-engineer team also shipping mobile apps. This revised plan addresses critical feasibility gaps:

| Dimension | Original | Revised | Rationale |
|-----------|----------|---------|-----------|
| Agent Count | 30 | 6 | 30 agents = 90 hrs/week maintenance (have 15 hrs) |
| Frameworks | LangGraph + CrewAI | CrewAI only | Two frameworks = zero expertise depth |
| Memory System | Mem0 v2.0 | Direct pgvector + Redis | v2.0 is 6 days old — too risky |
| Infrastructure | 9 components | 4 components | No DevOps/SRE to manage 9 services |
| Timeline | 12 weeks | 24 weeks | Engineers are building mobile apps full-time |
| Cost Estimate | $430-1,850/mo | $700-2,500/mo | Realistic with agent loops/retries |

---

## 1. Company Context

- **Team:** 3 engineers (building mobile apps full-time)
- **Product:** Mobile applications
- **Infrastructure:** GCP (Cloud Run, Cloud SQL, Redis) + Cloudflare
- **Goal:** Agent assistance for engineering, not replacement

**Core Principle:** Agents must run **on top of** existing mobile app work, not **instead of** it. Any plan that requires >20 hours/week of agent maintenance is not feasible.

---

## 2. Realistic Agent Count

### The Math

| Metric | Value | Notes |
|--------|-------|-------|
| Available team hours/week | 60 hrs (3 × 20) | Assuming 20 hrs each for mobile apps |
| Reserved for mobile apps | 45 hrs | Non-negotiable |
| Available for agent ops | 15 hrs | Maximum for agent maintenance |
| Hours per agent/week | 2-3 hrs | Ongoing maintenance, not initial setup |
| **Max agents steady-state** | **5-7** | Any more = degradation |

### Phase 1: 6 Agents

|| Agent | Role | Priority | Complexity |
|-------|-------|------|----------|------------|
| 1 | **Code Reviewer** | Auto-review PRs | P0 | Low |
| 2 | **CI/CD Assistant** | Run tests, report failures | P0 | Low |
| 3 | **Docs Writer** | Auto-update API docs from code | P1 | Medium |
| 4 | **Changelog Generator** | Auto-generate changelogs from PRs | P1 | Low |
| 5 | **Q&A Bot** | Answer questions about codebase | P2 | Medium |
| 6 | **Content Drafter** | First-draft marketing content | P2 | Medium |

**Rule:** No agent reaches production until the previous one is stable (2 weeks without incidents).

---

## 3. Infrastructure (4 Components Only)

### Keep It Simple

| Component | Service | Purpose | Cost |
|-----------|---------|---------|------|
| Compute | Cloud Run | Agent hosting, autoscales to zero | $50-150/mo |
| Database | Cloud SQL (PostgreSQL + pgvector) | Memory + knowledge storage | $100-200/mo |
| Cache/Queue | Redis (Memorystore) | Session state, rate limiting | $50-100/mo |
| Ingress | Cloudflare Tunnel | Secure API exposure | $0 (with existing plan) |

**Dropped (from original 9):**
- ~~Pub/Sub~~ — Use Redis queues instead
- ~~BigQuery~~ — Premature, use Cloud Logging
- ~~GCS~~ — Store documents in Cloud SQL for now
- ~~AI Gateway~~ — Add later when costs stabilize
- ~~Secret Manager~~ — Use Cloud Run env vars initially

### Why This Fits

- **2 engineers can operate this.** One person can handle incident response.
- **No data pipeline to manage.** All state in one database.
- **Single failure domain.** When Cloud SQL fails, everything fails — but this is also easier to debug.

---

## 4. Architecture: CrewAI Only

### Why CrewAI (Not LangGraph)

| Factor | CrewAI | LangGraph |
|--------|--------|-----------|
| Learning curve | 3-5 days | 3-5 weeks |
| Setup time | Hours | Days |
| Debugging | Moderate | Complex (state machines) |
| Multi-agent | Native | Manual wiring |
| Production ready | Yes (if used carefully) | Yes (more control) |

**Decision:** CrewAI for Phase 1. If you hit limitations, switch to LangGraph in Phase 2 — but only after proving CrewAI doesn't work.

### Single Framework = One Expertise

All 6 agents use CrewAI. One person becomes the CrewAI expert. This creates depth, not breadth.

---

## 5. Memory System: Direct pgvector + Redis

### Why NOT Mem0 v2.0

- **Released April 16, 2026** — 6 days old at time of writing
- **Ground-up redesign** — APIs will change
- **No production track record** — You are the beta tester
- **Foundation risk** — If memory corrupts, all 30 agents (future) lose context

### Implementation: Thin Abstraction Layer

```python
# /app/memory.py — Thin wrapper over pgvector
import psycopg2
import json
from datetime import datetime

class AgentMemory:
    """Simple memory layer over pgvector. No external dependencies."""
    
    def __init__(self, db_url: str):
        self.conn = psycopg2.connect(db_url)
    
    def add(self, agent_id: str, content: str, metadata: dict = None):
        """Store a memory with optional metadata."""
        cursor = self.conn.cursor()
        cursor.execute(
            """INSERT INTO agent_memories (agent_id, content, metadata, created_at)
               VALUES (%s, %s, %s, %s)""",
            (agent_id, content, json.dumps(metadata or {}), datetime.utcnow())
        )
        self.conn.commit()
    
    def search(self, agent_id: str, query: str, limit: int = 5):
        """Semantic search within agent's memory."""
        cursor = self.conn.cursor()
        cursor.execute(
            """SELECT content, metadata, created_at FROM agent_memories
               WHERE agent_id = %s
               ORDER BY embedding <=> pgEmbedding(%s)
               LIMIT %s""",
            (agent_id, query, limit)
        )
        return cursor.fetchall()
    
    def backup(self, filepath: str):
        """Export all memories to JSON."""
        # Simple backup to file
        pass
```

**Why this is better:**
1. **No dependency on external library** — You control the code
2. ** pgvector** has been stable for 2+ years
3. **Easy to debug** — 50 lines of Python vs. 50KB of library
4. **Backup/restore** — Simple JSON export

### Company Knowledge: Git + Markdown (GBrain Pattern)

```
catalinx/company-brain/
├── adr/                     # Architecture Decision Records
│   ├── 001-use-react-native.md
│   └── 002-auth-strategy.md
├── api/                     # API Documentation
│   ├── openapi.yaml
│   └── endpoints/
├── runbooks/                # Operational procedures
│   ├── deploy-production.md
│   └── incident-response.md
├── policies/                # Company policies
│   ├── code-style.md
│   └── content-guidelines.md
├── decisions/               # Meeting notes, decisions
│   └── 2026-04-*.md
└── skills/                  # Agent skill definitions
    └── code-reviewer.md
```

**Key points:**
- Agents read from this repo (human-editable source of truth)
- Engineers already know git
- Version control provides audit trail
- Self-hosted, no external dependency

---

## 6. Timeline: 24 Weeks

### Phase 1 (Weeks 1-4): Foundation

| Week | Task | Deliverable |
|------|------|-------------|
| 1 | GCP project, Cloud Run, Cloud SQL + pgvector | All 4 infra components running |
| 2 | Redis instance, basic auth | Agent can connect to all services |
| 3 | Memory layer (50-line wrapper) | `add()`, `search()`, `backup()` working |
| 4 | Clone company-brain repo, seed with 10 key ADRs | Agents can query knowledge |

**Milestone:** Basic infrastructure verified. 0 agents deployed.

### Phase 2 (Weeks 5-10): First 3 Agents

| Week | Task | Deliverable |
|------|------|-------------|
| 5-6 | Code Reviewer agent | Reviews PRs automatically |
| 7-8 | CI/CD Assistant | Runs tests, reports failures |
| 9-10 | Docs Writer | Auto-updates API docs |

**Milestone:** 3 production agents. Stability verified.

### Phase 3 (Weeks 11-16): Next 2 Agents

| Week | Task | Deliverable |
|------|------|-------------|
| 11-12 | Changelog Generator | Auto-generates changelogs |
| 13-14 | Q&A Bot | Answers codebase questions |
| 15-16 | Buffer period | Fix issues from first 5 agents |

**Milestone:** 5 production agents. Maintenance load understood.

### Phase 4 (Weeks 17-20): Final Agent + Hardening

| Week | Task | Deliverable |
|------|------|-------------|
| 17-18 | Content Drafter | First-draft marketing content |
| 19-20 | Circuit breakers, cost guards, DR | Production-ready |

**Milestone:** 6 agents, monitoring, backups, cost limits.

### Phase 5 (Weeks 21-24): Stabilization

| Week | Task |
|------|------|
| 21-22 | Fix all known issues |
| 23-24 | Document runbooks, incident response |

**Milestone:** Agents are stable. Team knows how to operate them.

### Buffer (Weeks 25-32, if needed)

If any phase overruns, use buffer. **Do not rush to meet dates.** Stability > speed.

---

## 7. Cost Analysis (Realistic)

### Monthly Burn (6 Agents)

| Component | Conservative | Realistic | Worst Case |
|-----------|--------------|-----------|------------|
| LLM API (6 agents) | $200 | $500 | $1,500 |
| Cloud Run | $50 | $100 | $300 |
| Cloud SQL + pgvector | $100 | $150 | $300 |
| Redis | $50 | $75 | $150 |
| Cloudflare (existing) | $0 | $0 | $0 |
| Monitoring (Cloud Logging) | $0 | $0 | $50 |
| **TOTAL** | **$400** | **$825** | **$2,300** |

### Cost Guardrails (Mandatory)

```python
# /app/guardrails.py
from functools import wraps
import time

class CostGuard:
    """Per-agent and global spending limits."""
    
    GLOBAL_MONTHLY_BUDGET = 1500  # USD
    PER_AGENT_DAILY_CAP = 10     # USD
    MAX_ITERATIONS = 10          # per task
    
    @staticmethod
    def check_budget(agent_id: str) -> bool:
        """Check if agent is within daily cap."""
        # Redis counter check
        pass
    
    @staticmethod
    def circuit_break(agent_id: str, error_rate: float):
        """Disable agent if error rate exceeds threshold."""
        if error_rate > 0.5:
            # Disable agent, alert on-call
            pass
```

**Required implementations:**
1. Global monthly budget with auto-shutoff
2. Per-agent daily caps
3. Iteration limits (max 10 per task)
4. Alerting on spend > 80% of budget

---

## 8. Risk Register

### HIGH RISK (Address Now)

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Team can't maintain 6 agents | HIGH | HIGH | 6 agents = 15 hrs/week maintenance; reserve 20 hrs |
| Mem0 chosen (v2.0 too new) | DONE | — | Now using direct pgvector |
| Two frameworks | DONE | — | Now using CrewAI only |
| No DevOps capacity | HIGH | HIGH | Simplified to 4 infra components |

### MEDIUM RISK (Monitor)

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Agent infinite loops | MEDIUM | HIGH | Circuit breakers, iteration caps |
| Cost overrun | MEDIUM | HIGH | Budget guardrails, alerting |
| Cloud SQL failure | LOW | HIGH | Backup to JSON weekly |
| Integration complexity | MEDIUM | MEDIUM | 6 agents = 6 integrations, not 15 |

### LOW RISK (Accept)

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Model API downtime | LOW | MEDIUM | Use multiple providers (OpenAI + Anthropic) |
| Knowledge corruption | LOW | HIGH | Git repository is source of truth |

---

## 9. Operational Requirements

### On-Call (Informal)

| Rotation | Person | Responsibility |
|----------|--------|----------------|
| Week A | Engineer 1 | Agent health, cost monitoring |
| Week B | Engineer 2 | Agent health, cost monitoring |
| Week C | Engineer 3 | Agent health, cost monitoring |

**On-call duties (30 min/day):**
1. Check cost dashboard
2. Check error logs
3. Review any agent failures at standup
4. No pager at night — check in morning

### Incident Response

| Severity | Definition | Response Time |
|----------|------------|---------------|
| SEV1 | All agents down | 2 hours |
| SEV2 | One agent down | 24 hours |
| SEV3 | Performance degradation | 1 week |

### Backup Strategy

| Data | Retention | Method |
|------|-----------|--------|
| Agent memories | 30 days | JSON export to GCS (weekly) |
| Company brain | Forever | Git (already versioned) |
| Cloud SQL | 7 days | Automatic (GCP) |
| Redis | 0 | Ephemeral, rebuild from Cloud SQL |

---

## 10. Success Criteria

### Phase 1 (Week 4) — Infrastructure

- [ ] Cloud Run accepting requests
- [ ] Cloud SQL + pgvector responding
- [ ] Redis connected and caching
- [ ] Cloudflare Tunnel ingress working

### Phase 2 (Week 10) — First 3 Agents

- [ ] Code Reviewer reviews >80% of PRs automatically
- [ ] CI/CD Assistant runs tests on every push
- [ ] Docs Writer updates API docs on code changes
- [ ] Error rate < 10%
- [ ] Maintenance time < 6 hours/week

### Phase 3 (Week 16) — 5 Agents

- [ ] All criteria above + Changelog + Q&A Bot
- [ ] Error rate < 5%
- [ ] Maintenance time < 10 hours/week

### Phase 4 (Week 20) — 6 Agents + Hardening

- [ ] All criteria above + Content Drafter
- [ ] Cost guardrails active
- [ ] Backup/restore tested
- [ ] Incident runbook documented
- [ ] Maintenance time < 15 hours/week

---

## 11. Go/No-Go Criteria

Before starting Phase 2:
- [ ] Infrastructure verified working (1 week)
- [ ] Team has 15 hours/week available for agent ops
- [ ] Budget approved ($800-1,500/month)
- [ ] On-call rotation agreed

**If any fail → do not proceed until resolved.**

---

## 12. Summary Decision Matrix

| Question | Answer |
|----------|--------|
| Use Paperclip? | No — overkill |
| Framework? | CrewAI only (skip LangGraph for now) |
| Memory? | Direct pgvector + Redis (skip Mem0 v2.0) |
| Agent count? | 6 (Phase 1), grow slowly |
| Infrastructure? | 4 components only (Cloud Run, Cloud SQL, Redis, Tunnel) |
| Timeline? | 24 weeks (with 8-week buffer) |
| Cost ceiling? | $2,500/month absolute max |
| First agent? | Code Reviewer (lowest risk, highest visibility) |

---

## Appendix: Why This Plan Works

### Original Problems (Solved)

| Original Problem | Solution |
|-----------------|----------|
| 30 agents for 3 people | 6 agents (10x reduction) |
| Two frameworks to learn | One framework (CrewAI) |
| Untested memory library | Direct pgvector (stable) |
| 9 infra components | 4 infra components |
| 12-week timeline | 24-week timeline (realistic) |
| $430-1,850 estimate | $700-2,500 real estimate |

### What Made This Revision Possible

1. **Start small, prove value:** Agents are assistants, not replacements
2. **Simplicity over features:** Fewer agents, fewer frameworks, fewer infra components
3. **Stable foundations:** pgvector (2+ years) over Mem0 v2.0 (6 days old)
4. **Realistic capacity:** Team can only maintain 15 hrs/week
5. **Buffer for the unknown:** 8 weeks buffer built in

### The Core Insight

**The original plan treated agents as a project. This plan treats agents as a product the team operates.** Products need operations. The team has capacity for 15 hours/week of operations. This plan is sized to fit that constraint.

---

*End of Plan — Ready for Approval*