---
title: "How to Build a JARVIS Inside Obsidian With Claude Code — The Full Setup From Scratch"
author: "@cyrilXBT"
date: 2026-04-23
source_url: "https://x.com/cyrilxbt/status/2047246104421388461"
sources: []
type: source
tags:
- source
- ai-agents
- claude-code
- obsidian
- personal-ai
- developer-tools
- automation
- x-article
created: '2026-04-24'
updated: '2026-04-24'
confidence: medium
status: current
agents:
- hermes
priority: important
summary: "CyrilXBT's guide to building a JARVIS-like AI assistant inside Obsidian using Claude Code as the engine, covering full setup from scratch."
compiled: true
---

## Summary

CyrilXBT (@cyrilXBT) published an X Article describing how to build a JARVIS-like personal AI assistant inside Obsidian, powered by Claude Code. The article frames the setup as the closest thing to a real JARVIS — not just a chatbot, but a persistent system that knows your context and executes workflows.

*Note: Full article text is behind X's auth wall. Metadata extracted via Twitter CDN API. Supplementary content compiled from related community sources.*

## Key Points

- **JARVIS concept**: Building a persistent AI assistant inside Obsidian that operates beyond simple chat — stays on, knows context, executes workflows
- **Obsidian as the interface**: Using Obsidian's markdown-native vault as the primary workspace for Claude Code
- **Claude Code as the engine**: Leveraging Claude Code's ability to read/write files, run commands, and maintain context across sessions
- **Full setup from scratch**: Step-by-step guide covering initial configuration through production-ready personal AI
- **Tony Stark framing**: The metaphor is deliberate — not a chatbot, but an always-on system that works alongside you

## Obsidian + Claude Code Integration Strategies (Community Reference)

Based on community research, five main strategies exist for this integration:

### Strategy 1: Dedicated Developer Vault with Symlinks
Best for developers working across multiple repos who want unified search.
```bash
mkdir ~/Developer-Vault
cd ~/Developer-Vault
ln -s ~/.claude claude-global
ln -s ~/projects/my-app my-app
```
Configure `.obsidian/app.json` to filter noise:
```json
{"userIgnoreFilters": ["node_modules/", ".next/", "dist/", ".git/"]}
```

### Strategy 2: Vault IS the Working Directory
Most popular approach — your Obsidian vault is where you run `claude` from:
```
my-vault/
├── CLAUDE.md              # Instructions + readable note
├── .claude/               # Skills, hooks, settings
├── daily-notes/
├── projects/
├── research/
└── templates/
```

### Strategy 3: MCP Bridge
Direct vault access via Model Context Protocol — Claude Code can read/write Obsidian notes through an MCP server.

### Strategy 4: One Vault Per Repo
Separate vault per project — cleanest isolation but no cross-project search.

### Strategy 5: QMD + Session Sync
Quick Markdown Document approach with session-based syncing between Claude Code and Obsidian.

## Connection to C0ldbrain

C0ldbrain wiki itself follows Strategy 2 — the Obsidian vault IS the knowledge base, and agents (Hermes) write directly to it. CyrilXBT's JARVIS concept parallels what C0ldbrain achieves with:
- `CLAUDE.md` → `SCHEMA.md` + `_scripts/wiki_config.py` as the operating manual
- Per-folder indices → `MANIFEST.md` as the live dashboard
- Claude Code skills → Hermes skills system
- Persistent context → MemPalace (L1) + C0ldbrain (L2) tiered memory

## Related Concepts

- [[claude-code]] — The engine powering this setup
- [[claude-code-patterns]] — Proven workflows and patterns
- [[agent-orchestration-stacks]] — Multi-tool orchestration
- [[personal-automation]] — Personal AI assistant patterns
- [[llm-optimized-wiki]] — LLM-native knowledge base architecture

## Source Metadata

- **Tweet**: https://x.com/cyrilxbt/status/2047246104421388461
- **X Article ID**: 2046413025037418496
- **Published**: April 23, 2026
- **Author**: CyrilXBT (AI/Tech/Crypto)
- **Engagement**: 883 likes, 26 replies, 2700+ bookmarks
- **Supplementary sources**: blog.starmorph.com Obsidian+Claude Code guide, dev.to community posts
