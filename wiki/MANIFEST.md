---
title: "Wiki Manifest"
type: meta
tags: [meta, wiki, changelog]
created: 2026-04-16
updated: 2026-04-24
confidence: high
status: current
priority: important
summary: "Tracking changes and additions to the C0ldbrain wiki structure"
---

## C0ldbrain Wiki Manifest


### 2026-04-24

- Added source: `bitter-lesson-agent-harnesses-gregpr07-2026-04.md` — Gregor Zunic's philosophical follow-up: don't wrap tools either. Raw CDP + self-editing harness. ~600 lines.
- Updated concept: `agent-harness.md` — Added "Bitter Lesson" section, upgraded confidence to high
- Updated concept: `browser-automation.md` — Expanded from stub with CDP vs wrapped-tools analysis
- Key insight: **Tool wrappers are abstractions too** — Every click()/type()/scroll() constrains the model. Raw protocol access + self-editing wins.

### 2026-04-24

- Added source: `harness-engineering-trae-ai-2026-04.md` — TRAE's definitive guide to Harness Engineering. R.E.S.T framework, PPAF cycle, REPL architecture, 6 design principles, token pipeline, 4 sandbox levels, state separation principle.
- Updated concept: `agent-harness.md` — Added comprehensive Harness Engineering section (R.E.S.T, PPAF, REPL, 6 principles, token pipeline, sandbox levels, spec coding), expanded tags
- Key framework: **R.E.S.T** — Reliability, Efficiency, Security, Traceability as core production agent objectives
- Key architecture: **REPL Harness** — Read→Eval→Print→Loop as deterministic shell around stochastic LLM
- Key principle: **State Separation** — LLM is stateless CPU; all cross-turn state in external Context State Manager
- Key concept: **Spec Coding** — Human engineers shift from line-by-line coding to architecting blueprints and guarding creation

### 2026-04-24

- Added source: `harness-engineering-trae-ai-2026-04.md` — TRAE's definitive guide to Harness Engineering. R.E.S.T framework, PPAF cycle, REPL architecture, 6 design principles, token pipeline, 4 sandbox levels, state separation principle.
- Updated concept: `agent-harness.md` — Added comprehensive Harness Engineering section (R.E.S.T, PPAF, REPL, 6 principles, token pipeline, sandbox levels, spec coding), expanded tags
- Key framework: **R.E.S.T** — Reliability, Efficiency, Security, Traceability as core production agent objectives
- Key architecture: **REPL Harness** — Read→Eval→Print→Loop as deterministic shell around stochastic LLM
- Key principle: **State Separation** — LLM is stateless CPU; all cross-turn state in external Context State Manager
- Key concept: **Spec Coding** — Human engineers shift from line-by-line coding to architecting blueprints and guarding creation

- Added source: `fingpt-ai4finance-2026-04.md` — FinGPT open-source financial LLM. 5-layer architecture, LoRA fine-tuning <$300, beats GPT-4 on sentiment. 6 papers IJCAI/NeurIPS/ICAIF/AAAI.
- Added concept: `financial-llms.md` — Financial LLMs landscape: FinGPT vs BloombergGPT, tasks, fine-tuning approaches, cost comparison, quant trading integration
- Added raw: `raw/github/fingpt-ai4finance-2026-04.md` — Full repo README
- Key insight: **LoRA adaptation** reduces financial LLM update cost from $3M (full retrain) to <$300, enabling weekly updates critical for dynamic markets
- Key benchmark: FinGPT v3.3 beats GPT-4 on FPB sentiment (0.882 vs 0.833 F1) at $17.25 cost

### 2026-04-23

- Added concept: `openchronicle.md` — Open-source local-first memory for AI agents. macOS AX Tree-first capture → Markdown + SQLite. MCP endpoint. Model-agnostic alternative to OpenAI Chronicle. 276 stars, MIT license.
- Added source: `openchronicle-einsia-2026-04.md` — Einsia/OpenChronicle: open-source agent memory with session-aware writing, structured file taxonomy, supersede-not-delete history.
- Updated concept: `memory-systems.md` — Added link to openchronicle
- Updated concept: `mcp-protocol.md` — Added link to openchronicle
- Key insight: **AX Tree > Screenshot/OCR** — Structured accessibility tree capture is cheaper, more intent-rich, and creates cleaner memory than vision pipelines
- Key pattern: **Session-aware writing** — Idle 5m / app-switch 3m / max 2h cutting rules compress noisy snapshots into coherent memory
- Key design: **Supersede-not-delete** — Memory history preserved via supersession rather than overwrite
- Key architecture: **6-layer pipeline** — watcher → dispatcher → parser → buffer → normalizer → reducer → classifier → store
  - Fixed: 1 frontmatter error (honcho.md YAML parse)
  - Fixed: 12 path-prefixed links normalized across 5 files
  - Fixed: 38 broken wikilinks in concept pages (redirected to existing pages or stubs)
  - Created: 41 stub pages (30 concepts + 10 research paper sources + 1 misc)
  - Created: 6 additional concept stubs for remaining source-page links
  - **Result: 0 broken links, 0 path-prefixed links** (was 154 broken, 12 path-prefixed)
  - Remaining: 12 concept orphans (warnings) — pages with 0 inbound links
  - Total wiki pages: 351 (was 270)

- Added concept: `skill-graphs.md` — Three-level skill composition: atoms (deterministic primitives), molecules (explicit orchestration of 2-10 atoms), compounds (high-level playbooks). Human brain RAM is the limiting resource — drive compounds for 100x leverage.
- Added concept: `hermes-kanban-bridge.md` — Obsidian plugin + 3 Hermes skills turning Hermes into autonomous project executor via Kanban boards. REST API localhost:27124, Markdown fallback, standups, reviews. GumbyEnder, 14 stars, v1.2.0.
- Added source: `hermes-kanban-gumbyender-2026-04.md` — GumbyEnder/hermes-kanban: Kanban bridge for Hermes Agent in Obsidian.
- Updated concept: `hermes-ecosystem-projects.md` — Added hermes-kanban-bridge link
- Key pattern: **REST bridge pattern** — Obsidian plugin runs local HTTP server, Hermes skills call REST endpoints, fallback to direct Markdown writes when offline
- Key insight: **Skill ecosystem extensibility** — First third-party Hermes skill+plugin combo demonstrating community extensibility
- Updated concept: `coral-multi-agent-discovery.md` — Expanded with full repo details: git worktree architecture, 3 heartbeat prompts (reflect/consolidate/pivot), warm-start research, 526 stars, MIT, NUS+Stanford. Added raw source and compiled source pages.
- Added source: `coral-human-agent-society-2026-04.md` — Human-Agent-Society/CORAL: multi-agent self-evolution infrastructure
- Key architecture: **Git worktree isolation + symlinked shared state** — Each agent in own branch, `.coral/public/` symlinked for zero-sync knowledge sharing
- Key pattern: **Heartbeat-driven meta-cognition** — Forced reflection intervals anchor in concrete results, consolidate cross-agent knowledge, detect plateaus for pivoting
- Key result: **50%+ breakthroughs from cross-agent building** — Shared knowledge beats solo exploration
- Added source: `skill-graphs-shivsakhuja-2026-04.md` — @shivsakhuja on composing skills: atoms/molecules/compounds framework, reliability ceiling at 8-10 molecules, implementation as capabilities/composites/playbooks.
- Updated concept: `agent-skills-systems.md` — Added link to skill-graphs
- Updated concept: `skill-composition-procedural-learning.md` — Added link to skill-graphs
- Key insight: **Atoms ≠ Molecules ≠ Compounds** — Explicit composition at each level prevents non-determinism in deep skill graphs
- Key pattern: **Drive compounds, not atoms** — Same brain RAM yields 500 vs 5 units of work when agents orchestrate at compound level
- Key ceiling: **8-10 molecule compound limit** — Beyond this, reliability degrades; higher abstractions needed
- Key requirement: **Test every level** — Reliability/consistency is non-trivial and time-consuming to validate

### 2026-04-22

- Added concept: `cloudflare-agent-memory.md` — Cloudflare managed agent memory: 5-channel retrieval, RRF fusion, SOC 2 + HIPAA
- Added concept: `openviking-context-database.md` — ByteDance context database (22.7K★): unified memory, resources, skills
- Added concept: `context-constitution.md` — Letta's framework for agent learning through context management
- Added concept: `cli-vs-mcp-debate.md` — Cognee's argument for CLI over MCP: token efficiency, simpler auth
- Added source: `apex-mem-acl-2026-2026-04.md` — APEX-MEM: semi-structured memory + temporal reasoning (ACL 2026 Main)
- Added source: `higmem-acl-2026-2026-04.md` — HiGMem: LLM-guided hierarchical memory retrieval (ACL 2026 Findings)
- Added source: `genericagent-contextual-density-2026-04.md` — GenericAgent: contextual information density maximization
- Key insight: **Memory as Infrastructure** — Cloudflare, MemPalace (48.9K★), OpenViking signal memory becoming cloud primitive
- Key pattern: **Hierarchical Memory Dominance** — ACL 2026 accepts 4 papers on structured/hierarchical memory
- Key trend: **CLI vs MCP** — Cognee argues CLI interfaces save ~44K tokens vs MCP tool schemas
- Key philosophy: **Context as Learning** — Letta: "Models identify with their ephemerality" — context management enables persistence

### 2026-04-21

- Added source: `multica-kimi-k26-agent-teams-multicaai-2026-04.md` — @multicaai playbook: build 5-agent engineering team with Kimi K2.6 in an afternoon
- Added concept: `multica-platform.md` — Multica open-source platform overview (17.5k★): workspaces, agents, skills, autopilot, multi-runtime support
- Updated concept: `multica-relational-agent-memory.md` — Added link to multica-platform
- Key insight: **Red lines > Responsibilities** — "What you DO NOT do" matters more than job description for agent prompts
- Key pattern: **Agent Pipeline** — Tia (triage) → Kai (code) → Rae (review) → Ren (report) with human merge authority
- Key finding: **Autopilot** — Scheduled/webhook-triggered agent jobs enable team rhythms without human kickoff
- Key optimization: **Cheap models for routine roles** — triager/reporter don't need premium models, save budget for engineering

- Added source: `paperclip-hermes-solo-ai-company-juliangoldieseo-2026-04.md` — @juliangoldieseo: Paperclip (orchestration) + Hermes (memory) as "solo AI company" stack
- Added concept: `agent-orchestration-stacks.md` — Two-layer pattern: orchestration + memory compounding over time
- Key insight: **Compounding > Reset** — agent stacks that remember and improve beat tools that start from zero each session
- Key shift: **Operator → Designer** — human role shifts from manual executor to machine designer when stack handles repetition

- Added source: `rlms-new-reasoning-models-rawworks-2026-04.md` — @raw_works deep dive: RLMs collapse reasoning + tool use, small models beat frontier LLMs
- Added concept: `recursive-language-models.md` — Inference paradigm: prompt as environment, recursive subcalls, 100× context window
- Key insight: **Democratization** — Qwen3.5-27B + RLM beats GPT-5.2 by 2× on LongCoT; frontier capabilities on consumer hardware
- Key benchmark: **LongCoT** — 2,500 expert long-horizon reasoning problems; frontier models <10%, Claude+RLM at 45.4%
- Key limitation: **Recursion depth** — deeper recursion can "overthink," hurt accuracy, explode cost

- Updated source: `agent-skills-osmani-2026-04.md` — Expanded from 7 commands to full 20-skill lifecycle system (17k+★)
- Added concept: `agent-skills-systems.md` — Pattern: lifecycle-organized skills with anti-rationalization + verification gates
- Key innovation: **Anti-rationalization tables** — common agent excuses to skip steps with documented counter-arguments
- Key principle: **Verification non-negotiable** — evidence requirements, "seems right" never sufficient
- Key insight: **Process > Prompts** — complete workflows with checkpoints beat one-shot prompts

### 2026-04-20 (Daily Research)

**Agentic Memory Research — 2026-04-20 (8pm cron)**

- Added source: `openviking-context-database-volcengine-2026-04.md` — Volcengine OpenViking "context database" (22,623★) — unified memory/RAG/skills
- Added source: `memmachine-multi-tier-memory-2026-04.md` — MemMachine 3-tier memory, 0.9169 LoCoMo, 80% fewer tokens than Mem0
- Added source: `atant-benchmark-critique-2026-04.md` — ATANT v1.1: benchmarks cover median 1 of 7 continuity properties. 23% LoCoMo unscorable
- Added source: `adam-privacy-attack-agent-memory-2026-04.md` — ADAM: 100% success rate extracting sensitive data from agent memory
- Added concept: `hierarchical-memory-architectures.md` — OS-inspired hierarchical memory convergence (6 independent systems)
- Updated concept: `memory-systems.md` — Added hierarchical convergence, OpenViking, ATANT, ADAM, 5 context engineering papers, 4 RAG alternatives
- Key insight: **Hierarchical Memory Convergence** — Multiple teams independently arriving at OS virtual memory analogy for agent context
- Key finding: **Context Database** — OpenViking introduces new product category (memory + RAG + skills unified)
- Key threat: **ADAM Privacy Attack** — 100% extraction success rate. More severe than memory poisoning
- Key critique: **ATANT** — Existing benchmarks (LoCoMo, LongMemEval) don't measure actual continuity
- Key papers: 13 new ArXiv papers on agent memory, context engineering, RAG alternatives

### 2026-04-20

- Added source: `llm-wiki-vs-notebooklm-artemxtech-2026-04.md` — @artemxtech critique of Karpathy's LLM wiki vs NotebookLM
- Added concept: `notebooklm-vs-llm-wiki.md` — Comparison: embedding-based tools vs LLM-maintained wikis for personal knowledge
- Updated concept: `karpathy-llm-wiki-agent.md` — Added Critiques section with NotebookLM comparison
- Updated concept: `karpathy.md` — Added Critiques section with @artemxtech analysis
- Key insight: **Skills > Storage** — Convert knowledge to actionable skills integrated into routines, not just wiki summaries
- Key finding: LLM wiki costs ~44K tokens/query; NotebookLM uses embeddings — instant ingestion, cheap queries
- Added source: `company-brain-vs-connectors-contextconor-2026-04.md` — @contextconor "Your company needs a brain, not more connectors"
- Added concept: `company-context-brain.md` — Synthesized organizational understanding vs retrieval (RAG/MCP)
- Updated concept: `context-substrate.md` — Added link to company-context-brain
- Key insight: **Access ≠ Understanding** — 2025 was connectors, 2026 is synthesis. Retrieval gives fragments, synthesis gives worldview.
- Key framework: 5 hard problems — conflict resolution, identity resolution, decay tracking, source authority, cross-source synthesis
- **SYNTHESIS**: Added `knowledge-management-synthesis.md` — Unified view of 3 paradigms: Retrieval (RAG), Compiled (LLM Wiki), Synthesized (Company Brain)
- **SYNTHESIS**: Added `ai-security-synthesis.md` — Unified security landscape: infrastructure, model, application layers + defense-in-depth
- Updated cross-links: `llm-knowledge-bases`, `knowledge-layer`, `notebooklm-vs-llm-wiki`, `company-context-brain` → knowledge-management-synthesis
- Updated cross-links: `emergent-agent-evolution-synthesis`, `prompt-injection-defense-guide` → ai-security-synthesis
- **SYNTHESIS**: Added `context-engineering-synthesis.md` — Context stack (L0-L4), Camp 1 vs Camp 2, practical recommendations
- Updated cross-links: `context-substrate` → context-engineering-synthesis
- Added source: `gbrain-garrytan-agent-brain-2026-04.md` — GBrain repo via @AYi_AInotes
- Added concept: `gbrain-agent-brain.md` — Garry Tan's production agent brain (9.5k ⭐)
- Updated cross-links: `llm-knowledge-bases`, `knowledge-layer`, `memory-systems` → gbrain-agent-brain
- Key finding: **GBrain** — 17,888 pages, hybrid search, self-wiring graph, 26 skills, Minions job queue ($0 tokens)
- Added source: `commoncrawl-backlinks-retlehs-2026-04.md` — @retlehs free backlink extraction via Common Crawl
- Added concept: `commoncrawl-backlink-extraction.md` — Open web graph data for competitive intelligence
- Key finding: **Free backlinks** — Common Crawl web graph replaces $100-999/mo SEO tools
- Added source: `hermes-team-guide-nyk-builderz-2026-04.md` — @nyk_builderz 4-profile Hermes team guide
- Added concept: `hermes-multi-profile-team.md` — Multi-agent team architecture with handoff contracts, memory KPIs, policy gates
- Updated concept: `hermes-agent-architecture.md` — Added link to multi-profile team
- Key insight: **Profiles are the feature. Boundaries are the moat.** — Isolated profiles prevent 14-day voice collapse
- Added source: `hermes-ecosystem-nftcps-2026-04.md` — @NFTCPS Hermes ecosystem explosion (5 projects)
- Added concept: `hermes-ecosystem-projects.md` — CaMeL security, Alpha deployment, Skill Factory, Maestro, Icarus
- Updated concept: `hermes-agent-architecture.md` — Added link to ecosystem projects

### 2026-04-19
- Added source page: `cloudflare-agent-memory-2026-04.md` — Cloudflare Agent Memory Private Beta (managed service)
- Added source page: `missing-memory-hierarchy-arxiv-2026-04.md` — Demand paging for LLM context (ArXiv 2603.09023)
- Added source page: `simplemem-github-2026-04.md` — SimpleMem lifelong memory framework (3,259 stars)
- Added source page: `agent-memory-poisoning-security-2026-04.md` — Memory poisoning security landscape (OWASP ASI06)
- Added concept: `demand-paging-for-agent-memory.md` — OS virtual memory analogy for agent context management
- Added concept: `memory-firewall.md` — Defense pattern against memory poisoning attacks
- Updated concept: `memory-systems.md` — added 4 new sources, demand paging section, memory security section
- Key insight: **Demand Paging for Agent Memory** — LLM context management maps to OS virtual memory
- Key entrant: **Cloudflare Agent Memory** (Private Beta) — ingest/remember/recall/list/forget API
- Key threat: **Memory Poisoning** — MINJA >95% injection success, OWASP ASI06 implementation
- Key tool: **SimpleMem MCP Server** — cloud-hosted lifelong memory at mcp.simplemem.cloud

- Added source page: `multica-agent-memory-mem0ai-2026-04.md` — mem0 analysis of Multica's relational agent memory architecture
- Added concept: `multica-relational-agent-memory.md` — pure SQL+JSONB memory pattern for multi-agent systems (15,400+ stars)
- Added source page: `openai-agents-python-sdk-github-2026-04.md` — OpenAI Agents Python SDK repository (22,600+ stars)
- Added concept: `openai-agents-sdk.md` — official OpenAI agent harness (sandbox agents, handoffs, tracing, MCP)
- Updated concept: `memory-systems.md` — added Multica source + concept reference
- Updated concept: `agent-harness.md` — added Multica + OpenAI Agents SDK as related concepts
- Key insight: **Relational > Embedding for coding agent harnesses** — explicit skill joins beat similarity retrieval when curation matters
- Key pattern: **Cold inference via JSONB snapshots** — assemble context at dispatch, no DB during inference
- Key feature: **Sandbox Agents (v0.14.0+)** — container-based agents for long-running real work (inspect files, run commands, apply patches)
- Added source page: `polymarket-weather-trading-0xmovez-2026-04.md` — @0xmovez guide for Polymarket weather bot with Hermes Agent
- Added concept: `polymarket-weather-trading-strategy.md` — strategy analysis: real alpha, overstated returns, shrinking edge
- Key insight: **Forecast edge is real but thin** — airport coordinate advantage + professional models > market, but 72,900% returns are survivorship bias


### 2026-04-18
- Added source page: `daily-research-agentic-memory-2026-04-18.md`
- Updated concept: `context-substrate.md` — added Camp Convergence section, new tools (Cloudflare, memweave, outcomeops/context-engineering, OpenViking)
- Updated concept: `memory-systems.md` — added 5 new ArXiv papers, ContextCurator analysis, market data
- Key insight: **Camp Convergence** — Memory backends and context substrates are merging as complementary layers
- Key entrant: **Cloudflare Agent Memory** (Private Beta) — validates agent memory as critical infra


Tracking changes and additions to the wiki structure.

---

## 2026-04-18

### Wiki Lint & Fix

Completed comprehensive wiki health audit:
- **Fixed all frontmatter** — 232 pages updated with required fields
- **Fixed structural issues** — RESOLVER.md, MANIFEST.md, index.md
- **Fixed GitHub-style links** — `owner/repo|name` → `slug`
- **Created stub pages** — 8 new concept pages for common broken links
  - mempalace, agent-harness, context-compaction, karpathy, skills-pattern, async-generators, tool-orchestration, rag
- **Stats** — 131 pages total (60 concepts, 62 sources, 3 synthesis)

#### Remaining Issues (Low Priority)
- ~80 broken links (mostly generic terms: llm, mcp, memory)
- ~37 orphan pages (sources rarely linked)
- Alias fix needed (ai-safety→ai-security)

---

### Wiki Lint & Fix (Continued)

Created 16 additional stub pages for broken link targets:
- **concepts/**: agent-architecture, user-sovereignty, claude-md, agent-infrastructure, quantization-techniques, token-optimization-and-efficiency, llm-optimized-wiki, ai-engineering, hermes-atropos-environments, aster-agentic-scaling, emergent-strategies, supersession-protocol, resolver-pattern, completeness-principle, escalation-protocol
- **sources/**: claude-35-evaluation-2025

Fixed case sensitivity issues in 2 files:
- local-llm-infrastructure.md
- claude-md-best-practices.md

#### Remaining Issues (Very Low Priority)
- ~64 broken links (generic terms should be tags, not wikilinks)
- ~37 orphan pages (sources = ingestion layer, backlinks optional)

---

## 2026-04-17

### Resolver Layer Added

Garry Tan's resolver pattern integrated into wiki architecture.

#### Files Created
- [[RESOLVER.md]] - Content routing table with domain mappings, anti-patterns, decision tree

#### Skills Updated
- wiki-x-article-ingest - Added resolver integration section
- wiki-compilation-standards - Added resolver anti-patterns to validation checklist

#### Architecture Change
**Before:** Implicit routing based on skill hardcoded paths
**After:** Explicit routing via RESOLVER.md domain mapping

**Filing Mandate:** "Before creating any wiki page, consult RESOLVER.md. File by primary subject, not source format."

#### Domain Mappings Added
| Domain | Directory |
|--------|----------|
| AI Security | concepts/ (flat) |
| AI Agents & Architecture | concepts/ (flat) |
| Knowledge Management | concepts/ (flat) |
| Coding Agents | concepts/ (flat) |
| Quant Trading | concepts/ (flat) |
| Infrastructure | concepts/ (flat) |
| MLOps | concepts/ (flat) |
| Research | sources/ (flat) |

---

## 2026-04-16

### Sources Added
- [[sources/resolvers-garrytan-2026-04.md]] - Garry Tan's X article on resolvers as routing tables for AI agent context

### Concepts Created
- [[concepts/resolvers.md]] - Routing table for context: 200 lines replaces 20K lines

### Concepts Updated (Bidirectional Links)
- [[concepts/hermes-agent-architecture.md]] - Added resolvers link
- [[concepts/llm-knowledge-bases.md]] - Added resolvers link  
- [[concepts/ai-coding-agents.md]] - Added resolvers link

---

## 2026-04-17 (Evening)

### X Article Ingested: AI Memory Tools Analysis

Comprehensive analysis by @witcheer of 450+ agent-memory and 460+ context-management repos.

#### Source Added
- [[sources/agent-memory-two-camps-witcheer-2026-04.md]] - Full analysis of memory backends vs context substrates

#### Concept Created
- [[concepts/context-substrate.md]] - Emerging paradigm: structured, human-readable context files

#### Concepts Updated
- [[concepts/memory-systems.md]] - Added "Two Camps" section comparing memory backends vs context substrates

---

## Stats Summary

| Metric | Count |
|---|---|
| Concept pages | 52 |
| Source pages | 62 |
| Synthesis handbooks | 3 |
| Domains covered | 6 |
