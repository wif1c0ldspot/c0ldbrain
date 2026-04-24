# Master Execution Workflow (Compile → Maintain → Synthesize)

**Single Command Trigger:** When user says "compile the wiki", run the **5-Phase Master Flow**:

## Phase 0: Resolver Check (MANDATORY — DO THIS FIRST)

Before ANY compilation task, consult the resolver:

**0.1 Read RESOLVER.md**
```bash
cat wiki/RESOLVER.md
```

**0.2 Determine Filing Strategy**
- What domain does this content belong to?
- Is it a source, concept, or both?
- Are there existing concepts to update instead of creating new?

**0.3 Consult Filing Rules**
```bash
cat _scripts/filing-rules.md
```
Check for known anti-patterns that apply.

**0.4 Log Filing Decision**
Before creating pages, state your routing decision:
> "Filing this under `concepts/ai-security/` based on resolver domain mapping."

---

## Phase 1: Ingest & Fetch

**1. Scan for new inputs:** 
- Check `MANIFEST.json` for `status: pending_fetch`.
- Scan `raw/**/*.md` for URLs.
- **Execute:** Follow `_scripts/fetch_urls.md`. Extract content from all URLs, save clean text to `raw/downloads/` with `status: uncompiled`.
- **Stage:** Ensure any manual notes have frontmatter and `status: uncompiled`.

## Phase 2: Compile

**1. Process "uncompiled" sources:**
- Read `MANIFEST.json`. Collect all `status == "uncompiled"`.
- **For each source:**
  - Read content and load ingester rules (`_scripts/ingesters/<type>.md`).
  - **MANDATORY: Consult RESOLVER.md before creating pages** (see Phase 0)
  - **Surface takeaways** to user and **WAIT for confirmation.**
  - Write `wiki/sources/<slug>.md` (Summary).
  - Write/Update `wiki/concepts/<slug>.md` (Synthesis).
  - **MANDATORY:** Run backlink audit. Add `[[wikilinks]]` bidirectionally.
  - Update `MANIFEST.json` → `status: compiled`.
  - **CRITICAL: Clean up raw files after successful compilation.** See Phase 2.5 below.

**2. Filing Verification**
After creating pages, verify:
- [ ] Content filed under correct domain per RESOLVER.md
- [ ] Source vs. concept separation correct
- [ ] No hardcoded path used — resolver consulted
- [ ] Bidirectional links added

## Phase 2.5: Raw File Cleanup (MANDATORY)

After each source is compiled, clean `raw/` to prevent duplicate scanning and storage bloat. Raw/ is a staging area, not an archive.

**Rules:**
1. **Compiled sources:** Delete the raw file (MANIFEST.json is the permanent record)
2. **Fetched downloads:** Delete from `raw/downloads/` once content is compiled into a source page
3. **Empty files:** Delete immediately (e.g., `[]`, blank files)
4. **Duplicate files:** Delete once confirmed content already exists in a compiled source
5. **Uncompilable files:** Move to `raw/archive/` with a note (e.g., "podcast with no transcript available")

**What persists:**
- MANIFEST.json -- permanent compilation record
- wiki/RESOLVER.md -- routing table (updated when new domains/patterns discovered)
- wiki/sources and concepts -- the actual knowledge
- _scripts/filing-rules.md -- misfiling pattern catalog
- Wiki log -- append-only audit trail

**What does NOT persist:**
- Raw source files after compilation
- Duplicate bookmarks
- Empty JSON arrays
- Downloaded intermediate files

**Cleanup commands:**
```bash
# After compiling a source, delete it from raw/
rm /Volumes/obsidian/C0ldbrain/raw/social/<compiled-file>
# Delete empty/duplicate bookmark files
rm /Volumes/obsidian/C0ldbrain/raw/social/x-bookmarks-*.json
# Delete fetched downloads that are compiled
rm /Volumes/obsidian/C0ldbrain/raw/downloads/<compiled-file>
```

## Phase 3: Maintain (Integrity Check)

**1. Run Lint Routine:**
- **Contradictions:** Scan new concepts against existing ones. Flag conflicts.
- **Dead Links:** Check URLs in new sources. If 404, flag as dead.
- **Orphans:** Flag pages with 0 inbound links.
- **Merge Suggestions:** If 80%+ overlap found, suggest a merge.

**2. Resolver Consistency Check:**
- Scan for skills/scripts that bypass RESOLVER.md
- Check for domain drift (concepts in wrong folders)
- Verify filing patterns match RESOLVER.md mappings

## Phase 4: Synthesize (Textbook Generation)

**1. Auto-Synthesis Trigger:**
- Look at tags. If a tag (e.g., "AI Agents") now has 3+ new sources/concepts:
- **Execute:** Follow `_scripts/synthesize.md` logic for that topic.
- Create `wiki/synthesis/<topic>-handbook.md` merging all related notes into one deep article.

## Phase 5: Finalize

**1. Update Graph:**
- Scan all wikilinks. Update `outputs/mermaid/wiki-graph.mmd` to reflect new connections.

**2. Log Everything:**
- Append to `wiki/log.md`: `## [DATE] LLM Master-Compile | Fetched N, Compiled M, Maintained, Synthesized K.`
- Update top-level `updated` in `MANIFEST.json`.
- **Update RESOLVER.md if new domains/patterns discovered**

**3. Resolver Pattern Discovery:**
If a misfiling was caught or prevented, document it in `_scripts/filing-rules.md`:
- What was the error?
- What pattern does it follow?
- How was it fixed?
- Add to Pattern Catalog

---

## Quick Reference

**Resolver Location:** `wiki/RESOLVER.md`
**Filing Rules Location:** `_scripts/filing-rules.md`
**Pattern Log:** `_scripts/filing-rules.md` → "Pattern Discovery Log"

**Resolver Mandate:** "Before creating any wiki page, consult RESOLVER.md. File by primary subject, not source format."
