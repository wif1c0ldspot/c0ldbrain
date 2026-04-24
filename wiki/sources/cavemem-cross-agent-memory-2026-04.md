---
title: "cavemem — Cross-Agent Persistent Memory for Coding Assistants"
type: source
tags: [memory-systems, context-engineering, agent-memory, caveman-compression, mcp]
created: 2026-04-21
updated: 2026-04-21
confidence: high
status: current
url: https://github.com/JuliusBrussee/cavemem
stars: 64
---

# cavemem — Cross-Agent Persistent Memory

**"why agent forget when agent can remember"**

Cross-agent persistent memory for coding assistants. Hooks fire at session boundaries, compress observations with the caveman grammar (~75% fewer prose tokens, code and paths preserved byte-for-byte), and write to local SQLite. Agents query their own history through three MCP tools. No network. No cloud.

## Key Features

- **Persistent memory across sessions** — hooks capture what happened; the store keeps it
- **Compressed at rest** — deterministic caveman grammar, round-trip-guaranteed expansion for humans
- **Progressive MCP retrieval** — `search`, `timeline`, `get_observations` — agents filter before fetching
- **Hybrid search** — SQLite FTS5 keyword + local vector index, combined with a tunable ranker
- **Local by default** — no network calls, optional remote embedding providers via config
- **Web viewer** — read-only UI at http://localhost:37777
- **Cross-IDE installers** — Claude Code, Cursor, Gemini CLI, OpenCode, Codex
- **Privacy-aware** — `<private>...</private>` stripped at write boundary

## Compression Example

```
Input:  "The auth middleware throws a 401 when the session token expires; we should add a refresh path."
Stored: "auth mw throws 401 @ session token expires. add refresh path."
Viewed: "The auth middleware throws a 401 when session token expires. Add refresh path."
```

Code blocks, URLs, paths, identifiers, and version numbers are never touched. Hook handlers complete in under 150ms.

## Architecture

```
session event → redact <private> → compress → SQLite + FTS5
                                                  ↑
                                       MCP queries on demand
```

## Ecosystem

- [caveman](https://github.com/JuliusBrussee/caveman) — "talk less" (compression grammar)
- **cavemem** — "remember more" (persistent memory)
- [cavekit](https://github.com/JuliusBrussee/cavekit) — "build better" (development toolkit)

## Camp Classification

**Camp 1.5 Hybrid** — Uses Camp 1 storage (local SQLite + vector index) but Camp 2 retrieval patterns (progressive MCP tools that let agents filter before fetching).

## Related Concepts

- [[memory-systems]] — broader memory landscape
- [[context-compaction]] — compression strategies
- [[demand-paging-for-agent-memory]] — lazy retrieval
- [[hierarchical-memory-architectures]] — tiered memory
