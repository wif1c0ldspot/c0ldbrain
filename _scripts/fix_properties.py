#!/usr/bin/env python3
"""
fix_properties.py — C0ldbrain Wiki Property Normalizer
======================================================

Fixes frontmatter gaps and inconsistencies across all wiki files to ensure
Obsidian Bases can reliably query properties. Complies with SCHEMA.md and
wiki_config.py conventions.

WHAT IT FIXES:
  1. Normalizes priority values to: critical | important | reference
  2. Sets missing 'updated' to 'created' date (or today)
  3. Sets missing 'created' to earliest reasonable date
  4. Sets missing 'confidence' based on file type and body length
  5. Sets missing 'status' to 'current' (or 'stub' if body <200 chars)
  6. Sets missing 'summary' to a placeholder
  7. Adds missing 'compiled' to sources (true if body >200 chars)
  8. Marks short concept pages as status: stub

SAFETY:
  - Creates .bak backup of every modified file
  - Dry-run mode: shows changes without writing
  - Only modifies frontmatter; body is never touched
  - Logs all changes to _scripts/property_fix_log.json

USAGE:
  python3 fix_properties.py                # Dry run (show changes)
  python3 fix_properties.py --apply        # Apply changes
  python3 fix_properties.py --apply --no-backup  # Skip backups
"""

import os
import sys
import json
import re
import shutil
import datetime
import argparse
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
import wiki_config

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Run: pip install pyyaml")
    sys.exit(1)

# --- Configuration (from wiki_config single source of truth) ---
WIKI_ROOT = wiki_config.WIKI_ROOT
CONCEPTS_DIR = wiki_config.CONCEPTS_DIR
SOURCES_DIR = wiki_config.SOURCES_DIR
SYNTHESIS_DIR = wiki_config.SYNTHESIS_DIR
PLANS_DIR = wiki_config.WIKI_DIR / "plans"

VALID_PRIORITIES = {"critical", "important", "reference"}
VALID_CONFIDENCES = {"high", "medium", "low"}
VALID_STATUSES = {"current", "deprecated", "stub", "emerging"}
VALID_TYPES = {"concept", "source", "synthesis", "analysis", "meta", "reference", "research-log"}

PRIORITY_MAP = {
    "high": "important",
    "medium": "important",
    "moderate": "important",
    "low": "reference",
    "2": "important",
    "1": "reference",
    "3": "critical",
}

TODAY = datetime.date.today().isoformat()


def parse_frontmatter(content):
    """Parse YAML frontmatter. Returns (metadata_dict, body_string, end_position)."""
    if not content.startswith("---"):
        return {}, content, 0
    end = content.find("---", 3)
    if end == -1:
        return {}, content, 0
    fm_str = content[3:end]
    body = content[end + 3:]
    try:
        fm = yaml.safe_load(fm_str) or {}
    except yaml.YAMLError:
        return {}, content, 0
    return fm, body, end + 3


def serialize_frontmatter(fm, body):
    """Reconstruct file with cleaned frontmatter."""
    fm_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
    return f"---\n{fm_str}---{body}"


def infer_confidence(fm, body, ftype):
    body_len = len(body.strip())
    status = fm.get("status", "")
    if status == "stub" or body_len < 200:
        return "low"
    if ftype == "source" and body_len > 500:
        return "high"
    return "medium"


def infer_priority(fm, ftype):
    tags = [t.lower() for t in fm.get("tags", [])]
    critical_tags = {"ai-agents", "agent-architecture", "ai-security", "prompt-injection"}
    if tags and any(t in critical_tags for t in tags):
        return "important"
    if ftype == "synthesis":
        return "important"
    if ftype == "source":
        return "reference"
    return "reference"


def analyze_file(filepath):
    """Analyze a single file and return proposed changes."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return {"file": filepath.name, "error": str(e), "changes": {}}

    fm, body, fm_end = parse_frontmatter(content)
    if not fm:
        return {"file": filepath.name, "error": "no frontmatter", "changes": {}}

    changes = {}
    ftype = fm.get("type", "")
    body_len = len(body.strip())

    # 1. Normalize priority
    priority = fm.get("priority")
    if not priority:
        changes["priority"] = {"from": None, "to": infer_priority(fm, ftype)}
    elif str(priority) not in VALID_PRIORITIES:
        mapped = PRIORITY_MAP.get(str(priority), "reference")
        changes["priority"] = {"from": priority, "to": mapped}

    # 2. Fix missing 'updated'
    if not fm.get("updated"):
        fallback = fm.get("created", TODAY)
        changes["updated"] = {"from": None, "to": str(fallback)}

    # 3. Fix missing 'created'
    if not fm.get("created"):
        changes["created"] = {"from": None, "to": TODAY}

    # 4. Fix missing 'confidence'
    if not fm.get("confidence"):
        changes["confidence"] = {"from": None, "to": infer_confidence(fm, body, ftype)}

    # 5. Fix missing 'status' / reclassify stubs
    if not fm.get("status"):
        status = "stub" if body_len < 200 else "current"
        changes["status"] = {"from": None, "to": status}
    elif fm.get("status") == "current" and body_len < 200:
        changes["status"] = {"from": "current", "to": "stub"}

    # 6. Fix missing 'summary'
    if not fm.get("summary"):
        title = fm.get("title", filepath.stem)
        changes["summary"] = {"from": None, "to": f"Auto-generated placeholder for {title}"}

    # 7. Add 'compiled' to sources
    if ftype == "source" and "compiled" not in fm:
        changes["compiled"] = {"from": None, "to": True if body_len > 200 else False}

    # 8. Normalize non-standard type
    if ftype == "article":
        changes["type"] = {"from": ftype, "to": "source"}

    return {"file": filepath.name, "type": ftype, "body_len": body_len, "changes": changes}


def apply_fixes(filepath, analysis, backup=True):
    """Apply proposed changes to a file."""
    if analysis.get("error") or not analysis.get("changes"):
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    fm, body, fm_end = parse_frontmatter(content)
    if not fm:
        return False

    if backup:
        bak_path = filepath.with_suffix(".md.bak")
        shutil.copy2(filepath, bak_path)

    for key, change in analysis["changes"].items():
        fm[key] = change["to"]

    new_content = serialize_frontmatter(fm, body)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main():
    parser = argparse.ArgumentParser(description="Fix C0ldbrain wiki frontmatter properties")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default is dry-run)")
    parser.add_argument("--no-backup", action="store_true", help="Skip .bak file creation")
    parser.add_argument("--verbose", action="store_true", help="Show all files including unchanged")
    args = parser.parse_args()

    dirs = [CONCEPTS_DIR, SOURCES_DIR, SYNTHESIS_DIR, PLANS_DIR]
    all_files = []
    for d in dirs:
        if d.exists():
            all_files.extend(d.glob("*.md"))

    print(f"C0ldbrain Wiki Property Fixer")
    print(f"{'=' * 50}")
    print(f"Files scanned: {len(all_files)}")
    print(f"Mode: {'APPLY' if args.apply else 'DRY RUN'}")
    print()

    results = []
    stats = defaultdict(int)
    change_types = defaultdict(int)

    for filepath in sorted(all_files):
        analysis = analyze_file(filepath)
        results.append(analysis)

        if analysis.get("error"):
            stats["errors"] += 1
            if args.verbose:
                print(f"  WARNING {analysis['file']}: {analysis['error']}")
            continue

        changes = analysis.get("changes", {})
        if not changes:
            stats["unchanged"] += 1
            if args.verbose:
                print(f"  OK {analysis['file']}")
            continue

        stats["changed"] += 1
        for key in changes:
            change_types[key] += 1

        icon = "EDIT" if args.apply else "PLAN"
        print(f"  [{icon}] {analysis['file']} ({analysis['type']}, {analysis['body_len']} chars)")
        for key, change in changes.items():
            print(f"       {key}: {change['from']} -> {change['to']}")

        if args.apply:
            success = apply_fixes(filepath, analysis, backup=not args.no_backup)
            if success:
                stats["applied"] += 1

    print(f"\n{'=' * 50}")
    print(f"Summary:")
    print(f"  Unchanged: {stats['unchanged']}")
    print(f"  Needs changes: {stats['changed']}")
    print(f"  Applied: {stats.get('applied', 0)}")
    print(f"  Errors: {stats['errors']}")
    print(f"\nChanges by type:")
    for key, count in sorted(change_types.items(), key=lambda x: -x[1]):
        print(f"  {key}: {count} files")

    # Write log
    log_path = WIKI_ROOT / "_scripts" / "property_fix_log.json"
    log_entry = {
        "date": TODAY,
        "mode": "apply" if args.apply else "dry-run",
        "files_scanned": len(all_files),
        "files_changed": stats["changed"],
        "files_applied": stats.get("applied", 0),
        "change_types": dict(change_types),
    }

    existing_log = []
    if log_path.exists():
        try:
            with open(log_path, "r") as f:
                existing_log = json.load(f)
            if not isinstance(existing_log, list):
                existing_log = []
        except:
            pass

    existing_log.append(log_entry)
    with open(log_path, "w") as f:
        json.dump(existing_log, f, indent=2, default=str)

    print(f"\nLog: {log_path}")
    if not args.apply:
        print(f"\nDRY RUN - no files modified. Run with --apply to apply changes.")


if __name__ == "__main__":
    main()
