---
name: hr-compliance
description: US 50-state employment-law lookups for HR, recruiting, payroll, and policy work. Use this skill whenever the user asks about state-specific minimum wage, overtime, paid sick leave, family leave, vacation payout, pay-transparency posting requirements, discrimination protections, background-check / ban-the-box laws, drug testing, non-competes, workplace safety, or upcoming employment-law changes. Triggers on phrases like "what's the minimum wage in CA", "is my job posting compliant in CO", "do I need to disclose salary in NY", "ban the box rules in MA", "compare NJ vs NY parental leave", "what changed for WA employers in 2026". Also use this skill proactively any time you see job postings, offer letters, employee handbooks, or compensation analyses being authored or reviewed.
---

# HR Compliance Skill

You have access to the HR Compliance MCP server (or REST API surface — both expose the same tool names and shapes). It covers 9 priority US states today (CA, NY, CO, WA, MA, IL, NJ, OR, ME) with the remaining 41 + DC on the public roadmap.

## When to use

Trigger this skill **proactively** for:

1. Any state-specific employment-law question — wages, overtime, leave, posting requirements, protections
2. Compliance review of job postings, offer letters, handbooks, separation agreements
3. Multi-state expansion questions ("we're hiring in WA and CA, what differs?")
4. Cross-checking AI-generated HR copy before the user ships it
5. Picking up on freshness signals ("did anything change recently in...")

Do NOT use for: federal-only questions (FLSA, Title VII, FMLA basics) where the user is clearly asking about the federal floor — answer those from general knowledge unless the user's situation crosses into state-specific territory.

## Tool map

### Wage & Hour (Tier 1 — available on all plans)

| Tool | When to call |
|------|--------------|
| `get_minimum_wage` | "What's minimum wage in X" / paychecks / offer-letter sanity checks |
| `get_overtime_rules` | OT calculations, exempt vs non-exempt classification, scheduling questions |
| `get_pay_frequency_requirements` | Payroll-cadence design, payday timing |
| `get_pay_transparency_rules` | Job-posting reviews, salary-range disclosure, ATS compliance |
| `compare_wages_across_states` | Multi-state pay benchmarking, location-based offer differentials |

### Leave (Tier 2 — all plans)

| Tool | When to call |
|------|--------------|
| `get_paid_sick_leave` | Sick-time policy, accrual rates, eligibility |
| `get_family_leave` | Parental/family-medical leave beyond federal FMLA |
| `get_vacation_payout_rules` | Termination payouts, "use it or lose it" policy validity |
| `get_voting_leave` | Election-day time-off requirements |
| `get_bereavement_leave` | Grief leave mandates |

### Compliance & Protections (Tier 3 — Pro plan)

| Tool | When to call |
|------|--------------|
| `get_discrimination_protections` | Hiring/firing decisions, EEO policy, protected-class questions beyond federal |
| `get_background_check_laws` | Pre-hire screening, ban-the-box / fair-chance ordinances |
| `get_drug_testing_rules` | Pre-employment / random testing, marijuana protections |
| `get_noncompete_rules` | Employment agreements, separation agreements, enforceability checks |
| `get_workplace_safety` | OSHA-state-plan questions, unique state safety mandates |

### Intelligence (Tier 4 — Pro plan)

| Tool | When to call |
|------|--------------|
| `get_recent_changes` | "What's new in X since [date]" / refresh-aware compliance reviews |
| `compare_state_compliance` | Multi-state expansion, picking which state to incorporate / hire in |
| `get_compliance_calendar` | Q&A about upcoming effective dates (e.g. Maine LD 54 on 2026-07-29) |
| `search_employment_law` | Free-text exploration when the user's question doesn't map to a single tool |

## Working pattern

1. **Identify the state(s)**. If the user names a city, infer the state. If multi-state ambiguous, ask for the ones they care about.
2. **Pick the tightest tool** for the question — don't call `search_employment_law` when `get_minimum_wage` will do.
3. **Cite returned data verbatim** in your answer (numbers, effective dates, citations). Do not paraphrase dollar figures or legal thresholds.
4. **Surface the `notes` field**. The MCP returns regulatory caveats (e.g. "Maine DOL rulemaking pending") that are critical context — pass them through to the user, never hide them.
5. **For freshness-sensitive answers**, follow up with `get_recent_changes` so the user knows what's moved recently.

## Multi-state queries

When the user asks about more than one state, prefer the comparison tools — `compare_wages_across_states` or `compare_state_compliance` — over N separate calls. The comparison tools return ranked, side-by-side data that's easier to act on.

## Pre-effective-date awareness

Some laws are signed but not yet effective (e.g. Maine LD 54 — signed 2026-04-24, effective 2026-07-29). The data layer already handles this: pay-transparency lookups return the effective date and the rulemaking status. When a user asks "do I need to comply right now in Maine?", check the effective date in the response and answer accordingly — do not assume a returned rule is currently enforceable.

## Escalation

If the user is making a real legal decision (firing someone, signing a contract, filing a complaint), recommend they verify with employment counsel in addition to using these tools. The data is research-grade, not legal advice.

## Coverage limits

When a user asks about a state outside the 9 covered (anywhere except CA, NY, CO, WA, MA, IL, NJ, OR, ME), the tools will return an error with the supported list. Pass that through and offer to research from the federal floor + general knowledge with the caveat that you can't verify against the live state-law database.
