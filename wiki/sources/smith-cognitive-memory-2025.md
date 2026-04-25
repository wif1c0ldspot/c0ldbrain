---
title: 'SMITH: Unifying Dynamic Tool Creation and Experience Sharing via Cognitive
  Memory'
type: source
tags:
- ai-agents
- cognitive-architecture
- procedural-memory
- declarative-memory
- tool-creation
confidence: high
status: current
summary: 'Separate procedural (tool creation) and declarative (knowledge) pathways
  in unified memory hub. Score: 9/10.'
priority: important
updated: '2026-04-24'
created: '2026-04-24'
compiled: true
source_url: aggregate

---

# SMITH: Unifying Dynamic Tool Creation and Experience Sharing via Cognitive Memory

**Source:** Liu et al., 2025

## Key Findings

- Separate **procedural** (tool creation) and **declarative** (knowledge sharing) pathways
- Unified memory hub for cross-task sharing
- Directly implements cognitive dual-process theory in agent architecture
- Tool creation = procedural memory (how to do)
- Knowledge sharing = declarative memory (what to know)

## Emergence Potential: 9/10

**Why it matters:** First explicit implementation of the cognitive dual-process model (procedural vs declarative) in agent architecture. The separation enables agents to build both "how-to" knowledge and "what-is" knowledge independently.

## Architecture
```
SMITH Cognitive Architecture
├── Procedural Pathway (Tool Creation)
│   ├── Skill extraction from interactions
│   ├── Tool program synthesis
│   └── Habitual execution of created tools
├── Declarative Pathway (Knowledge Sharing)
│   ├── Experience documentation
│   ├── Knowledge base construction
│   └── Cross-task knowledge transfer
└── Unified Memory Hub
    ├── Cross-pathway queries
    ├── Shared context
    └── Integrated reasoning
```

## Related Concepts
- [[skill-composition-procedural-learning]] — Day 2 research concept
- [[memory-systems]] — Agent memory architecture
