---
confidence: high
created: '2026-04-16'
priority: reference
sources:
- llm-wiki-v2-rohitg00
status: current
summary: Rohit Gupta extends Karpathy's LLM Wiki with memory lifecycle, knowledge
  graph, hybrid search, event-driven automation, quality/self-correction, multi-agent
  collaboration, privacy/governance, and crystallization.
tags:
- knowledge-management
- memory-systems
- knowledge-graph
- crystallization
- hybrid-search
- knowledge-lifecycle
title: LLM Wiki v2 — Extending Karpathy's Pattern with Memory Lifecycle
type: source
updated: 2026-04-14
---


# LLM Wiki v2

## Summary

Rohit Gupta (rohitg00) extends Andrej Karpathy's original LLM Wiki idea with production lessons from building agentmemory — a persistent memory engine for AI coding agents. The article identifies what breaks at scale, what's missing from the original pattern, and what separates a wiki that stays useful from one that rots. 373 stars, 50 forks — high signal.

**Source:** [GitHub Gist](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2) · Author: rohitg00 (Rohit Gupta) · Date: 2026-04-06

## Key Additions Over Karpathy Original

### 1. Memory Lifecycle

Original treats all wiki content as equally valid forever. This adds:

- **Confidence scoring** — every fact carries score based on source count, recency, contradictions. Decays over time, strengthens with reinforcement.
- **Supersession** — contradicting info explicitly supersedes old. Linked, timestamped, old preserved but marked stale.
- **Forgetting** — Ebbinghaus forgetting curve applied. Facts not accessed/reinforced gradually deprioritize (not deleted). Architecture decisions decay slow, transient bugs decay fast.
- **Consolidation tiers** — Working → Episodic → Semantic → Procedural. Each tier more compressed, more confident, longer-lived. LLM promotes info up as evidence accumulates.

### 2. Knowledge Graph

Beyond flat pages with wikilinks:

- **Entity extraction** on ingest — people, projects, libraries, concepts, files, decisions
- **Typed relationships** — "uses", "depends on", "contradicts", "caused", "fixed", "supersedes" carry different semantic weight
- **Graph traversal for queries** — walk edges to find downstream connections keyword search misses
- Graph augments pages; pages for reading, graph for navigation/discovery

### 3. Hybrid Search

Original's `index.md` works to ~100-200 pages. Beyond that:

- **BM25** (keyword + stemming/synonym expansion) + **Vector search** (semantic similarity) + **Graph traversal** (entity-aware)
- Fused with reciprocal rank fusion
- Keep `index.md` as human-readable catalog, not primary search past ~100 pages

### 4. Event-Driven Automation

Hooks that fire automatically:

| Event | Action |
|-------|--------|
| New source | Auto-ingest, extract entities, update graph, update index |
| Session start | Load relevant context from wiki based on recent activity |
| Session end | Compress session into observations, file insights |
| Query | Check if answer worth filing back (quality score > threshold) |
| Memory write | Check for contradictions, trigger supersession |
| Schedule | Periodic lint, consolidation, retention decay |

### 5. Quality and Self-Correction

- **Score everything** — LLM-written content gets quality score (structure, citations, consistency). Below threshold = flagged for review or rewritten.
- **Self-healing** — lint auto-fixes: orphans linked/flagged, stale claims marked, broken cross-refs repaired.
- **Contradiction resolution** — propose which claim more likely correct based on recency, authority, supporting observations.

### 6. Multi-Agent Collaboration

- **Mesh sync** — multiple agents merge observations into shared wiki. Last-write-wins with timestamp + manual override.
- **Shared vs private** — knowledge scoping. Private observations roll up into shared when promoted.
- **Work coordination** — lightweight tracking of who's working on what.

### 7. Privacy and Governance

- Filter on ingest (auto-strip API keys, tokens, passwords, PII)
- Audit trail on every operation
- Bulk operations audited and reversible

### 8. Crystallization

Automatically distill completed work chains (research, debugging, analysis) into structured digests: question → findings → entities → lessons. Digests become first-class wiki pages. Explorations are sources, just like articles/papers.

### 9. Output Formats Beyond Markdown

Comparison tables, timeline visualizations, dependency graphs, slide decks, structured exports (JSON/CSV), team briefs. Format matches audience and question.

### 10. Schema is the Real Product

Schema document turns generic LLM into disciplined knowledge worker. Co-evolve over time, transferable to others.

## Implementation Spectrum

| Level | Addition | When to Add |
|-------|----------|-------------|
| MVP | raw + wiki + index.md + schema | Start here (Karpathy original) |
| Lifecycle | Confidence scoring, supersession, retention decay | When wiki starts aging |
| Structure | Entity extraction, typed relationships, knowledge graph | When pages >50 |
| Automation | Auto-ingest, auto-lint, context injection hooks | When manual ops slow you down |
| Scale | Hybrid search, consolidation tiers, quality scoring | At 100s+ pages |
| Collaboration | Mesh sync, shared/private scoping, work coordination | When multiple agents contribute |

## Key Insights

1. Flat wikilinks aren't enough — typed relationships carry semantic weight
2. Knowledge has lifecycle — confidence decays, facts get superseded, old info fades
3. Consolidation tiers (working → episodic → semantic → procedural) mirror human memory
4. Event-driven hooks keep wiki healthy without manual intervention
5. Explorations and sessions are first-class sources, not just external articles
6. Schema is the most important file — it encodes the knowledge worker's discipline

## Related Concepts

- [[karpathy-llm-wiki-agent|extends]] — Original Karpathy pattern that this article builds upon
- [[llm-knowledge-bases|extends]] — Core LLM wiki architecture that v2 extends
- [[memory-systems|related]] — Consolidation tiers and forgetting curves from memory research
