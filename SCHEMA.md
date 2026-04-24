# Wiki Schema

## Identity

- **Root:** `/Volumes/obsidian/C0ldbrain`
- **Purpose:** Human-managed knowledge base (external reference), NOT agent memory. The agent manages its own L1/L2 separately.
- **Created:** 2026-04-06
- **Last Updated:** 2026-04-17
- **Current State:**
  - C0ldbrain Wiki: 40+ concept pages, 53+ source pages, all sources compiled
  - MemPalace: 536 drawers (search index auto-synced from wiki, NOT agent memory)
  - L3: Synthesis on demand for complex queries

## Two-System Clarification

This wiki is the **agent's external knowledge base**, not its memory:

| System | Purpose | Managed By |
|--------|---------|------------|
| **Hermes Agent Memory** | Session context, working memory, task state | Hermes (built-in) |
| **C0ldbrain Knowledge Base** | Reference material, research synthesis | Human (you) |

**MemPalace** is a search index for C0ldbrain, NOT agent working memory. The agent's session context goes to Hermes's built-in SQLite store.

## Directory Structure

```
raw/                    ← Staging area (empty when all compiled)
  notes/                ← THE ONLY FOLDER WHERE HUMANS WRITE DIRECTLY
  telegram/             ← Incoming Telegram links (created on use)

wiki/                   ← L2: COMPILED KNOWLEDGE (Source of Truth)
  sources/              ← One summary page per raw source (flat)
  concepts/             ← Synthesized concept articles (flat)
  archive/              ← Merged/deprecated pages (never delete)
  index.md              ← Master content catalog (by domain, priority, recency)
  log.md                ← Append-only audit trail

_scripts/               ← LLM workflow scripts
  README.md             ← Agent master guide (read first) - includes tiered retrieval
  wiki_config.py        ← PATH CONFIGURATION
  compile.py            ← 5-phase Python compiler
  ingest.md             ← Stage raw source with metadata
  fetch_urls.md         ← Extract URLs into readable markdown
  compile.md            ← 5-phase master workflow
  synthesize.md         ← L3: Merge scattered notes into Textbook
  ask.md                ← L1→L2: Query wiki with citations
  lint.md               ← Health audit (links, orphans, contradictions)
  graph_visualizer.md   ← Mermaid graph generator
  maint_auto.md         ← Automated maintenance
  merge.md              ← Deduplicate concept pages
  reflect.md            ← L3: Cross-source pattern discovery
  telegram_ingest.md    ← Handle incoming Telegram messages
  ingesters/            ← Per-source-type ingest rules
    article.md, github.md, social.md, podcast.md
    paper.md, newsletter.md, image.md, data.md
    x-bookmarks-export.md

# L1: WORKING MEMORY (MemPalace) — Auto-indexed from wiki/
# Wing: c0ldbrain
#   Room: documentation ← wiki/concepts/, wiki/sources/, _scripts/
#   Room: raw         ← Staged sources, SCHEMA.md, filing-rules.md
#   Room: outputs     ← Generated reports, analyses, digests
# File hooks auto-sync L2 → L1 (never write L1 directly for wiki content)

MANIFEST.json           ← Tracks ALL sources, compilation status, confidence
SCHEMA.md               ← This file (includes tiered memory architecture)
ABOUT.md                ← Human-facing architecture guide
watch_lists.json        ← Autonomous research topic definitions
```

## Page Frontmatter

Every wiki page (sources and concepts) MUST have:

```yaml
---
title: "Page Title"
type: source | concept | analysis
tags: [controlled-vocab-tag, secondary-tag]
sources: [source-slug-1, source-slug-2]
updated: YYYY-MM-DD
confidence: high | medium | low
status: current | deprecated
summary: "One-line machine-readable summary"
supersedes: [replaced-slug]       # LLM Wiki v2
superseded_by: [new-slug]         # LLM Wiki v2
priority: critical | important | reference
last_reinforced: YYYY-MM-DD       # LLM Wiki v2
---
```

**Required fields:** title, type, tags, updated
**Recommended:** sources, confidence, status, summary, priority
**Priority values:** critical, important, reference

**Tag Taxonomy (must be in this list before use):**
- Domains: `ai-agents`, `ml-models`, `crypto-quant`, `devops`, `security`, `infrastructure`
- Topics: `knowledge-management`, `token-optimization`, `memory-systems`, `mcp-protocol`, `prompt-engineering`, `local-models`, `voice-ai`, `prompt-injection`, `red-teaming`, `owasp`, `compliance`, `defense-mechanisms`, `llm-attacks`, `rag`, `multimodal`, `crystallization`, `knowledge-graph`
- Additional: `hermes`, `quantitative-trading`, `developer-tools`, `cost`, `autonomous-optimization`, `meta-agents`, `benchmarking`, `open-source`, `incident-response`, `timeline`, `stub`, `knowledge-lifecycle`, `hybrid-search`

## Raw File Frontmatter

Every file in `raw/` gets:

```yaml
---
source: <URL | "manual" | "paste" | "x-bookmarks">
ingested_at: YYYY-MM-DD
type: article | paper | github | social | podcast | newsletter | note | telegram | data | image
status: uncompiled | pending_fetch | archived
---
```

## Cross-Reference Convention

- Use `[[wikilinks]]` — format: `[[slug]]` where slug = filename without `.md`
- ALL links must be bidirectional: if A links to B, B must have `[[A]]` in its Related Concepts
- Backlink audit is MANDATORY after every compile
- Slugs must be unique across wiki/sources/ and wiki/concepts/

### Typed Relationships (LLM Wiki v2 addition)

Wikilinks should include relationship type for stronger semantics:
- `[[slug|uses]]` — A directly uses B
- `[[slug|depends-on]]` — A requires B to function
- `[[slug|contradicts]]` — A conflicts with B (triggers supersession check)
- `[[slug|supersedes]]` — A replaces B (marks B as deprecated)
- `[[slug|caused]]` — A caused B (incident/bug context)
- `[[slug|fixed]]` — A solves the issue described in B
- `[[slug|extends]]` — A builds on top of B
- `[[slug|related]]` — Generic connection (fallback)

Format in pages: `- [[slug|relationship-type]] — description`
Parser extracts: regex `\[\[([^|]+)\|([^\]]+)\]\]`

### Supersession Tracking

When new info contradicts old:
1. New concept page gets `supersedes: [old-slug]` in frontmatter
2. Old concept page gets `superseded_by: [new-slug]` and `status: deprecated`
3. Both pages link to each other with explicit supersession note
4. LLM should prefer superseder in queries unless explicitly asked for history

Supersession entries in frontmatter:
```yaml
supersedes: [old-concept-slug]     # New version
superseded_by: [new-concept-slug]  # Old version
```

## Knowledge Lifecycle (LLM Wiki v2 addition)

### Confidence Decay
- Confidence is NOT static — it decays over time without reinforcement
- High confidence: 90 days without reinforcement → medium; 180 days → low
- Medium confidence: 30 days without reinforcement → low
- Low confidence: 14 days without reinforcement → deprioritize
- Types decay at different rates: architecture (slow), tools (fast), security (medium)

### Forgetting Curve (Ebbinghaus)
- Facts not accessed or confirmed in threshold days get deprioritized
- Deprioritized = moved to end of search results, not deleted
- Each access/reinforcement resets the decay timer
- Thresholds: architecture=180d, patterns=90d, security=60d, tools=30d, transient=14d
- Compile phase MAINTAIN should flag stale content and update confidence
### Consolidation Tiers (Knowledge Base Reference Only)

These tiers are for the **C0ldbrain knowledge base**, NOT agent memory:

```
KNOWLEDGE BASE TIERS (C0ldbrain Wiki):
─────────────────────────────────────────────────────────────────────────────
Index: MemPalace Search (NOT agent memory)
   ├── Fast semantic search, auto-indexed from disk
   ├── Use for: Discovery — "find concepts about X"
   └── Cost: ~$0.001/query, Latency: ~10ms

Wiki: Disk (Source of Truth)
   ├── Authoritative markdown, YAML frontmatter, human-readable
   ├── Use for: Factual verification, deep dives
   └── Cost: ~$0.01/file, Latency: ~100ms

Synthesis: Deep Research (Computed On Demand)
   ├── Generated analysis, cross-concept reasoning
   ├── Use for: Comparisons, pattern discovery (sparingly)
   └── Cost: ~$0.10+, Latency: 1-5s
─────────────────────────────────────────────────────────────────────────────
```

**Retrieval Protocol:** Index finds → Wiki verifies → Synthesis generates. Never parallel.

#### Information Lifecycle (Knowledge Base)

- **Working memory (L1)**: raw/ observations, not yet compiled (<7 days old)
- **Episodic memory (L2)**: wiki/sources/ summaries from individual sessions
- **Semantic memory (L2)**: wiki/concepts/ cross-session facts (consolidated)
- **Procedural memory (L3)**: synthesis-level workflows and patterns

Information promotes up the tiers as evidence accumulates. MemPalace L1 is auto-indexed from L2 via file hooks — C0ldbrain disk is always the source of truth.

## MANIFEST.json Schema

```json
{
  "version": 1,
  "updated": "YYYY-MM-DD",
  "sources": {
    "raw/<type>/<filename>": {
      "type": "<source type>",
      "status": "uncompiled | compiled | skipped",
      "compiled_at": "YYYY-MM-DD",
      "concept_pages_created": ["slug-1", "slug-2"],
      "confidence": "high | medium | low",
      "last_reinforced": "YYYY-MM-DD",
      "access_count": 0
    }
  }
}
```

**Additional fields (LLM Wiki v2):**
- `last_reinforced`: last time this source was accessed/confirmed (resets decay)
- `access_count`: how many times queried/read by agents
- `superseded_by`: slug of concept that supersedes this one
- `supersedes`: array of slugs this concept supersedes
- `decay_rate`: numeric decay multiplier for this source
- `deprioritized`: boolean — true if past forgetting threshold
```

**Status values:** `uncompiled` (needs processing), `compiled` (done), `skipped`
**Rule:** Raw files are deleted after successful compilation.

## Page Structure

```markdown
# Page Title

## Summary
[2-3 sentence summary]

## Key Facts
- [Fact 1 with source]
- [Fact 2]

## Tables / Comparisons
[Use tables for tools, metrics, trade-offs]

## Related Concepts
- [[wikilink]] — relationship description
```

**Concept pages additionally need:** synthesis from multiple sources, decision tables where applicable, open questions.
**Source pages additionally need:** original URL, extracted content summary, key insights from this source.

## Log Format

```markdown
## [YYYY-MM-DD] <agent> <operation> | <result>
Sources: [processed files]
Changes: [summary]
```

Supported operations: `ingest`, `fetch`, `compile`, `ask`, `reflect`, `lint`, `merge`, `synthesize`, `output`, `graph`, `maintain`, `digest`, `migrate`

## Conventions

1. `raw/` is IMMUTABLE after ingest. Raw files are deleted after compilation.
2. `wiki/log.md` is APPEND-ONLY — never rewritten.
3. `wiki/index.md` and `MANIFEST.json` are updated on every operation.
4. Flat structure: all source summaries and concept articles flat — no subdirectories.
5. NEVER delete wiki pages — move to `wiki/archive/` with explanation.
6. **Backlink audit is MANDATORY after every compile.**
7. Use tables for comparisons — not prose lists.
8. When concepts have 3+ sources, suggest synthesis into a "Textbook" article.
9. Confidence: high (verified), medium (likely), low (speculation or single unverified source).
10. **Confidence decays with time** — MAINTAIN phase recalculates based on last_reinforced date.
11. **Supersession over notes** — when facts conflict, mark old as deprecated with link to new.
12. **Deprioritize not delete** — stale content fades, doesn't vanish.
13. **Typed relationships** — use `[[slug|rel-type]]` format, not plain `[[slug]]`.
14. **Crystallization** — after completing any significant work session (research, debug, analysis), distill findings into a wiki source. Explorations ARE sources.
15. **Quality score** — all LLM-generated content scored for structure, citations, consistency. Below threshold = flagged for review.
16. **Privacy filter** — auto-strip API keys, tokens, passwords, PII before anything hits wiki.
