# Fetch URLs — Web Extraction Engine

Scan `raw/` for pending URLs, fetch them, extract clean content, and stage for compilation.

## Pre-condition
Read `SCHEMA.md`. Read `MANIFEST.json` to check for `pending_fetch` status.

## Trigger
1. Manual trigger: "fetch the wiki" or "/fetch"
2. Pre-requisite: `/compile` automatically checks for pending URLs before processing.

## Process

### 1. Scan for URLs
Search all files in `raw/` (except `raw/downloads/` to avoid loops) for URLs.
Pattern: `https://...` or `[link](https...)`.
Also check `MANIFEST.json` for entries with `status: "pending_fetch"`.

### 2. For each URL found
**a. Sluggify the URL**
Example: `https://site.com/article-name` -> `site-com-article-name.md`

**b. Fetch the content**
*   **Primary Method:** Use `browser_navigate` to open the URL, then use `browser_snapshot(full=true)` to extract text.
*   **Alternative:** Use `web_extract` tool if available.
*   **Fallback:** `terminal: curl URL | python3 -c "import sys; print(sys.stdin.read())"` (raw HTML).

**c. Clean the content**
Remove: Navigation bars, sidebars, cookie banners, ads, "Related Articles", comment sections.
Keep: Main body text, title, author, date, images (save images to `wiki/assets/` and reference them).

**d. Save to `raw/downloads/`**
Create a new file:
```yaml
---
source: <original URL>
ingested_at: YYYY-MM-DD
type: download
status: uncompiled
fetched_at: YYYY-MM-DD
---

# <Article Title>
**Original URL:** <URL>
**Author:** <Author or Unknown>
**Fetched:** <Date>

<Extracted article content>
```

### 3. Error Handling
*   **404 / Dead Link:** Log error in `MANIFEST.json` with `status: "dead"`.
*   **Paywall / Captcha:** Mark as `status: "protected"` and note the blocker.
*   **Connection Error:** Mark as `status: "retry_later"`.

### 4. Update MANIFEST.json
For each processed URL, update or add entry in `MANIFEST.json`.
Change status from `pending_fetch` to `uncompiled`.
Update top-level `updated` timestamp.

### 5. Report
"Found N URLs. Fetched M successfully. K failed.
New files staged in `raw/downloads/`. Ready for `/compile`."

## Rules
*   **Rate Limit:** Wait 3 seconds between fetches to avoid blocking.
*   **Never overwrite** existing files in `raw/downloads/`.
*   **Always** clean the extracted content. We want the *signal*, not the noise.
