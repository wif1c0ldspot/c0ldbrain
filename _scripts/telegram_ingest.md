---
name: telegram-ingest
description: Handle incoming links and text from Telegram by staging them in raw/telegram/.
---

# Telegram Ingest

When receiving messages via Telegram:

## Process

1. **If message is a URL:**
   - Extract the URL.
   - Slugify: `domain-com-keywords.md`.
   - Save to `raw/telegram/<slug>.md`.

2. **If message is text/note:**
   - Save to `raw/telegram/note-YYYY-MM-DD-MD5.md`.

3. **Frontmatter:**
```yaml
---
source: telegram
ingested_at: YYYY-MM-DD
type: telegram-note  # or telegram-link
status: uncompiled
---

# Telegram Note/Link
<Content pasted by user>
```

4. **Update MANIFEST.json**:
   Add entry to sources with status `uncompiled`.

5. **Report**:
   "Received and staged in raw/telegram/. Will be compiled during next daily cycle."
