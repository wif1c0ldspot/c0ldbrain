#!/usr/bin/env python3
"""
Knowledge Lifecycle Detection Pipeline

Scans wiki pages, evaluates them against the lifecycle decision framework,
and generates candidate lists for condense, archive, converge, and discard actions.

Usage:
    python3 lifecycle_detect.py [--output-dir PATH] [--similarity-threshold FLOAT]

Output:
    - outputs/lifecycle/lifecycle-report.json (machine-readable)
    - outputs/lifecycle/lifecycle-report.md (human-readable)
"""

import os
import re
import json
import yaml
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

# Configuration
import wiki_config
WIKI_ROOT = wiki_config.WIKI_ROOT
WIKI_CONCEPTS = wiki_config.CONCEPTS_DIR
WIKI_SOURCES = wiki_config.SOURCES_DIR
DEFAULT_OUTPUT = wiki_config.LIFECYCLE_DIR

# Decision thresholds - tune these based on your wiki's characteristics
THRESHOLDS = {
    "retain": {
        "min_access_count": 3,
        "max_age_days": 90,
        "min_inbound_links": 2,
        "min_confidence": "medium"
    },
    "condense": {
        "min_word_count": 800,
        "max_access_count": 5,
        "min_age_days": 30,
        "high_temporal_refs": 3
    },
    "archive": {
        "max_last_accessed_days": 90,
        "project_specific": True,
        "max_inbound_links": 1
    },
    "discard": {
        "max_access_count": 0,
        "orphan": True,
        "superseded": True
    }
}


def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if content.startswith('---'):
        try:
            parts = content.split('---', 2)
            if len(parts) >= 3:
                fm = yaml.safe_load(parts[1])
                body = parts[2]
                return fm if fm else {}, body
        except Exception as e:
            pass
    return {}, content


def extract_wikilinks(content):
    """Extract all wikilinks [[like this]] from content."""
    pattern = r'\[\[([^\]]+)\]\]'
    return re.findall(pattern, content)


def extract_temporal_refs(content):
    """Count temporal references (dates, versions, "current", "now")."""
    date_pattern = r'\b(20\d{2})[-/](0[1-9]|1[0-2])[-/](0[1-9]|[12]\d|3[01])\b'
    version_pattern = r'\b(v?\d+\.\d+(?:\.\d+)?)\b'
    temporal_words = r'\b(current|now|today|recently|latest|new|old|deprecated)\b'
    
    dates = len(re.findall(date_pattern, content))
    versions = len(re.findall(version_pattern, content))
    temporal = len(re.findall(temporal_words, content, re.IGNORECASE))
    
    return dates + versions + temporal


def calculate_semantic_similarity(content1, content2):
    """Simple word overlap similarity for convergence detection."""
    # Normalize: lowercase, extract words
    words1 = set(re.findall(r'\b\w+\b', content1.lower()))
    words2 = set(re.findall(r'\b\w+\b', content2.lower()))
    
    # Remove common stop words
    stop_words = {'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been',
                  'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
                  'would', 'could', 'should', 'may', 'might', 'must', 'shall',
                  'can', 'need', 'dare', 'ought', 'used', 'to', 'of', 'in',
                  'for', 'on', 'with', 'at', 'by', 'from', 'as', 'into',
                  'through', 'during', 'before', 'after', 'above', 'below',
                  'between', 'under', 'and', 'but', 'or', 'yet', 'so', 'if',
                  'because', 'although', 'though', 'while', 'where', 'when',
                  'that', 'which', 'who', 'whom', 'whose', 'what', 'this',
                  'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they'}
    
    words1 = words1 - stop_words
    words2 = words2 - stop_words
    
    if not words1 or not words2:
        return 0.0
    
    intersection = words1 & words2
    union = words1 | words2
    return len(intersection) / len(union)


def analyze_page(filepath):
    """Analyze a single wiki page and return metrics."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Warning: Could not read {filepath}: {e}")
        return None
    
    frontmatter, body = parse_frontmatter(content)
    
    # Basic metrics
    word_count = len(body.split())
    wikilinks = extract_wikilinks(content)
    temporal_refs = extract_temporal_refs(content)
    
    # Parse dates
    created = frontmatter.get('created', '')
    updated = frontmatter.get('updated', '')
    
    # Lifecycle metadata
    lifecycle = frontmatter.get('lifecycle', {})
    access_count = lifecycle.get('access_count', 0)
    last_accessed = lifecycle.get('last_accessed', updated or created)
    
    # Calculate age
    age_days = 999
    try:
        if updated:
            updated_str = str(updated).split('T')[0].split()[0]
            updated_date = datetime.strptime(updated_str, '%Y-%m-%d')
            age_days = (datetime.now() - updated_date).days
        elif created:
            created_str = str(created).split('T')[0].split()[0]
            created_date = datetime.strptime(created_str, '%Y-%m-%d')
            age_days = (datetime.now() - created_date).days
    except:
        pass
    
    # Last accessed days
    last_accessed_days = age_days
    try:
        if last_accessed:
            last_str = str(last_accessed).split('T')[0].split()[0]
            last_date = datetime.strptime(last_str, '%Y-%m-%d')
            last_accessed_days = (datetime.now() - last_date).days
    except:
        pass
    
    return {
        'filepath': str(filepath),
        'slug': filepath.stem,
        'type': 'concept' if 'concepts' in str(filepath) else 'source',
        'title': frontmatter.get('title', filepath.stem),
        'word_count': word_count,
        'wikilinks': wikilinks,
        'outbound_links': len(wikilinks),
        'temporal_refs': temporal_refs,
        'created': created,
        'updated': updated,
        'age_days': age_days,
        'access_count': access_count,
        'last_accessed_days': last_accessed_days,
        'confidence': frontmatter.get('confidence', 'medium'),
        'status': frontmatter.get('status', 'current'),
        'tags': frontmatter.get('tags', []),
        'summary': frontmatter.get('summary', ''),
        'lifecycle': lifecycle,
        'raw_frontmatter': frontmatter,
        'content_preview': body[:500] if body else ''
    }


def scan_wiki():
    """Scan all wiki pages and return list of page data."""
    pages = []
    
    # Scan concepts
    if WIKI_CONCEPTS.exists():
        for f in WIKI_CONCEPTS.glob('*.md'):
            if f.name not in ['index.md', 'README.md']:
                page = analyze_page(f)
                if page:
                    pages.append(page)
    
    # Scan sources
    if WIKI_SOURCES.exists():
        for f in WIKI_SOURCES.glob('*.md'):
            if f.name not in ['index.md', 'README.md']:
                page = analyze_page(f)
                if page:
                    pages.append(page)
    
    return pages


def build_link_graph(pages):
    """Build inbound link counts for each page."""
    inbound = defaultdict(int)
    
    for page in pages:
        for link in page['wikilinks']:
            # Handle piped links [[slug|display]]
            target = link.split('|')[0].strip()
            inbound[target] += 1
    
    # Add inbound counts to pages
    for page in pages:
        page['inbound_links'] = inbound.get(page['slug'], 0)
    
    return inbound


def calculate_condense_score(page):
    """
    Calculate multi-factor condense priority score for CONCEPT pages only.
    Revised thresholds to prevent information loss:
    
    EXCLUSIONS (return score 0):
    - Source pages (sources/*) - archival value requires verbatim
    - Already archived/superseded pages
    - Low confidence pages (need expansion, not compression)
    - Pages with 2+ inbound links (protected as growing hubs)
    
    REVISED THRESHOLDS:
    - Length: 800w=1pt, 1200w=2pt, 1800w=3pt (higher bars)
    - Temporal: >0.05 refs/100w = 2pt (stricter - reduces citation misfires)
    - Connectivity: 0 inbounds=2pt, 1 inbound=1pt, 2+=protected
    - Hub bonus: -2pt if linked by 2+ pages (active growth indicator)
    
    Trigger: score >= 5 (requires strong evidence)
    """
    score = 0
    reasons = []
    
    # === EXCLUSIONS: Never condense these ===
    
    # Exclude source pages - archival value requires verbatim preservation
    if page['type'] == 'source':
        return 0, ["source page (excluded from condensation)"]
    
    # Exclude already processed pages
    if page['status'] in ['archived', 'superseded']:
        return 0, [f"status: {page['status']} (excluded)"]
    
    # Exclude low confidence pages - these need expansion, not compression
    if page['confidence'] == 'low':
        return 0, ["low confidence (needs expansion, not condensation)"]
    
    # === PROTECTION: Growing hubs should NOT be condensed ===
    if page['inbound_links'] >= 2:
        return 0, ["protected: growing hub (2+ inbounds)"]
    
    # === LENGTH FACTOR (0-3 points) - Higher thresholds ===
    if page['word_count'] > 1800:
        score += 3
        reasons.append(f"very long ({page['word_count']} words)")
    elif page['word_count'] > 1200:
        score += 2
        reasons.append(f"long ({page['word_count']} words)")
    elif page['word_count'] > 800:
        score += 1
        reasons.append(f"verbose ({page['word_count']} words)")
    else:
        # Too short to benefit from condensation
        return 0, ["too short for condensation"]
    
    # === TEMPORAL DENSITY FACTOR (0-2 points) - Stricter threshold ===
    # Use density (refs per 100 words) not raw count
    temporal_density = page['temporal_refs'] / max(page['word_count'] / 100, 1)
    if temporal_density > 0.05:  # >5 refs per 100 words (was 0.03)
        score += 2
        reasons.append(f"high temporal density ({temporal_density:.2f} per 100w)")
    elif temporal_density > 0.03:
        score += 1
        reasons.append(f"moderate temporal density ({temporal_density:.2f} per 100w)")
    
    # === CONNECTIVITY FACTOR (0-3 points) - age-qualified orphan scoring ===
    # New orphans are protected (just born, haven't been discovered)
    # Old orphans are concerning (stale, deliberately avoided)
    orphan_age = page['age_days']
    
    if page['inbound_links'] == 0:
        if orphan_age <= 7:
            # Hard exclude: too new
            return 0, ["new orphan (≤7 days - discovery period)"]
        elif orphan_age <= 30:
            score += 1
            reasons.append(f"young orphan ({orphan_age} days)")
        elif orphan_age <= 60:
            score += 2
            reasons.append(f"orphan ({orphan_age} days)")
        else:
            score += 3
            reasons.append(f"stale orphan ({orphan_age} days)")
    elif page['inbound_links'] == 1:
        if orphan_age <= 30:
            score += 0  # Young leaf - protected
        else:
            score += 1
            reasons.append(f"leaf node ({orphan_age} days old)")
    
    # === ENGAGEMENT FACTOR (0-1 point) ===
    if page['access_count'] == 0 and page['age_days'] > 60:
        score += 1
        reasons.append("never accessed, aging")
    elif page['access_count'] <= 2 and page['age_days'] > 90:
        score += 1
        reasons.append("low access, stale")
    
    # === RECENCY BONUS (0-1 point) ===
    # Recent pages with 0 access may just need time to be discovered
    if page['age_days'] <= 14:
        score -= 1  # Penalty for very new pages
        reasons.append("very new (discovery period)")
    
    return max(0, score), reasons


def evaluate_candidates(pages):
    """Evaluate each page and assign lifecycle actions using optimized thresholds."""
    candidates = {
        'retain': [],
        'condense': [],
        'archive': [],
        'discard': []
    }
    
    for page in pages:
        # Skip already archived/superseded
        if page['status'] in ['archived', 'superseded']:
            continue
            
        scores = {
            'retain': 0,
            'condense': 0,
            'archive': 0,
            'discard': 0
        }
        reasons = []
        
        # === RETAIN criteria (positive signals) ===
        if page['access_count'] >= 3:
            scores['retain'] += 1
        if page['inbound_links'] >= 3:  # Hub pages
            scores['retain'] += 2
        elif page['inbound_links'] >= 1:
            scores['retain'] += 1
        if page['age_days'] < 90:
            scores['retain'] += 1
        if page['confidence'] in ['high', 'very high']:
            scores['retain'] += 1
        if page['word_count'] >= 400 and page['word_count'] <= 1000:
            scores['retain'] += 1  # Sweet spot length
        if 'pattern' in page['tags'] or 'principle' in page['tags']:
            scores['retain'] += 1
        
        # === CONDENSE criteria (multi-factor scoring) ===
        condense_score, condense_reasons = calculate_condense_score(page)
        scores['condense'] = condense_score
        reasons.extend(condense_reasons)
            
        # === ARCHIVE criteria (stale, project-specific, orphaned) ===
        if page['last_accessed_days'] > 90:
            scores['archive'] += 1
            reasons.append(f"stale ({page['last_accessed_days']} days)")
        if any(tag in page['tags'] for tag in ['project', 'project-specific', 'sprint']):
            scores['archive'] += 1
            reasons.append("project-specific")
        if page['inbound_links'] == 0 and page['outbound_links'] <= 2:
            scores['archive'] += 1
            reasons.append("orphan/minimal links")
        if page['temporal_refs'] > 5 and page['age_days'] > 180:
            scores['archive'] += 1
            reasons.append("time-heavy, old")
        if page['status'] == 'draft':
            scores['archive'] += 1
            reasons.append("draft status")
        # Never accessed sources older than 60 days
        if page['access_count'] == 0 and page['age_days'] > 60 and page['type'] == 'source':
            scores['archive'] += 1
            reasons.append("source never accessed")
            
        # === DISCARD criteria (unused, isolated, superseded) ===
        if page['access_count'] == 0 and page['age_days'] > 90:
            scores['discard'] += 1
            reasons.append("never accessed, very old")
        if page['inbound_links'] == 0 and page['outbound_links'] == 0:
            scores['discard'] += 2
            reasons.append("completely isolated")
        if page['status'] == 'superseded':
            scores['discard'] += 3
            reasons.append("explicitly superseded")
        if page['word_count'] < 80 and page['age_days'] > 60:
            scores['discard'] += 1
            reasons.append("stub, aging")
        if 'deprecated' in page['tags'] or 'obsolete' in page['tags']:
            scores['discard'] += 2
            reasons.append("tagged deprecated")
        if 'delete' in page['tags'] or 'discard' in page['tags']:
            scores['discard'] += 3
            reasons.append("tagged for deletion")
        
        # === DECISION LOGIC ===
        # Priority: discard > archive > condense > retain
        action = 'retain'
        
        # DISCARD: Must have strong evidence (score >= 3)
        if scores['discard'] >= 3:
            action = 'discard'
        # ARCHIVE: Moderate evidence (score >= 2)
        elif scores['archive'] >= 2:
            action = 'archive'
        # CONDENSE: Multi-factor score >= 5 (very high confidence)
        # Source pages are already excluded in calculate_condense_score
        elif scores['condense'] >= 5:
            action = 'condense'
        # Default: retain
        else:
            action = 'retain'
        
        # Override: High-value pages (2+ inbounds) always retain
        # Note: This is backup protection - calculate_condense_score already protects
        if page['inbound_links'] >= 2 and action == 'condense':
            action = 'retain'
            reasons.append("protected: high-value hub")
        
        # Override: Very short pages don't need condensing
        # Note: calculate_condense_score already requires >800w
        if action == 'condense' and page['word_count'] < 800:
            action = 'retain'
            reasons.append("below minimum length threshold")
            
        page['action'] = action
        page['scores'] = scores
        page['condense_score'] = scores['condense']  # for reporting
        page['reasons'] = list(set(reasons))  # dedupe
        candidates[action].append(page)
    
    return candidates


def find_convergence_candidates(pages, threshold=0.7):
    """Find pages with high semantic similarity for potential merging."""
    convergence_pairs = []
    
    # Only check same-type pages for convergence
    for i, p1 in enumerate(pages):
        if p1['status'] in ['archived', 'superseded']:
            continue
            
        for p2 in pages[i+1:]:
            if p2['status'] in ['archived', 'superseded']:
                continue
            if p1['type'] != p2['type']:
                continue
            
            # Skip if already very short
            if p1['word_count'] < 200 or p2['word_count'] < 200:
                continue
                
            try:
                content1 = Path(p1['filepath']).read_text()
                content2 = Path(p2['filepath']).read_text()
                similarity = calculate_semantic_similarity(content1, content2)
                
                if similarity >= threshold:
                    convergence_pairs.append({
                        'page1': p1['slug'],
                        'page2': p2['slug'],
                        'similarity': round(similarity, 3),
                        'type': p1['type'],
                        'combined_word_count': p1['word_count'] + p2['word_count'],
                        'page1_words': p1['word_count'],
                        'page2_words': p2['word_count'],
                        'recommendation': f"Merge {p2['slug']} into {p1['slug']}" if p1['word_count'] > p2['word_count'] else f"Merge {p1['slug']} into {p2['slug']}"
                    })
            except Exception as e:
                continue
    
    # Sort by similarity
    convergence_pairs.sort(key=lambda x: x['similarity'], reverse=True)
    return convergence_pairs


def generate_report(candidates, pages, convergence_pairs):
    """Generate comprehensive lifecycle report."""
    return {
        'generated_at': datetime.now().isoformat(),
        'summary': {
            'total_pages': len(pages),
            'retain': len(candidates['retain']),
            'condense': len(candidates['condense']),
            'archive': len(candidates['archive']),
            'discard': len(candidates['discard']),
            'converge_pairs': len(convergence_pairs)
        },
        'candidates': candidates,
        'convergence_opportunities': convergence_pairs,
        'statistics': {
            'avg_word_count': sum(p['word_count'] for p in pages) / len(pages) if pages else 0,
            'avg_age_days': sum(p['age_days'] for p in pages) / len(pages) if pages else 0,
            'total_wikilinks': sum(len(p['wikilinks']) for p in pages),
            'orphan_pages': len([p for p in pages if p['inbound_links'] == 0]),
            'stale_pages': len([p for p in pages if p['last_accessed_days'] > 90]),
            'total_words': sum(p['word_count'] for p in pages)
        }
    }


def generate_markdown_report(report):
    """Generate human-readable markdown report."""
    s = report['summary']
    stats = report['statistics']
    
    md = f"""# Knowledge Lifecycle Report

**Generated**: {report['generated_at'][:19]}

## Summary

| Action | Count | Percentage |
|--------|-------|------------|
| ✅ RETAIN | {s['retain']} | {s['retain']/s['total_pages']*100:.1f}% |
| 📝 CONDENSE | {s['condense']} | {s['condense']/s['total_pages']*100:.1f}% |
| 📁 ARCHIVE | {s['archive']} | {s['archive']/s['total_pages']*100:.1f}% |
| 🚮 DISCARD | {s['discard']} | {s['discard']/s['total_pages']*100:.1f}% |
| **Total** | **{s['total_pages']}** | 100% |

## Statistics

- Total words: {stats['total_words']:,}
- Average page length: {stats['avg_word_count']:.0f} words
- Average age: {stats['avg_age_days']:.0f} days
- Total wikilinks: {stats['total_wikilinks']}
- Orphan pages: {stats['orphan_pages']}
- Stale pages (>90 days): {stats['stale_pages']}

## Priority Actions

"""
    
    candidates = report['candidates']
    
    # Condense candidates
    if candidates['condense']:
        md += "### 📝 Condense Candidates\n\n"
        md += "*Extract enduring patterns, remove temporal specifics, compress to essentials*\n\n"
        for p in sorted(candidates['condense'], key=lambda x: x['word_count'], reverse=True)[:15]:
            md += f"| [[{p['slug']}]] | {p['word_count']}w | {p['inbound_links']} in | {', '.join(p['reasons'][:2])} |\n"
        md += "\n"
    
    # Archive candidates
    if candidates['archive']:
        md += "### 📁 Archive Candidates\n\n"
        md += "*Move to `archive/`, preserve but deprioritize*\n\n"
        for p in sorted(candidates['archive'], key=lambda x: x['last_accessed_days'], reverse=True)[:15]:
            md += f"| [[{p['slug']}]] | {p['last_accessed_days']}d | {p['inbound_links']} in | {', '.join(p['reasons'][:2])} |\n"
        md += "\n"
    
    # Discard candidates
    if candidates['discard']:
        md += "### 🚮 Discard Candidates\n\n"
        md += "*Review carefully before deletion*\n\n"
        for p in candidates['discard']:
            md += f"- **[[{p['slug']}]]** — {', '.join(p['reasons'])}\n"
        md += "\n"
    
    # Convergence opportunities
    if report['convergence_opportunities']:
        md += "### 🔗 Convergence Opportunities\n\n"
        md += "*High similarity pages that could be merged*\n\n"
        md += "| Page 1 | Page 2 | Similarity | Recommendation |\n"
        md += "|--------|--------|------------|----------------|\n"
        for pair in report['convergence_opportunities'][:10]:
            md += f"| [[{pair['page1']}]] | [[{pair['page2']}]] | {pair['similarity']*100:.1f}% | {pair['recommendation']} |\n"
        md += "\n"
    
    # Retain highlights
    if candidates['retain']:
        high_value = [p for p in candidates['retain'] if p['inbound_links'] >= 3]
        if high_value:
            md += "### ⭐ High-Value Hub Pages\n\n"
            md += "*Well-connected pages — keep maintaining*\n\n"
            md += "| Page | Inbound | Access | Words |\n"
            md += "|------|---------|--------|-------|\n"
            for p in sorted(high_value, key=lambda x: x['inbound_links'], reverse=True)[:10]:
                md += f"| [[{p['slug']}]] | {p['inbound_links']} | {p['access_count']} | {p['word_count']} |\n"
            md += "\n"
    
    md += """## Recommended Workflow

1. **Review CONDENSE candidates** — Extract patterns, move specifics to sources/
2. **Review ARCHIVE candidates** — Move stale project pages to `archive/`
3. **Check DISCARD candidates** — Verify no hidden value before deletion
4. **Consider CONVERGE pairs** — Merge fragmented similar content
5. **Maintain HIGH-VALUE pages** — These are your knowledge anchors

---

## Automation Scripts

```bash
# Run lifecycle detection
python3 _scripts/lifecycle_detect.py

# Apply condense recommendations (interactive)
python3 _scripts/lifecycle_condense.py --dry-run

# Apply archive recommendations
python3 _scripts/lifecycle_archive.py --dry-run
```

---

*Auto-generated by lifecycle detection pipeline. Manual review required.*
"""
    return md


def main():
    parser = argparse.ArgumentParser(description='Knowledge Lifecycle Detection Pipeline')
    parser.add_argument('--output-dir', type=Path, default=DEFAULT_OUTPUT,
                        help='Output directory for reports')
    parser.add_argument('--similarity-threshold', type=float, default=0.7,
                        help='Similarity threshold for convergence detection (0.0-1.0)')
    parser.add_argument('--json-only', action='store_true',
                        help='Only generate JSON report')
    args = parser.parse_args()
    
    # Ensure output directory exists
    args.output_dir.mkdir(parents=True, exist_ok=True)
    
    print("🔍 Scanning wiki pages...")
    pages = scan_wiki()
    print(f"   Found {len(pages)} pages")
    
    if not pages:
        print("   ⚠️ No pages found! Check wiki paths.")
        return
    
    print("🔗 Building link graph...")
    build_link_graph(pages)
    
    print("📊 Evaluating lifecycle candidates...")
    candidates = evaluate_candidates(pages)
    
    print(f"   ✅ RETAIN: {len(candidates['retain'])}")
    print(f"   📝 CONDENSE: {len(candidates['condense'])}")
    print(f"   📁 ARCHIVE: {len(candidates['archive'])}")
    print(f"   🚮 DISCARD: {len(candidates['discard'])}")
    
    print("🔍 Finding convergence opportunities...")
    convergence_pairs = find_convergence_candidates(pages, args.similarity_threshold)
    print(f"   Found {len(convergence_pairs)} potential merges")
    
    print("📄 Generating reports...")
    report = generate_report(candidates, pages, convergence_pairs)
    
    # Save JSON
    json_path = args.output_dir / "lifecycle-report.json"
    with open(json_path, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    print(f"   JSON: {json_path}")
    
    # Save Markdown
    if not args.json_only:
        md_path = args.output_dir / "lifecycle-report.md"
        markdown_report = generate_markdown_report(report)
        with open(md_path, 'w') as f:
            f.write(markdown_report)
        print(f"   Markdown: {md_path}")
    
    # Summary
    s = report['summary']
    print(f"\n" + "="*50)
    print(f"📊 LIFECYCLE SUMMARY")
    print(f"="*50)
    print(f"Total pages analyzed: {s['total_pages']}")
    print(f"✅ RETAIN:     {s['retain']:3d} ({s['retain']/s['total_pages']*100:5.1f}%)")
    print(f"📝 CONDENSE:   {s['condense']:3d} ({s['condense']/s['total_pages']*100:5.1f}%)")
    print(f"📁 ARCHIVE:    {s['archive']:3d} ({s['archive']/s['total_pages']*100:5.1f}%)")
    print(f"🚮 DISCARD:    {s['discard']:3d} ({s['discard']/s['total_pages']*100:5.1f}%)")
    print(f"🔗 CONVERGE:   {s['converge_pairs']:3d} pairs")
    print(f"="*50)


if __name__ == '__main__':
    main()
