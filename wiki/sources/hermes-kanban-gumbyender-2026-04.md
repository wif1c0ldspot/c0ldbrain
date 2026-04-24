---
title: Hermes Kanban Bridge — GumbyEnder
type: source
tags:
- github
- hermes
- obsidian
- kanban
- project-management
- productivity
source_url: https://github.com/GumbyEnder/hermes-kanban
sources: []
created: '2026-04-23'
updated: '2026-04-23'
confidence: high
status: current
priority: important
summary: Obsidian plugin + 3 Hermes skills — autonomous project execution via Kanban
  boards. REST API localhost:27124, Markdown fallback, standups, reviews.
compiled: true
---

# Hermes Kanban Bridge — GumbyEnder/hermes-kanban

**Source:** https://github.com/GumbyEnder/hermes-kanban
**Stars:** 14 | **Language:** TypeScript | **Version:** 1.2.0 | **Created:** 2026-04-22

## What It Does

Obsidian plugin that bridges Hermes Agent with Kanban boards. Hermes breaks goals into boards, manages cards, runs standups/reviews — all local inside Obsidian vaults.

## Architecture

Plugin runs HTTP server (localhost:27124) inside Obsidian → REST API → Kanban Markdown files → visual rendering via mgmeyers obsidian-kanban. 3 Hermes skills: kanban-orchestrator, project-breakdown-to-kanban, kanban-rituals. Markdown fallback when plugin offline.

## Key API Surface

GET /health, GET/POST /boards, POST /cards, POST /cards/move, GET /query, POST /ritual/standup, POST /ritual/review. Cards support priority, due dates, tags, blockers, recurring schedules, cross-board wikilinks.

## Configuration

Port 27124, board folder "Kanban", trust mode "confirm" (modal) or "auto".

## Related

- [[hermes-kanban-bridge]]
- [[hermes-agent-architecture]]
- [[hermes-ecosystem-projects]]
