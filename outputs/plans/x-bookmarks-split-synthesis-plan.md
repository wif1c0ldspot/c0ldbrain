# X-Bookmarks Split & Synthesis Plan

## Current State

| Attribute | Value |
|-----------|-------|
| File | `wiki/sources/x-bookmarks-2026-04.md` |
| Size | 1,064 words, 128 lines |
| Bookmarks | 173 total (30 displayed in markdown) |
| Inbounds | 0 (orphaned) |
| Type | Aggregation (violates source-verbatim principle) |

## Problem

This file violates the C0ldbrain wiki principle that **sources should be verbatim captures of individual external content**. Instead, it's an aggregation of 173 bookmarks with only preview text, not full content.

## Solution: Split + Synthesize

Extract high-value bookmarks as individual sources, synthesize concept pages for each theme, link them together.

---

## Phase 1: Extract High-Value Individual Sources

### Selection Criteria
- **Keep**: Detailed technical content, announcements with specs, tutorial threads, GitHub releases
- **Discard**: Vague "BREAKING" announcements without substance, single links without context, duplicates

### Priority 1: Knowledge Management (Karpathy Theme)

| # | Bookmark | Action | Source Filename |
|---|----------|--------|-----------------|
| 2 | Karpathy's LLM obsidian knowledge base viral | **EXTRACT** | `karpathy-llm-knowledge-base-viral-2026-04.md` |
| 10 | Karpathy's self-improving second brain | **EXTRACT** | `karpathy-self-improving-second-brain-2026-04.md` |
| 11 | Full architecture of LLM Knowledge Base | **EXTRACT** | `karpathy-llm-kb-architecture-2026-04.md` |
| 12 | Building personal knowledge base for agents | **EXTRACT** | `karpathy-personal-kb-agents-2026-04.md` |
| 13 | LLM Knowledge Bases (Karpathy) | **EXTRACT** | `karpathy-llm-kb-pattern-2026-04.md` |

**Concept to Create**: `llm-knowledge-base-pattern` (synthesizes all Karpathy sources)

### Priority 2: Claude Code & AI Coding

| # | Bookmark | Action | Source Filename |
|---|----------|--------|-----------------|
| 1 | Caveman token strategy for Claude | **EXTRACT** | `claude-caveman-token-strategy-2026-04.md` |
| 4 | AI job search system for Claude Code | **EXTRACT** | `claude-code-job-search-system-2026-04.md` |
| 5 | Claude Code skill graphs | **EXTRACT** | `claude-code-skill-graphs-2026-04.md` |
| 27 | /model opus for planning in Claude Code | **EXTRACT** | `claude-code-opus-planning-2026-04.md` |

**Concept to Create**: `claude-code-patterns` (synthesizes workflows)

### Priority 3: Memory & Context Systems

| # | Bookmark | Action | Source Filename |
|---|----------|--------|-----------------|
| 7 | Knowledge graph engine for codebase | **EXTRACT** | `knowledge-graph-codebase-engine-2026-04.md` |
| 9 | Memvid (MP4 for AI memory) | **EXTRACT** | `memvid-mp4-ai-memory-2026-04.md` |
| 16 | MLX + TurboQuant local power | **EXTRACT** | `mlx-turboquant-local-power-2026-04.md` |
| 17 | TurboQuant KV cache experiments | **EXTRACT** | `turboquant-kv-cache-experiments-2026-04.md` |

**Concept to Update**: `memory-systems` (add these as sources)

### Priority 4: AI Infrastructure & Tools

| # | Bookmark | Action | Source Filename |
|---|----------|--------|-----------------|
| 8 | NVIDIA PersonaPle voice AI | **EXTRACT** | `nvidia-personaple-voice-ai-2026-04.md` |
| 14 | Excalidraw diagrams stream to Claude | **EXTRACT** | `excalidraw-claude-streaming-2026-04.md` |
| 18 | GLM-OCR open-source | **EXTRACT** | `glm-ocr-open-source-2026-04.md` |
| 19 | 397B params on MacBook | **EXTRACT** | `local-397b-model-macbook-2026-03.md` |
| 28 | Alibaba GUI agent | **EXTRACT** | `alibaba-gui-agent-web-control-2026-03.md` |

**Concept to Create**: `ai-infrastructure-releases` (April 2026 roundup)

### Priority 5: Quant & Automation

| # | Bookmark | Action | Source Filename |
|---|----------|--------|-----------------|
| 23 | Automated stock research | **EXTRACT** | `automated-stock-research-agent-2026-03.md` |
| 24 | Crucix open-source intel | **EXTRACT** | `crucix-osint-tool-2026-03.md` |

**Concept to Link**: `quantitative-trading`, `agentic-research`

### Discard (Low Value / Vague)

| # | Bookmark | Reason |
|---|----------|--------|
| 3 | "Delete Notion" | Vague, no technical substance |
| 6 | Link only (t.co) | No preview text |
| 14 | Diagram streaming (already captured) | Partial duplicate |
| 15 | "Bullish on open source" | Opinion, no specifics |
| 20-22 | Links only | No content to extract |
| 25 | "PDF to MD" | Tool mention, no details |
| 26 | JSON visual diagrams | Single tool mention |
| 29 | Instagram privacy | Off-topic |
| 30 | Hardware simulation | Off-topic |

---

## Phase 2: Create/Update Concept Pages

### New Concept: `llm-knowledge-base-pattern`

**Purpose**: Synthesize Karpathy's LLM wiki pattern from multiple sources

**Structure**:
```markdown
# LLM Knowledge Base Pattern

## Core Philosophy
- File-native over database
- Verbatim capture over extraction
- Compounding context over retrieval

## Architecture Components
1. **Ingest Layer** (raw/)
2. **Processing Layer** (wiki/sources/)
3. **Concept Layer** (wiki/concepts/)
4. **Link Layer** (wikilinks)

## Implementations
- [[karpathy-llm-knowledge-base-viral-2026-04]] — Original viral thread
- [[karpathy-self-improving-second-brain-2026-04]] — Self-improving aspect
- [[karpathy-llm-kb-architecture-2026-04]] — Full architecture breakdown
- [[karpathy-personal-kb-agents-2026-04]] — Agent integration
- [[karpathy-llm-kb-pattern-2026-04]] — Core pattern explanation

## Related
- [[context-substrate]] — Camp 2 memory paradigm
- [[memory-systems]] — Technical implementations
```

### Update: `memory-systems`

Add sources section:
```markdown
## Sources
- [[memvid-mp4-ai-memory-2026-04]] — Video-based memory
- [[mlx-turboquant-local-power-2026-04]] — Local quantized memory
- [[turboquant-kv-cache-experiments-2026-04]] — KV cache optimization
- [[knowledge-graph-codebase-engine-2026-04]] — Codebase KG
```

### New Concept: `claude-code-patterns`

**Purpose**: Document proven Claude Code workflows

**Structure**:
- Token optimization (caveman strategy)
- Skill graphs
- Job search automation
- Planning with Opus

---

## Phase 3: Execution Sequence

### Step 1: Create Individual Sources (20 files)
```bash
# Create sources for each extracted bookmark
# Template: wiki/sources/{slug}-{date}.md
```

### Step 2: Create Concept Pages (2 new)
- `wiki/concepts/llm-knowledge-base-pattern.md`
- `wiki/concepts/claude-code-patterns.md`

### Step 3: Update Existing Concepts
- Add sources to `memory-systems`
- Link to `ai-coding-agents`
- Link to `open-source-ai-infra`

### Step 4: Delete Aggregation
```bash
rm wiki/sources/x-bookmarks-2026-04.md
```

### Step 5: Verify Link Graph
```bash
python3 _scripts/lifecycle_detect.py
# Expect: New sources linked to concepts
# Expect: x-bookmarks removed from orphan count
```

---

## Expected Outcomes

| Metric | Before | After |
|--------|--------|-------|
| Source files | 64 | 84 (+20) |
| Concept files | 76 | 78 (+2) |
| Orphaned sources | ~10 | 0 |
| Average source words | 1,064 | ~200-400 |
| Inbound links to new concepts | 0 | 20+ |

---

## File Naming Convention

```
wiki/sources/{author-topic}-{descriptor}-{YYYY-MM}.md

Examples:
- karpathy-llm-knowledge-base-viral-2026-04.md
- claude-caveman-token-strategy-2026-04.md
- mlx-turboquant-local-power-2026-04.md
```

## Frontmatter Template

```yaml
---
title: "[Author]: [Topic]"
type: source
source_url: "https://x.com/..."
author: "@handle"
created: '2026-04-DD'
updated: '2026-04-DD'
confidence: medium
status: current
tags: [source, ai-agents, topic-tag]
summary: "One-line summary"
---
```

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Losing low-value bookmarks | Raw JSON gone, but low-value = okay to lose |
| Broken links after deletion | Search/replace any links to x-bookmarks |
| Over-extraction | Only extract bookmarks with substance |
| Duplicate concepts | Check existing concepts before creating new |

---

## Decision Required

**Should I execute this plan?** 

Alternative: **Simpler approach** — Keep x-bookmarks as-is, just create 1-2 concept pages that link to it (treat aggregation as a "roundup source").

Recommend: **Execute full split** — Better aligns with wiki principles, improves discoverability, enables granular linking.