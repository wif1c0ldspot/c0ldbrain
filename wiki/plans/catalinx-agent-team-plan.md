---
title: Catalinx Multi-Agent Team Deployment Plan
created: 2026-04-22
status: active
company: Catalinx (3 engineers, mobile apps)
stack: GCP + Cloudflare
priority: reference
updated: '2026-04-22'
confidence: medium
summary: Auto-generated placeholder for Catalinx Multi-Agent Team Deployment Plan
---

# Catalinx Agent Team — Deployment Plan

## Company Context
- **Team:** 3 engineers
- **Product:** Mobile applications
- **DNS:** Cloudflare
- **Cloud:** GCP
- **Goal:** Agent team for full-stack engineering, marketing, bookkeeping, documentation

---

## Phase 0: Foundation (Week 1–2)

### Infrastructure Setup
- **GCP Cloud Run** — host agent services (serverless, scales to zero, pay-per-use)
- **Pub/Sub** — async inter-agent messaging
- **Memorystore (Redis)** — short-term agent state, caching
- **Cloud SQL** — persistent data (bookkeeping, task state)
- **Secret Manager** — all API keys, credentials
- **Cloudflare Tunnel** — secure API exposure without open ports
- **Cloudflare AI Gateway** — proxy/cache LLM calls (cost savings + observability)

### Framework Selection
**Recommendation: LangGraph for production + CrewAI for rapid prototyping**

| Use Case | Framework | Why |
|----------|-----------|-----|
| Engineering workflow | LangGraph | Fine-grained state control, CI/CD integration |
| Marketing pipeline | CrewAI | Role-based agents, natural content chain |
| Bookkeeping | LangGraph | Audit trail, structured state, compliance |
| Documentation | CrewAI | Simple pipeline, fast to stand up |

### Model Routing (Cost Optimization)
| Tier | Model | Use For | Est. Cost/1M tokens |
|------|-------|---------|---------------------|
| Fast | GPT-4o-mini / Claude Haiku | Classification, routing, simple tasks | $0.15–$0.25 |
| Standard | GPT-4o / Claude Sonnet | Content, code, analysis | $3–$5 |
| Power | Claude Opus / o3 | Complex reasoning, architecture | $15–$30 |
| Vision | GPT-4o / Gemini Flash | UI analysis, document OCR | $0.15–$3 |

**Rule:** Route 80% of tasks to Fast tier. Reserve Power tier for <5% of tasks.

---

## Phase 1: Engineering Agents (Week 2–4)

### Architecture: Orchestrator-Worker Pattern
```
Product Spec / GitHub Issue
        ↓
  Planning Agent (Fast tier)
    ├── Task breakdown
    ├── Effort estimation  
    └── Branch assignment
        ↓
  ┌───────────────┼───────────────┐
  ↓               ↓               ↓
Frontend       Backend         DevOps
Agent           Agent           Agent
(React/Vue)    (API/DB)     (CI/CD/Infra)
  ↓               ↓               ↓
  └───────────────┼───────────────┘
                  ↓
        Code Review Agent (Standard tier)
                  ↓
        Test Agent (Fast tier — unit/integration)
                  ↓
        Security Scan Agent (Fast tier)
                  ↓
        Deploy Agent (Staging → Production)
                  ↓
        Monitor Agent (alerts, logs, errors)
```

### Agent Definitions

| Agent | Role | Model Tier | Tools | Human Gate |
|-------|------|-----------|-------|------------|
| **Planner** | Break specs into tasks, assign branches | Fast | GitHub Issues API, project board | ✅ Review plan |
| **Frontend** | Write UI code, components, styles | Standard | GitHub, linters, Storybook | ❌ Auto |
| **Backend** | API endpoints, DB schemas, logic | Standard | GitHub, DB tools, Postman | ❌ Auto |
| **DevOps** | Dockerfiles, CI/CD, Terraform | Standard | GitHub Actions, gcloud CLI | ✅ Apply infra |
| **Reviewer** | Code review, suggest fixes | Standard | GitHub PR API, linting | ✅ Approve PR |
| **Tester** | Generate + run tests | Fast | pytest, Jest, Playwright | ❌ Auto |
| **Security** | Vulnerability scanning | Fast | pip-audit, Snyk, OWASP | ✅ Fix critical |
| **Deploy** | Deploy to staging/prod | Fast | Cloud Run, Cloudflare API | ✅ Prod deploy |
| **Monitor** | Watch logs, alert on errors | Fast | Cloud Monitoring, PagerDuty | ❌ Auto (alert) |

### Engineering Workflow Integration
1. Engineer creates GitHub Issue with spec
2. Planner agent breaks it into sub-tasks, creates branches
3. Frontend/Backend agents implement on their branches
4. Agents open PRs → Reviewer agent reviews
5. Engineer reviews + approves
6. Tester agent runs full test suite
7. Security agent scans
8. Deploy agent pushes to staging (auto)
9. Engineer approves production deploy
10. Monitor agent watches for errors

### CI/CD Pipeline (GitHub Actions)
```yaml
on: [pull_request]
jobs:
  agent-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Agent Test Suite
        run: |
          pytest tests/ --junitxml=report.xml
      - name: Security Scan
        run: |
          pip-audit -r requirements.txt
      - name: Lint
        run: |
          ruff check .
```

---

## Phase 2: Marketing Agents (Week 4–6)

### Architecture: Pipeline Pattern (CrewAI)
```
Market Research Agent → Content Strategy Agent
                              ↓
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
   Blog Writer   Social Media   Email Campaign
   Agent         Agent          Agent
        ↓             ↓             ↓
        └─────────────┼─────────────┘
                      ↓
            SEO/Optimization Agent
                      ↓
            Analytics Agent (ROI tracking)
```

### Agent Definitions

| Agent | Role | Schedule | Output |
|-------|------|----------|--------|
| **Researcher** | Competitor analysis, trends, keywords | Daily @ 8am | Trend report (GCS) |
| **Strategist** | Content calendar, topic planning | Weekly Monday | Content calendar (Notion) |
| **Writer** | Blog posts, app descriptions, case studies | On-demand | Draft articles |
| **Social** | Tweets, LinkedIn posts, App Store updates | 3x/week scheduled | Social posts |
| **Email** | Newsletter, onboarding sequences | Weekly/biweekly | Email campaigns |
| **SEO** | Keyword optimization, meta descriptions | Per content piece | Optimized content |
| **Analytics** | Track engagement, conversions, ROI | Daily @ 9pm | Performance dashboard |

### Integrations
- **CMS:** WordPress/Ghost API or direct Webflow API
- **Social:** Buffer API or native X/LinkedIn APIs
- **Email:** Mailchimp/SendGrid API
- **SEO:** SerpAPI, Google Search Console API
- **Analytics:** Google Analytics 4 API
- **Images:** DALL-E 3 / Midjourney API

### Workflow
1. Researcher scans trends daily → saves to shared GCS bucket
2. Strategist builds weekly content calendar (human-approved)
3. Writer produces drafts from calendar
4. Social adapts content per platform
5. Email creates campaigns from content
6. SEO optimizes before publishing
7. Analytics tracks performance → feeds back to Strategist

---

## Phase 3: Bookkeeping Agents (Week 6–8)

### Architecture: Sequential + Guardrail Pattern (LangGraph)
```
Document Inbox (email/GCS upload)
        ↓
Receipt/Invoice Parser (Vision + OCR)
        ↓
Classification Agent (categorize expense/revenue)
        ↓
    ┌───────────┼───────────┐
    ↓           ↓           ↓
Match       Reconcile    Compliance
Agent       Agent        Agent
    ↓           ↓           ↓
    └───────────┼───────────┘
                ↓
        Journal Entry Agent (creates entries)
                ↓
        Reporting Agent (P&L, balance sheet, cash flow)
                ↓
        Advisory Agent (insights, forecasts, anomalies)
```

### Agent Definitions

| Agent | Role | Model | Human Gate |
|-------|------|-------|------------|
| **Parser** | Extract data from invoices/receipts/bank statements | Vision + Fast | ❌ Auto |
| **Classifier** | Categorize by type, department, project | Fast | ❌ Auto |
| **Matcher** | Match to POs, existing records | Fast | ❌ Auto |
| **Reconciler** | Match transactions to bank feeds | Standard | ✅ Flagged items |
| **Compliance** | Policy checks, anomaly detection | Standard | ✅ Anomalies |
| **Bookkeeper** | Create journal entries in accounting system | Fast | ✅ New vendors |
| **Reporter** | Generate financial reports | Standard | ❌ Auto |
| **Advisor** | Cash flow forecasts, budget variance | Standard | ✅ Action items |

### Integrations
- **Accounting:** Xero API or QuickBooks Online API
- **Banking:** Bank feed APIs, Stripe API
- **Documents:** Google Document AI / GCS for storage
- **Storage:** Cloud SQL for structured financial data
- **Reporting:** Google Sheets API or Looker Studio

### Singapore-Specific Considerations (if applicable)
- GST tracking and filing preparation
- IRAS compliance requirements
- SFRS for Small Entities reporting standards

### Security Requirements
- Financial agents on isolated VPC
- Read-only access to bank feeds (no write)
- Every journal entry has audit trail
- Anomaly threshold alerts to finance person
- Monthly human review of all agent-created entries

---

## Phase 4: Documentation Agents (Week 8–10)

### Architecture: Pipeline Pattern (CrewAI)
```
Code Commits / PR Merges
        ↓
Code Analysis Agent (reads changes)
        ↓
Doc Writer Agent (updates docs)
        ↓
    ┌───────────┼───────────┐
    ↓           ↓           ↓
API Docs    User Guide   Internal
Agent       Agent        Wiki Agent
    ↓           ↓           ↓
    └───────────┼───────────┘
                ↓
        Doc Review Agent (quality check)
                ↓
        Publish Agent (deploy to site/wiki)
```

### Output Targets
- **API documentation** — OpenAPI/Swagger auto-updated
- **User guides** — Markdown in Git, deployed to docs site
- **Internal wiki** — Confluence/Notion/GitHub Wiki
- **Changelogs** — Auto-generated from merge commits
- **Onboarding docs** — Developer onboarding materials

---

## Phase 5: Integration & Optimization (Week 10–12)

### Cross-Agent Communication
```
GCP Pub/Sub Topics:
  - agent.engineering.tasks
  - agent.marketing.tasks
  - agent.finance.tasks
  - agent.documentation.tasks
  - agent.notifications (cross-domain alerts)
```

### Shared Services
| Service | Purpose | Implementation |
|---------|---------|----------------|
| **Model Router** | Classify task → route to cheapest capable model | Cloud Function + Redis cache |
| **Memory Store** | Persistent agent memory, context | Memorystore + Cloud SQL |
| **Audit Logger** | Every agent action logged | Cloud Logging + BigQuery |
| **Cost Tracker** | Token usage per agent per task | Cloud Monitoring + dashboard |
| **Auth Gateway** | Agent identity, permissions | Cloudflare Zero Trust + IAM |
| **Notification Hub** | Alerts, approvals, summaries | Telegram / Slack webhook |

### Observability Stack
- **LangSmith** — Agent traces, prompt versioning, evaluation
- **Cloud Monitoring** — Infrastructure metrics, uptime
- **Cloudflare Analytics** — LLM API call metrics, caching
- **Custom Dashboard** — Cost per agent, task completion rate, error rate

### Cost Budget
| Category | Monthly Estimate |
|----------|-----------------|
| LLM API calls (mixed models) | $300–$1,200 |
| GCP Cloud Run (agent hosting) | $50–$200 |
| Pub/Sub, Redis, SQL, Storage | $30–$100 |
| Observability (LangSmith etc.) | $0–$150 |
| Third-party APIs (SEO, email, etc.) | $50–$200 |
| **Total** | **$430–$1,850/month** |

---

## Implementation Priority

### Immediate (This Week)
1. Set up GCP project + Cloud Run + Pub/Sub
2. Configure Cloudflare Tunnel + AI Gateway
3. Deploy first agent: **Planning Agent** for GitHub Issues
4. Set up model router with cost tracking

### Short-term (Week 2–4)
5. Build engineering agent team (Frontend, Backend, Reviewer, Tester)
6. Wire into GitHub Actions CI/CD
7. Add Security + Deploy agents

### Medium-term (Week 4–8)
8. Stand up marketing agent pipeline
9. Build bookkeeping agents with Xero/QBO integration
10. Add documentation agents

### Long-term (Week 8–12)
11. Cross-agent integration via Pub/Sub
12. Full observability dashboard
13. Cost optimization pass (model routing, caching)
14. Self-improvement loop (agent meta-optimization)

---

## Key Principles

1. **Start small, prove value** — 2-3 agents first, expand after ROI proven
2. **Human gates at critical decisions** — Deploy, financial entries, content publish
3. **Model routing saves 60-80%** — Most tasks don't need GPT-4o
4. **Serverless keeps costs low** — Cloud Run scales to zero when idle
5. **Audit everything** — Every agent action logged for compliance
6. **Security from day 1** — Least privilege, sandboxed tools, input validation
7. **Prompts as code** — Version controlled, tested, deployed via CI/CD
8. **Iterate weekly** — Review agent performance, optimize prompts, cut waste

---

## Security Checklist

- [ ] Each agent has own GCP service account (least privilege)
- [ ] Tool access restricted per agent role
- [ ] Financial agents on isolated VPC
- [ ] All agent actions audit-logged to BigQuery
- [ ] Prompt injection defenses (input sanitization, output filtering)
- [ ] Rate limiting on all agent APIs (Cloudflare WAF)
- [ ] Secret rotation via Secret Manager
- [ ] Code execution in sandboxed containers
- [ ] Approval gates for destructive operations
- [ ] Monthly security review of agent permissions
