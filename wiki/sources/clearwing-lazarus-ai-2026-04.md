---
title: "Clearwing Lazarus Ai 2026 04"
date: 2026-04-17
type: source
compiled: true
tags: []
---

     1|---
     2|title: Clearwing
     3|type: source
     4|tags:
     5|- security
     6|- vulnerability-scanner
     7|- agentic-coding
     8|- langgraph
     9|- pentest
    10|- source-code-audit
    11|- multi-agent
    12|- glasswing-inspired
    13|source_url: https://github.com/Lazarus-AI/clearwing
    14|sources: []
    15|created: '2026-04-18'
    16|updated: '2026-04-18'
    17|confidence: high
    18|status: current
    19|agents:
    20|- hermes
    21|priority: high
    22|summary: "Autonomous vulnerability scanner and source-code hunter by Eric Hartford (Lazarus AI), inspired by Anthropic's Glasswing. Dual-mode: network pentest agent + source-code hunter pipeline."
    23|---
    24|
    25|# Clearwing - Autonomous Vulnerability Scanner & Source-Code Hunter
    26|
    27|**Author:** Eric Hartford (Lazarus AI)  
    28|**Version:** 1.0.0  
    29|**License:** MIT  
    30|**Requires:** Python 3.10+, optional Rust toolchain for genai-pyo3  
    31|**Source:** https://github.com/Lazarus-AI/clearwing  
    32|**Inspired by:** Anthropic's Glasswing
    33|
    34|## Summary
    35|
    36|Clearwing is a dual-mode offensive-security tool built on LangGraph:
    37|
    38|1. **Network-pentest agent** — ReAct-loop with 63 bind-tools that scans targets, detects services/vulnerabilities, runs sandboxed Kali tools, attempts exploits (human-approval gated), writes reports to knowledge graph
    39|2. **Source-code hunter** — File-parallel agent pipeline that ranks source files, fans out per-file hunters, uses ASan/UBSan crashes as ground truth, adversarial second-pass verification, optional patch generation, SARIF/markdown/JSON reports
    40|
    41|**Evidence levels:** `suspicion → static_corroboration → crash_reproduced → root_cause_explained → exploit_demonstrated → patch_validated`
    42|
    43|## Key Details
    44|
    45|### Install
    46|
    47|```bash
    48|git clone https://github.com/Lazarus-AI/clearwing.git
    49|cd clearwing
    50|uv sync --all-extras
    51|source .venv/bin/activate
    52|clearwing setup    # Interactive provider wizard
    53|clearwing doctor   # Environment check
    54|```
    55|
    56|**Providers:** Anthropic, OpenRouter, Ollama, LM Studio, OpenAI, Together, Groq, DeepSeek, Fireworks
    57|
    58|```bash
    59|# Provider env vars
    60|export CLEARWING_BASE_URL=https://openrouter.ai/api/v1
    61|export CLEARWING_API_KEY=***
    62|export CLEARWING_MODEL=anthropic/claude-opus-4
    63|```
    64|
    65|### Architecture
    66|
    67|```
    68|┌──────────────────────┐      ┌────────────────────────────────┐
    69|│ Network-pentest agent│      │ Source-code hunter             │
    70|│ clearwing.agent.graph│      │ clearwing.sourcehunt.runner    │
    71|│  (63 tools, ReAct)   │      │                                │
    72|│                      │      │ preprocess → rank → pool →     │
    73|│                      │      │   hunter → verify → exploit →  │
    74|│                      │      │   variant loop → auto-patch →  │
    75|│                      │      │   report                       │
    76|└─────────┬────────────┘      └────────┬───────────────────────┘
    77|          │                             │
    78|          └───────────┬─────────────────┘
    79|                      ▼
    80|┌───────────────────────────────────────────────────────────────┐
    81|│                    Shared substrate                          │
    82|│  Finding dataclass  │  capabilities probe  │  sandbox layer  │
    83|│  knowledge graph    │  episodic memory     │  event bus      │
    84|│  telemetry          │  guardrails + audit  │  CVSS scoring   │
    85|└───────────────────────────────────────────────────────────────┘
    86|```
    87|
    88|### CLI Commands
    89|
    90|```bash
    91|# Network scan
    92|clearwing scan 192.168.1.10 -p 22,80,443 --detect-services
    93|
    94|# Source-code hunt (sandboxed LLM hunters, adversarial verifier)
    95|clearwing sourcehunt https://github.com/example/project --depth standard
    96|
    97|# Interactive ReAct chat
    98|clearwing interactive
    99|
   100|# CI mode with SARIF output
   101|clearwing ci --config .clearwing.ci.yaml --sarif results.sarif
   102|```
   103|
   104|### Key Dependencies
   105|
   106|- **Core:** scapy, aiohttp, pyyaml, rich
   107|- **Network:** asyncssh, pysmb
   108|- **LLM bridge:** genai-pyo3 (native Rust)
   109|- **Sandbox:** docker
   110|- **Memory:** chromadb, networkx, numpy
   111|- **Source analysis:** tree-sitter (C, C++, Python, JS, Go, Rust)
   112|- **TUI:** textual
   113|- **Web UI:** fastapi, uvicorn, websockets
   114|
   115|### Source Hunt Pipeline
   116|
   117|1. **Ranker** — Pre-selects candidate files from large repos
   118|2. **Pool** — Fans out per-file hunter agents
   119|3. **Hunter** — Per-file analysis with ASan/UBSan ground truth
   120|4. **Verifying** — Adversarial second-pass agent confirms findings
   121|5. **Exploiter** — Attempts exploit demonstration
   122|6. **Variant loop** — Generates patched variants
   123|7. **Auto-patch** — Optional validated patch generation
   124|8. **Report** — SARIF/markdown/JSON with evidence levels
   125|
   126|### Human-Aware Guardrails
   127|
   128|- Exploits gated through **human-approval** interface
   129|- `--export-disclosures` generates pre-filled MITRE CVE-request and HackerOne templates for findings at `evidence_level >= root_cause_explained`
   130|- Clearwing vulnerabilities → GitHub Security Advisories
   131|- Found vulnerabilities → vendor disclosure channels
   132|
   133|### Related Projects
   134|
   135|- **Glasswing (Anthropic):** https://github.com/anthropics/glasswing — Original inspiration
   136|- **LangGraph:** Framework for multi-agent orchestration
   137|
   138|## Notes
   139|
   140|- Clearwing designed to produce Glasswing-like results using accessible models
   141|- Large repos (FFmpeg ~10k files) use tier-A hunter pool, runs for hours
   142|- AsyncLLMClient supports per-stage model routing (different models for ranker/hunter/verifier/exploiter)
   143|- Reports include explicit evidence levels for each finding
   144|- CONSIDER: Potential integration with our security research workflows
   145|
   146|## Quickstart Walkthrough
   147|
   148|### Local repo hunt (FFmpeg example)
   149|
   150|```bash
   151|git clone https://github.com/FFmpeg/FFmpeg.git
   152|cd FFmpeg
   153|
   154|# Run sourcehunt locally via API
   155|uv run python -u - <<'PY'
   156|import logging
   157|from clearwing.llm.native import AsyncLLMClient
   158|from clearwing.sourcehunt.runner import SourceHuntRunner
   159|
   160|REPO = './FFmpeg'
   161|RUN_DIR = './sourcehunt-results-ffmpeg'
   162|COMMON = dict(
   163|    provider_name='openai_resp',
   164|    api_key='YOUR_KEY',
   165|    base_url='http://localhost:8183/v1',
   166|    max_concurrency=15,
   167|)
   168|
   169|runner = SourceHuntRunner(
   170|    repo_url=REPO, local_path=REPO,
   171|    depth='standard',
   172|    budget_usd=1000.0,
   173|    max_parallel=15,
   174|    output_dir=RUN_DIR,
   175|    output_formats=['json', 'markdown'],
   176|    ranker_llm=AsyncLLMClient(model_name='gpt-5.4-mini', **COMMON),
   177|    hunter_llm=AsyncLLMClient(model_name='gpt-5.4', **COMMON),
   178|    verifier_llm=AsyncLLMClient(model_name='gpt-5.4-mini', **COMMON),
   179|    exploiter_llm=AsyncLLMClient(model_name='gpt-5.3-codex', **COMMON),
   180|    enable_patch_oracle=True,
   181|)
   182|print(runner.run())
   183|PY
   184|```
   185|
   186|### Documentation
   187|
   188|| Doc | What it covers |
   189||---|---|
   190|| docs/index.md | Landing page + table of contents |
   191|| docs/quickstart.md | Full install + first run walkthrough |
   192|| docs/providers.md | Provider recipes, per-task routing, env-var precedence |
   193|| docs/architecture.md | Both pipelines, substrate, capability gating, tool layout |
   194|| docs/cli.md | Every subcommand flag |
   195|| docs/api.md | API reference |
   196|