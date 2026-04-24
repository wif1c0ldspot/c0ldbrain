# Analysis: Agent Memory Architecture for Hermes Harness

**Date:** 2026-04-17  
**Purpose:** Determine the correct memory architecture for Joel's Hermes agent harness vs human knowledge base

---

## Part 1: Understanding the Two Memory Paradigms

### Camp 1: Memory Backends (Fact Extraction)
```
Conversation → Extract facts → Vector/Graph DB → Retrieve relevant → Inject into context
```
**Examples:** Mem0, MemPalace, Cognee, Supermemory  
**Optimizes for:** Recall accuracy  
**Question:** "What should the AI remember?"

### Camp 2: Context Substrates (Structured Files)
```
Agent reads context file → Works within it → Writes updates → Richer context next session
```
**Examples:** OpenClaw (358k stars), Zep (rebranded to "context engineering"), TrustGraph  
**Optimizes for:** Compounding improvement over time  
**Question:** "What context should the AI work inside?"

**Key Insight (from @witcheer analysis of 900+ repos):**
> "Camp 1 asks: 'what should the AI remember?' Camp 2 asks: 'what context should the AI work inside?'"

---

## Part 2: Four Memory Layers (Agent Architecture)

Based on agent-memory research and Cognee taxonomy:

| Layer | Example | Persistence | Semantics | Relations |
|-------|---------|-------------|-----------|-----------|
| **L1** | `messages = []` | No | No | No |
| **L2** | CLAUDE.md, MEMORY.md | Yes | No | No |
| **L3** | ChromaDB, LanceDB | Yes | Yes | No |
| **L4** | Cognee, MemPalace | Yes | Yes | Yes |

**Harrison Chase's Framework:**
> "Memory is just a form of context. Short-term memory (messages in the conversation, large tool call results) are handled by the harness. Long-term memory (cross-session memory) needs to be updated and read by the harness."

**Sarah Wooders' Insight:**
> "Asking to plug memory into an agent harness is like asking to plug driving into a car."

Memory is **not a plugin** — it's a core harness responsibility.

---

## Part 3: GoClaw 3-Tier Memory (Production Reference)

Production multi-tenant agent gateway (2.7k stars):

| Tier | Name | Purpose |
|------|------|---------|
| **T1** | Short-term | Conversation context within a session |
| **T2** | Working | Task-relevant information across sessions |
| **T3** | Long-term | Knowledge Vault for persistent organizational knowledge |

This aligns with:
- L1: Session messages (handled by harness)
- L2: Working context (files/memory)
- L3: Persistent knowledge (wiki/knowledge base)

---

## Part 4: The Current Setup Analysis

### What Joel Has:

**MemPalace (currently framed as "L1"):**
- Hierarchical storage (wings → rooms → drawers)
- Semantic search via HNSW
- Session diary (AAAK format)
- Knowledge graph with temporal validity
- 536 drawers indexed from C0ldbrain
- MCP server for Claude/Cursor integration

**C0ldbrain Wiki (currently framed as "L2"):**
- Markdown files with YAML frontmatter
- 40+ concept pages, 53+ source pages
- Flat structure (v2.0)
- Human-readable, version controlled
- Source of truth on disk

### The Confusion:

**Current framing:**
```
L1: MemPalace → Fast discovery
L2: C0ldbrain → Authoritative verification
```

**Problem:** MemPalace is literally indexing C0ldbrain. Searching MemPalace then verifying in C0ldbrain is redundant — same content, just cached.

**Real architecture:**
```
MemPalace = Index + Session diary (L3/L4 hybrid for agent)
C0ldbrain = Knowledge base (human-readable, L3 for reference)
```

---

## Part 5: What Hermes Agent Already Has

From Hermes skill documentation:

**Built-in Memory:**
- `~/.hermes/sessions/` — Session transcripts (SQLite)
- `~/.hermes/hermes_state.py` — Session state management
- Context compression near token limits
- Persistent memory across sessions (pluggable backends)

**Memory Providers:**
- Built-in (SQLite)
- Honcho (user-centric memory)
- Mem0 (fact extraction)
- Custom backends

**Key Point:** Hermes ALREADY manages:
- L1: Session messages (in-memory + SQLite)
- L2: Working memory (session history)
- Has hooks for L3: Long-term memory

---

## Part 6: Proposed Architecture for Joel's Harness

### The Real Distinction

Joel is conflating two different systems:

| System | Purpose | For Whom |
|--------|---------|----------|
| **Agent Memory** | Session context, task state, agent working memory | Hermes agent |
| **Knowledge Base** | Reference material, research, accumulated wisdom | Human (Joel) |

### Recommended Architecture

```
┌──────────────────────────────────────────────────────────────────────────┐
│  AGENT MEMORY (Hermes-Managed)                                        │
│                                                                         │
│  L1: Session Context                                                  │
│    ├── In-memory message buffer (current conversation)                   │
│    ├── Tool call results                                               │
│    └── Auto-compression near token limit                               │
│                                                                         │
│  L2: Working Memory (SQLite)                                          │
│    ├── Session history (~/.hermes/sessions/)                             │
│    ├── User preferences (learned over time)                              │
│    └── Task state across sessions                                        │
│                                                                         │
│  L3: Agent Long-Term (OPTIONAL - MemPalace integration)               │
│    ├── Session diary for pattern recognition                             │
│    ├── Cross-session knowledge graph                                     │
│    └── Use ONLY for agent self-improvement, not fact retrieval           │
└──────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ Reference only (not agent memory)
                                    ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  KNOWLEDGE BASE (Human-Managed, Agent-Referenced)                      │
│                                                                         │
│  C0ldbrain Wiki                                                        │
│    ├── Authoritative reference material                                  │
│    ├── Research synthesis, concepts, sources                             │
│    ├── Human-readable, version controlled                                │
│    └── Agent READS but doesn't WRITE (except via explicit compile)       │
│                                                                         │
│  Access Pattern:                                                       │
│    Agent: "I need info on X"                                           │
│      ├── Search C0ldbrain index (fast)                                   │
│      ├── Read relevant wiki pages                                        │
│      └── Synthesize into answer                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Part 7: Resolver's Role

The **RESOLVER** is for **Knowledge Base Organization** (C0ldbrain), NOT agent memory:

| Resolver Purpose | Example |
|------------------|---------|
| Where to file new concepts | `wiki/concepts/agent-meta-optimization.md` |
| Domain routing | AI Security → `wiki/concepts/` (flat) |
| Naming conventions | `kebab-case-concept.md` |
| Anti-patterns | No subdirectories, use tags |

**Resolver is NOT for:**
- Agent memory management (handled by Hermes)
- Session context (handled by Hermes)
- Working memory (handled by Hermes)

---

## Part 8: Recommended Integration

### Option A: Minimal Integration (Recommended)

**Hermes manages its own memory (built-in SQLite):**
- L1: Session context (in-memory)
- L2: Working memory (SQLite sessions/)
- L3: Not needed for most use cases

**C0ldbrain as external knowledge base:**
- Agent queries C0ldbrain when user asks "What do we know about X?"
- Agent does NOT write to C0ldbrain automatically
- Explicit compile workflow only

**Pros:**
- Simple, uses Hermes defaults
- Clear separation of concerns
- No redundancy

**Cons:**
- Agent doesn't "learn" into C0ldbrain automatically
- Requires explicit "compile" step

### Option B: MemPalace as Hermes Memory Plugin

**Integrate MemPalace as Hermes L3 memory:**
- MemPalace becomes the `memory` provider for Hermes
- Agent writes session diary to MemPalace
- Agent reads cross-session patterns from MemPalace
- C0ldbrain remains separate knowledge base

**Pros:**
- Agent has true long-term memory
- Pattern recognition across sessions
- Knowledge graph for relationships

**Cons:**
- More complex
- Potential redundancy with C0ldbrain
- Needs careful sync logic

### Option C: C0ldbrain-First (Context Substrate)

**Make C0ldbrain the agent's context substrate:**
- Agent reads CLAUDE.md, MEMORY.md equivalents from C0ldbrain
- Agent writes updates back to C0ldbrain
- Compounding improvement over time

**Pros:**
- True Camp 2 architecture
- Human-readable agent memory
- Git version control for agent state

**Cons:**
- Requires significant refactor
- Conflicts with Hermes built-in memory
- May be overkill

---

## Part 9: Recommendation

**For Joel's current setup: Use Option A (Minimal Integration)**

### Rationale:

1. **Hermes already has memory** — SQLite session store, context compression, user preferences. Don't reinvent.

2. **C0ldbrain is a knowledge base** — For human reference, research synthesis, accumulated wisdom. Not agent working memory.

3. **Clear separation:**
   - Agent memory = Hermes-managed (ephemeral, task-focused)
   - Knowledge base = C0ldbrain (persistent, reference-focused)

4. **Simple integration:**
   - Agent queries C0ldbrain when user asks
   - Agent does NOT write to C0ldbrain (user initiates compile)
   - No sync issues, no redundancy

5. **Future option:**
   - If agent needs true L3 long-term memory, integrate MemPalace as Hermes memory plugin
   - Keep C0ldbrain separate for human reference

---

## Part 10: Updated Architecture Diagram

```
HERMES AGENT HARNESS
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  AGENT MEMORY (Hermes-Managed)                                          │
│  ──────────────────────────────────────────────────────────────────────────┘
│                                                                         │
│  L1: Session Context      ← In-memory message buffer                     │
│    • Current conversation                                                │
│    • Tool call results                                                   │
│    • Auto-compression at token limit                                     │
│                                                                         │
│  L2: Working Memory       ← SQLite (~/.hermes/sessions/)                 │
│    • Session history                                                     │
│    • User preferences (learned)                                          │
│    • Task state across sessions                                          │
│                                                                         │
│  [L3: Long-term OPTIONAL] ← MemPalace plugin (future)                    │
│    • Cross-session patterns                                              │
│    • Knowledge graph                                                     │
│                                                                         │
└──────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ Agent queries when user asks
                                    │ "What do we know about X?"
                                    ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  KNOWLEDGE BASE (Human-Managed)                                         │
│  ──────────────────────────────────────────────────────────────────────────┘
│                                                                         │
│  C0ldbrain Wiki                                                         │
│    ──────────────────────────────────────────────────────────────────────────┘
│                                                                         │
│  wiki/concepts/          ← Synthesized knowledge (40+ pages)            │
│    • Agent reads for reference                                           │
│    • Agent does NOT write automatically                                  │
│    • User initiates "compile" to update                                  │
│                                                                         │
│  wiki/sources/           ← Source summaries (53+ pages)                 │
│    • Reference material                                                  │
│    • Cited by concepts                                                   │
│                                                                         │
│  MemPalace Index (L1 search layer)                                      │
│    • Auto-indexed from C0ldbrain via file hooks                         │
│    • Fast semantic search for agent discovery                           │
│    • Always verify in C0ldbrain (source of truth)                       │
│                                                                         │
│  RESOLVER.md             ← Content routing (for compile workflow)       │
│    • Where to file new concepts                                          │
│    • Domain → directory mapping                                          │
│    • Filing anti-patterns (P1-P12)                                       │
│                                                                         │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Part 11: Key Takeaways

1. **MemPalace is NOT L1** — It's L3/L4 long-term memory (graph + vector)
2. **Hermes already has L1/L2** — Session context and working memory
3. **C0ldbrain is a knowledge base** — For human reference, not agent working memory
4. **Resolver is for filing** — Content organization, not memory management
5. **Recommended approach:** Minimal integration (Option A)
   - Use Hermes built-in memory
   - Query C0ldbrain on demand
   - Keep concerns separate

6. **Future:** If agent needs true L3 long-term memory, integrate MemPalace as Hermes plugin, not as wiki index

---

## Part 12: Action Items

1. **Update skills** to reflect correct architecture:
   - `tiered-knowledge-retrieval` → Clarify Hermes memory vs C0ldbrain knowledge base
   - Remove "L1=MemPalace, L2=C0ldbrain" framing
   - Replace with "Agent Memory (Hermes) vs Knowledge Base (C0ldbrain)"

2. **Update documentation**:
   - ABOUT.md → Clarify MemPalace is index, not primary L1
   - SCHEMA.md → Separate agent memory tiers from knowledge base
   - _scripts/README.md → Query classification for knowledge base access

3. **Consider:** MemPalace as Hermes memory plugin (separate from C0ldbrain workflow)
