# Crystallize — Distill Completed Work into Wiki Sources

**LLM Wiki v2 addition.** Treat completed work sessions as wiki sources.

## When to use
- After research threads (e.g., "research latest AI agent frameworks")
- After debugging sessions with discoveries
- After deep-dive analysis sessions
- After multi-hour exploration threads
- User says "crystallize this session" or "save what we learned"

## Process

1. **Review the conversation** — identify key findings, decisions, files touched
2. **Extract facts** — what is now known that wasn't before? What was confirmed? What was debunked?
3. **Create source summary** — write to `raw/articles/session-<YYYY-MM-DD>-<topic>.md`:
   ```yaml
   ---
   source: "crystallization"
   ingested_at: YYYY-MM-DD
   type: article
   session_type: research | debug | analysis | planning
   status: uncompiled
   summary: "What was accomplished in 1 line"
   ---
   ```
4. **Include in summary:**
   - Original question/goal
   - What was explored and found
   - Key conclusions and decisions
   - Files/scripts/configs modified
   - Lessons learned / patterns discovered
   - Open questions remaining
5. **Register in MANIFEST.json** as uncompiled source
6. **Trigger compile** — the new source flows through normal pipeline

## Why this matters

RAG systems forget conversations entirely. This pattern turns ephemeral work into durable knowledge. Each crystallization becomes a first-class source that feeds concepts, strengthens confidence scores, and builds the graph.

Over time, this creates a compounding effect: every debugging session makes future debugging smarter. Every research thread builds on previous research automatically.
