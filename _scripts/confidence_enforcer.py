#!/usr/bin/env python3
"""confidence_enforcer.py — Auto-downgrade confidence and archive stale pages."""
import os, re, sys, argparse, json, shutil
from pathlib import Path
from collections import defaultdict
import datetime

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from wiki_config import WIKI_ROOT, WIKI_DIR, CONCEPTS_DIR, SOURCES_DIR, MANIFEST_PATH

ARCHIVE_DIR = WIKI_DIR / "archive"

DECAY_RULES = [
    ('high', 90, 'medium'),
    ('medium', 120, 'low'),
    ('low', 180, 'archive'),
]

def read_safe(path):
    try: return path.read_text(encoding='utf-8')
    except (IOError, OSError): return None

def write_safe(path, content):
    try: path.write_text(content, encoding='utf-8'); return True
    except (IOError, OSError): return False

def parse_page(content):
    if not content.startswith('---'): return {}, content
    fm_end = content.find('---', 3)
    if fm_end == -1: return {}, content
    return content[:fm_end+3], content[fm_end+3:]

def main():
    parser = argparse.ArgumentParser(description="Auto-downgrade confidence and archive stale pages.")
    parser.add_argument("--auto", action="store_true", help="Apply changes")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()
    
    apply_changes = args.auto and not args.dry_run
    today = datetime.date.today()
    stats = {'downgraded': 0, 'archived': 0, 'skipped': 0}
    
    print(f"Wiki: {WIKI_DIR}")
    print(f"Mode: {'APPLY' if apply_changes else 'DRY-RUN'}\n")
    
    for base_dir in [CONCEPTS_DIR, SOURCES_DIR]:
        if not base_dir.exists(): continue
        for f in sorted(base_dir.glob("*.md")):
            text = read_safe(f)
            if text is None: continue
            fm_text, body = parse_page(text)
            
            # Extract confidence and updated date
            conf_match = re.search(r'confidence:\s*["\']?(high|medium|low)["\']?', fm_text)
            updated_match = re.search(r"updated:\s*['\"]?(\d{4}-\d{2}-\d{2})", fm_text)
            
            if not conf_match or not updated_match: continue
            
            confidence = conf_match.group(1)
            try:
                updated = datetime.datetime.strptime(updated_match.group(1), '%Y-%m-%d').date()
            except ValueError: continue
            
            days_old = (today - updated).days
            
            # Check decay rules
            for rule_conf, threshold, new_conf in DECAY_RULES:
                if confidence == rule_conf and days_old > threshold:
                    if new_conf == 'archive':
                        if apply_changes:
                            ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
                            dest = ARCHIVE_DIR / f.name
                            shutil.move(str(f), str(dest))
                            # Create redirect stub
                            redirect = f"---\ntitle: \"{f.stem}\"\ntype: concept\nstatus: deprecated\nsummary: \"Archived — see archive/{f.stem}\"\n---\n\n# {f.stem}\n\nArchived to [[archive/{f.stem}]].\n"
                            write_safe(f, redirect)
                        print(f"  {'Would archive' if not apply_changes else 'Archived'}: {f.stem} ({days_old}d old, {confidence})")
                        stats['archived'] += 1
                    else:
                        if apply_changes:
                            new_fm = re.sub(r'confidence:\s*["\']?' + confidence + r'["\']?', 
                                          f'confidence: {new_conf}', fm_text)
                            write_safe(f, new_fm + body)
                        print(f"  {'Would downgrade' if not apply_changes else 'Downgraded'}: {f.stem} {confidence}->{new_conf} ({days_old}d old)")
                        stats['downgraded'] += 1
                    break
    
    print(f"\nResults: {stats}")

if __name__ == "__main__":
    main()
