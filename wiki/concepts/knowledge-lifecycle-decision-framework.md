---
confidence: high
created: '2026-04-16'
date: 2026-04-18
priority: reference
status: current
summary: Systematic framework for evaluating when knowledge becomes outdated, when
  it retains value, and how to action it through discard, condense, or converge decisions.
  Addresses the Camp 2 context substrate growth problem.
tags:
- knowledge-management
- curation
- decision-framework
- memory-lifecycle
- context-substrate
title: Knowledge Lifecycle Decision Framework
type: concept
updated: '2026-04-18'
---


# Knowledge Lifecycle Decision Framework

## The Problem

Camp 2 context substrates (C0ldbrain wiki, OpenClaw MEMORY.md, Thoth personal KG) accumulate without bound. Unlike Camp 1 vector databases where recall degrades with size, Camp 2 systems hit context window limits and attention dilution. The question is not "can we store it?" but "should we keep it, and in what form?"

## Part 1: What Makes Knowledge Outdated vs. Enduring

### Knowledge Decay Factors (What Kills Value)

| Factor | Mechanism | Example |
|--------|-----------|---------|
| **Temporal Obsolescence** | Time-bound facts expire naturally | "iPhone 14 price is $799" (prices change) |
| **Version Supersession** | New releases invalidate old documentation | Python 3.9 asyncio patterns vs 3.13 |
| **Context Drift** | Original context becomes irrelevant | "Current sprint goal: refactor auth" (sprint ended) |
| **Dependency Rot** | External systems change, breaking relevance | AWS API v1 docs when v2 launches |
| **Solved Problem** | Issue resolved, workaround no longer needed | Bug workaround for fixed vulnerability |
| **Ephemeral State** | Transient system conditions | "Redis connection pool at 80%" (momentary) |
| **Failed Prediction** | Forecasts that didn't materialize | "Q3 revenue will grow 20%" (missed) |
| **Abandoned Project** | Initiative cancelled, context orphaned | "Project Phoenix architecture" (cancelled) |

### Knowledge Endurance Factors (What Retains Value)

| Factor | Mechanism | Example |
|--------|-----------|---------|
| **First Principles** | Underlying truths independent of implementation | CAP theorem, FLP impossibility |
| **Pattern Recognition** | Recurring solution templates | Circuit breaker pattern, saga pattern |
| **Causal Models** | Mechanism explanations that transfer | "Why async/await reduces thread contention" |
| **Decision Rationale** | Why choices were made, with tradeoffs | "Chose PostgreSQL over MySQL for JSONB support" |
| **Failure Analysis** | Root causes with transferable lessons | Postmortem: cascade failure from single point |
| **Validated Heuristics** | Rules that survived multiple applications | "Always validate at system boundaries" |
| **Connection Graph** | Links between concepts that enable discovery | Seeing emergent-agent evolution connects to quantization research |
| **Historical Trajectory** | How understanding evolved over time | "We believed X until Y evidence changed view" |

### The Critical Distinction

**Outdated knowledge** = specific, time-bound, implementation-dependent facts that lose utility when conditions change.

**Enduring knowledge** = patterns, principles, and decision frameworks that transfer across contexts and compound with new experiences.

The same *topic* can produce both:
- "Gemma 4 launched April 2025" → **outdated** (temporal)
- "Model routing by capability tier outperforms single-model approaches" → **enduring** (pattern)

## Part 2: Knowledge Valuation Dimensions

Evaluate every piece of knowledge across six dimensions:

### 1. Reference Frequency (Access Pattern)
- **High**: Consulted weekly+ for active work
- **Medium**: Consulted monthly for reference
- **Low**: Rarely accessed, mostly archival
- **Never**: Not accessed since creation

### 2. Confidence Stability (Truth Durability)
- **Stable**: Core principles, unlikely to change
- **Evolving**: Active area with new developments
- **Volatile**: Rapidly changing, version-dependent
- **Superseded**: Known to be outdated

### 3. Transfer Potential (Reusability)
- **Universal**: Applies across domains
- **Domain**: Applies within knowledge domain
- **Project**: Specific to one context
- **Moment**: Single-use, never reusable

### 4. Connection Density (Graph Value)
- **Hub**: Central node linking many concepts
- **Bridge**: Connects two clusters
- **Leaf**: Single connection, peripheral
- **Orphan**: No connections, isolated

### 5. Synthesis Depth (Compression Level)
- **Raw**: Primary source, unprocessed
- **Summarized**: Condensed from source
- **Synthesized**: Combined multiple sources
- **Crystallized**: Distilled to reusable pattern

### 6. Decision Dependency (Action Relevance)
- **Critical**: Directly impacts current decisions
- **Supporting**: Informs but doesn't decide
- **Historical**: Explains past, not current
- **None**: No decision relevance

## Part 3: Decision Matrix

Based on valuation dimensions, apply one of four actions:

| Valuation Profile | Action | Criteria |
|-------------------|--------|----------|
| **High frequency + Stable + Universal + Hub** | **RETAIN** | Core knowledge, actively used, highly connected |
| **Medium frequency + Evolving + Domain + Bridge** | **CONDENSE** | Keep essence, compress detail, maintain links |
| **Low frequency + Volatile + Project + Leaf** | **ARCHIVE** | Move to archive/, preserve but deprioritize |
| **Never + Superseded + Moment + Orphan** | **DISCARD** | Delete or merge into higher-value content |

### Detailed Decision Rules

#### RETAIN (Keep As-Is)
**Trigger**: 4+ of these conditions
- [ ] Accessed within last 14 days
- [ ] Referenced by 3+ other pages
- [ ] Contains first principles or patterns
- [ ] Decision-critical for active work
- [ ] High synthesis depth (crystallized)
- [ ] Stable confidence (not version-dependent)

**Action**: No change. Continue maintenance.

---

#### CONDENSE (Compress & Elevate)
**Trigger**: 3+ of these conditions
- [ ] Medium reference frequency (monthly)
- [ ] Contains both enduring and outdated elements
- [ ] Too verbose for utility (can compress 50%+)
- [ ] Bridge node connecting two concepts
- [ ] Evolving confidence (active area)
- [ ] Raw or summarized depth (not yet crystallized)

**Action**: 
1. Extract enduring patterns/principles
2. Remove temporal specifics (dates, versions)
3. Compress implementation details to essentials
4. Add links to canonical sources for details
5. Mark as `condensed: 2026-04-18`

**Example transformation**:
```
BEFORE (800 words):
"On April 12, 2025, Anthropic released Claude 3.5 Sonnet. 
The pricing was $3/$15 per million tokens. We tested it 
on our customer support chatbot and found it reduced 
escalations by 23%..."

AFTER (150 words):
"Claude 3.5 Sonnet (2025) demonstrated that mid-size 
models can outperform larger models on specific tasks 
when fine-tuned for the domain. Key pattern: task-appropriate 
sizing outperforms raw capability for bounded problems. 
[See full evaluation: [[claude-35-evaluation-2025]]]"
```

---

#### CONVERGE (Merge Related)
**Trigger**: 2+ of these conditions
- [ ] Multiple pages on same narrow topic
- [ ] Content overlaps >60% semantically
- [ ] Each page has low individual value
- [ ] Better understood as single synthesized view
- [ ] Fragmented understanding across pages

**Action**:
1. Identify primary page (most comprehensive or linked)
2. Merge unique insights from secondary pages
3. Update all inbound links to primary
4. Redirect or delete secondary pages
5. Mark merge event in edit history

---

#### ARCHIVE (Deprioritize)
**Trigger**: 3+ of these conditions
- [ ] Not accessed in 90+ days
- [ ] Project-specific, project inactive
- [ ] Version-dependent, version deprecated
- [ ] No inbound links (orphan or leaf)
- [ ] Superseded by newer content
- [ ] Historical value only

**Action**:
1. Move to `archive/` directory
2. Add `status: archived` to frontmatter
3. Add archival reason to header
4. Preserve but remove from main index
5. Exclude from active search/retrieval

---

#### DISCARD (Delete)
**Trigger**: 2+ of these conditions
- [ ] Never accessed since creation
- [ ] Known incorrect or superseded
- [ ] Duplicates other content exactly
- [ ] No connections, no value
- [ ] Ephemeral state with no historical relevance
- [ ] Failed experiment or abandoned line

**Action**:
1. Verify no inbound links exist
2. Check for unique insights worth preserving
3. If none: delete file
4. If insights exist: merge into relevant page first
5. Mark deletion in log.md

## Part 4: Domain-Specific Decay Curves

Different knowledge types have different natural half-lives:

| Knowledge Type | Decay Rate | Review Cadence | Action Bias |
|----------------|------------|----------------|-------------|
| **API Documentation** | Fast (3-6 months) | Monthly | Condense aggressively |
| **Architecture Decisions** | Slow (2-5 years) | Quarterly | Retain with ADR format |
| **Bug Workarounds** | Fast (until fixed) | Weekly | Archive when resolved |
| **Research Papers** | Medium (1-2 years) | Bi-annually | Synthesize to patterns |
| **Meeting Notes** | Very Fast (1-4 weeks) | Weekly | Condense or discard |
| **Personal Learnings** | Variable | Monthly | Condense to heuristics |
| **Security Vulnerabilities** | Fast (until patched) | Weekly | Supersede when fixed |
| **Tool Configurations** | Medium (6-12 months) | Quarterly | Version in filename |

## Part 5: Implementation for C0ldbrain

### Automated Detection Pipeline

```python
# Pseudocode for knowledge lifecycle detection

def evaluate_knowledge_page(page):
    metrics = {
        'last_accessed': get_access_log(page),
        'inbound_links': count_backlinks(page),
        'outbound_links': count_outlinks(page),
        'age_days': (now - page.created).days,
        'last_modified': (now - page.updated).days,
        'word_count': len(page.content),
        'synthesis_score': detect_crystallization(page),
        'temporal_references': count_date_mentions(page),
        'version_mentions': count_version_refs(page),
    }
    
    # Decision logic
    if should_retain(metrics):
        return Action.RETAIN
    elif should_condense(metrics):
        return Action.CONDENSE
    elif should_converge(metrics):
        return Action.CONVERGE
    elif should_archive(metrics):
        return Action.ARCHIVE
    else:
        return Action.DISCARD
```

### Frontmatter Integration

Add lifecycle tracking to page frontmatter:

```yaml
---
title: "Async Python Patterns"
created: 2024-03-15
updated: 2026-04-18
confidence: high
status: current  # current | condensed | archived | superseded
lifecycle:
  last_reviewed: 2026-04-18
  review_cadence: quarterly
  access_count: 47
  last_accessed: 2026-04-17
  condense_candidate: false
  archive_candidate: false
---
```

### Health Dashboard Integration

Extend `wiki-health-monitoring` to include:
- Condense candidates: pages >1000 words, low access, medium age
- Archive candidates: no access 90+ days, project-specific, no links
- Converge candidates: semantic similarity >0.8 between pages
- Discard candidates: orphans, never accessed, superseded

### Manual Review Workflow

1. **Weekly**: Review auto-flagged candidates
2. **Monthly**: Run full lifecycle analysis
3. **Quarterly**: Deep review of architecture decisions
4. **Annually**: Archive review (restore or purge)

## Part 6: Principles to Remember

1. **Never delete without checking connections** — orphaned knowledge may still have value
2. **Preserve decision rationale even when outdated** — why we chose X matters even when we choose Y now
3. **Condense, don't just truncate** — extract the enduring insight, don't just cut words
4. **Temporal specifics belong in sources/** — wiki/concepts/ should be timeless patterns
5. **Version in filename for fast-moving topics** — `python-async-2025.md` not `python-async.md`
6. **Archived ≠ deleted** — move aside, don't destroy; restore if needed
7. **Growth is not the goal** — signal-to-noise ratio is

## Related Concepts

- [[knowledge-management-handbook-2026]] — Memory lifecycle, consolidation tiers
- [[context-substrate]] — Camp 2 accumulation problem
- [[memory-systems]] — Confidence decay, supersession
- [[wiki-health-monitoring]] — Automated health detection
- [[supersession-protocol]] — Formal contradiction handling

## Sources

- [[agent-memory-two-camps-witcheer-2026-04]] — OpenClaw dreaming, consolidation thresholds
- [[llm-wiki-v2-rohitg00]] — Confidence decay, forgetting curves
- [[karpathy-llm-wiki-agent]] — raw/wiki pattern
