#!/usr/bin/env python3
"""
Lifecycle Condense Script

Interactively condenses verbose wiki pages by extracting enduring patterns
and removing temporal specifics.

Usage:
    python3 lifecycle_condense.py [--slug SLUG] [--dry-run] [--auto]

With --slug: condense specific page
Without --slug: process all condense candidates from lifecycle report
"""

import os
import re
import json
import yaml
import argparse
from pathlib import Path
from datetime import datetime

import wiki_config
WIKI_ROOT = wiki_config.WIKI_ROOT
LIFECYCLE_REPORT = wiki_config.LIFECYCLE_REPORT


def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if content.startswith('---'):
        try:
            parts = content.split('---', 2)
            if len(parts) >= 3:
                fm = yaml.safe_load(parts[1])
                body = parts[2]
                return fm if fm else {}, body
        except:
            pass
    return {}, content


def build_condensed_frontmatter(original_fm, original_word_count, new_word_count):
    """Build updated frontmatter with condensation metadata."""
    fm = dict(original_fm)
    
    # Update basic fields
    fm['updated'] = datetime.now().strftime('%Y-%m-%d')
    
    # Add/update lifecycle tracking
    if 'lifecycle' not in fm:
        fm['lifecycle'] = {}
    
    fm['lifecycle']['condensed'] = datetime.now().strftime('%Y-%m-%d')
    fm['lifecycle']['original_word_count'] = original_word_count
    fm['lifecycle']['condensed_word_count'] = new_word_count
    fm['lifecycle']['compression_ratio'] = round(new_word_count / original_word_count, 2)
    
    return fm


def condense_content(content, strategy='extract_patterns'):
    """
    Condense content by removing temporal specifics and extracting patterns.
    
    Strategies:
    - extract_patterns: Keep principles/patterns, remove examples/dates
    - remove_fluff: Remove redundant sentences, filler
    - synthesize: Compress multiple paragraphs to key points
    """
    frontmatter, body = parse_frontmatter(content)
    original_word_count = len(body.split())
    
    lines = body.split('\n')
    condensed_lines = []
    in_example_block = False
    
    for line in lines:
        stripped = line.strip()
        
        # Skip empty lines at start/end
        if not stripped and not condensed_lines:
            continue
            
        # Handle code blocks (keep but mark)
        if stripped.startswith('```'):
            in_example_block = not in_example_block
            condensed_lines.append(line)
            continue
            
        if in_example_block:
            # Keep code blocks but consider them for removal if too long
            condensed_lines.append(line)
            continue
        
        # Remove specific dates (keep year only)
        line = re.sub(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+(20\d{2})', r'\2', line)
        line = re.sub(r'(20\d{2})[-/](0[1-9]|1[0-2])[-/](0[1-9]|[12]\d|3[01])', r'\1', line)
        
        # Remove version-specific statements
        line = re.sub(r'\bversion\s+\d+\.\d+(?:\.\d+)?\b', 'the current version', line, flags=re.IGNORECASE)
        
        # Remove filler phrases
        fillers = [
            r'\bIt is important to note that\b',
            r'\bIt should be noted that\b',
            r'\bAs mentioned earlier\b',
            r'\bAs you may know\b',
            r'\bIn my opinion\b',
            r'\bI think that\b',
            r'\bBasically\b',
            r'\bEssentially\b',
            r'\bAt the end of the day\b',
            r'\bThe fact of the matter is\b',
        ]
        for filler in fillers:
            line = re.sub(filler, '', line, flags=re.IGNORECASE)
        
        # Clean up double spaces
        line = re.sub(r'  +', ' ', line)
        
        if stripped:  # Only add non-empty lines
            condensed_lines.append(line)
    
    # Remove trailing empty lines
    while condensed_lines and not condensed_lines[-1].strip():
        condensed_lines.pop()
    
    condensed_body = '\n'.join(condensed_lines)
    new_word_count = len(condensed_body.split())
    
    # Build new frontmatter
    new_fm = build_condensed_frontmatter(frontmatter, original_word_count, new_word_count)
    
    # Reconstruct document
    fm_yaml = yaml.dump(new_fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    new_content = f"---\n{fm_yaml}---\n{condensed_body}\n"
    
    return new_content, original_word_count, new_word_count


def condense_page(filepath, dry_run=True, auto=False):
    """Condense a single wiki page."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"   ❌ Error reading {filepath}: {e}")
        return False
    
    frontmatter, body = parse_frontmatter(content)
    original_word_count = len(body.split())
    
    if original_word_count < 500:
        print(f"   ⚠️  {filepath.stem}: Too short to condense ({original_word_count} words)")
        return False
    
    print(f"   📝 {filepath.stem}: {original_word_count} words → condensing...")
    
    new_content, orig, new = condense_content(content)
    reduction = (1 - new/orig) * 100
    
    print(f"      Result: {orig} → {new} words ({reduction:.1f}% reduction)")
    
    if dry_run:
        print(f"      (dry-run: not saved)")
        return True
    
    if not auto:
        response = input(f"      Save changes? [y/N]: ").strip().lower()
        if response != 'y':
            print(f"      Skipped")
            return False
    
    # Backup original
    backup_path = filepath.with_suffix('.md.backup')
    filepath.rename(backup_path)
    
    # Write condensed version
    filepath.write_text(new_content, encoding='utf-8')
    
    print(f"      ✅ Saved (backup: {backup_path.name})")
    return True


def main():
    parser = argparse.ArgumentParser(description='Condense wiki pages')
    parser.add_argument('--slug', help='Specific page slug to condense')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done')
    parser.add_argument('--auto', action='store_true', help='Auto-approve without prompting')
    args = parser.parse_args()
    
    if args.slug:
        # Condense specific page
        for subdir in ['concepts', 'sources']:
            filepath = Path(WIKI_ROOT) / 'wiki' / subdir / f"{args.slug}.md"
            if filepath.exists():
                condense_page(filepath, dry_run=args.dry_run, auto=args.auto)
                return
        print(f"❌ Page not found: {args.slug}")
        return
    
    # Process candidates from report
    if not LIFECYCLE_REPORT.exists():
        print(f"❌ No lifecycle report found. Run lifecycle_detect.py first.")
        return
    
    with open(LIFECYCLE_REPORT) as f:
        report = json.load(f)
    
    candidates = report['candidates']['condense']
    
    if not candidates:
        print("✅ No condense candidates found.")
        return
    
    print(f"📝 Found {len(candidates)} condense candidates")
    print(f"   Mode: {'DRY-RUN' if args.dry_run else 'APPLY'}")
    print()
    
    condensed = 0
    for candidate in sorted(candidates, key=lambda x: x['word_count'], reverse=True):
        filepath = Path(candidate['filepath'])
        if condense_page(filepath, dry_run=args.dry_run, auto=args.auto):
            condensed += 1
    
    print()
    print(f"📊 Condensed {condensed} pages")


if __name__ == '__main__':
    main()
