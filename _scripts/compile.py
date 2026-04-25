#!/usr/bin/env python3
"""
compile.py — C0ldbrain Wiki 5-Phase Compiler
=============================================

Implements Karpathy's LLM Wiki pattern: ingest, compile, maintain, synthesize, finalize.

USAGE:
  python3 compile.py                    # Run all 5 phases
  python3 compile.py --phases fetch     # Run only fetch phase
  python3 compile.py --phases fetch compile  # Run fetch + compile
  python3 compile.py --dry-run          # Show what would happen
  python3 compile.py --verbose          # Detailed output

AS AN LLM AGENT:
  1. Call `python3 compile.py` to scan the wiki state
  2. Read the FETCH phase output to see raw sources needing processing
  3. For each raw source, extract knowledge and write to concepts/
  4. Call `register_compiled_concept()` after writing each concept
  5. Run MAINTAIN to validate integrity
  6. Run SYNTHESIZE to merge overlapping concepts
  7. Run FINALIZE to regenerate index, graph, and log

PHASES:
  FETCH:     Scan raw/ for new sources → build worklist
  COMPILE:   Extract knowledge from raw sources → write concept pages  
  MAINTAIN:  Lint for schema violations, dead wikilinks, orphans, contradictions
  SYNTHESIZE: Find merge candidates based on tag/content overlap
  FINALIZE:  Regenerate index.md, wiki-graph.mmd, update MANIFEST.json

LLM INTEGRATION:
  The compiler is designed to be run by LLM agents. It provides clear
  worklists, validation feedback, and helper functions for agents to
  register their work as they process sources.
"""

import os
import sys
import json
import re
import glob
import datetime
import argparse
from pathlib import Path
from collections import defaultdict

# Import canonical path configuration
import wiki_config

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Use wiki_config for wiki root
WIKI_ROOT = wiki_config.WIKI_ROOT
CONCEPTS_DIR = wiki_config.CONCEPTS_DIR
SOURCES_DIR = wiki_config.SOURCES_DIR
SYNTHESIS_DIR = wiki_config.SYNTHESIS_DIR
RAW_DIR = wiki_config.RAW_DIR
MANIFEST_PATH = wiki_config.MANIFEST_PATH
INDEX_PATH = wiki_config.INDEX_PATH
LOG_PATH = wiki_config.LOG_PATH
MERMAID_DIR = WIKI_ROOT / "outputs" / "mermaid"

# Use canonical VALID_TAGS from wiki_config (138 tags, single source of truth)
VALID_TAGS = wiki_config.VALID_TAGS

# ---------------------------------------------------------------------------
# Knowledge Lifecycle helpers (LLM Wiki v2 — rohitg00 additions)
# ---------------------------------------------------------------------------

CONFIDENCE_DECAY_RATES = {
    "architecture": 0.01,     # 1% confidence decay per day
    "tools": 0.03,            # 3% per day (change fast)
    "security": 0.02,         # 2% per day
    "patterns": 0.015,        # 1.5% per day
    "default": 0.02,          # 2% default
}

# Forgetting curve decay tiers (Ebbinghaus-inspired)
DAYS_UNTIL_DEPRIORITIZE = {
    "architecture": 180,      # 6 months
    "patterns": 90,           # 3 months
    "security": 60,           # 2 months
    "tools": 30,              # 1 month
    "transient_bug": 14,      # 2 weeks
    "default": 60,            # 2 months default
}

def compute_confidence_decay(confidence_base, last_confirmed_date, tags, today=None):
    """Apply time-based confidence decay. Returns updated confidence string."""
    from datetime import datetime, date
    if today is None:
        today = date.today()
    if isinstance(last_confirmed_date, str):
        # Strip comments and extra text from date strings
        if isinstance(last_confirmed_date, str):
            last_confirmed_date = last_confirmed_date.split("#")[0].strip().strip("'").strip('"').strip()
        last_confirmed_date = datetime.strptime(last_confirmed_date, "%Y-%m-%d").date()
    
    days_since = (today - last_confirmed_date).days
    # Find decay rate from tags
    rate = CONFIDENCE_DECAY_RATES.get("default")
    for tag in (tags or []):
        if tag in CONFIDENCE_DECAY_RATES:
            rate = CONFIDENCE_DECAY_RATES[tag]
            break
    
    # Confidence value mapping
    conf_map = {"high": 0.9, "medium": 0.6, "low": 0.3}
    rev_map = {0.8: "high", 0.55: "medium", 0.25: "low"}
    base_val = conf_map.get(confidence_base, 0.6)
    decayed = base_val * (1 - rate) ** days_since
    
    # Map back to nearest tier
    if decayed >= 0.8:
        return "high"
    elif decayed >= 0.55:
        return "medium"
    else:
        return "low"


def should_deprioritize(last_confirmed_date, tags, today=None):
    """Check if content should be deprioritized (Ebbinghaus forgetting)."""
    from datetime import datetime, date
    if today is None:
        today = date.today()
    if isinstance(last_confirmed_date, str):
        # Strip comments and extra text from date strings
        if isinstance(last_confirmed_date, str):
            last_confirmed_date = last_confirmed_date.split("#")[0].strip().strip("'").strip('"').strip()
        last_confirmed_date = datetime.strptime(last_confirmed_date, "%Y-%m-%d").date()
    
    days_since = (today - last_confirmed_date).days
    threshold = DAYS_UNTIL_DEPRIORITIZE.get("default")
    for tag in (tags or []):
        if tag in DAYS_UNTIL_DEPRIORITIZE:
            threshold = DAYS_UNTIL_DEPRIORITIZE[tag]
            break
    
    return days_since > threshold


# ---------------------------------------------------------------------------
# Parse helpers
# ---------------------------------------------------------------------------

def parse_frontmatter(text):
    """Parse YAML-like frontmatter. Returns (dict, body)."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return {}, text
    header = {}
    for line in lines[1:end_idx]:
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip().strip('"').strip("'") for v in value[1:-1].split(",")]
            header[key] = [v for v in items if v]
        elif (value.startswith('"') and value.endswith('"')) or \
             (value.startswith("'") and value.endswith("'")):
            header[key] = value[1:-1]
        else:
            header[key] = value
    body = "\n".join(lines[end_idx + 1:])
    return header, body


def find_wikilinks(text):
    """Find all [[wikilink]] references. Returns list of slugs (stripped of aliases and fragments)."""
    raw = re.findall(r"\[\[([^\]]+)\]\]", text)
    slugs = []
    for link in raw:
        slug = link.split("|")[0].strip()  # Strip alias
        slug = slug.split("#")[0].strip()  # Strip fragment
        slug = slug.rstrip("\\").strip()  # Strip table escape
        if slug and "/" not in slug:
            slugs.append(slug)
    return slugs


def slugify(text):
    """Convert text to wiki-safe slug."""
    return re.sub(r"[^a-z0-9-]+", "-", text.lower()).strip("-")


# ---------------------------------------------------------------------------
# Manifest operations
# ---------------------------------------------------------------------------

def load_manifest():
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH) as f:
            return json.load(f)
    return {"version": 1, "updated": datetime.date.today().isoformat(), "sources": {}}


def save_manifest(manifest):
    manifest["updated"] = datetime.date.today().isoformat()
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))


def register_compiled_concept(slug, source_key=None, confidence="medium", tags=None):
    """Helper for LLM agents: mark a concept as compiled."""
    manifest = load_manifest()
    now = datetime.date.today().isoformat()
    
    if source_key:
        if source_key in manifest.get("sources", {}):
            manifest["sources"][source_key]["status"] = "compiled"
            manifest["sources"][source_key]["compiled_at"] = now
        manifest["sources"][f"concepts/{slug}"] = {
            "type": "concept",
            "status": "compiled",
            "compiled_at": now,
            "confidence": confidence,
            "last_linted": now,
            "tags": tags or [],
        }
    else:
        manifest["sources"][f"concepts/{slug}"] = {
            "type": "concept",
            "status": "compiled",
            "compiled_at": now,
            "confidence": confidence,
            "last_linted": now,
            "tags": tags or [],
        }
    
    save_manifest(manifest)
    return f"Registered: concepts/{slug} (confidence: {confidence})"


# ---------------------------------------------------------------------------
# Phase 1: FETCH — Scan raw/ for new sources
# ---------------------------------------------------------------------------

def phase_fetch(dry_run=False, verbose=False):
    """Scan raw/ directories and MANIFEST to identify work needed."""
    if verbose:
        print("\n" + "="*60)
        print("PHASE 1: FETCH — Discovering raw sources")
        print("="*60)
    
    manifest = load_manifest()
    worklist = []
    
    if not RAW_DIR.exists():
        print(f"raw/ directory not found at {RAW_DIR}")
        return {"status": "no_raw_dir", "worklist": [], "manifest": manifest}
    
    # Scan all raw subdirectories
    for type_dir in sorted(RAW_DIR.iterdir()):
        if not type_dir.is_dir():
            continue
        
        for source_file in sorted(type_dir.glob("*.md")):
            relative_path = f"raw/{type_dir.name}/{source_file.name}"
            
            if relative_path not in manifest.get("sources", {}):
                worklist.append({
                    "path": str(source_file),
                    "relative": relative_path,
                    "type": type_dir.name,
                    "action": "needs_compilation",
                    "status": "unprocessed"
                })
    
    if dry_run:
        return {
            "status": "dry_run",
            "worklist": worklist,
            "manifest": manifest,
            "message": f"Would discover {len(worklist)} unprocessed sources"
        }
    
    # Update manifest with newly discovered sources
    for item in worklist:
        manifest.setdefault("sources", {})[item["relative"]] = {
            "type": "raw",
            "status": "unprocessed",
            "discovered_at": datetime.date.today().isoformat()
        }
    save_manifest(manifest)
    
    print(f"FETCH complete: {len(worklist)} sources to process")
    for item in worklist:
        print(f"  → {item['relative']} ({item['type']})")
    
    return {"status": "complete", "worklist": worklist, "manifest": manifest}


# ---------------------------------------------------------------------------
# Phase 2: COMPILE — Identify unprocessed sources for LLM
# ---------------------------------------------------------------------------

def phase_compile(dry_run=False, verbose=False):
    """Identify sources not yet compiled. LLM processes them."""
    if verbose:
        print("\n" + "="*60)
        print("PHASE 2: COMPILE — Sources ready for LLM processing")
        print("="*60)
    
    manifest = load_manifest()
    uncompiled = []
    
    for source_key, source_data in manifest.get("sources", {}).items():
        if source_data.get("status") in ("unprocessed", "pending_fetch"):
            uncompiled.append({
                "source": source_key,
                "type": source_data.get("type", "unknown"),
                "status": source_data.get("status", "unknown"),
                "discovered": source_data.get("discovered_at", "unknown")
            })
    
    # Also check concepts for stubs (frontmatter only, no body content)
    stub_concepts = []
    if CONCEPTS_DIR.exists():
        for concept_file in sorted(CONCEPTS_DIR.glob("*.md")):
            with open(concept_file) as f:
                content = f.read()
            fm, body = parse_frontmatter(content)
            if not body.strip():
                stub_concepts.append(concept_file.stem)
    
    if dry_run:
        return {
            "status": "dry_run",
            "uncompiled_sources": uncompiled,
            "stub_concepts": stub_concepts,
            "message": f"{len(uncompiled)} uncompiled sources, {len(stub_concepts)} stub concepts"
        }
    
    print(f"COMPILE complete: {len(uncompiled)} uncompiled sources, {len(stub_concepts)} stubs")
    if uncompiled:
        print("\nUncompiled sources:")
        for s in uncompiled:
            print(f"  ❌ {s['source']} ({s['type']})")
    if stub_concepts:
        print("\nStub concepts (need content):")
        for slug in stub_concepts:
            print(f"  📝 {slug}")
    
    return {
        "status": "complete",
        "uncompiled_sources": uncompiled,
        "stub_concepts": stub_concepts
    }


# ---------------------------------------------------------------------------
# Phase 3: MAINTAIN — Lint and validate
# ---------------------------------------------------------------------------

def phase_maintain(dry_run=False, verbose=False):
    """Run maintenance checks on ALL wiki pages (sources, concepts, synthesis)."""
    if verbose:
        print("\n" + "="*60)
        print("PHASE 3: MAINTAIN — Validating wiki integrity")
        print("="*60)

    issues = []
    pages = {}  # slug -> {frontmatter, body, path, links, subdir}

    # PASS 1: Load ALL pages from all directories
    for subdir in ['sources', 'concepts', 'synthesis']:
        dir_path = WIKI_ROOT / "wiki" / subdir
        if not dir_path.exists():
            continue
        for page_file in sorted(dir_path.glob("*.md")):
            slug = page_file.stem
            with open(page_file) as f:
                content = f.read()
            fm, body = parse_frontmatter(content)
            links = find_wikilinks(body)
            # Also find wikilinks in frontmatter (sources: list)
            fm_links = find_wikilinks(str(fm))
            all_links = list(set(links + fm_links))
            pages[slug] = {
                "frontmatter": fm,
                "body": body,
                "path": str(page_file),
                "links": all_links,
                "subdir": subdir
            }

    all_slugs = set(pages.keys())

    # PASS 2: Check all pages against complete slug set

    # 1. Schema validation
    required_fields = ["title", "tags", "confidence", "priority", "status", "summary"]
    for slug, data in pages.items():
        fm = data["frontmatter"]
        for field in required_fields:
            if field not in fm:
                issues.append({
                    "type": "schema_violation",
                    "slug": slug,
                    "detail": f"Missing required field: {field}"
                })

    # 2. Source pages must have source_url
    for slug, data in pages.items():
        if data["subdir"] == "sources":
            fm = data["frontmatter"]
            if "source_url" not in fm:
                issues.append({
                    "type": "missing_source_url",
                    "slug": slug,
                    "detail": "Source page missing source_url in frontmatter"
                })

    # 3. Controlled vocabulary check (concepts only)
    for slug, data in pages.items():
        if data["subdir"] != "concepts":
            continue
        fm = data["frontmatter"]
        tags = fm.get("tags", [])
        invalid = [t for t in tags if t not in VALID_TAGS]
        if invalid:
            issues.append({
                "type": "invalid_tags",
                "slug": slug,
                "detail": f"Invalid tags: {invalid}"
            })

    # 4. Dead wikilinks (TWO-PASS: check against ALL slugs from ALL directories)
    for slug, data in pages.items():
        for link in data["links"]:
            # Strip fragment and trailing backslash
            clean = link.rstrip("\\").strip()
            if "#" in clean:
                clean = clean.split("#")[0].strip()
            if clean and clean not in all_slugs and "/" not in clean:
                issues.append({
                    "type": "dead_wikilink",
                    "slug": slug,
                    "detail": f"Links to non-existent page: {clean}"
                })

    # 5. Orphan detection (pages with 0 inbound links)
    is_linked_to = set()
    for slug, data in pages.items():
        for link in data["links"]:
            clean = link.rstrip("\\").strip()
            if "#" in clean:
                clean = clean.split("#")[0].strip()
            if clean:
                is_linked_to.add(clean)
    
    exceptions = {"index", "RESOLVER", "log", "MANIFEST", "overview", "README", "SCHEMA"}
    for slug in pages:
        if slug not in is_linked_to and slug not in exceptions:
            issues.append({
                "type": "orphan",
                "slug": slug,
                "detail": f"No inbound links ({pages[slug]['subdir']})"
            })

    # 6. Empty body detection (concepts only)
    for slug, data in pages.items():
        if data["subdir"] == "concepts" and not data["body"].strip():
            issues.append({
                "type": "empty_body",
                "slug": slug,
                "detail": "Concept has no body content (stub only)"
            })

    # 7. Confidence decay + forgetting (LLM Wiki v2)
    for slug, data in pages.items():
        fm = data["frontmatter"]
        updated = fm.get("updated")
        confidence = fm.get("confidence", "medium")
        tags = fm.get("tags", [])

        if updated:
            decayed_confidence = compute_confidence_decay(confidence, updated, tags)
            if decayed_confidence != confidence:
                issues.append({
                    "type": "confidence_decayed",
                    "slug": slug,
                    "detail": f"Confidence {confidence} -> {decayed_confidence} (stale since {updated})",
                    "suggested_confidence": decayed_confidence
                })

            if should_deprioritize(updated, tags):
                issues.append({
                    "type": "should_deprioritize",
                    "slug": slug,
                    "detail": f"Past forgetting threshold (last updated {updated})",
                    "tags": tags
                })

    # 8. Supersession check
    supersession_map = {}
    for slug, data in pages.items():
        fm = data["frontmatter"]
        superseded_by = fm.get("superseded_by")
        if superseded_by:
            supersession_map[slug] = superseded_by

    for slug, new_slug in supersession_map.items():
        if new_slug in pages:
            if slug not in pages[slug].get("body", ""):
                issues.append({
                    "type": "supersession_missing_link",
                    "slug": slug,
                    "detail": f"Marked superseded by {new_slug} but no wikilink present"
                })

    # Update manifest
    manifest = load_manifest()
    for slug in pages:
        source_key = f"{pages[slug]['subdir']}/{slug}"
        if source_key in manifest.get("sources", {}):
            manifest["sources"][source_key]["last_linted"] = datetime.date.today().isoformat()
    save_manifest(manifest)

    if dry_run:
        return {"status": "dry_run", "issues": issues, "pages_checked": len(pages)}

    # Summary
    issue_types = {}
    for issue in issues:
        issue_types[issue["type"]] = issue_types.get(issue["type"], 0) + 1
    
    print(f"MAINTAIN complete: {len(pages)} pages checked, {len(issues)} issues found")
    for itype, count in sorted(issue_types.items()):
        emoji = {"schema_violation": "❌", "missing_source_url": "⚠️", 
                 "invalid_tags": "⚠️", "dead_wikilink": "🔗",
                 "orphan": "📄", "empty_body": "📝",
                 "confidence_decayed": "⏰", "should_deprioritize": " Archives"}
        bullet = '\u2022'
        print(f"  {emoji.get(itype, bullet)} {count}x {itype}")

    return {"status": "complete", "issues": issues, "pages_checked": len(pages)}

def phase_synthesize(dry_run=False, verbose=False):
    """Find overlapping concepts that should be merged."""
    if verbose:
        print("\n" + "="*60)
        print("PHASE 4: SYNTHESIZE — Finding merge candidates")
        print("="*60)
    
    concepts = {}
    if CONCEPTS_DIR.exists():
        for concept_file in sorted(CONCEPTS_DIR.glob("*.md")):
            slug = concept_file.stem
            with open(concept_file) as f:
                content = f.read()
            fm, body = parse_frontmatter(content)
            concepts[slug] = {
                "frontmatter": fm,
                "body": body,
                "tags": set(fm.get("tags", [])),
                "links": set(find_wikilinks(body)),
                "summary_words": set(fm.get("summary", "").lower().split())
            }
    
    candidates = []
    slugs = list(concepts.keys())
    
    for i, s1 in enumerate(slugs):
        for s2 in slugs[i+1:]:
            # Calculate overlap scores
            tag_overlap = len(concepts[s1]["tags"] & concepts[s2]["tags"])
            link_overlap = len(concepts[s1]["links"] & concepts[s2]["links"])
            word_overlap = len(concepts[s1]["summary_words"] & concepts[s2]["summary_words"])
            
            # Weight: tags > links > summary words
            score = (tag_overlap * 3 + link_overlap * 2 + word_overlap)
            
            if score >= 4:  # Threshold for suggestion
                candidates.append({
                    "concept_1": s1,
                    "concept_2": s2,
                    "score": score,
                    "shared_tags": list(concepts[s1]["tags"] & concepts[s2]["tags"]),
                    "shared_links": list(concepts[s1]["links"] & concepts[s2]["links"]),
                    "shared_words": len(concepts[s1]["summary_words"] & concepts[s2]["summary_words"])
                })
    
    candidates.sort(key=lambda x: x["score"], reverse=True)
    
    if dry_run:
        return {"status": "dry_run", "candidates": candidates}
    
    print(f"SYNTHESIZE complete: {len(candidates)} merge candidates found")
    for c in candidates:
        print(f"  🔀 {c['concept_1']} + {c['concept_2']} (score: {c['score']})")
        if c['shared_tags']:
            print(f"     Shared tags: {c['shared_tags']}")
    
    return {"status": "complete", "candidates": candidates}


def merge_concepts(keep_slug, merge_slug, manifest=None):
    """Helper for LLM agents: merge one concept into another."""
    if manifest is None:
        manifest = load_manifest()
    
    # Remove merged concept
    merge_path = CONCEPTS_DIR / f"{merge_slug}.md"
    if merge_path.exists():
        merge_path.unlink()
    
    # Update manifest
    merge_key = f"concepts/{merge_slug}"
    if merge_key in manifest.get("sources", {}):
        manifest["sources"][merge_key]["status"] = "merged_into_keep"
    
    save_manifest(manifest)
    return f"Merged {merge_slug} into {keep_slug}"


# ---------------------------------------------------------------------------
# Phase 5: FINALIZE — Regenerate artifacts
# ---------------------------------------------------------------------------

def phase_finalize(dry_run=False, verbose=False):
    """Regenerate index.md, Mermaid graph, and update logs."""
    if verbose:
        print("\n" + "="*60)
        print("PHASE 5: FINALIZE — Regenerating artifacts")
        print("="*60)
    
    now = datetime.date.today().isoformat()
    concepts = {}
    
    # Load all concepts
    if CONCEPTS_DIR.exists():
        for concept_file in sorted(CONCEPTS_DIR.glob("*.md")):
            slug = concept_file.stem
            with open(concept_file) as f:
                content = f.read()
            fm, body = parse_frontmatter(content)
            links = find_wikilinks(body)
            concepts[slug] = {
                "frontmatter": fm,
                "body": body,
                "links": links
            }
    
    # 1. Regenerate index.md
    domain_groups = defaultdict(list)
    for slug, data in concepts.items():
        fm = data["frontmatter"]
        tags = fm.get("tags", [])
        # Find first valid domain tag
        domain = None
        for tag in tags:
            if tag in VALID_DOMAINS:
                domain = tag
                break
        if not domain:
            domain = "uncategorized"
        
        domain_groups[domain].append((slug, fm.get("title", slug), fm.get("summary", "")))
    
    index_lines = [
        "---",
        f'title: "Wiki Index"',
        f'updated: "{now}"',
        "---",
        "",
        "# C0ldbrain Wiki - Master Index",
        "",
    ]
    
    for domain in sorted(domain_groups.keys()):
        index_lines.append(f"## {domain.title().replace('-', ' ')}")
        index_lines.append("")
        for slug, title, summary in domain_groups[domain]:
            index_lines.append(f"- [[{slug}]] — {summary}")
        index_lines.append("")
    
    # Stats
    index_lines.extend([
        "## Stats",
        f"- Total concepts: {len(concepts)}",
        f"- Domains covered: {len(domain_groups)}",
        f"- Last compiled: {now}",
        ""
    ])
    
    INDEX_PATH.write_text("\n".join(index_lines))
    
    # 2. Generate Mermaid graph
    MERMAID_DIR.mkdir(parents=True, exist_ok=True)
    
    # Color by domain
    domain_colors = {
        "ai-agents": "#4CAF50",
        "ml-models": "#2196F3",
        "crypto-quant": "#FF9800",
        "devops": "#9C27B0",
        "security": "#F44336",
        "infrastructure": "#607D8B",
    }
    
    graph_lines = ["graph TD"]
    graph_lines.append("    classDef security fill:#F44336,stroke:#fff,stroke-width:2px")
    graph_lines.append("    classDef ai_agents fill:#4CAF50,stroke:#fff,stroke-width:2px")
    graph_lines.append("    classDef ml_models fill:#2196F3,stroke:#fff,stroke-width:2px")
    graph_lines.append("    classDef crypto_quant fill:#FF9800,stroke:#fff,stroke-width:2px")
    graph_lines.append("    classDef devops fill:#9C27B0,stroke:#fff,stroke-width:2px")
    graph_lines.append("    classDef infrastructure fill:#607D8B,stroke:#fff,stroke-width:2px")
    graph_lines.append("    classDef uncategorized fill:#E0E0E0,stroke:#fff,stroke-width:2px")
    
    for slug, data in concepts.items():
        fm = data["frontmatter"]
        title = fm.get("title", slug).replace('"', '\\"')
        
        # Find domain
        domain = "uncategorized"
        for tag in fm.get("tags", []):
            if tag in VALID_DOMAINS:
                domain = tag
                break
        
        class_name = domain.replace("-", "_")
        node_id = slug.replace("-", "_")
        graph_lines.append(f'    {node_id}["{title}"]:::{class_name}')
    
    # Add links
    added_links = set()
    for slug, data in concepts.items():
        node_id = slug.replace("-", "_")
        for link in data["links"]:
            link_id = link.replace("-", "_")
            link_key = f"{node_id} --> {link_id}"
            if link_key not in added_links:
                graph_lines.append(f"    {node_id} --> {link_id}")
                added_links.add(link_key)
    
    graph_path = MERMAID_DIR / "wiki-graph.mmd"
    graph_path.write_text("\n".join(graph_lines))
    
    # 3. Update log
    log_entry = f"| {now} | Compile | Processed {len(concepts)} concepts, {len(domain_groups)} domains |\n"
    if LOG_PATH.exists():
        current_log = LOG_PATH.read_text()
        if log_entry.strip() not in current_log:
            LOG_PATH.write_text(current_log + log_entry)
    else:
        LOG_PATH.write_text(
            "---\ntitle: 'Wiki Change Log'\n---\n\n# Wiki Activity Log\n\n| Date | Action | Details |\n|------|--------|-------- |\n" + log_entry
        )
    
    # 4. Update manifest
    manifest = load_manifest()
    manifest["last_compile"] = now
    manifest["concept_count"] = len(concepts)
    save_manifest(manifest)
    
    if dry_run:
        return {
            "status": "dry_run",
            "concepts": len(concepts),
            "domains": len(domain_groups),
            "links": len(added_links)
        }
    
    print(f"FINALIZE complete:")
    print(f"  📊 index.md updated ({len(concepts)} concepts, {len(domain_groups)} domains)")
    print(f"  🕸️  wiki-graph.mmd generated ({len(added_links)} links)")
    print(f"  📝 log.md updated")
    print(f"  📦 MANIFEST.json updated")
    
    return {
        "status": "complete",
        "concepts": len(concepts),
        "domains": len(domain_groups),
        "links": len(added_links)
    }


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------

def run_all_phases(dry_run=False, verbose=False):
    """Run all 5 phases in sequence."""
    results = {}
    
    phases = {
        "fetch": phase_fetch,
        "compile": phase_compile,
        "maintain": phase_maintain,
        "synthesize": phase_synthesize,
        "finalize": phase_finalize,
    }
    
    for phase_name, phase_func in phases.items():
        if verbose:
            print(f"\n{'='*60}")
            print(f"Running phase: {phase_name.upper()}")
            print(f"{'='*60}")
        
        results[phase_name] = phase_func(dry_run=dry_run, verbose=verbose)
        
        if dry_run:
            print(f"  [DRY RUN] {phase_name}: {results[phase_name].get('message', 'OK')}")
    
    return results


def main():
    parser = argparse.ArgumentParser(description="C0ldbrain Wiki 5-Phase Compiler")
    parser.add_argument("--phases", nargs="+", help="Specific phases to run (default: all)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen")
    parser.add_argument("--verbose", action="store_true", help="Detailed output")
    args = parser.parse_args()
    
    all_phases = {
        "fetch": phase_fetch,
        "compile": phase_compile,
        "maintain": phase_maintain,
        "synthesize": phase_synthesize,
        "finalize": phase_finalize,
    }
    
    phases_to_run = {}
    phase_names = args.phases or list(all_phases.keys())
    
    for name in phase_names:
        if name in all_phases:
            phases_to_run[name] = all_phases[name]
        else:
            print(f"Warning: Unknown phase '{name}', skipping")
    
    print(f"C0ldbrain Wiki Compiler — Running phases: {', '.join(phases_to_run.keys())}")
    if args.dry_run:
        print("[DRY RUN MODE]")
    print()
    
    results = {}
    for phase_name, phase_func in phases_to_run.items():
        results[phase_name] = phase_func(dry_run=args.dry_run, verbose=args.verbose)
        
        if args.dry_run:
            msg = results[phase_name].get('message', 'OK')
            print(f"  [DRY RUN] {phase_name}: {msg}")
    
    if args.dry_run:
        print(f"\nDry run complete. {len(phases_to_run)} phases checked.")
    else:
        print(f"\nCompile complete! {len(phases_to_run)} phases executed.")


if __name__ == "__main__":
    main()
