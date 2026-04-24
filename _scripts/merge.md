# Merge — Deduplicate Concepts

Find concept pages covering the same topic. Consolidate and archive.

## Process

1. Scan wiki/concepts/ for similar topics (tags, sources, titles)
2. For each candidate pair: read both, determine if merge makes sense
3. Propose merged page structure to user
4. If confirmed:
   - Write merged wiki/concepts/<merged-slug>.md
   - Update all [[slug]] references across wiki to point to merged page
   - Move originals to wiki/archive/
   - Update wiki/index.md
5. Log
