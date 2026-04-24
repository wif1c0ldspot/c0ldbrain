# Automated Maintenance Workflow

Periodic self-cleaning for the wiki to prevent decay.

## Trigger
"maintain the wiki" or "/maintain"
(Can also be cron-jobbed to run weekly)

## Process

### 1. Link Rot Check
For every URL in `raw/` and `wiki/sources/`:
- Ping the URL (HTTP HEAD).
- If 404, mark as `status: dead` in MANIFEST.json.
- If alive, update `last_checked` timestamp.

### 2. Orphan Check
Identify pages with **zero inbound links**.
- If it's an old concept page (updated >60 days ago) and has 0 links, suggest moving to `wiki/archive/`.
- If it's a new page, suggest adding links from `wiki/index.md`.

### 3. Consolidation Suggestions
Identify pages with:
- **High Overlap:** 80%+ content similarity to another page.
- **Action:** Suggest merging into one comprehensive page.
- Prompt user: "Merge [[page-a]] and [[page-b]] into [[page-merged]]?"

### 4. Confidence Audit
Review pages with `confidence: low`.
- Check if new sources (`status: compiled`) have verified the claims.
- If yes, upgrade to `confidence: medium` or `high`.
- If no sources found, prompt for `status: deprecated`.

### 5. Report
"Checked N links, flagged M dead.
Found N orphans, N merge candidates.
Suggested Confidence Upgrades: N."

## Rules
- **Never delete** without confirmation (use `wiki/archive/`).
- **Never merge** without showing the diff first.
- Log every action in `wiki/log.md`.
