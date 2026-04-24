# Knowledge Lifecycle Pipeline

Automated detection and management of knowledge decay in Camp 2 context substrates.

## Overview

As your wiki grows, not all content retains equal value. Some pages become outdated, others are verbose, and some are rarely accessed. The lifecycle pipeline identifies these and recommends actions:

- **RETAIN** — Core knowledge, actively used, well-connected
- **CONDENSE** — Verbose pages that should be compressed to patterns
- **ARCHIVE** — Stale or project-specific content to deprioritize
- **DISCARD** — Unused/isolated content for deletion review
- **CONVERGE** — Similar pages that could be merged

## Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `lifecycle_detect.py` | Scan wiki, generate candidate lists | `python3 lifecycle_detect.py` |
| `lifecycle_condense.py` | Compress verbose pages | `python3 lifecycle_condense.py [--dry-run]` |
| `lifecycle_archive.py` | Move stale pages to archive/ | `python3 lifecycle_archive.py [--dry-run]` |

## Quick Start

```bash
# 1. Run detection (generates report)
python3 _scripts/lifecycle_detect.py

# 2. Review reports
#    - outputs/lifecycle/lifecycle-report.md (human-readable)
#    - outputs/lifecycle/lifecycle-report.json (machine-readable)

# 3. Dry-run condense candidates
python3 _scripts/lifecycle_condense.py --dry-run

# 4. Apply condense (interactive)
python3 _scripts/lifecycle_condense.py

# 5. Dry-run archive candidates
python3 _scripts/lifecycle_archive.py --dry-run

# 6. Apply archive (interactive)
python3 _scripts/lifecycle_archive.py
```

## Decision Criteria

### Condense Candidates
- Word count > 800
- High temporal references (dates, versions)
- Low access count (< 3) + aging (> 30 days)
- Leaf node (only 1 inbound link)

### Archive Candidates
- Not accessed in 90+ days
- Tagged as project-specific
- No inbound links (orphan)
- Time-heavy content > 180 days old
- Draft status

### Discard Candidates
- Never accessed + aging > 60 days
- Isolated (no inbound or outbound links)
- Explicitly superseded
- Stub (< 100 words) + aging
- Tagged deprecated/obsolete

### Convergence Candidates
- Semantic similarity > 70%
- Same content type (both concepts or both sources)
- Neither already archived/superseded

## Outputs

```
outputs/lifecycle/
├── lifecycle-report.json    # Machine-readable data
├── lifecycle-report.md      # Human-readable report
└── ...                      # Future: action logs
```

## Integration with Wiki

### Frontmatter Lifecycle Tracking

Add lifecycle metadata to track page usage:

```yaml
---
title: "Async Python Patterns"
lifecycle:
  last_reviewed: 2026-04-18
  review_cadence: quarterly
  access_count: 47
  last_accessed: 2026-04-17
  condense_candidate: false
  archive_candidate: false
---
```

### Automated Workflow (Cron)

```bash
# Add to crontab for weekly lifecycle review
0 9 * * 1 cd /Volumes/obsidian/C0ldbrain && python3 _scripts/lifecycle_detect.py
```

## Best Practices

1. **Always review before condensing** — The algorithm flags candidates, but human judgment determines what's pattern vs. temporal

2. **Archive, don't delete** — Move to `archive/` first. Only delete after 6+ months if truly useless

3. **Update `access_count`** — When you reference a page, increment its access_count in frontmatter

4. **Run monthly** — Weekly is too frequent; quarterly lets problems accumulate

5. **Watch convergence pairs** — High similarity often indicates fragmented understanding

## Related

- [[wiki/concepts/knowledge-lifecycle-decision-framework]] — Theoretical framework
- [[wiki/concepts/context-substrate]] — Camp 2 accumulation problem
