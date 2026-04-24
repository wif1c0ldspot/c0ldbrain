---
compiled: 2026-04-15
confidence: high
created: '2026-04-16'
priority: 2
source_url: https://axi.md/
stars: —
status: current
summary: 10 design principles for agent-ergonomic CLI tools. TOON format achieves
  40% token savings. Benchmarked across 915 runs.
tags:
- token-optimization
- ai-agents
- prompt-engineering
- benchmarking
title: AXI — Agent eXperience Interface
type: source
updated: '2026-04-18'
---


# AXI — Agent eXperience Interface

## Key Insights

- Defines Agent eXperience Interface (AXI) — design principles for building CLI tools that AI coding agents can use efficiently
- Introduces TOON format (Terse Output, Optional Noise) that achieves 40% token reduction
- 10 design principles for agent-ergonomic tools, benchmarked across 915 test runs
- Core insight: tools designed for humans waste tokens on agents; agent-native interfaces are structurally different

## Technical Details

### TOON Format
- Terse Output, Optional Noise — structured output that strips human-friendly formatting
- Agents consume structured data faster than human-readable prose
- 40% token savings verified by benchmark across 915 runs

### 10 Design Principles
1. Machine-parseable output first
2. Minimize token waste in responses
3. Structured error messages over prose
4. Stateful awareness across commands
5. Predictable output schemas
6. Batch operations over sequential calls
7. Semantic compression of repeated patterns
8. Agent-friendly help and documentation
9. Context-aware verbosity levels
10. Streaming support for long operations

### Benchmark Results
- 915 runs comparing traditional CLI vs AXI-optimized tools
- Consistent 40% token reduction without information loss
- Faster agent completion times due to less context pollution

## Related Concepts

- [[token-optimization]] — TOON format is a direct token optimization strategy
- [[ai-coding-agents]] — AXI tools designed specifically for AI coding agents
- [[hermes-agent-architecture]] — applicable to Hermes tool design
