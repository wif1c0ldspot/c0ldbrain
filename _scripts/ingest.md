# Ingest — Staged Intake with URL Extraction

Capture sources into `raw/` with metadata frontmatter. Automatically detects and stages URLs for extraction.

## Pre-condition

Read `SCHEMA.md` for conventions. Read `MANIFEST.json` to check if source already staged.

## Process

### 1. Accept the source

| Input | Action |
|-------|--------|
| File path | Copy to `raw/<type>/<filename>` if not already there |
| Markdown file with links | Scan for URLs. Stage each URL individually (see step 2). |
| `.urls` file (one URL per line) | Read each URL, stage individually. |
| Human note | Save to `raw/notes/<slug>.md` |

### 2. URL Auto-Staging (New!)

If the input contains URLs:
1. **Extract all URLs** from the file content.
2. **Slugify each URL** (e.g., `https://site.com/article` → `site-com-article.md`).
3. **Save each URL** as a placeholder in `raw/downloads/<slug>.md`:
   ```yaml
   ---
   source: <URL>
   ingested_at: YYYY-MM-DD
   type: download
   status: pending_fetch
   ---
   ```
4. **Update MANIFEST.json** for each URL.

### 3. Report

- "Staged N sources."
- "Found X URLs — marked as `pending_fetch`."
- "To extract and compile, run `/compile`."

## Rules

- Ingestion NEVER triggers compilation automatically.
- URLs are never fetched during ingest (fetching happens at compile time to allow batching).
- If a URL is already staged, skip and report.
- Always append new entries to `MANIFEST.json` and update the `updated` timestamp.
