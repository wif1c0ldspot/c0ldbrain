---
title: Clearwing
type: concept
tags: [security, vulnerability-scanner, agentic-coding, langgraph, pentest, source-code-audit, multi-agent]
sources:
- clearwing-lazarus-ai-2026-04
created: '2026-04-19'
updated: '2026-04-19'
confidence: high
status: current
priority: important
summary: "Autonomous vulnerability scanner by Lazarus AI — dual-mode network pentest + source-code hunter with evidence-based severity scoring"
---

# Clearwing

## Summary

Clearwing is an autonomous vulnerability scanner and source-code hunter built by Eric Hartford (Lazarus AI), inspired by Anthropic's Glasswing. Dual-mode architecture: network pentest agent + source-code hunter pipeline.

## Architecture

### Network Pentest Agent
- ReAct-loop with 63 bind-tools
- Scans targets, detects services/vulnerabilities
- Runs sandboxed Kali tools
- Attempts exploits (human-approval gated)
- Writes findings to knowledge graph

### Source-Code Hunter
- File-parallel agent pipeline
- Ranks source files, fans out per-file hunters
- Uses ASan/UBSan crashes as ground truth
- Adversarial second-pass verification
- Optional patch generation

### Evidence Levels
`suspicion → static_corroboration → crash_reproduced → root_cause_explained → exploit_demonstrated → patch_validated`

## Source
[[clearwing-lazarus-ai-2026-04]]

## Related
- [[llm-vulnerability-scanners]] — LLM security scanning tools
- [[owasp-top-10-for-llm]] — LLM security framework
- [[continuous-red-teaming]] — ongoing security assessment
