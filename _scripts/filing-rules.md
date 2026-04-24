# Filing Rules — Known Misfiling Patterns

**Purpose:** Catalog of common errors to prevent recurrence. Updated when misfilings are discovered.

---

## Pattern Catalog

### P1: Source vs. Concept Confusion

**Problem:** Filing a source article in `concepts/` instead of `sources/`.

**Wrong:**
```
concepts/resolvers-garrytan-2026-04.md  ❌
```

**Correct:**
```
sources/resolvers-garrytan-2026-04.md  ✅ (source page)
concepts/resolvers.md                   ✅ (concept page)
```

**Rule:** Sources go in `sources/`, concepts in `concepts/`. Never mix.

---

### P2: File by Source Format Instead of Subject

**Problem:** Filing content based on where it came from rather than what it's about.

**Wrong:**
```
sources/social/  ← X/Twitter articles
sources/github/  ← GitHub repos
sources/arxiv/   ← Papers
```

**Correct:** File by primary subject domain:
```
concepts/ai-security/prompt-injection-attack-vectors.md
concepts/agent-architecture/resolvers.md
concepts/knowledge-management/llm-wiki.md
```

**Rule:** The source URL/metadata goes in frontmatter. The filing location goes in `sources/` OR `concepts/` based on content type.

---

### P3: Skill-Internal Filing Defaults

**Problem:** Ingestion skills with hardcoded default paths bypass resolver logic.

**Wrong:**
```
idea-ingest → always writes to sources/
pdf-ingest → always writes to originals/
meeting-ingest → always writes to meetings/
```

**Correct:**
```
Any skill → MUST consult RESOLVER.md → file by primary subject
```

**Rule:** Skills must not have hardcoded destinations. Always check resolver first.

---

### P4: Person vs. Company Ambiguity

**Problem:** When a person IS their company (founder profiles, sole operators).

**Wrong:**
```
concepts/companies/karpathy.md  ← When it's about Andrew Ng the researcher
```

**Correct:**
```
concepts/people/andrew-ng.md    ← Bio, research, opinions
concepts/companies/deepmind.md  ← Company analysis, products, funding
```

**Rule:** 
- Research contributions, opinions, personal updates → `people/`
- Company analysis, funding, product launches, org changes → `companies/`
- If about BOTH, file by PRIMARY FOCUS of the content

---

### P5: Domain Drift — AI Security

**Problem:** Filing AI security content under general AI categories.

**Wrong:**
```
concepts/ai-coding-agents/prompt-injection.md  ← Should be under ai-security
```

**Correct:**
```
concepts/ai-security/prompt-injection-attack-vectors.md
concepts/ai-security/prompt-injection-defense-guide.md
```

**Rule:** Prompt injection, red teaming, supply chain attacks, compliance = AI Security domain. Don't file under coding agents or general AI.

---

### P6: Nested Concept Proliferation

**Problem:** Creating too many nested subdirectories making things hard to find.

**Wrong:**
```
concepts/ai/agents/architecture/patterns/resolvers.md
```

**Correct:**
```
concepts/agent-architecture/resolvers.md
```

**Rule:** Max 2 levels deep: `concepts/<domain>/<name>.md`. No triple nesting.

---

### P7: Concept Source Hybrid Pages

**Problem:** Creating pages that are both a source summary and a concept definition.

**Wrong:**
```
concepts/resolvers-garrytan-2026-04.md  ← Mixes source + concept
```

**Correct:**
```
sources/resolvers-garrytan-2026-04.md   ← Full source summary
concepts/resolvers.md                   ← Pure concept definition
```

**Rule:** Separate concerns. Source pages summarize ONE source. Concept pages synthesize MULTIPLE sources into unified understanding.

---

### P8: Orphan Source Pages

**Problem:** Source pages without any links to or from concept pages.

**Wrong:** `sources/some-article.md` with no wikilinks.

**Correct:** Source pages MUST link to:
1. Related concept page(s)
2. Index or relevant section in index

**Rule:** Every source page needs outbound links. Check with lint: `--check-orphans`.

---

### P9: Duplicate Concepts

**Problem:** Same concept filed under multiple names.

**Wrong:**
```
concepts/memory-systems.md
concepts/ai-memory.md
concepts/context-management.md  ← All the same topic
```

**Correct:**
```
concepts/memory-systems.md  ← Single canonical page
```

**Rule:** Before creating new concept, search for existing synonyms. Update existing page instead of creating duplicate.

---

### P10: Stale Resolver References

**Problem:** Resolver updated but skills/scripts not updated to match.

**Wrong:** RESOLVER.md says file AI security under `ai-security/` but compile script still uses `security/`.

**Rule:** 
- Resolver changes require updating `_scripts/compile.md`
- Skills must be checked against resolver after resolver updates
- Run `lint --check-resolver-consistency` monthly

---

### P11: MemPalace-Only Write ⚠️ CRITICAL

**Problem:** Adding content to MemPalace without corresponding disk write to C0ldbrain.

**Why this happens:**
- `mempalace_add_drawer()` is convenient
- "wing: c0ldbrain" naming creates confusion with C0ldbrain wiki
- Skills describe correct flow but don't explicitly forbid wrong flow

**Impact:**
- Content lost if MemPalace rebuilds from disk
- Human can't read MemPalace drawers directly
- Future compilation workflows miss the data
- Skills reference disk paths that don't exist

**Wrong:**
```python
# NEVER DO THIS for wiki content
mempalace_add_drawer(wing="c0ldbrain", room="documentation", content=...)  # ❌
```

**Correct:**
```python
# ALWAYS write to disk FIRST
write_file("/Volumes/obsidian/C0ldbrain/wiki/concepts/<slug>.md", content)  # ✅
# MemPalace auto-indexes via file hooks - do NOT manually add drawers
```

**Rule:** 
- **ALWAYS** use `write_file()` to `/Volumes/obsidian/C0ldbrain/wiki/` FIRST
- Never use `mempalace_add_drawer()` for content that should persist to wiki
- MemPalace is auto-indexed mirror, not source of truth
- **NO EXCEPTIONS** — Docker-down does not permit MemPalace staging (see Docker-Down Policy)

---

### P12: MemPalace Staging Without Recovery (DEPRECATED)

**Status:** This pattern is deprecated. Docker-down scenarios no longer permit MemPalace staging.

**Previous Problem:** Writing to MemPalace during Docker-down fallback, then never syncing back to disk.

**Current Policy:** During Docker-down, the wiki is read-only. No staging, no exceptions.

**Legacy Note:** If you encounter stale staging entries from before this policy change:
1. Check `outputs/pending-sync.md` for old entries
2. If found, manually sync to disk
3. Clear the pending list

---

## Filing Decision Checklist

Before creating any wiki page, verify:

- [ ] Consulted RESOLVER.md
- [ ] Identified correct domain
- [ ] Identified correct subject type (person/company/concept/product)
- [ ] No existing concept covers this topic (check synonyms)
- [ ] Source page goes in `sources/`, concept page in `concepts/`
- [ ] Will add bidirectional wikilinks
- [ ] Updated MANIFEST.json
- [ ] Not creating a hybrid source-concept page
- [ ] **Will use `write_file()` to disk, NOT `mempalace_add_drawer()` (P11)**
- [ ] **If Docker-down exception: added to `outputs/pending-sync.md` (P12)**

---

## Pattern Discovery Log

| Date | Pattern | Discovery Context | Fix Applied |
|------|---------|-------------------|-------------|
| 2026-04-17 | P2: File by source format | Initial resolver setup | Created RESOLVER.md |
| 2026-04-17 | P11: MemPalace-Only Write | AI emergence research stored only in MemPalace, not wiki | Updated skills + filing-rules.md, synced files to disk |

---

*Add new patterns here when discovered. Every misfiling is a learning opportunity.*
