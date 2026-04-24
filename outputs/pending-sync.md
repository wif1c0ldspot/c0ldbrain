---
title: "Pending MemPalace-to-Disk Sync"
type: meta
status: active
summary: "Tracking content written to MemPalace during Docker-down scenarios that needs to be synced back to C0ldbrain disk"
---

# Pending MemPalace-to-Disk Sync

This file tracks content that was written to MemPalace (due to Docker being unavailable) but has not yet been synced to the C0ldbrain wiki disk.

## How This Works

1. When Docker is down, content may be written to MemPalace as a fallback
2. Each entry gets added to this file with metadata
3. When Docker returns, sync these entries to disk
4. Clear entries after successful sync

## Pending Entries

| Date | MemPalace Room | Drawer ID | Topic | Synced | Notes |
|------|---------------|-----------|-------|--------|-------|

*(No pending entries)*

## Sync Procedure

When Docker is back online:

1. Read this file
2. For each pending entry:
   - Retrieve content from MemPalace using `drawer_id`
   - Write to correct path in `/Volumes/obsidian/C0ldbrain/wiki/`
   - Mark as synced in this table
3. Clear the table when all entries synced
4. Commit changes to log

## Template for New Entry

```markdown
| YYYY-MM-DD | room_name | drawer_id_here | Brief topic | ❌ | Context |
```

---

**Rule:** Entries older than 24h without sync = violation of P12. Investigate immediately.
