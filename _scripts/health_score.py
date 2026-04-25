#!/usr/bin/env python3
"""health_score.py — Calculate wiki health metrics."""
import os, re, sys, json
from pathlib import Path
from collections import defaultdict
import datetime

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from wiki_config import WIKI_ROOT

WIKI_DIR = WIKI_ROOT / "wiki"
OUTPUTS_DIR = WIKI_ROOT / "outputs"
WIKILINK_RE = re.compile(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]')

def read_safe(path):
    try: return path.read_text(encoding='utf-8')
    except (IOError, OSError): return None

def parse_page(content):
    if not content.startswith('---'): return {}, content
    fm_end = content.find('---', 3)
    if fm_end == -1: return {}, content
    return content[3:fm_end], content[fm_end+3:].strip()

def page_score(body_len, link_count, inbound_count, days_since_update, fm_complete):
    """0-100 score."""
    body_pts = min(25, int(body_len / 20))  # 0-25, 500+ chars = 25
    link_pts = min(25, link_count * 5)  # 0-25, 5+ links = 25
    inbound_pts = min(25, inbound_count * 3)  # 0-25, 8+ inbound = 25
    recency_pts = max(0, 15 - int(days_since_update / 6))  # 15 at 0d, 0 at 90d
    fm_pts = 10 if fm_complete else 5
    return body_pts + link_pts + inbound_pts + recency_pts + fm_pts

def main():
    today = datetime.date.today()
    
    # Scan all pages
    all_slugs = set()
    outbound = defaultdict(set)
    inbound = defaultdict(int)
    slug_data = {}
    
    for sub in ['sources', 'concepts', 'synthesis']:
        d = WIKI_DIR / sub
        if not d.exists(): continue
        for f in d.glob("*.md"):
            slug = f.stem
            all_slugs.add(slug)
            text = read_safe(f)
            if text is None: continue
            fm, body = parse_page(text)
            
            # Extract metadata
            updated_match = re.search(r"updated:\s*['\"]?(\d{4}-\d{2}-\d{2})", fm)
            days = 999
            if updated_match:
                try: days = (today - datetime.datetime.strptime(updated_match.group(1), '%Y-%m-%d').date()).days
                except: pass
            
            required = ['title', 'type', 'tags', 'created', 'updated', 'confidence', 'status', 'priority', 'summary']
            fm_complete = sum(1 for r in required if r + ':' in fm) >= len(required) - 1
            
            for m in WIKILINK_RE.finditer(body):
                target = m.group(1).strip().rstrip('\\')
                if target: outbound[slug].add(target)
            
            slug_data[slug] = {
                'body_len': len(body), 'link_count': 0, 'days': days,
                'fm_complete': fm_complete, 'subdir': sub
            }
    
    # Build inbound counts
    for src, targets in outbound.items():
        for t in targets:
            inbound[t] += 1
        if src in slug_data:
            slug_data[src]['link_count'] = len(targets)
    
    # Calculate scores
    scores = {}
    for slug, data in slug_data.items():
        s = page_score(
            data['body_len'], data['link_count'],
            inbound.get(slug, 0), data['days'], data['fm_complete']
        )
        scores[slug] = s
        data['score'] = s
    
    # Report
    avg_score = sum(scores.values()) / max(len(scores), 1)
    healthy = sum(1 for s in scores.values() if s >= 80)
    needs_work = sum(1 for s in scores.values() if 50 <= s < 80)
    at_risk = sum(1 for s in scores.values() if s < 50)
    
    print(f"=== WIKI HEALTH REPORT ===")
    print(f"Date: {today}")
    print(f"Total pages: {len(all_slugs)}")
    print(f"Average health: {avg_score:.1f}/100")
    print(f"Healthy (80+): {healthy}")
    print(f"Needs work (50-79): {needs_work}")
    print(f"At risk (<50): {at_risk}")
    print(f"\n--- Top at-risk pages ---")
    for slug, score in sorted(scores.items(), key=lambda x: x[1])[:10]:
        data = slug_data.get(slug, {})
        print(f"  {score:3d}/100  {slug} ({data.get('subdir', '?')}, {data.get('body_len', 0)} chars, {data.get('days', '?')}d old)")
    
    # Save report
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    health_dir = OUTPUTS_DIR / "health"
    health_dir.mkdir(parents=True, exist_ok=True)
    
    report = {
        'date': str(today), 'total_pages': len(all_slugs),
        'average_score': round(avg_score, 1),
        'healthy': healthy, 'needs_work': needs_work, 'at_risk': at_risk,
        'at_risk_pages': [(s, scores[s]) for s in sorted(scores, key=scores.get)[:20]],
    }
    
    report_path = health_dir / f"{today}.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\nReport saved: {report_path}")

if __name__ == "__main__":
    main()
