---
confidence: high
created: '2026-04-16'
priority: important
sources:
- career-ops-2026-04
status: current
summary: AI job search command center (13.6k stars) built on Claude Code — 14 skill
  modes, Go dashboard, PDF generation, batch processing, ATS normalization.
tags:
- source
- ai-agents
- developer-tools
- career
title: Career-Ops - AI Job Search Pipeline
type: source
updated: '2026-04-07'
---


# Career-Ops — AI Job Search Pipeline

**Source:** https://github.com/santifer/career-ops
**Type:** Claude Code job search system
**Author:** @santifer
**Stats:** 13.6k stars, 2.7k forks, 38 commits
**License:** MIT
**Latest:** Apr 7, 2026

## Summary

AI-powered job search pipeline built on Claude Code. Instead of manual spreadsheet tracking, provides an AI-agent-driven pipeline with 14 skill modes, a Go-based dashboard, PDF report generation, and batch processing for job applications.

## Key Features

| Feature | Detail |
|--------|--------|
| Skill Modes | 14 modes for different job search tasks |
| Dashboard | Go-based web UI for application tracking |
| PDF Generation | Automated report/CV generation |
| Batch Processing | Portal scanning, application handling |
| ATS Normalization | Standardized application parsing |
| Interview Prep | STAR + Reflection framework with Story Bank |
| Auto-update | Data contract system |
| Bilingual | English + Spanish support |
| Portal Scanning | Includes DACH/European AI companies |

## Architecture

```
.claude/skills/career-ops/ ← Skill for slash command
batch/ ← Batch processing
config/ ← Configuration
dashboard/ ← Go web dashboard
data/ ← Application data
docs/ ← Documentation
examples/ ← Sample outputs
interview-prep/ ← Interview frameworks
jds/ ← Job descriptions
modes/ ← 14 skill mode definitions
output/ ← Generated outputs
reports/ ← Analysis reports
templates/ ← Templates + portal scanners
```

## Core Scripts
- cv-sync-check.mjs — Resume validation
- dedup-tracker.mjs — Deduplication of applications
- generate-pdf.mjs — PDF report generation
- merge-tracker.mjs — Application merging
- normalize-statuses.mjs — Status normalization
- update-system.mjs — Auto-update system
- verify-pipeline.mjs — Pipeline verification
- test-all.mjs — Pre-merge test suite

## Key Insights

1. Claude Code is becoming a platform for specialized command-center apps (career, project management, etc.)
2. Go-based dashboard shows performance-conscious design
3. STAR interview framework integration is practical and structured
4. 14 skill modes means this covers the full job search lifecycle
5. Auto-update with data contract shows production-grade design
6. Bilingual support is unusual and noteworthy

## Related Concepts

- [[ai-coding-agents]] — AI coding platforms extending beyond code
- [[hermes-agent-architecture]] — Claude Code as competitor/comparison to Hermes
- [[skill-registry]] — 14 skill modes pattern
