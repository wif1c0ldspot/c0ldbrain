---
title: "Browser Automation"
type: concept
tags: ['ai-agents', 'browser', 'automation', 'CDP']
created: '2026-04-23'
updated: 2026-04-24
confidence: medium
status: current
priority: reference
summary: "Automating browser interactions with AI agents via CDP, DOM manipulation, and agent-driven tool use."
---

# Browser Automation

Automating browser interactions using AI agents. Two main paradigms:

## Approaches

1. **Wrapped tool APIs** — `click()`, `type()`, `scroll()` abstractions (Playwright, Selenium patterns). Easy to start but constrain the model's action space.

2. **Raw CDP access** — Direct Chrome DevTools Protocol. LLMs already know CDP from training data. The agent writes missing helpers on the fly. See [[agent-harness#The Bitter Lesson of Harnesses]] for why this approach wins.

3. **GUI-based** — Visual screenshot + coordinate-level interaction. Works across any UI, not just browsers. See [[alibaba-gui-agent-web-control-2026-03]].

## Key Insight: The Bitter Lesson

The "bitter lesson" for browser automation: don't wrap tools. Give the agent raw protocol access and let it self-heal. ~600 lines of code is sufficient when the agent can edit its own harness mid-task.

See [[bitter-lesson-agent-harnesses-gregpr07-2026-04]] for full argument.

## Sources
- [[bitter-lesson-agent-harnesses-gregpr07-2026-04]] — Raw CDP, self-healing harness philosophy
- [[browser-harness-browser-use]] — browser-harness repo (~600 lines, self-editing)
- [[alibaba-gui-agent-web-control-2026-03]] — GUI agent with browser control

## Related Concepts
- [[agent-harness]]
- [[harness-design]]
- [[ai-coding-agents]]
