#!/usr/bin/env python3
"""backfill_links.py — Backfill bidirectional wikilinks & adopt orphan pages."""
import os, re, sys, argparse, json
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from wiki_config import WIKI_ROOT, WIKI_DIR, CONCEPTS_DIR, SOURCES_DIR, SYNTHESIS_DIR, MANIFEST_PATH


WIKILINK_RE = re.compile(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]')
DATE_PREFIX_RE = re.compile(r'^\d{4}-\d{2}-\d{2}')
EXCEPTION_SLUGS = {"index", "RESOLVER", "log", "MANIFEST", "overview", "README", "SCHEMA"}

def read_safe(path):
    try: return path.read_text(encoding='utf-8')
    except (IOError, OSError) as e: print(f"  WARN: {e}"); return None

def write_safe(path, content):
    try: path.write_text(content, encoding='utf-8'); return True
    except (IOError, OSError) as e: print(f"  WARN: {e}"); return False

def normalize_target(raw):
    t = raw.strip().rstrip('\\')
    if '#' in t: t = t.split('#')[0]
    return t.strip()

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

def scan_wiki():
    slug_to_path = {}
    outbound = defaultdict(set)
    slug_tags = {}
    slug_category = {}

    for category, base_dir in [("sources", SOURCES_DIR), ("concepts", CONCEPTS_DIR), ("synthesis", SYNTHESIS_DIR)]:
        if not base_dir.exists(): continue
        for md_file in sorted(base_dir.glob("*.md")):
            slug = md_file.stem
            slug_to_path[slug] = md_file
            slug_category[slug] = category
            text = read_safe(md_file)
            if text is None: continue
            # Tags from frontmatter
            if text.startswith('---'):
                fm_end = text.find('---', 3)
                if fm_end != -1:
                    slug_tags[slug] = parse_tags(text[3:fm_end])
                    body = text[fm_end+3:]
                else:
                    body = text
            else:
                body = text
            # Links from body only
            for m in WIKILINK_RE.finditer(body):
                target = normalize_target(m.group(1))
                if target and '/' not in target:
                    outbound[slug].add(target)
    return slug_to_path, outbound, slug_tags, slug_category

def build_inbound(outbound):
    inbound = defaultdict(set)
    for src, targets in outbound.items():
        for tgt in targets:
            inbound[tgt].add(src)
    return inbound

def add_link_to_related(body, slug):
    if f'[[{slug}]]' in body: return body, False
    if '## Related' not in body:
        body = body.rstrip('\n') + '\n\n## Related\n'
    # Find ## Related and append
    lines = body.split('\n')
    insert_idx = None
    for i, line in enumerate(lines):
        if line.strip() == '## Related':
            insert_idx = i + 1
            while insert_idx < len(lines) and lines[insert_idx].strip().startswith('- '):
                insert_idx += 1
            break
    if insert_idx is None:
        lines.append(f'- [[{slug}]]')
    else:
        lines.insert(insert_idx, f'- [[{slug}]]')
    return '\n'.join(lines), True

def backfill_bidirectional(slug_to_path, outbound, slug_category, max_per_page=30, dry_run=False):
    print("\n=== Backfill Bidirectional Links ===\n")
    inbound = build_inbound(outbound)
    changes = 0
    for slug in sorted(slug_to_path):
        if slug_category.get(slug) not in ('concepts', 'synthesis'): continue
        backlinkers = inbound.get(slug, set())
        if not backlinkers: continue
        path = slug_to_path[slug]
        text = read_safe(path)
        if text is None: continue
        # Split frontmatter and body
        if text.startswith('---'):
            fm_end = text.find('---', 3)
            if fm_end != -1:
                fm_text = text[:fm_end+3]
                body = text[fm_end+3:]
            else:
                fm_text = ''
                body = text
        else:
            fm_text = ''
            body = text
        current = outbound.get(slug, set())
        missing = [bl for bl in sorted(backlinkers)
                   if bl not in current and not DATE_PREFIX_RE.match(os.path.basename(bl))
                   and bl.upper() not in EXCEPTION_SLUGS and bl not in EXCEPTION_SLUGS]
        if not missing: continue
        missing = missing[:max_per_page]
        added = 0
        for bl in missing:
            body, was = add_link_to_related(body, bl)
            if was: added += 1
        if not added: continue
        if dry_run:
            print(f"  Would add {added} backlink(s) to {slug}")
        else:
            if write_safe(path, fm_text + body):
                print(f"  Added {added} backlink(s) to {slug}")
        changes += 1
    print(f"\n  {'Would modify' if dry_run else 'Modified'} {changes} page(s)")
    return changes

def adopt_orphans(slug_to_path, outbound, inbound, slug_tags, slug_category, max_adopt=20, dry_run=False):
    print("\n=== Adopt Orphan Pages ===\n")
    orphans = []
    for slug in slug_to_path:
        if slug in EXCEPTION_SLUGS: continue
        if DATE_PREFIX_RE.match(os.path.basename(slug)): continue
        if inbound.get(slug): continue
        tags = slug_tags.get(slug, [])
        if tags: orphans.append((slug, tags))
    orphans.sort(key=lambda x: len(x[1]), reverse=True)
    print(f"  Found {len(orphans)} adoptable orphan(s)")
    # Build tag index for concepts
    concept_tags = {}
    for slug in slug_to_path:
        if slug_category.get(slug) == 'concepts':
            t = slug_tags.get(slug, [])
            if t: concept_tags[slug] = set(t)
    adopted = 0
    for orphan_slug, orphan_tag_list in orphans:
        if adopted >= max_adopt: break
        orphan_set = set(orphan_tag_list)
        candidates = [(cs, len(orphan_set & ct)) for cs, ct in concept_tags.items() if orphan_set & ct]
        if not candidates: continue
        candidates.sort(key=lambda x: -x[1])
        hub_slug, overlap = candidates[0]
        hub_path = slug_to_path[hub_slug]
        text = read_safe(hub_path)
        if text is None: continue
        if text.startswith('---'):
            fm_end = text.find('---', 3)
            if fm_end != -1:
                fm_text = text[:fm_end+3]
                body = text[fm_end+3:]
            else:
                fm_text = ''
                body = text
        else:
            fm_text = ''
            body = text
        new_body, was = add_link_to_related(body, orphan_slug)
        if not was: continue
        if dry_run:
            print(f"  Would adopt [{orphan_slug}] -> hub [{hub_slug}] ({overlap} shared tags)")
        else:
            if write_safe(hub_path, fm_text + new_body):
                print(f"  Adopted [{orphan_slug}] -> hub [{hub_slug}] ({overlap} shared tags)")
        adopted += 1
    print(f"\n  {'Would adopt' if dry_run else 'Adopted'} {adopted} orphan(s)")
    return adopted

def main():
    parser = argparse.ArgumentParser(description="Backfill bidirectional wikilinks and adopt orphan pages.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--backfill", action="store_true")
    parser.add_argument("--orphans", action="store_true")
    parser.add_argument("--auto", action="store_true")
    parser.add_argument("--max-per-page", type=int, default=30)
    parser.add_argument("--max-adopt", type=int, default=20)
    args = parser.parse_args()
    if not (args.backfill or args.orphans or args.auto):
        parser.print_help(); sys.exit(1)
    print(f"Wiki: {WIKI_DIR}")
    if args.dry_run: print("Mode: DRY-RUN")
    slug_to_path, outbound, slug_tags, slug_category = scan_wiki()
    print(f"  {len(slug_to_path)} pages scanned")
    inbound = build_inbound(outbound)
    total = 0
    if args.backfill or args.auto:
        total += backfill_bidirectional(slug_to_path, outbound, slug_category, args.max_per_page, args.dry_run)
    if args.orphans or args.auto:
        total += adopt_orphans(slug_to_path, outbound, inbound, slug_tags, slug_category, args.max_adopt, args.dry_run)
    print(f"\nDone. Total changes: {total}")

if __name__ == "__main__":
    main()
