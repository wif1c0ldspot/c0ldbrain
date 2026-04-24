---
title: 'Catalinx: Paperclip, Competitors & Knowledge Base Architecture'
created: 2026-04-22
status: active
company: Catalinx (3 engineers, mobile apps)
stack: GCP + Cloudflare
priority: reference
updated: '2026-04-22'
confidence: medium
summary: 'Auto-generated placeholder for Catalinx: Paperclip, Competitors & Knowledge
  Base Architecture'
---

# Paperclip, Competitors & Knowledge Base Architecture for Catalinx

## 1. What Paperclip Actually Is

**Paperclip** is an **orchestration layer** — it routes tasks, connects steps, and keeps multiple agents moving in the same direction. It's positioned as the "enterprise" option in the managed-agents space.

### Features (from wiki sources)
- Org charts and team hierarchy
- Approval workflows
- Spend controls
- Task routing and handoff management
- Multi-agent coordination

### Paperclip + Hermes Stack
The popular pairing is **Paperclip (orchestration) + Hermes Agent (memory/skills)**. The value proposition: repeatability. The system remembers what worked, improves over time, and keeps workflows connected instead of breaking after every task.

### The Catch
Paperclip is **enterprise-oriented**. For a 3-person mobile app team, it may be overkill — you're paying for org charts and spend controls you don't need yet. The "solo AI company" framing is aspirational; the tooling is built for larger organizations.

**Verdict for Catalinx:** Interesting reference architecture, but not the right fit at your stage. The orchestration you need is simpler (LangGraph/CrewAI on Cloud Run). The memory layer is what actually matters.

---

## 2. Competitor Landscape

### Managed Agent Platforms

| Tool | Stars | Type | Best For | Lock-in | Catalinx Fit |
|------|-------|------|----------|---------|--------------|
| **Paperclip** | N/A | Managed orchestration | Enterprise teams, approval workflows | High | ⭐ Low — overkill for 3 people |
| **Claude Code** | — | Coding agent harness | Software engineering | Claude-only | ⭐⭐ High — but single-agent, not team |
| **Claude Managed Agents** | — | Anthropic managed | Claude ecosystem users | High (Claude) | ⭐⭐ Medium — good but locked to Claude |
| **Multica** | 15.4k | Open-source managed | Vendor-neutral teams | Low | ⭐⭐⭐ High — open, relational, lightweight |
| **OpenClaw** | 358k | Context substrate | Context-heavy workflows | Low | ⭐⭐ Medium — powerful but complex |
| **OpenAI Agents SDK** | 22.6k | SDK/framework | OpenAI-native prototyping | Medium | ⭐⭐ Medium — good for quick starts |
| **Letta** | 21.9k | Stateful memory agent | Memory-heavy applications | Low | ⭐⭐⭐ High — stateful, self-improving |

### Key Differentiators

**Multica** (15.4k stars)
- Pure relational memory (PostgreSQL + JSONB) — no vector embeddings
- Workspace-scoped tables with ON DELETE CASCADE
- Skills attached by SQL join, not similarity search
- Cold inference via JSONB snapshots assembled at dispatch
- Open-source, vendor-neutral
- *Limitation:* No fuzzy recall — untagged skills are invisible

**Letta** (21.9k stars, evolved from MemGPT)
- Stateful agents with advanced memory (archival, recall, working)
- Self-improvement over time
- MCP integration for tools
- Cloud and self-hosted options
- *Best for:* Applications where memory and learning are the core value

**OpenClaw** (358k stars)
- Context substrate camp — structured, human-readable context files
- GBrain integration: 26 skills, hybrid search, self-wiring KG
- *Best for:* Teams that want agents to read/write structured context

**Claude Code**
- Single-agent coding harness (not multi-agent)
- Excellent for engineering tasks
- CLAUDE.md file-based memory
- *Use it for:* Individual engineering agent, not team orchestration

---

## 3. Knowledge Base Architecture for Agent Teams

### The Two Camps

**Camp 1: Memory Backends** (extract facts → store → retrieve)
- Optimizes for recall accuracy
- Examples: Mem0, MemPalace, SimpleMem, Cognee

**Camp 2: Context Substrates** (structured context files agents read/write)
- Optimizes for compounding improvement
- Examples: OpenClaw, Zep, TrustGraph

**For Catalinx: You need both.** Company knowledge = Camp 2 (structured, human-readable). Agent working memory = Camp 1 (fast retrieval).

---

### Option A: Shared Vector DB (Simplest)

All agents query the same vector database for company knowledge.

```
┌────────────────────────────────────┐
│  Shared Vector DB (Chroma/Qdrant/pgvector)   │
│  - Company docs, code, decisions, runbooks   │
└────────────────────────────────────┘
         ↑          ↑          ↑
    Frontend   Backend    Marketing
     Agent      Agent       Agent
```

**Pros:** Simple, single source of truth, cheap
**Cons:** No agent-specific memory, no temporal reasoning, privacy concerns (all agents see everything)

---

### Option B: Agent-Specific Memory (Isolated)

Each agent has its own memory system. No shared context.

```
Frontend Agent          Backend Agent           Marketing Agent
    ↓                       ↓                        ↓
MemPalace #1          MemPalace #2            MemPalace #3
(SQLite)               (SQLite)                (SQLite)
```

**Pros:** Strong isolation, personalized learning per agent
**Cons:** Siloed knowledge, duplicated effort, no company-wide coherence

---

### Option C: Hybrid (Recommended for Catalinx)

**Shared Company Brain** (structured, human-readable) + **Agent Working Memory** (fast retrieval)

```
┌────────────────────────────────────┐
│  Company Brain (Git + Markdown + pgvector)   │
│  - Source of truth, human-editable            │
│  - Hybrid search: vector + keyword + RRF      │
│  - Self-wiring knowledge graph                │
│  - Version controlled                         │
└────────────────────────────────────┘
         ↑          ↑          ↑
    ┌─────┐    ┌─────┐    ┌─────┐
    │ Mem0  │    │ Mem0  │    │ Mem0  │
    │(wkg)  │    │(wkg)  │    │(wkg)  │
    └─────┘    └─────┘    └─────┘
   Frontend    Backend     Marketing
    Agent       Agent        Agent
```

**Company Brain stores:**
- Architecture decisions (ADRs)
- API documentation
- Runbooks and procedures
- Marketing brand guidelines
- Financial policies and chart of accounts
- Meeting notes and decisions
- Agent skills and SOUL.md files

**Agent Working Memory stores:**
- Conversation history
- Task-specific context
- Learned preferences
- Temporary working state

---

### Option D: Cloudflare Agent Memory (Managed)

Cloudflare just launched **Agent Memory** (private beta, April 2026). Since you already use Cloudflare:

```
Cloudflare Agent Memory (managed)
  - ingest / remember / recall / list / forget API
  - Integrated with Workers ecosystem
  - Edge-distributed
```

**Pros:** Zero infrastructure, edge-distributed, managed by Cloudflare
**Cons:** Private beta (access not guaranteed), vendor lock-in, less control over retrieval logic

**Verdict:** Apply for beta access. Good for agent working memory. Still need a Company Brain for structured knowledge.

---

## 4. Recommended Architecture for Catalinx

Given your constraints (3 engineers, GCP + Cloudflare, mobile apps), here's the specific recommendation:

### Knowledge Stack

| Layer | Tool | Purpose | Cost |
|-------|------|---------|------|
| **Company Brain** | Git repo + Cloud SQL (pgvector) | Structured knowledge, version-controlled, human-editable | $20-50/mo |
| **Agent Memory** | Mem0 v2.0 + Redis (Memorystore) | Fast working memory per agent, entity linking | $30-80/mo |
| **Document Store** | GCS bucket | Raw documents, receipts, screenshots | $5-20/mo |
| **Search** | Hybrid (vector + keyword + RRF) | Accurate retrieval across all knowledge | Included |

### Why This Stack

1. **Git + Markdown Company Brain**
   - Human-readable source of truth
   - Engineers already know git
   - Agents can read/write markdown
   - GBrain pattern proven at 17,888 pages scale
   - Version control = audit trail for free

2. **Mem0 v2.0 for Agent Memory**
   - 53k+ stars, becoming the default
   - v2.0: single-pass extraction, hybrid retrieval, built-in entity linking
   - Works with any LLM provider
   - Python SDK, easy to integrate

3. **Cloud SQL + pgvector**
   - GCP-native, managed
   - Hybrid search (vector + keyword + RRF) = 95% recall@5
   - Single store for both Company Brain embeddings and agent memory

4. **Redis (Memorystore)**
   - Short-term agent state
   - Session caching
   - Fast context assembly

### Implementation Pattern

```python
# Company Brain query (shared knowledge)
from gbrain import Brain  # or custom implementation

brain = Brain(
    repo_url="github.com/catalinx/company-brain",
    db_url="postgresql://...",
    search_mode="hybrid"  # vector + keyword + RRF
)

context = brain.query(
    "How do we handle OAuth in our mobile apps?",
    filters={"domain": "engineering", "recency": "< 6 months"}
)

# Agent Working Memory (per-agent)
from mem0 import Memory

memory = Memory(
    user_id="frontend-agent-1",
    vector_store={"provider": "pgvector", "config": {...}},
    llm={"provider": "openai", "config": {"model": "gpt-4o-mini"}}
)

memory.add("User prefers React Native over Flutter for new features", user_id="frontend-agent-1")
recalled = memory.search("What tech stack does the team prefer?", user_id="frontend-agent-1")
```

### Data Flow

```
Engineer writes ADR → Git push → Brain auto-indexes → pgvector
                                    ↓
Agent needs context → Queries brain + working memory → Hybrid search
                                    ↓
Agent learns from task → Writes to Mem0 → Redis + Cloud SQL
                                    ↓
Weekly → Mem0 compacts → Important memories promoted to Company Brain
```

---

## 5. Security Considerations for KB

From wiki research (ADAM attack, memory poisoning):

- **Encrypt at rest:** Cloud SQL encryption + GCS CMEK
- **Access controls:** Each agent service account → least privilege
- **Audit logging:** Every brain query and memory write logged to BigQuery
- **Memory firewall:** Semantic drift detection, write gates for sensitive domains
- **PII scrubbing:** Before storing in agent memory or company brain
- **Retention policies:** Auto-delete old agent working memory (keep brain forever)

---

## 6. Summary & Decision Matrix

| Question | Answer |
|----------|--------|
| Use Paperclip? | No — overkill for 3 people |
| Managed platform? | Multica or Letta if you want open-source managed; build custom if you want control |
| Company knowledge | Git + Markdown + pgvector (GBrain pattern) |
| Agent working memory | Mem0 v2.0 + Redis |
| Document storage | GCS |
| Search | Hybrid (vector + keyword + RRF) |
| Cloudflare integration | AI Gateway (cost optimization) + apply for Agent Memory beta |

### Immediate Next Steps
1. Create `catalinx/company-brain` git repo
2. Deploy Cloud SQL (PostgreSQL + pgvector extension)
3. Set up Mem0 v2.0 with pgvector backend
4. Connect Cloudflare AI Gateway to your LLM APIs
5. Apply for Cloudflare Agent Memory private beta
6. Start with 1 agent (Engineering Planner) → test knowledge retrieval → expand
