#!/usr/bin/env python3
"""stub_resolver.py — Auto-expand concept stubs using linked sources."""
import os, re, sys, argparse, datetime
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from wiki_config import WIKI_ROOT, WIKI_DIR, CONCEPTS_DIR, SOURCES_DIR

STUB_THRESHOLD = 200

WIKILINK_RE = re.compile(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]')
BULLET_RE = re.compile(r'^[-*]\s+(.+)', re.MULTILINE)

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
    return content[3:fm_end], content[fm_end+3:].strip()

def parse_tags(fm):
    tags = []
    m = re.search(r'tags:\s*\n((?:- .+\n)*)', fm)
    if m:
        for line in m.group(1).strip().split('\n'):
            t = line.strip().lstrip('-').strip()
            if t: tags.append(t)
    else:
        m2 = re.search(r'tags:\s*\[(.*?)\]', fm)
        if m2: tags = [t.strip().strip("'\"") for t in m2.group(1).split(',') if t.strip()]
    return tags

def scan_wiki():
    all_slugs = set()
    outbound = defaultdict(set)
    slug_tags = {}
    
    for base_dir in [SOURCES_DIR, CONCEPTS_DIR, WIKI_DIR / "synthesis"]:
        if not base_dir.exists(): continue
        for f in base_dir.glob("*.md"):
            slug = f.stem
            all_slugs.add(slug)
            text = read_safe(f)
            if text is None: continue
            fm, body = parse_page(text)
            slug_tags[slug] = parse_tags(fm)
            for m in WIKILINK_RE.finditer(body):
                target = m.group(1).strip().rstrip('\\')
                if target: outbound[slug].add(target)
    return all_slugs, outbound, slug_tags

def rank_stubs():
    all_slugs, outbound, slug_tags = scan_wiki()
    inbound = defaultdict(int)
    for src, targets in outbound.items():
        for t in targets:
            inbound[t] += 1
    
    stubs = []
    if not CONCEPTS_DIR.exists(): return stubs
    for f in CONCEPTS_DIR.glob("*.md"):
        slug = f.stem
        text = read_safe(f)
        if text is None: continue
        fm, body = parse_page(text)
        if len(body.strip()) < STUB_THRESHOLD:
            stubs.append((slug, inbound.get(slug, 0), len(body.strip()), f))
    stubs.sort(key=lambda x: -x[1])
    return stubs

def find_linking_sources(slug):
    linking = []
    if not SOURCES_DIR.exists(): return linking
    for f in SOURCES_DIR.glob("*.md"):
        text = read_safe(f)
        if text is None: continue
        _, body = parse_page(text)
        for m in WIKILINK_RE.finditer(body):
            if m.group(1).strip().rstrip('\\') == slug:
                linking.append(f)
                break
    return linking

def expand_stub(slug, dry_run=False):
    fpath = CONCEPTS_DIR / f"{slug}.md"
    if not fpath.exists():
        print(f"  ERROR: {slug} not found"); return False
    text = read_safe(fpath)
    if text is None: return False
    fm, body = parse_page(text)
    if len(body.strip()) >= STUB_THRESHOLD:
        print(f"  SKIP: {slug} not a stub ({len(body)} chars)"); return False
    
    tags = parse_tags(fm)
    sources = find_linking_sources(slug)
    
    definitions = []
    bullets = []
    related = set()
    source_slugs = []
    
    for src_path in sources:
        src_text = read_safe(src_path)
        if src_text is None: continue
        _, src_body = parse_page(src_text)
        source_slugs.append(src_path.stem)
        
        # Extract first sentence mentioning concept
        name_variants = [slug, slug.replace('-', ' '), slug.replace('-', '')]
        for line in src_body.split('\n'):
            line = line.strip()
            if 30 < len(line) < 250 and not line.startswith('#') and not line.startswith('-'):
                if any(v.lower() in line.lower() for v in name_variants):
                    definitions.append(line)
                    break
        
        # Extract relevant bullets
        terms = set(tags + name_variants)
        for m in BULLET_RE.finditer(src_body):
            b = m.group(1).strip()
            if 15 < len(b) < 150 and any(t.lower() in b.lower() for t in terms):
                bullets.append(b)
        
        # Related concepts
        for m in WIKILINK_RE.finditer(src_body):
            t = m.group(1).strip().rstrip('\\')
            if t and t != slug: related.add(t)
    
    # Generate body
    parts = []
    if definitions:
        parts.append(definitions[0])
    else:
        parts.append(f"*Concept in the {tags[0] if tags else 'general'} domain — needs expansion.*")
    
    parts.append('')
    for b in bullets[:5]:
        parts.append(f'- {b}')
    while len(parts) < 7:  # Ensure at least 3 bullets
        parts.append('- *Key aspect to be expanded*')
    
    if related:
        parts.append('')
        parts.append('## Related')
        parts.append(' · '.join(f'[[{r}]]' for r in list(related)[:8]))
    
    if source_slugs:
        parts.append('')
        parts.append('## Sources')
        parts.append(', '.join(f'[[{s}]]' for s in source_slugs[:8]))
    
    new_body = '\n'.join(parts)
    if len(new_body) > 500:
        new_body = new_body[:497] + '...'
    
    today = datetime.date.today().isoformat()
    # Update frontmatter updated date
    fm_updated = re.sub(r"updated:\s*['\"]?.*?['\"]?\s*$", f"updated: '{today}'", fm, flags=re.MULTILINE)
    
    if dry_run:
        print(f"  Would expand {slug} ({len(new_body)} chars from {len(sources)} sources)")
        return True
    
    full = f"---{fm_updated}---\n\n{new_body}\n"
    if write_safe(fpath, full):
        print(f"  Expanded {slug} ({len(new_body)} chars, {len(sources)} sources, {len(related)} related)")
        return True
    return False

def main():
    parser = argparse.ArgumentParser(description="Auto-expand concept stubs.")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--resolve", type=str)
    parser.add_argument("--auto", action="store_true")
    parser.add_argument("--max", type=int, default=5)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    
    if args.list:
        stubs = rank_stubs()
        print(f"{'Rank':<5} {'Inbound':<9} {'Body':<8} {'Slug'}")
        for i, (slug, count, blen, _) in enumerate(stubs, 1):
            print(f"{i:<5} {count:<9} {blen:<8} {slug}")
        print(f"\nTotal: {len(stubs)} stubs (<{STUB_THRESHOLD} chars body)")
    elif args.resolve:
        expand_stub(args.resolve, args.dry_run)
    elif args.auto:
        stubs = rank_stubs()
        expanded = 0
        for slug, count, _, _ in stubs[:args.max]:
            if expand_stub(slug, args.dry_run):
                expanded += 1
        print(f"\n{'Would expand' if args.dry_run else 'Expanded'} {expanded} stub(s)")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
