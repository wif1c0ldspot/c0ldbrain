---
title: "C0ldbrain Resolver"
type: resolver
tags: [meta, resolver, wiki-governance]
created: 2026-04-17
updated: 2026-04-18
confidence: high
status: current
priority: critical
summary: "Content routing table for C0ldbrain wiki — domain mappings, filing rules, anti-patterns"
version: 2.0
---

# C0ldbrain Resolver — Content Routing Table

**Purpose:** When task type X appears, load document Y first. Routing table for all wiki content.

**Mandate:** Before creating any wiki page, consult this resolver. File by primary subject, not source format.

**FLAT STRUCTURE:** `wiki/concepts/` and `wiki/sources/` have NO subdirectories. Tags provide categorization.

---

## Filing Rules

### Primary Dimensions (file by these, in order)

1. **Domain** — What field does this belong to?
2. **Subject** — What is the core entity/concept?
3. **Type** — Is it a source, concept, or synthesis?

### Domain → Directory Mapping (FLAT)

| Domain | Destination | Examples |
|--------|-------------|----------|
| **AI Security** | `wiki/concepts/` (flat) | Prompt injection, defense tools, red teaming |
| **AI Agents & Architecture** | `wiki/concepts/` (flat) | Resolvers, skills, MCP, multi-agent |
| **Knowledge Management** | `wiki/concepts/` (flat) | Wikis, memory, context management |
| **Coding Agents** | `wiki/concepts/` (flat) | Claude Code, cursor, dev tools |
| **Quant Trading** | `wiki/concepts/` (flat) | Strategies, backtesting, momentum |
| **Infrastructure** | `wiki/concepts/` (flat) | Local LLM, deployment, tooling |
| **MLOps** | `wiki/concepts/` (flat) | Training, fine-tuning, serving |
| **Research & Papers** | `wiki/sources/` (flat) | arXiv papers, articles, GitHub repos |
| **People & Companies** | `wiki/concepts/` (flat) | Individual bios, org analysis |

**CRITICAL:** All content goes directly into `wiki/concepts/` or `wiki/sources/`. NO subdirectories. Use TAGS for categorization, not folders.

### Subject → File Name Mapping

| Subject Type | Pattern | Examples |
|--------------|---------|---------|
| **Person** | `concepts/firstname-lastname.md` | garrytan.md, karpathy-andrej.md |
| **Company** | `concepts/company-name.md` | openai.md, anthropic.md |
| **Product/Tool** | `concepts/tool-name.md` | claude-code.md, mempalace.md |
| **Concept/Pattern** | `concepts/kebab-case.md` | agent-meta-optimization.md, rag-patterns.md |
| **Protocol/Standard** | `concepts/protocol-name.md` | mcp-protocol.md |
| **Research Source** | `sources/source-slug.md` | arxiv-2603-20441.md, karpathy-wiki-2026-04.md |

### Source vs. Concept Routing (FLAT)

| Content Type | Source Page | Concept Page |
|--------------|-------------|--------------|
| **ArXiv paper** | `wiki/sources/arxiv-XXXX-XXXXX.md` | Create in `wiki/concepts/` with tag `research` |
| **GitHub repo** | `wiki/sources/repo-name-YYYY-MM.md` | Create in `wiki/concepts/` with tag `tool` |
| **X/Twitter thread** | `wiki/sources/topic-handle-YYYY-MM.md` | If new concept → `wiki/concepts/` |
| **Article/Blog** | `wiki/sources/slug.md` | Create in `wiki/concepts/` |
| **Video/Podcast** | `wiki/sources/topic-YYYY-MM.md` | Extract key concepts → `wiki/concepts/` |

---

## Standard Tags (Use These)

| Tag | Use For |
|-----|---------|
| `ai-security` | Prompt injection, red teaming, defense |
| `ai-agents` | Agent frameworks, multi-agent systems |
| `agentic-ai` | Agent development patterns |
| `knowledge-management` | Wikis, memory, RAG |
| `coding-agents` | Claude Code, Cursor, dev tools |
| `quantitative-trading` | Crypto quant, strategies |
| `infrastructure` | Local LLM, Docker, deployment |
| `mlops` | Training, fine-tuning, serving |
| `research` | Papers, arXiv, academic |
| `source` | Source page indicator |
| `concept` | Concept page indicator |
| `synthesis` | Synthesis handbook |

---

## Filing Anti-Patterns (DO NOT DO)

1. ❌ **File by source format** — `social/`, `github/`, `arxiv/` subdirectories — WRONG
2. ❌ **File without checking** — Always consult resolver before creating pages
3. ❌ **Duplicate filing** — One concept = one page, update existing not create new
4. ❌ **Source-concept hybrid** — Separate source summary from concept synthesis
5. ❌ **MemPalace-only write** — Always write to disk first via `write_file()`, NOT `mempalace_add_drawer()`

---

## Routing Decision Tree (FLAT)

```
New content received:
├── Is it a SOURCE (paper, article, repo)?
│   └── Yes → `wiki/sources/<slug>.md` (flat, no subdir)
├── Is it about a PERSON?
│   └── Yes → `wiki/concepts/firstname-lastname.md`
├── Is it about a COMPANY?
│   └── Yes → `wiki/concepts/company-name.md`
├── What is the PRIMARY DOMAIN?
│   ├── AI Security → `wiki/concepts/<slug>.md` (tag: ai-security)
│   ├── AI Agents → `wiki/concepts/<slug>.md` (tag: ai-agents)
│   ├── Knowledge Management → `wiki/concepts/<slug>.md` (tag: knowledge-management)
│   ├── Coding Agents → `wiki/concepts/<slug>.md` (tag: coding-agents)
│   ├── Quant Trading → `wiki/concepts/<slug>.md` (tag: quantitative-trading)
│   ├── Infrastructure → `wiki/concepts/<slug>.md` (tag: infrastructure)
│   └── MLOps → `wiki/concepts/<slug>.md` (tag: mlops)
└── Add TAGS for categorization (NOT subdirectories)
```

---

## Resolver Maintenance

| Action | Frequency | Who |
|--------|-----------|-----|
| Add new domains | When needed | Hermes (human approve) |
| Update anti-patterns | When misfiling discovered | Hermes |
| Audit routing decisions | Monthly | Hermes |
| Flat structure enforcement | Always | CHECKLIST below |

---

## Filing Decision Checklist (MANDATORY)

Before creating any wiki page, verify:

- [ ] Consulted this RESOLVER.md
- [ ] Identified correct domain (AI Security, AI Agents, etc.)
- [ ] Source goes in `wiki/sources/` (flat), concept goes in `wiki/concepts/` (flat)
- [ ] NO subdirectories created in `wiki/concepts/` or `wiki/sources/`
- [ ] Added appropriate TAGS (not folder structure)
- [ ] No existing concept covers this topic (check first)
- [ ] Will add bidirectional `[[wikilinks]]`
- [ ] Updated MANIFEST.json
- [ ] **Used `write_file()` to disk, NOT `mempalace_add_drawer()` (P11 violation)**
- [ ] **If Docker-down: added to `outputs/pending-sync.md` (P12 violation)**

---

*This resolver is the governance layer of C0ldbrain. Treat it as such.*

**Last Updated:** 2026-04-17 — Migrated from hierarchical to FLAT structure (v2.0)
