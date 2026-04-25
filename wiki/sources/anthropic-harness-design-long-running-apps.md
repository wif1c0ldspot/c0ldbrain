---
title: Anthropic Harness Design Long Running Apps
date: 2026-04-17
type: source
compiled: true
tags:
- source
- ai-agents
- agent-harness
- anthropic
priority: reference
updated: '2026-04-24'
created: '2026-04-24'
confidence: high
status: current
summary: Auto-generated placeholder for Anthropic Harness Design Long Running Apps
source_url: https://www.anthropic.com/engineering/harness-design-long-running-apps
---

     1|---
     2|title: Harness design for long-running application development
     3|type: source
     4|tags:
     5|- ai-engineering
     6|- agentic-coding
     7|- anthropic
     8|- claude
     9|- harness-design
    10|- multi-agent
    11|- frontend-design
    12|- evaluators
    13|source_url: https://www.anthropic.com/engineering/harness-design-long-running-apps
    14|sources: []
    15|created: '2026-04-18'
    16|updated: '2026-04-18'
    17|confidence: high
    18|status: current
    19|agents:
    20|- hermes
    21|priority: high
    22|summary: "Anthropic Labs' Prithvi Rajasekaran details a GAN-inspired multi-agent harness (planner/generator/evaluator) for long-running coding tasks, with frontend design criteria and context reset patterns."
    23|---
    24|
    25|# Harness design for long-running application development - Anthropic Engineering
    26|
    27|**Author:** Prithvi Rajasekaran (Anthropic Labs)  
    28|**Published:** March 24, 2026  
    29|**Source:** https://www.anthropic.com/engineering/harness-design-long-running-apps
    30|
    31|## Summary
    32|
    33|Anthropic Labs developed a multi-agent harness architecture inspired by GANs, using separate **generator** and **evaluator** agents to push Claude's capabilities in frontend design and long-running autonomous software engineering. The three-agent system (planner, generator, evaluator) produced rich full-stack applications over multi-hour autonomous coding sessions, significantly outperforming single-agent baselines.
    34|
    35|## Key Details
    36|
    37|### Core Problems Addressed
    38|
    39|1. **Context Anxiety**: Models begin wrapping up work prematurely as they approach perceived context limits
    40|2. **Self-Evaluation Bias**: Agents skew positive when grading their own work, especially on subjective tasks
    41|3. **Coherence Degradation**: Models lose coherence on lengthy tasks as context window fills
    42|
    43|### Frontend Design Harness
    44|
    45|**Four Grading Criteria** (weighted toward design quality and originality):
    46|- **Design Quality**: Coherent whole vs collection of parts; distinct mood/identity
    47|- **Originality**: Evidence of custom decisions vs template defaults; penalizes "AI slop" patterns
    48|- **Craft**: Technical execution (typography, spacing, color, contrast)
    49|- **Functionality**: Usability independent of aesthetics
    50|
    51|**Implementation:**
    52|- 5-15 iteration loops using Claude Agent SDK
    53|- Generator creates HTML/CSS/JS frontend
    54|- Evaluator uses Playwright MCP to interact with live page before scoring
    55|- Generator makes strategic decisions: refine current direction or pivot aesthetic
    56|- Full runs up to 4 hours
    57|
    58|### Long-Running Coding Harness (V1)
    59|
    60|**Three-Agent Architecture:**
    61|1. **Planner**: Expands 1-4 sentence prompt into full product spec; finds AI feature opportunities
    62|2. **Generator**: Works in sprints, one feature at a time; React/Vite/FastAPI/SQLite stack; git version control
    63|3. **Evaluator**: Uses Playwright MCP to test UI/API/database; grades against criteria with hard thresholds
    64|
    65|**Sprint Contract Pattern:**
    66|- Generator and evaluator negotiate what "done" looks like before coding
    67|- Bridges gap between high-level user stories and testable implementation
    68|- Communication via files between agents
    69|
    70|**Cost Comparison** (retro game maker prompt):
    71|| Harness | Duration | Cost |
    72||---------|----------|------|
    73|| Solo agent | 20 min | $9 |
    74|| Full harness | 6 hr | $200 |
    75|
    76|**Results:** Full harness produced working game with AI features; solo run had broken core functionality.
    77|
    78|### Harness Iteration (V2) - Opus 4.6
    79|
    80|**Simplifications with improved model:**
    81|- Removed sprint construct (model handles longer coherent sessions natively)
    82|- Moved evaluator to single pass at end vs per-sprint grading
    83|- Planner still essential to prevent under-scoping
    84|
    85|**Cost Comparison** (DAW prompt with Opus 4.6):
    86|| Phase | Duration | Cost |
    87||-------|----------|------|
    88|| Planner | 4.7 min | $0.46 |
    89|| Build Round 1 | 2 hr 7 min | $71.08 |
    90|| QA Round 1 | 8.8 min | $3.24 |
    91|| Build Round 2 | 1 hr 2 min | $36.89 |
    92|| QA Round 2 | 6.8 min | $3.09 |
    93|| Build Round 3 | 10.9 min | $5.88 |
    94|| QA Round 3 | 9.6 min | $4.06 |
    95|| **Total** | **3 hr 50 min** | **$124.70** |
    96|
    97|**QA Still Added Value:** Caught gaps like stubbed audio recording, missing clip interactions, and display-only features.
    98|
    99|### Key Patterns
   100|
   101|1. **Context Resets vs Compaction**: Full context resets provide clean slate addressing context anxiety; compaction alone insufficient for Sonnet 4.5
   102|2. **Generator-Evaluator Separation**: Tuning standalone evaluator to be skeptical more tractable than making generator self-critical
   103|3. **Handoff Artifacts**: Structured state transfer between sessions
   104|4. **Model-Dependent Harnessing**: Evaluator worth the cost when task sits beyond what model does reliably solo
   105|5. **Retest Assumptions**: Strip away non-load-bearing components as models improve
   106|
   107|### Related Work
   108|
   109|- **Frontend Design Skill**: https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md
   110|- **Long-running Agent Harness (earlier)**: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
   111|- **Context Engineering**: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
   112|- **"Ralph Wiggum" method**: https://ghuntley.com/ralph/
   113|
   114|## Notes
   115|
   116|- Opus 4.6 improvements (planning, sustained agentic tasks, code review) reduced need for some scaffolding
   117|- Evaluator required significant tuning: early versions identified bugs then talked themselves into approving anyway
   118|- Common failure: evaluator tested superficially rather than probing edge cases
   119|- Claude's training data thin on recent agent-building patterns—required iteration to get generator building proper agents
   120|- Limitation: Claude can't actually hear—QA feedback less effective for musical taste
   121|
   122|## Full Article Content
   123|
   124|Written by Prithvi Rajasekaran, a member of our Labs team.
   125|
   126|Over the past several months I've been working on two interconnected problems: getting Claude to produce high-quality frontend designs, and getting it to build complete applications without human intervention. This work originated with earlier efforts on our frontend design skill and long-running coding agent harness, where my colleagues and I were able to improve Claude's performance well above baseline through prompt engineering and harness design—but both eventually hit ceilings.
   127|
   128|To break through, I sought out novel AI engineering approaches that held across two quite different domains, one defined by subjective taste, the other by verifiable correctness and usability. Taking inspiration from Generative Adversarial Networks (GANs), I designed a multi-agent structure with a generator and evaluator agent. Building an evaluator that graded outputs reliably—and with taste—meant first developing a set of criteria that could turn subjective judgments like "is this design good?" into concrete, gradable terms.
   129|
   130|I then applied these techniques to long-running autonomous coding, carrying over two lessons from our earlier harness work: decomposing the build into tractable chunks, and using structured artifacts to hand off context between sessions. The final result was a three-agent architecture—planner, generator, and evaluator—that produced rich full-stack applications over multi-hour autonomous coding sessions.
   131|
   132|[Full article content continues in original source...]
   133|