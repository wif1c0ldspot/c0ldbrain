#!/usr/bin/env python3
"""synthesis_engine.py — Detect tag clusters missing synthesis handbooks and generate them."""
import os, re, sys, argparse, json
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from wiki_config import WIKI_ROOT

WIKI_DIR = WIKI_ROOT / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
CONCEPTS_DIR = WIKI_DIR / "concepts"
SYNTHESIS_DIR = WIKI_DIR / "synthesis"
MANIFEST_PATH = WIKI_ROOT / "MANIFEST.json"

WIKILINK_RE = re.compile(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]')
SOURCE_TYPE_TAGS = {'source', 'github', 'arxiv', 'article', 'social', 'x', 'paper', 'gist', 'synthesis', 'concept', 'daily-research'}

def read_safe(path):
    try: return path.read_text(encoding='utf-8')
    except (IOError, OSError): return None

def write_safe(path, content):
    try: path.write_text(content, encoding='utf-8'); return True
    except (IOError, OSError): return False

def parse_tags(fm_text):
    tags = []
    m = re.search(r'tags:\s*\n((?:- .+\n)*)', fm_text)
    if m:
        for line in m.group(1).strip().split('\n'):
            t = line.strip().lstrip('-').strip()
            if t: tags.append(t)
    else:
        m2 = re.search(r'tags:\s*\[(.*?)\]', fm_text)
        if m2:
            tags = [t.strip().strip("'\"") for t in m2.group(1).split(',') if t.strip()]
    return tags

def parse_frontmatter(content):
    if not content.startswith('---'): return {}, content
    fm_end = content.find('---', 3)
    if fm_end == -1: return {}, content
    fm_text = content[3:fm_end]
    body = content[fm_end+3:].strip()
    return fm_text, body

def get_existing_handbook_tags():
    """Get tags covered by existing synthesis handbooks."""
    covered = set()
    if not SYNTHESIS_DIR.exists(): return covered
    for f in SYNTHESIS_DIR.glob("*.md"):
        text = read_safe(f)
        if text is None: continue
        fm_text, body = parse_frontmatter(text)
        tags = parse_tags(fm_text)
        for t in tags:
            if t not in SOURCE_TYPE_TAGS:
                covered.add(t)
    return covered

def get_tag_clusters():
    """Build tag -> [(slug, title, body_len)] mapping for concepts."""
    clusters = defaultdict(list)
    if not CONCEPTS_DIR.exists(): return clusters
    for f in sorted(CONCEPTS_DIR.glob("*.md")):
        text = read_safe(f)
        if text is None: continue
        fm_text, body = parse_frontmatter(text)
        slug = f.stem
        title_match = re.search(r'title:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)
        title = title_match.group(1) if title_match else slug
        tags = parse_tags(fm_text)
        for t in tags:
            if t not in SOURCE_TYPE_TAGS:
                clusters[t].append((slug, title, len(body)))
    return clusters

def detect_gaps(min_concepts=8):
    """Find tag clusters with enough concepts but no synthesis handbook."""
    clusters = get_tag_clusters()
    covered = get_existing_handbook_tags()
    gaps = []
    for tag, pages in sorted(clusters.items(), key=lambda x: -len(x[1])):
        if tag in covered: continue
        if len(pages) >= min_concepts:
            gaps.append((tag, len(pages), pages))
    return gaps

def generate_handbook(tag, concept_pages, dry_run=False):
    """Generate a synthesis handbook from concept pages."""
    tag_title = tag.replace('-', ' ').title()
    today = os.popen('date +%Y-%m-%d').read().strip()
    
    # Read concept bodies to extract key themes
    all_bullets = []
    all_links = set()
    concept_summaries = []
    source_refs = set()
    
    for slug, title, _ in concept_pages:
        fpath = CONCEPTS_DIR / f"{slug}.md"
        text = read_safe(fpath)
        if text is None: continue
        fm_text, body = parse_frontmatter(text)
        
        # Extract first meaningful sentence
        lines = body.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 30 and not line.startswith('#') and not line.startswith('-') and not line.startswith('['):
                concept_summaries.append(f"**{title}**: {line[:150]}")
                break
        
        # Extract key bullets
        for line in lines:
            line = line.strip()
            if line.startswith('- ') and 20 < len(line) < 200:
                all_bullets.append(line[2:])
        
        # Extract linked sources
        for m in WIKILINK_RE.finditer(body):
            target = m.group(1).strip()
            if target != slug:
                all_links.add(target)
                if os.path.exists(SOURCES_DIR / f"{target}.md"):
                    source_refs.add(target)
    
    # Build handbook content
    concepts_section = '\n'.join(f'- [[{slug}]] — {title}' for slug, title, _ in concept_pages)
    themes = '\n'.join(f'- {b[:120]}' for b in all_bullets[:15])
    sources_section = '\n'.join(f'- [[{s}]]' for s in sorted(source_refs)[:15])
    
    handbook = f"""---
title: "{tag_title} Handbook"
type: synthesis
tags:
- synthesis
- {tag}
sources:
{chr(10).join('- ' + slug for slug, _, _ in concept_pages)}
created: '{today}'
updated: '{today}'
confidence: high
status: current
priority: important
summary: "Synthesis handbook covering {len(concept_pages)} concepts in the {tag} domain."
---

# {tag_title} Handbook

Synthesized from {len(concept_pages)} concept pages in the **{tag}** domain.

## Overview

This handbook consolidates key knowledge about {tag_title}, drawing from multiple sources and concepts in the C0ldbrain wiki.

## Core Concepts

{concepts_section}

## Key Themes

{themes}

## Open Questions

- What emerging patterns in {tag_title} are not yet captured?
- How do these concepts interconnect with adjacent domains?

## Sources

{sources_section}
"""
    
    slug = f"{tag}-handbook-2026"
    outpath = SYNTHESIS_DIR / f"{slug}.md"
    
    if dry_run:
        print(f"  Would create: {outpath} ({len(handbook)} chars)")
        return slug
    
    SYNTHESIS_DIR.mkdir(parents=True, exist_ok=True)
    if write_safe(outpath, handbook):
        print(f"  Created: {outpath}")
        # Update MANIFEST
        try:
            manifest = json.load(open(MANIFEST_PATH))
            manifest["sources"][f"synthesis/{slug}"] = {
                "type": "synthesis", "status": "compiled",
                "ingested_at": today, "compiled_at": today,
                "source_page": f"wiki/synthesis/{slug}.md"
            }
            manifest["synthesis_count"] = len(list(SYNTHESIS_DIR.glob("*.md")))
            manifest["last_compile"] = today
            with open(MANIFEST_PATH, 'w') as f:
                json.dump(manifest, f, indent=2)
        except Exception as e:
            print(f"  WARN: MANIFEST update failed: {e}")
        return slug
    return None

def main():
    parser = argparse.ArgumentParser(description="Synthesis gap detector and handbook generator.")
    parser.add_argument("--scan", action="store_true", help="Detect gaps only")
    parser.add_argument("--generate", action="store_true", help="Generate top gap")
    parser.add_argument("--auto", action="store_true", help="Generate up to max_new handbooks")
    parser.add_argument("--max-new", type=int, default=2)
    parser.add_argument("--min-concepts", type=int, default=8)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    
    if not (args.scan or args.generate or args.auto):
        parser.print_help(); sys.exit(1)
    
    print(f"Wiki: {WIKI_DIR}")
    gaps = detect_gaps(args.min_concepts)
    
    print(f"\n=== Synthesis Gaps (>{args.min_concepts} concepts, no handbook) ===\n")
    if not gaps:
        print("  No gaps found — all clusters covered!")
        return
    
    for tag, count, pages in gaps:
        print(f"  {tag}: {count} concepts")
        for slug, title, blen in pages[:3]:
            print(f"    - [[{slug}]] ({blen} chars)")
        if len(pages) > 3:
            print(f"    ... +{len(pages)-3} more")
    
    if args.scan: return
    
    # Generate handbooks
    to_generate = gaps[:args.max_new]
    created = []
    for tag, count, pages in to_generate:
        print(f"\nGenerating handbook for '{tag}' ({count} concepts)...")
        slug = generate_handbook(tag, pages, args.dry_run)
        if slug: created.append(slug)
    
    print(f"\n{'Would create' if args.dry_run else 'Created'} {len(created)} handbook(s)")

if __name__ == "__main__":
    main()
