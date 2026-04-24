---
title: "Hermes Kanban Bridge"
type: concept
tags: [hermes, obsidian, kanban, project-management, task-management, productivity, rest-api]
created: 2026-04-23
updated: 2026-04-23
confidence: high
status: current
priority: important
summary: "Obsidian plugin bridging Hermes Agent with Kanban boards — REST API on localhost:27124, 3 skills, daily standups, weekly reviews, Markdown fallback."
---

# Hermes Kanban Bridge

Turns Hermes into an autonomous project executor using Kanban boards inside Obsidian vaults.

## Core Idea

Instead of managing tasks in a separate tool, Hermes reads/writes Kanban boards directly in your Obsidian vault via a local REST API. The boards render visually using the mgmeyers obsidian-kanban plugin.

## Architecture

- **Plugin**: TypeScript Obsidian plugin (`hermes-kanban-bridge`) runs HTTP server on localhost:27124
- **REST API**: Full CRUD for boards, cards, moves, queries, rituals (standup/review)
- **3 Skills**: kanban-orchestrator, project-breakdown-to-kanban, kanban-rituals
- **Fallback**: Direct Markdown writes if plugin is offline
- **Trust modes**: `confirm` (modal) or `auto` (no prompts)

## Key Features

- Break any goal into structured Kanban board with single prompt
- Cards with priority, due dates, tags, blockers, recurring schedules
- Cross-board card linking via wikilinks
- Daily standup: surfaces in-progress, blocked, overdue items
- Weekly review: velocity tracking, completed vs planned, blockers retrospective
- Recurring cards: auto-recreate checked recurring items
- Query API: filter by column, tag, blocked status, overdue

## Project Details

- **Repo**: https://github.com/GumbyEnder/hermes-kanban
- **Author**: GumbyEnder
- **Version**: 1.2.0
- **Stars**: 14
- **License**: None
- **Created**: 2026-04-22
- **Status**: Complete, released

## Relevance

First third-party Hermes skill+plugin combo that turns Hermes into a project management tool. Demonstrates the Hermes skill ecosystem extensibility pattern — community-built skills that integrate with external tools (Obsidian) via REST bridges.

## Sources

- [[hermes-kanban-gumbyender-2026-04]]

## Related Concepts

- [[hermes-agent-architecture]]
- [[hermes-ecosystem-projects]]
- [[mcp-protocol]]
