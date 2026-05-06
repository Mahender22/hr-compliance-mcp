# HR Compliance MCP

[![CI](https://github.com/Mahender22/hr-compliance-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/Mahender22/hr-compliance-mcp/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-64%20passing-brightgreen.svg)]()

**The first US employment-law MCP server for AI assistants.**

Connect Claude, GPT, Cursor, or any MCP-compatible AI to 50-state employment compliance data. Minimum wage, overtime, paid leave, pay transparency, discrimination, background checks, non-competes, safety — all queryable in seconds, not hours of DOL site spelunking.

---

## 30-Second Demo

```
You:  Is this California job posting compliant?
      "Senior Backend Engineer — remote, salary TBD, 200-person company"

HR-Compliance-MCP:  No — 1 violation found.

  California requires a salary range in all public job postings for
  employers with 15+ employees.

  Cal. Lab. Code § 432.3 — penalty $100-$10,000 per violation.
  Effective 2023-01-01. Your employer size (200) is well over the
  15-employee threshold.

  Fix: add a posted salary range before publishing.
```

## Why HR-Compliance-MCP?

| | Old way | AI + HR-Compliance-MCP |
|---|---|---|
| Check if a job posting is legal | Read 9 state DOL pages | *"Is this posting compliant in CA?"* |
| Compare sick leave rules across states | 3 hours + a spreadsheet | *"Compare CA, NY, CO sick leave."* |
| Track what changed this quarter | Subscribe to legal newsletters ($200/mo) | *"What employment laws changed in 2026?"* |
| Build compliance into your ATS | Hire a consultant | Call it from your own code |
| Monthly cost | $200-800 (ComplyRight, XpertHR, counsel) | **Free** |

## Quick Start

### Install

```bash
# Create and activate a virtual environment
python -m venv hr-mcp-env

# Windows
hr-mcp-env\Scripts\activate

# Mac/Linux
source hr-mcp-env/bin/activate

# Install from GitHub (PyPI release coming soon)
pip install git+https://github.com/Mahender22/hr-compliance-mcp.git
```

### Run

```bash
hr-compliance-mcp
```

To try it without configuring anything, demo mode runs on the pre-loaded 9-state dataset:

```bash
# Mac/Linux
export HR_MCP_DEMO=true

# Windows
set HR_MCP_DEMO=true

hr-compliance-mcp
```

### Connect to Claude Desktop

Add to your `claude_desktop_config.json`:

**Windows** (`%APPDATA%\Claude\claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "hr-compliance": {
      "command": "C:/path/to/hr-mcp-env/Scripts/hr-compliance-mcp.exe"
    }
  }
}
```

**Mac/Linux** (`~/Library/Application Support/Claude/claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "hr-compliance": {
      "command": "/path/to/hr-mcp-env/bin/hr-compliance-mcp"
    }
  }
}
```

### Connect to Claude Code

```bash
# Mac/Linux
claude mcp add hr-compliance -- hr-compliance-mcp

# Windows
claude mcp add hr-compliance -- C:\path\to\hr-mcp-env\Scripts\hr-compliance-mcp.exe
```

### Connect to Cursor / Windsurf

Works with any MCP-compatible client. Add the `hr-compliance-mcp` command to your tool's MCP server configuration.

## Configuration

| Variable | Required | Description |
|----------|----------|-------------|
| `HR_MCP_DEMO` | Optional | Set `true` to run on the bundled 9-state dataset with no setup |
| `HR_MCP_TIER` | Optional | `starter` or `pro` (default: `pro`). Starter exposes wage/hour + leave; Pro adds intelligence tools and all categories |

## All 19 Tools

### Wage & Hour

| Tool | What it does |
|------|--------------|
| `get_minimum_wage` | State + local minimum wage, tipped wage, scheduled increases |
| `get_overtime_rules` | Daily vs weekly thresholds, multipliers, exemptions |
| `get_pay_frequency_requirements` | How often employers must pay (weekly/bi-weekly/monthly) |
| `get_pay_transparency` | Salary-range posting rules, thresholds, penalty ranges |

### Leave

| Tool | What it does |
|------|--------------|
| `get_sick_leave` | Accrual rate, cap, carryover, eligible employers |
| `get_family_leave` | State FMLA variants, job protection, paid vs unpaid |
| `get_vacation_policy` | Use-it-or-lose-it legality, PTO payout on termination |
| `get_voting_leave` | Paid/unpaid time off to vote |
| `get_bereavement_leave` | Mandatory bereavement rules |

### Compliance

| Tool | What it does |
|------|--------------|
| `get_discrimination_law` | Protected classes beyond federal Title VII |
| `get_background_check_rules` | Ban-the-box, consent, disclosure requirements |
| `get_drug_testing_rules` | Pre-employment, random, post-accident legality |
| `get_noncompete_rules` | Enforceability, income thresholds, blue-pencil rules |
| `get_safety_requirements` | State OSHA variants, poster requirements |

### Intelligence

| Tool | What it does |
|------|--------------|
| `get_recent_changes` | Laws that changed in the last N days |
| `get_compliance_calendar` | Upcoming effective dates across a date range |
| `compare_states` | Diff two states on any topic |
| `search_employment_law` | Full-text search across all data |
| `get_state_summary` | Everything on file for one state |

## Coverage

### Live States (9)

California (CA), New York (NY), Colorado (CO), Washington (WA), Massachusetts (MA), Illinois (IL), New Jersey (NJ), Oregon (OR), Maine (ME — LD 54, effective 2026-07-29).

These 9 states cover the densest pay-transparency, sick-leave, and non-compete requirements in the country. Maine LD 54 was signed 2026-04-24 and is included now so you can plan ahead of the July 29 effective date — implementation details are pending Maine DOL rulemaking and clearly flagged in the data.

### Pipeline

The remaining 41 states + DC are on the roadmap, with wage/hour data scheduled first (highest query volume), then leave, then full compliance coverage. Data is scraped from state DOL sites, parsed locally, and reviewed before publishing — no LLM hallucinations in the shipped data.

## How It Works

```
┌──────────────┐     MCP      ┌──────────────────┐     local     ┌──────────────┐
│              │  ──────────►  │                  │  ──────────►  │              │
│  Claude /    │   Tool calls  │  HR-Compliance   │    lookup     │  9-state     │
│  GPT /       │  ◄──────────  │   MCP Server     │  ◄──────────  │  dataset     │
│  Cursor      │    Results    │   (your PC)      │    + cites    │  + penalties │
└──────────────┘               └──────────────────┘               └──────────────┘
```

Runs entirely on your machine. No API keys, no telemetry, no data leaves your box.

## Pricing

**The MCP server is free and open source.** MIT licensed, all 19 tools.

A paid REST API with the same data is planned — HTTP/JSON surface, usage-based billing, webhook alerts when state laws change. [Join the waitlist](https://github.com/Mahender22/hr-compliance-mcp/issues) or watch this repo.

## Development

```bash
git clone https://github.com/Mahender22/hr-compliance-mcp.git
cd hr-compliance-mcp
pip install -e ".[dev]"

# Run tests (64 passing)
pytest

# Run server locally
python -m hr_compliance_mcp
```

## License

[MIT](LICENSE) — use it however you want.
