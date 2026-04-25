---
title: Thealexker Harness Optimization Guide 2026 04
date: 2026-04-17
type: source
compiled: true
tags:
- source
- ai-agents
- agent-harness
- optimization
priority: reference
updated: '2026-04-24'
created: '2026-04-24'
confidence: high
status: current
summary: Auto-generated placeholder for Thealexker Harness Optimization Guide 2026
  04
source_url: https://x.com/thealexker/status/2045203785304232162
---

     1|---
     2|title: Harnesses are everything. Here's how to optimize yours.
     3|type: source
     4|tags:
     5|- ai-engineering
     6|- harness-design
     7|- agentic-coding
     8|- claude-code
     9|- codex
    10|- opencode
    11|- context-management
    12|- progressive-disclosure
    13|source_url: https://x.com/thealexker/status/2045203785304232162
    14|sources: []
    15|created: '2026-04-18'
    16|updated: '2026-04-18'
    17|confidence: high
    18|status: current
    19|agents:
    20|- hermes
    21|priority: high
    22|summary: "Alex Ker's guide on harness optimization: progressive disclosure, R.P.I. framework (Research/Plan/Implement), and subagent patterns for clean context management."
    23|---
    24|
    25|# Harnesses are everything. Here's how to optimize yours. - Alex Ker
    26|
    27|**Author:** Alex Ker (@thealexker)  
    28|**Published:** April 18, 2026  
    29|**Source:** https://x.com/thealexker/status/2045203785304232162
    30|
    31|## Summary
    32|
    33|Alex Ker shares practical harness optimization techniques from contributing to open-source harnesses. Three key practices separate harnesses that compound output from ones that compound mistakes: lean config files, R.P.I. prompt framework, and subagent patterns for context management.
    34|
    35|## Key Details
    36|
    37|### Core Harness Function
    38|
    39|The harness acts as scaffolding that:
    40|1. **Manages context** in stateless LLMs via sessions and compressions
    41|2. **Enables functions** like tool calls, I/O processing, and guardrails
    42|
    43|Think of it as: `while (have next message) do {tool}` loop
    44|
    45|### The "Instruction Budget" Problem
    46|
    47|Frontier LLMs can only follow a few hundred instructions before entering the **"dumb zone"** — missing relevant instructions among bloat. Too many instructions = encouraging hallucination.
    48|
    49|**Finding:** ETH research shows LLM-generated system prompts degrade performance while costing ~20% more in inference.
    50|
    51|### Progressive Disclosure Pattern
    52|
    53|Only let the agent pull context when needed. Individual .md files with descriptive names let the agent discover resources on demand.
    54|
    55|#### CLIs
    56|Agents run `--help` to discover commands, same as engineers. Critical for internal/custom CLIs with zero training data.
    57|
    58|**Example:** For uv (gaining adoption, models still fumble):
    59|```
    60|"use uv for Python package management, run uv --help to discover 
    61|subcommands before assuming syntax"
    62|```
    63|
    64|#### Skills
    65|Industry converged on: load only name/description at startup, read SKILL.md only when relevant. Codex explicitly calls this "progressive disclosure" — core to keeping context clean.
    66|
    67|#### MCP Tools
    68|- **Claude Code:** Built-in MCP tool search, loads lightweight index, pulls schemas on demand (~85% context reduction)
    69|- **Codex/OpenCode:** Load all configured MCP tool definitions at session start (OpenCode warns to limit enabled servers)
    70|
    71|**Recommendation:** Be selective about MCP servers per project; disconnect unused ones.
    72|
    73|### R.P.I. Framework (HumanLayer)
    74|
    75|Every prompt should do exactly one of:
    76|
    77|1. **Research:** Problem statement only; agent explores codebase, prior art, function definitions. **No action taken.**
    78|2. **Plan:** Agent writes step-by-step execution plan. **Human reviews and verifies.** Outsourcing thinking here costs dearly later.
    79|3. **Implement:** Execute approved plan in fresh context window. Use subagents if plan is long — keeps intermediate states out of main window.
    80|
    81|### Subagent Patterns
    82|
    83|**Core heuristic:** Use when a summary is sufficient for the main agent. If you need intermediary context, keep it in primary window.
    84|
    85|#### Parallel Fan-Out
    86|Best for investigation/research. Example: Alert fires → agent generates 3 candidate root cause theories → 3 subagents investigate logs/traces/metrics simultaneously → main agent synthesizes conclusion.
    87|
    88|**Value:** Speed + context isolation. Hundreds of log lines stay contained.
    89|
    90|#### Pipelines
    91|Enforce depth where fan-out explores breadth. Sequential roles: UX designer → architect → devil's advocate. Each stage receives previous output and adds analysis. Main agent gets layered evaluation without holding all lenses in context.
    92|
    93|**Extension:** Use frontier model as judge to consolidate responses.
    94|
    95|### Harness Selection Advice
    96|
    97|- **Don't constantly switch harnesses** — lose institutional knowledge in config files, restart failure-case log from zero
    98|- **Pick one** that covers majority of team's use case
    99|- **Treat every failure as data point:** what broke, at which step, under what conditions
   100|- **Customize and iterate:** Best harness is the one shaped by your team's usage
   101|
   102|### Mentioned Tools/Projects
   103|
   104|- Claude Code (Anthropic)
   105|- Codex (OpenAI)
   106|- OpenCode
   107|- Baseten (parallel fan-out example)
   108|
   109|### Image References
   110|
   111|- Image 1: https://pbs.twimg.com/media/HGIE2JobEAAc1WQ?format=png&name=small
   112|- Image 2: https://pbs.twimg.com/media/HGIEskvaUAASj-F?format=png&name=small
   113|- Image 3: https://pbs.twimg.com/media/HGIFZ3wbUAAO7ug?format=jpg&name=small
   114|- Image 4: https://pbs.twimg.com/media/HGIFd7YWAAATYYv?format=png&name=small
   115|- Image 5: https://pbs.twimg.com/media/HGIFmlzWsAA64u0?format=jpg&name=small
   116|
   117|## Notes
   118|
   119|- Complements Anthropic's harness design article (ingested same day)
   120|- R.P.I. framework aligns with planner/generator/evaluator patterns
   121|- Progressive disclosure is key theme across both articles
   122|- Subagent patterns map to multi-agent architectures
   123|
   124|## Full Content
   125|
   126|Engineers used to argue about IDEs, now we argue about harnesses.
   127|
   128|I've been using and contributing to open-source harnesses, and here's what I wish I knew on day one: there are three things you can do right now to make your harness output orthogonal to slop. Yet all three still require human judgment.
   129|
   130|This guide covers these simple surfaces that separate harnesses that compound your output from ones that compound your mistakes: how to keep your config files lean enough to reason over, how to structure prompts using the R.P.I. framework so the model approaches problems the way a staff engineer would, and how to use subagents to keep your main context window clean.
   131|
   132|[Full article content preserved in source above...]
   133|