# HR Compliance MCP — 50-State US Employment Compliance Stack

## What is this

A three-layer employment-compliance product for small businesses, HR consultants, payroll providers, and AI-assistant users:

1. **MCP server** (this package, `hr_compliance_mcp/`) — 19 tools for querying US employment law by state. Open source, drives awareness.
2. **REST API** (to build, `api/`) — HTTP/JSON wrapper around the same data. Paid tiers via Stripe. Self-hosted + own Stripe, **not** marketplace-dependent.
3. **Claude Code Skill Pack** (to build, `skill/`) — SKILL.md bundle so any Claude Code user can drop compliance intelligence into their agent workflow with one command. First-mover in the verifiable-MRR Skills category.

All three share the same compliance data layer. They compound: the MCP server + Skill Pack get organic dev-channel distribution; the REST API monetizes serious users who need SLAs, change alerts, and programmatic access.

## Source opportunity

Selected from `C:/GO-CRAZY/discovery/sprint-2026-04-17-v2.md` items **#1 (HIGH — API), #2 (HIGH — Skill Pack), #3 (HIGH — Niche Data / Pay Transparency extension)**. Those three opportunities were ranked as independent until the user noted they compound into one complete product. This CLAUDE.md reflects that merged vision.

**Why this one:**
- Uncontested lane: 5 nearby compliance MCP servers checked (Ansvar-Systems, US_Compliance_MCP, JamesANZ, TCoder920x, America's Law Graph), none cover employment law
- Fragmented-data moat is the strongest on the evaluated list: 50 state DOLs + hundreds of local jurisdictions + 48 documented changes for 2026 alone
- Anthropic Legal Plugin (2026-01-30) collapsed the legal-research wedge; employment-compliance is untouched
- Skills ecosystem is nascent-but-real (4,200+ skills on claudemarketplaces.com, GitHub `gh skill install` CLI shipped 2026-04-16) with no published MRR yet — first-mover window is narrow

## Who it's for

- **Primary buyers**: HR tech startups (need embeddable compliance), small HR consultancies, PEOs, payroll companies, multi-state small businesses, employment lawyers, fractional HR professionals
- **Where they live**: r/mcp (Mahender's proven sub), r/ClaudeAI, r/SaaS, HN Show HN, ProductHunt, GitHub, claudemarketplaces.com, Agent37 / SkillHQ listings
- **Who buys the Skill Pack specifically**: Claude Code users building HR tech or internal compliance tools — reachable via the same channels plus #buildinpublic on X

## Revenue model

- **Free tier** (distribution):
  - Open-source MCP server — self-host, drives Reddit/HN virality
  - Claude Code Skill Pack (baseline) — free on GitHub, listed on claudemarketplaces.com + Agent37 + SkillHQ
- **Paid REST API** (primary revenue):
  - Starter: $49/mo — 1,000 queries/mo, 10 priority states, wage/hour + leave laws only
  - Pro: $99/mo — 5,000 queries/mo, all 50 states + DC, all categories, change-log feed
  - Business: $199/mo — 25,000 queries/mo, webhook alerts on law changes, SLA, multi-tenancy
- **Self-hosted enterprise**: $499/mo — unlimited on-prem, support SLA, compliance attestation
- **Skill Pack Pro** (one-time or subscription):
  - $29 one-time for premium Skill bundle (advanced workflows, audit templates, multi-state comparison agents), OR $9/mo via Gumroad/LemonSqueezy for continuous updates
- **Payment processor**: Stripe direct. Never MCPize, Agent37-billing, or any marketplace-held revenue (those are unverified per feedback_mcpize_reality.md)

## Stack

- **Language**: Python 3.10+
- **MCP server**: FastMCP (same pattern as `C:/GO-CRAZY/legal-mcp/`, proven — 18 tools, viral on Reddit)
- **REST API** (to add): FastAPI + Uvicorn, shared service layer with MCP server
- **Skill Pack** (to add): Plain SKILL.md + supporting markdown in `skill/` directory, references the MCP/REST endpoints
- **Data store**: JSON/YAML files per state for now (already working); migrate to SQLite when we need multi-tenant API rate-limiting
- **Tests**: pytest (existing test suite, 7 test files)
- **CI**: GitHub Actions (existing, `.github/workflows/ci.yml`)
- **Regulatory-text parsing**: Ollama on 3090 for dense state-DOL text (planned for data-refresh pipeline, not runtime)
- **Billing**: Stripe + Stripe webhooks, API-key gating via signed JWTs or a simple `api_keys` table

## Directory structure (current + planned)

Current (committed):
```
hr-compliance-mcp/
├── hr_compliance_mcp/
│   ├── src/
│   │   ├── server.py          # FastMCP server, 19 tools, 2 resources
│   │   ├── compliance.py      # discrimination, background check, drug testing, noncompete, safety
│   │   ├── leave.py           # sick, family, vacation, voting, bereavement
│   │   ├── wages.py           # min wage, OT, pay frequency, pay transparency
│   │   ├── intelligence.py    # recent changes, compliance calendar, state comparison, search
│   │   ├── models.py          # 15 data models
│   │   ├── config.py          # env, tier gating
│   │   ├── __init__.py
│   │   └── __main__.py
│   └── tests/                 # 7 test files, all passing
├── .github/workflows/ci.yml   # CI passing
├── .mcp.json
├── pyproject.toml
├── README.md
├── CLAUDE.md                  # this file
├── .gitignore
└── docs/
```

Planned additions (Phase 2):
```
hr-compliance-mcp/
├── api/                       # FastAPI REST wrapper (new)
│   ├── app.py
│   ├── auth.py                # API key auth + Stripe-backed entitlements
│   ├── routes/                # endpoints mirroring MCP tools
│   └── tests/
├── skill/                     # Claude Code Skill Pack (new)
│   ├── SKILL.md               # main skill definition
│   ├── references/
│   │   ├── state-data-formats.md
│   │   └── workflow-examples.md
│   └── assets/                # example outputs, templates
├── data/                      # migrate from inline constants to files
│   ├── wages/<state>.yaml
│   ├── leave/<state>.yaml
│   └── compliance/<state>.yaml
├── billing/                   # Stripe integration (new)
│   ├── webhook.py
│   └── entitlements.py
└── LAUNCH.md                  # per ship-product skill Phase 3
```

## How to run

```bash
# install (existing, works)
pip install -e ".[dev]"

# tests
pytest

# run the MCP server (stdio)
python -m hr_compliance_mcp.src
```

Once the REST API lands:
```bash
# dev server
uvicorn api.app:app --reload
```

## Current state (as of 2026-04-17)

**Built and tested:**
- 19 MCP tools across wage/hour, leave, compliance (discrimination/BG/drug/noncompete/safety), and intelligence (change log, calendar, search, comparison)
- 2 MCP resources exposed
- 8 priority states with full data coverage (CA, NY, CO, WA, MA, IL, NJ, OR)
- 15 data models
- Tier gating tests (Starter vs Pro access control — already in place)
- GitHub Actions CI green
- 10 clean commits on main

**Not yet built:**
- REST API layer (FastAPI)
- Stripe billing + API-key auth
- Claude Code Skill Pack
- Pay-transparency-specific endpoint with compliance-check logic (the #3 extension from the sprint)
- Remaining 42 states + DC
- Webhook change-alert feed for Pro tier
- LAUNCH.md with platform posts
- Public deployment (Fly.io / Railway / Render)

## Next tasks (priority order)

1. **Ship the MCP server publicly** — push current state to `github.com/<user>/hr-compliance-mcp`, list on claudemarketplaces.com + Agent37 + SkillHQ. No paid tier yet, just distribution.
2. **Build the Skill Pack** (`skill/SKILL.md`) — thin wrapper over the MCP server that gives Claude Code users pre-baked workflows: "check if this job posting complies with pay transparency in state X", "compare sick leave rules across states A/B/C", "compliance calendar for my company's states". This is the first-mover bet in the Skills-as-monetization market.
3. **Wrap as REST API** (`api/`) — FastAPI layer calling the same service functions the MCP server uses. Read-only endpoints, same tier gating, API-key auth.
4. **Stripe integration** — checkout page, webhook handler, API key issuance on successful subscription. Starter + Pro tiers only for v1.
5. **Pay-transparency compliance endpoint** — the #3 extension. Takes a job posting (salary range, state, locality) and returns pass/fail + jurisdiction-specific violations. $10K/violation penalty angle, EU Directive June 2026.
6. **Fill to 50 states** — wage/hour first (highest query volume), then leave, then compliance. Scripted scrape + Ollama parsing + manual review.
7. **Deploy** (Fly.io likely — one-command, cheap, good DX), put behind custom domain.
8. **Run ship-product's Phase 3** to generate LAUNCH.md with platform-tailored posts.

Each next-task should land as a test-first commit. No impl without a failing test that motivated it.

## Known constraints

- Mahender is on F1 STEM OPT; income flows through professor LLC, no W-2 outside OPT employer.
- No Claude co-author trailers, no "generated with Claude Code" stamps in any commit, README, CLAUDE.md, LAUNCH.md, or public-facing text (per `feedback_no_coauth.md`).
- Open source + paid tier pattern. Own Stripe. Never depend on MCPize / Agent37 / SkillHQ for revenue — those are distribution, not billing (per `feedback_mcpize_reality.md`).
- Anthropic may ship a native HR/employment Plugin in the future. Monitor `claude.com/plugins` monthly. If they do, the wedge shifts to pay-transparency / multi-state / jurisdictional niches (see `project_anthropic_native_plugins.md`).
- Distribution must match audience: dev-channel first (r/mcp, r/ClaudeAI, HN, GitHub, claudemarketplaces.com). HR-consultant channels (r/humanresources, LinkedIn HR groups) are secondary and should come AFTER dev-channel validation — don't repeat the trades-mcp mistake of posting to the audience that isn't on Reddit.

## What NOT to touch without explicit ask

- `hr_compliance_mcp/src/models.py` — 15 data models already shape all downstream code + tests. Additive changes OK; structural renames break everything.
- `hr_compliance_mcp/tests/test_tier_gating.py` — pins the Starter/Pro access contract. Breaking this changes pricing surface area.
- Production Stripe keys (when they exist) — live in `.env.production`, gitignored. Only Mahender edits.

## Useful context from the lab

- `C:/GO-CRAZY/CLAUDE.md` — lab-level workspace overview
- `C:/GO-CRAZY/discovery/sprint-2026-04-17-v2.md` — the refined sprint that ranks items #1/#2/#3 as the chosen bet
- `C:/GO-CRAZY/legal-mcp/` — reference implementation. Same FastMCP pattern, viral on Reddit. Re-read its launch posts for tonal calibration before drafting this project's LAUNCH.md.
- `C:/Users/mahen/.claude/projects/C--GO-CRAZY/memory/` — feedback + project memory, applies here.
- `C:/Users/mahen/.claude/skills/ship-product/` — end-to-end scaffold/build/launch skill. Phase 3 (LAUNCH.md) is the natural follow-up to Next Task #7.
