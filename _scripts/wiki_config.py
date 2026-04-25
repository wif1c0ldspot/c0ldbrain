#!/usr/bin/env python3
"""
wiki_config.py — Single source of truth for C0ldbrain Wiki paths.
Root: /Volumes/obsidian/C0ldbrain
"""
import os
from pathlib import Path

WIKI_ROOT = Path("/Volumes/obsidian/C0ldbrain")

WIKI_DIR = WIKI_ROOT / "wiki"
CONCEPTS_DIR = WIKI_DIR / "concepts"
SOURCES_DIR = WIKI_DIR / "sources"
SYNTHESIS_DIR = WIKI_DIR / "synthesis"
RAW_DIR = WIKI_ROOT / "raw"
MANIFEST_PATH = WIKI_ROOT / "MANIFEST.json"
SCHEMA_PATH = WIKI_ROOT / "SCHEMA.md"
INDEX_PATH = WIKI_DIR / "index.md"
LOG_PATH = WIKI_DIR / "log.md"
OUTPUTS_DIR = WIKI_ROOT / "outputs"
MERMAID_DIR = OUTPUTS_DIR / "mermaid"
ARCHIVE_DIR = WIKI_DIR / "archive"
LIFECYCLE_DIR = OUTPUTS_DIR / "lifecycle"
LIFECYCLE_REPORT = LIFECYCLE_DIR / "lifecycle-report.json"
RAW_ARTICLES = RAW_DIR / "articles"
RAW_SOCIAL = RAW_DIR / "social"
RAW_GITHUB = RAW_DIR / "github"
RAW_PAPERS = RAW_DIR / "papers"
RAW_DAILY_RESEARCH = RAW_DIR / "daily-research"
RAW_SYNTHESES = RAW_DIR / "syntheses"

VALID_TAGS = {
    "CDP", "active-inference", "agent-architecture", "agent-harness", "agent-memory", "agent-platform", "agent-teams", "agentic-ai", "agentic-coding", "agentic-memory", "ai-agents", "ai-coding-agents", "ai-infrastructure", "ai-powered", "ai-research", "ai-security", "alpha-factors", "architecture", "article", "arxiv", "automation", "autonomous-optimization", "autopilot", "benchmarking", "brain-inspired", "brain-inspired-ai", "browser", "claude-code", "coding-agents", "compliance", "concept", "consciousness", "content-type-identification", "context-engineering", "continuous-red-teaming", "cost", "crypto", "crypto-quant", "cursor", "daily-research", "data-engineering", "day3-pathway", "deep-learning", "defense", "defense-mechanisms", "developer-tools", "devops", "domain-intel", "ecosystem", "emergence", "emergent-capabilities", "ev-kelly", "file-type-detection", "financial-llm", "framework", "gist", "github", "global-workspace-theory", "google", "harness-engineering", "hermes", "incident-response", "infrastructure", "kanban", "kelly-criterion", "knowledge-management", "langgraph", "llm", "llm-attacks", "llm-wiki", "local-models", "machine-learning", "markov-chains", "mcp", "mcp-protocol", "memory", "memory-systems", "meta-agents", "metrics", "ml-models", "mlops", "multi-agent", "multi-module-coordination", "multimodal", "neural-oscillation", "nlp", "notebooklm", "nvidia", "obsidian", "open-data", "open-source", "openai", "operations", "orchestration", "organizational-intelligence", "owasp", "paper", "pentest", "people", "personal-automation", "polymarket", "postgresql", "prediction-markets", "productivity", "project-management", "prompt-engineering", "prompt-injection", "python", "quant-trading", "quantitative-trading", "rag", "red-teaming", "relational-memory", "research", "research-tracking", "rest-api", "security", "sentiment-analysis", "seo", "skills-based-knowledge", "skills-pattern", "social", "software-engineering", "source", "source-code-audit", "state-machine", "stub", "synthesis", "task-management", "timeline", "token-optimization", "tool-calling", "voice-ai", "vulnerability-scanner", "weather-trading", "web-graph", "wiki", "x"
}
