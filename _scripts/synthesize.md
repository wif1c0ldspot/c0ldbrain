# Synthesis Mode — Deep Knowledge Generation

Instead of compiling source-by-source, this mode synthesizes multiple sources into a single, authoritative "Textbook" article.

## Pre-condition
Read `SCHEMA.md`. Ensure wiki has at least 5 concept pages.

## Trigger
"synthesize [topic]" or "/synthesize"

## Process

### 1. Topic Selection
Identify a cluster of related concepts. 
*   **Manual:** User specifies "Token Optimization".
*   **Automatic:** Find tags that have high frequency (e.g., 3+ articles tagged `ai-agents`).

### 2. Ingestion
Read **ALL** concept pages and source summaries related to the topic.
Identify common themes, unique insights, and conflicting info.

### 3. Synthesis (Textbook Generation)
Create a new file: `wiki/synthesis/<topic>-handbook.md`.
Structure it like a textbook, not a list:
*   **Definition:** What is this topic?
*   **History/Evolution:** How has it changed (Timeline)?
*   **Core Methods:** The main approaches (e.g., RAG vs Wiki vs Vector).
*   **Tools & Ecosystem:** Comparison table of all tools mentioned.
*   **Conflicting Views:** Summary of where sources disagree.
*   **Final Consensus:** The "State of the Art" as of today.

### 4. Cross-Linking
Add `[[wikilinks]]` from the new handbook back to the original source articles.
Update `wiki/index.md` to highlight this new authoritative guide.

### 5. Report
"Synthesized [Topic] Handbook. Merged [N] concepts into one deep-dive article."

## Rules
*   **Do NOT repeat** the source summaries. Synthesize into new text.
*   **Highlight conflicts.** Don't smooth them over.
*   **Source everything.** Use `[[wikilinks]]` for every claim.
