# Lint — Wiki Health Audit

Check for broken links, orphans, contradictions, stale claims, and source freshness.

## Pre-condition

Read SCHEMA.md for wiki root path and conventions.

**Automated alternative (Phase 1+2):**
Run `python3 _scripts/build_dashboard_data.py && python3 _scripts/generate_health_report.py` to generate a programmatic health report instead of manual linting.
- Data pipeline reads all pages, builds graph from wikilinks, extracts health metrics, and writes `outputs/dashboard/wiki-data.json`.
- Health report generator produces `outputs/dashboard/health.md` with: composite health score (0-100), broken links, orphans, stale content, pending ingestion, missing metadata, and recommendations.
- Also outputs a one-line Telegram summary.
- Can be run via `/lint`, `/health`, or cron.

## Process

### 1. Build inventory

Read wiki/index.md, overview.md, ALL files in wiki/sources/ and wiki/concepts/, and MANIFEST.json.

Build a map:
- All existing slugs (filenames without .md)
- All [[slug]] references in any page
- All sources listed in frontmatter
- All raw files and their compilation status
- **Date stamps** from each file (created/updated) to check freshness

### 2. Run checks

**🔴 Errors (must fix):**
- Broken [[slug]] links — no corresponding page exists
- Missing frontmatter (title, tags, or sources missing)
- Manifest mismatch — file in wiki/ but not in MANIFEST or vice versa

**🟡 Warnings (should fix):**
- Orphan pages — zero inbound links (exclude index/overview)
- Stale claims — content mentioning "currently", "newest" or years 2+ old
- **Contradictions** — Scan all pages for the same topic. If page A says "X is true" and page B says "X is false", flag with `> ⚠️ CONFLICT: [[page-a]] says "..." vs [[page-b]] says "..."`.
- **Link Rot** — Check URLs in raw/sources files via HTTP HEAD. If 404, flag `> ⚠️ DEAD LINK: URL in [[page-name]]`.

**🔵 Info (consider):**
- Missing concept pages ([[slug]] referenced 3+ times, no page)
- Coverage gaps
- Uncompiled backlog >7 days

### 3. Write lint report

Write outputs/analyses/lint-YYYY-MM-DD.md

### 4. Offer fixes with diffs. Apply after confirmation.

### 5. Log
```
## [YYYY-MM-DD] <agent> lint | N errors, N warnings, N info
```
