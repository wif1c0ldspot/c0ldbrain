---
title: Browser Harness
date: 2026-04-20
type: source
compiled: true
tags:
- source
- hermes
- agent
- browser-automation
source: raw/github/browser-harness-browser-use.md
priority: reference
updated: '2026-04-24'
created: '2026-04-24'
confidence: high
status: current
summary: Auto-generated placeholder for Browser Harness
---

---
title: Browser Harness
type: source
tags:
- browser-automation
- CDP
- LLM-agent
- self-healing
- browser-control
- agentic-coding
- claude-code
- codex
source_url: https://github.com/browser-use/browser-harness
sources:
- https://x.com/gregpr07/status/2045566284319134008
created: '2026-04-18'
updated: '2026-04-18'
confidence: high
status: current
agents:
- hermes
priority: high
summary: "Self-healing browser harness built directly on CDP that gives LLMs complete freedom to complete any browser task. ~592 lines of Python. Agent edits harness mid-task."
---

# Browser Harness - Self-Healing Browser Control for LLMs

**Author:** browser-use (Gregor Zunic)  
**Version:** 0.1.0  
**Source:** https://github.com/browser-use/browser-harness  
**Announced via:** https://x.com/gregpr07/status/2045566284319134008

## Summary

The simplest, thinnest, **self-healing** harness that gives LLM **complete freedom** to complete any browser task. Built directly on CDP (Chrome DevTools Protocol). No framework, no recipes, no rails. One websocket to Chrome, nothing between.

**Core innovation:** The agent writes what's missing mid-task. If `upload_file()` is missing from helpers.py, the agent edits the harness and writes it.

## Key Details

### Architecture (~592 lines of Python)

| File | Lines | Purpose |
|------|-------|---------|
| `run.py` | ~36 | Runs plain Python with helpers preloaded |
| `helpers.py` | ~195 | Starting tool calls; agent edits these |
| `admin.py` + `daemon.py` | ~361 | Daemon bootstrap + CDP websocket bridge |
| `SKILL.md` | — | Day-to-day usage instructions |
| `install.md` | — | First-time install and browser bootstrap |

### How It Works

```
agent: wants to upload a file
    │
helpers.py → upload_file() missing
    │
agent edits the harness and writes it    helpers.py   192 → 199 lines
    │                                                       + upload_file()
    ✓ file uploaded
```

### Setup (Claude Code or Codex)

```text
Set up https://github.com/browser-use/browser-harness for me.

Read `install.md` first to install and connect this repo to my real browser.
Then read `SKILL.md` for normal usage. Always read `helpers.py` because that
is where the functions are. When you open a setup or verification tab, activate
it so I can see the active browser tab. After it is installed, if I am already
logged in to GitHub, star this repository as a small verification task; if I am
not logged in, just go to browser-use.com.
```

### Quick Start

```bash
uv run bh <<'PY'
goto("https://browser-use.com")
wait_for_load()
print(page_info())
PY
```

### Tool Call Shape

```bash
browser-harness <<'PY'
# any python. helpers pre-imported. daemon auto-starts.
PY
```

### Remote Browsers (Optional)

For sub-agents or deployment. **Free tier: 3 concurrent browsers, no card required.**

```bash
# Get key at cloud.browser-use.com/new-api-key
uv run python - <<'PY'
from admin import start_remote_daemon
print(start_remote_daemon("work"))
PY

BU_NAME=work uv run browser-harness <<'PY'
print(page_info())
PY
```

### Domain Skills

Available in `domain-skills/`:
- `tiktok/upload.md` — TikTok upload automation

### Interaction Skills

Available in `interaction-skills/`:
- `cookies.md`
- `cross-origin-iframes.md`
- `dialogs.md`
- `downloads.md`
- `drag-and-drop.md`
- `dropdowns.md`
- `iframes.md`
- `network-requests.md`
- `print-as-pdf.md`
- `screenshots.md`
- `scrolling.md`
- `shadow-dom.md`
- `tabs.md`
- `uploads.md`
- `viewport.md`

### Installation

```bash
git clone https://github.com/browser-use/browser-harness
cd browser-harness
uv tool install -e .
command -v browser-harness
```

**Claude Code integration:**
Add `@~/src/browser-harness/SKILL.md` to `~/.claude/CLAUDE.md`

**Codex integration:**
```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills/browser-harness"
ln -sf "$PWD/SKILL.md" "${CODEX_HOME:-$HOME/.codex}/skills/browser-harness/SKILL.md"
```

### Key Design Principles

1. **Self-healing:** Agent edits the harness mid-task when functions are missing
2. **No framework overhead:** Direct CDP websocket, nothing between
3. **Agent ownership:** helpers.py is yours; extend it as needed
4. **Domain knowledge accumulation:** PR back what you learn about site quirks
5. **Progressive disclosure:** Only load skills as needed

### What to Contribute Back

- **Private APIs** a page calls (10× faster than DOM scraping)
- **Stable selectors** that beat obvious ones
- **Framework quirks** ("dropdown only commits on Escape")
- **Hidden gotchas** that cost multiple steps to discover

## Notes

- **Complements Hermes browser tools:** Browser harness is more agent-centric (self-healing, editable) while Hermes browser tools are more static
- **Design philosophy aligns with:** Bitter lesson — simple harness > complex framework
- **uv-first:** All commands use `uv run`
- **Domain skill accumulation:** Agents learn and share improvements across runs
- **592 lines total:** Incredibly minimal design

## Related Content in Wiki

- **Anthropic Harness Design** (raw/articles/anthropic-harness-design-long-running-apps.md)
- **Alex Ker Harness Optimization** (raw/social/thealexker-harness-optimization-guide-2026-04.md)
- **Claude Code Agent Design Space** (raw/papers/claude-code-agent-design-space-arxiv-2026-04.md)
- **Clearwing** (raw/github/clearwing-lazarus-ai.md) — Different harness, same agentic pattern


---

## Related Concepts
- [[hermes-agent-architecture]]
- [[agent-harness]]
- [[llm-optimized-wiki]]
