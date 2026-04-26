---
author: '@excalidraw'
compiled: true
confidence: medium
created: '2026-04-01'
priority: reference
source_url: https://x.com//status/2039422442339233816
status: current
summary: Excalidraw diagrams now stream shape-by-shape to Claude as generated
tags:
- source
- diagrams
- excalidraw
- claude
- visualization
title: Excalidraw Diagrams Streaming to Claude
type: source
updated: '2026-04-26'
---

## Summary

Excalidraw now supports streaming diagrams directly to Claude in real-time, showing the diagram being built shape-by-shape as it's drawn.

## The Integration

### What It Does
1. User draws in Excalidraw
2. Each shape streams to Claude
3. Claude sees diagram forming
4. Real-time context for reasoning

### How It Works
```
Excalidraw Canvas → Stream → Claude → Understanding
```

## Use Cases

### Architecture Discussions
- Draw system diagram
- Claude understands immediately
- Discuss trade-offs
- Iterate together

### Code Architecture
- Sketch interfaces
- Explain data flow
- Model relationships
- Document decisions

### Brainstorming
- Visual thinking
- Rapid iteration
- Shared understanding
- Immediate feedback

## Benefits

### For Users
- Visual + textual reasoning
- Better communication
- Faster iteration
- Living diagrams

### For Claude
- Spatial context
- Visual understanding
- Architecture awareness
- Diagram comprehension

## Technical Details

### Streaming Approach
- WebSocket connection
- Incremental updates
- Efficient传输
- Low latency

### Claude Processing
- Shape-by-shape understanding
- Build mental model
- Query as needed
- Context preserved

## Related Concepts

- [[visualization]]
- [[claude-integration]]
- [[diagram-tools]]
- [[multi-modal-ai]]
