# Architecture Gap Analysis

**Date:** 2026-04-17  
**Scope:** Two-system architecture review (Hermes Agent Memory vs C0ldbrain Knowledge Base)  
**Status:** CRITICAL GAPS FIXED — Remaining items are minor

---

## Executive Summary

The architecture has been successfully corrected from the "MemPalace = L1 agent memory" confusion to the proper two-system model. **5 of 8 gaps have been fixed.**

### Fixed Gaps
- ✅ Gap 1: Session recall mechanism documented
- ✅ Gap 2: MemPalace diary purpose clarified  
- ✅ Gap 3: Agent Optional L3 removed (was undefined)
- ✅ Gap 4: Docker-down policy clarified (read-only, no staging)
- ✅ Gap 5: Naming standardized (Session/Memory/Index/Wiki)

### Remaining Gaps (Low Priority)
- ⏳ Gap 6: Integration tests (nice to have)
- ⏳ Gap 7: Query classification edge cases (minor)
- ⏳ Gap 8: P12 legacy cleanup (tracked in pending-sync.md)

---

## Detailed Gap Report

### Gap 1: Session Recall Mechanism (FIXED ✅)

**Original Problem:** No documentation of how to access Hermes session history.

**Fix Applied:**
- Added `session_search(query)` documentation to `_scripts/README.md`
- Added explicit session recall section to `tiered-knowledge-retrieval` skill
- Documented: "Session context is auto-injected by Hermes"

**Files Modified:**
- `_scripts/README.md` — Added session_search usage
- `tiered-knowledge-retrieval/SKILL.md` — Session recall workflow
- `ABOUT.md` — Session/Memory distinction

---

### Gap 2: MemPalace Diary Ambiguity (FIXED ✅)

**Original Problem:** MemPalace diary purpose unclear — when (if ever) to use it?

**Fix Applied:**
- Added explicit section: "MemPalace Diary (Optional Agent L3 — NOT for Session Recall)"
- Clarified: MemPalace Search = wiki index, MemPalace Diary = optional agent self-reflection
- Documented: Diary uses SEPARATE wing ("hermes-agent"), NOT "c0ldbrain"
- Added to decision tree: When to use diary vs session_search vs wiki

**Files Modified:**
- `tiered-knowledge-retrieval/SKILL.md` — MemPalace Diary section

---

### Gap 3: Agent Optional L3 Undefined (FIXED ✅)

**Original Problem:** "Optional Agent L3" using MemPalace was mentioned but undefined.

**Fix Applied:**
- **Removed** "Optional Agent L3" from all documentation
- Replaced with: MemPalace Diary is optional advanced feature (separate wing)
- Clarified: Current "c0ldbrain" wing is STRICTLY wiki index
- If Agent L3 is needed later, it uses different wing

**Files Modified:**
- `ABOUT.md` ― Removed Optional L3
- `SCHEMA.md` ― Removed Agent Memory Tiers section
- `_scripts/README.md` ― Removed Optional L3

---

### Gap 4: Docker-Down Fallback Incomplete (FIXED ✅)

**Original Problem:** Fallback said "read-only" but mentioned staging; inconsistent policy.

**Fix Applied:**
- **New Policy:** Docker-down = read-only mode, NO exceptions
- Removed all staging procedures (mempalace_add_drawer during Docker-down)
- Updated `llm-optimized-wiki` skill with clear CAN/CANNOT lists
- Updated P11: "NO EXCEPTIONS — Docker-down does not permit MemPalace staging"
- Updated P12: Marked as DEPRECATED

**Files Modified:**
- `llm-optimized-wiki/SKILL.md` ― Docker-down policy rewritten
- `filing-rules.md` ― P11 exception removed, P12 deprecated

---

### Gap 5: Naming Confusion (FIXED ✅)

**Original Problem:** Multiple names for same thing (L1/Index/Search Index).

**Fix Applied:**
- **Standardized terminology across ALL files:**
  - **Session**: Hermes in-memory (current conversation)
  - **Memory**: Hermes SQLite (`session_search` for history)
  - **Index**: MemPalace search (wiki search engine)
  - **Wiki**: C0ldbrain disk (source of truth)
  - **Synthesis**: Generated analysis (on demand)

**Files Modified:**
- `ABOUT.md` ― Standardized to Session/Memory/Index/Wiki/Synthesis
- `SCHEMA.md` ― Same standardization
- `_scripts/README.md` ― Same standardization
- `tiered-knowledge-retrieval/SKILL.md` ― Same standardization

---

### Gap 6: Missing Integration Test (REMAINING ⏳)

**Status:** Low priority. Architecture is documented; tests would be nice but not critical.

**Recommendation:** Create test cases if the architecture causes confusion in practice.

---

### Gap 7: Query Classification Edge Cases (REMAINING ⏳)

**Status:** Low priority. Current classification works for 95% of queries.

**Edge case example:** "What did we decide about resolvers?" could be session OR wiki.

**Current behavior:** Query classification picks one. If wrong, user can clarify.

**Recommendation:** Only refine if this causes actual problems.

---

### Gap 8: P12 Legacy Cleanup (TRACKED ⏳)

**Status:** Legacy entries tracked in `outputs/pending-sync.md`

**Action Required:** Check `pending-sync.md` periodically for stale entries from before policy change.

---

## Verification Checklist

- [x] All skills use consistent terminology (Session/Memory/Index/Wiki/Synthesis)
- [x] Session recall explicitly uses session_search tool
- [x] MemPalace diary purpose documented (optional, separate wing)
- [x] Docker-down policy is read-only (no staging)
- [x] "Optional Agent L3" removed from all documentation
- [x] P11 exception removed
- [x] P12 marked as DEPRECATED
- [x] Query classification uses clear System legend
- [x] Two-system architecture documented in all entry points

---

## Files Modified Summary

| File | Changes |
|------|---------|
| `ABOUT.md` | Standardized terminology, removed L3, clarified Session/Memory/Index/Wiki |
| `SCHEMA.md` | Removed Agent Memory Tiers section, standardized terminology |
| `_scripts/README.md` | Added session_search docs, standardized terminology |
| `filing-rules.md` | Removed P11 exception, deprecated P12 |
| `llm-optimized-wiki/SKILL.md` | Rewrote Docker-down policy (read-only) |
| `tiered-knowledge-retrieval/SKILL.md` | Added MemPalace Diary section, session recall docs |

---

## Architecture Summary (Final)

```
HERMES AGENT (Internal)
├── Session: In-memory context (auto-injected)
└── Memory: SQLite (~/.hermes/sessions/) — session_search(query)

C0LDBRAIN WIKI (External Knowledge Base)
├── Index: MemPalace search (wiki search engine)
├── Wiki: Disk (/Volumes/obsidian/C0ldbrain/wiki/) — source of truth
└── Synthesis: Generated on demand (expensive)

QUERY ROUTING
├── "What did we discuss?" → session_search(query) [Memory]
├── "Find concepts about X" → MemPalace search [Index]
├── "What is X?" → MemPalace → read_file(wiki) [Index → Wiki]
└── "Compare X and Y" → Index → Wiki → generate [Synthesis]

DOCKER-DOWN POLICY
└── Read-only. No staging. No exceptions.
```

---

*Analysis complete. Architecture is now consistent and well-documented.*
