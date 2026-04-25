#!/usr/bin/env python3
"""
Lifecycle Archive Script

Moves stale, project-specific, or orphaned pages to archive/ directory.

Usage:
    python3 lifecycle_archive.py [--slug SLUG] [--dry-run] [--auto]

With --slug: archive specific page
Without --slug: process all archive candidates from lifecycle report
"""

import os
import json
import yaml
import argparse
import shutil
from pathlib import Path
from datetime import datetime

import wiki_config
WIKI_ROOT = wiki_config.WIKI_ROOT
LIFECYCLE_REPORT = wiki_config.LIFECYCLE_REPORT
ARCHIVE_DIR = wiki_config.ARCHIVE_DIR


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


def archive_page(filepath, dry_run=True, auto=False):
    """Archive a single wiki page."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"   ❌ Error reading {filepath}: {e}")
        return False
    
    frontmatter, body = parse_frontmatter(content)
    
    print(f"   📁 {filepath.stem}")
    print(f"      Reason: {frontmatter.get('status', 'current')} → archived")
    
    if dry_run:
        print(f"      (dry-run: not archived)")
        return True
    
    if not auto:
        response = input(f"      Archive this page? [y/N]: ").strip().lower()
        if response != 'y':
            print(f"      Skipped")
            return False
    
    # Update frontmatter
    frontmatter['status'] = 'archived'
    frontmatter['archived_at'] = datetime.now().strftime('%Y-%m-%d')
    frontmatter['original_path'] = str(filepath.relative_to(WIKI_ROOT))
    
    # Reconstruct document
    fm_yaml = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
    new_content = f"---\n{fm_yaml}---\n{body}\n"
    
    # Ensure archive directory exists
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    
    # Move to archive
    archive_path = ARCHIVE_DIR / filepath.name
    
    # Handle duplicates
    if archive_path.exists():
        timestamp = datetime.now().strftime('%Y%m%d')
        archive_path = ARCHIVE_DIR / f"{filepath.stem}_{timestamp}.md"
    
    # Write archived version
    archive_path.write_text(new_content, encoding='utf-8')
    
    # Remove original
    filepath.unlink()
    
    print(f"      ✅ Archived to {archive_path.relative_to(WIKI_ROOT)}")
    return True


def main():
    parser = argparse.ArgumentParser(description='Archive wiki pages')
    parser.add_argument('--slug', help='Specific page slug to archive')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done')
    parser.add_argument('--auto', action='store_true', help='Auto-approve without prompting')
    args = parser.parse_args()
    
    if args.slug:
        # Archive specific page
        for subdir in ['concepts', 'sources']:
            filepath = Path(WIKI_ROOT) / 'wiki' / subdir / f"{args.slug}.md"
            if filepath.exists():
                archive_page(filepath, dry_run=args.dry_run, auto=args.auto)
                return
        print(f"❌ Page not found: {args.slug}")
        return
    
    # Process candidates from report
    if not LIFECYCLE_REPORT.exists():
        print(f"❌ No lifecycle report found. Run lifecycle_detect.py first.")
        return
    
    with open(LIFECYCLE_REPORT) as f:
        report = json.load(f)
    
    candidates = report['candidates']['archive']
    
    if not candidates:
        print("✅ No archive candidates found.")
        return
    
    print(f"📁 Found {len(candidates)} archive candidates")
    print(f"   Archive directory: {ARCHIVE_DIR.relative_to(WIKI_ROOT)}")
    print(f"   Mode: {'DRY-RUN' if args.dry_run else 'APPLY'}")
    print()
    
    archived = 0
    for candidate in sorted(candidates, key=lambda x: x['last_accessed_days'], reverse=True):
        filepath = Path(candidate['filepath'])
        if archive_page(filepath, dry_run=args.dry_run, auto=args.auto):
            archived += 1
    
    print()
    print(f"📊 Archived {archived} pages")


if __name__ == '__main__':
    main()
