#!/usr/bin/env python3
"""
wiki_config.py — Single source of truth for C0ldbrain Wiki paths.
Root: /Volumes/obsidian/C0ldbrain
"""
import os
from pathlib import Path

WIKI_ROOT = Path("/Volumes/obsidian/C0ldbrain")

CONCEPTS_DIR = WIKI_ROOT / "wiki" / "concepts"
RAW_DIR = WIKI_ROOT / "raw"
MANIFEST_PATH = WIKI_ROOT / "MANIFEST.json"
SCHEMA_PATH = WIKI_ROOT / "SCHEMA.md"
INDEX_PATH = WIKI_ROOT / "wiki" / "index.md"
LOG_PATH = WIKI_ROOT / "wiki" / "log.md"
OUTPUTS_DIR = WIKI_ROOT / "outputs"
MERMAID_DIR = OUTPUTS_DIR / "mermaid"

VALID_TAGS = {
    "ai-agents", "ml-models", "crypto-quant", "devops", "security", "infrastructure",
    "knowledge-management", "token-optimization", "memory-systems", "mcp-protocol",
    "prompt-engineering", "local-models", "voice-ai", "prompt-injection",
    "red-teaming", "owasp", "compliance", "defense-mechanisms", "llm-attacks",
    "rag", "multimodal", "hermes", "quantitative-trading", "developer-tools",
    "cost", "autonomous-optimization", "meta-agents", "benchmarking",
    "open-source", "incident-response", "timeline", "stub"
}
