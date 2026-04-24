---
title: The Bitter Lesson of Agent Harnesses
author: '@gregpr07 (Gregor Zunic)'
date: 2026-04-24
type: source
compiled: true
tags:
- source
- agent-harness
- CDP
- browser-automation
- bitter-lesson
- self-healing
source_url: https://x.com/gregpr07/status/2047358189327520166
confidence: high
status: current
priority: important
summary: 'Philosophical follow-up to browser-harness: your tool abstractions are constraints
  too. Delete them. Give LLMs raw CDP access + ability to edit their own harness.
  ~600 lines total. Agent writes missing functions mid-task.'
updated: '2026-04-24'
created: '2026-04-24'
---

# The Bitter Lesson of Agent Harnesses

**Author:** Gregor Zunic (@gregpr07)
**Date:** 2026-04-24
**Source:** https://x.com/gregpr07/status/2047358189327520166

## Summary

Gregor Zunic's philosophical evolution on agent harness design: not only should you not wrap the LLM in abstractions (previous lesson), you shouldn't wrap its tools either. Every `click()`, `type()`, `scroll()` helper is a constraint the model fights around. Instead, give the agent raw CDP access and let it write what it needs.

## Key Takeaways

1. **Don't wrap tools either.** The first bitter lesson said "don't wrap the LLM." This one goes further — `click()`, `type()`, `scroll()` are all abstractions that constrain the model. LLMs already know CDP natively from training data.

2. **Self-healing through self-editing.** When a helper is missing, the agent greps the codebase, writes the missing function, and reruns. The agent found that `upload_file()` was missing and wrote it using raw `DOM.setFileInputFiles`.

3. **Chunked error recovery is emergent.** Agent tried to upload 12MB, hit CDP's 10MB websocket cap, read the error, and switched to chunked upload — without being told to.

4. **No watchdog services needed.** Previous approach built handlers for 10 Chrome crash modes. With direct CDP, the agent reads errors and recovers on its own — it's already seen ten thousand Chrome crash threads in training.

5. **~600 lines total.** `run.py` (13 lines), `helpers.py` (192 lines), `admin.py` + `daemon.py` (220 lines), `SKILL.md`. Everything above Chrome is rewriteable by the agent.

6. **The bitter lesson generalizes.** Your helpers are abstractions too. Delete them. Let the agent write what it needs.

## Key Quotes

> "Every click(), type(), scroll() helper is an abstraction you decided the model needs. Every one of them is a constraint the RL'd model has to fight around."

> "The 'complexities of CDP' we were trying to hide weren't something to hide. They were something to let the model see."

> "The agent isn't writing new code from first principles. It's writing the one function that was missing, the same way it'd fix a missing import on any codebase."

## Real-World Examples

- **Upload:** Agent wrote `upload_file()` using raw `DOM.setFileInputFiles` mid-task
- **Chunked upload:** Hit 10MB CDP limit, autonomously switched to chunked pattern
- **Gusto → Calendar:** Navigated Gusto employee tab, extracted dates, created Google Calendar events
- **Azure admin:** Used coordinate-level `Input.dispatchMouseEvent` to handle iframe-heavy Azure portal

## Related Concepts
- [[agent-harness]]
- [[browser-automation]]
- [[harness-design]]
- [[ai-coding-agents]]
- [[hermes-agent-architecture]]

## Related Sources
- [[browser-harness-browser-use]] — Original browser-harness repo source
- [[thealexker-harness-optimization-guide-2026-04]] — Harness optimization techniques
- [[anthropic-harness-design-long-running-apps]] — Anthropic's multi-agent harness
