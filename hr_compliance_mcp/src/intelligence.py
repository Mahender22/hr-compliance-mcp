from .models import LawChange
from . import wages, leave, compliance

SUPPORTED_STATES = {"CA", "NY", "CO", "WA", "MA", "IL", "NJ", "OR"}

LAW_CHANGES = [
    # California
    LawChange(state="CA", state_name="California", category="minimum_wage",
              description="Minimum wage increased to $16.50/hr (CPI adjustment)", effective_date="2026-01-01",
              impact="All employers regardless of size"),
    LawChange(state="CA", state_name="California", category="workplace_safety",
              description="Workplace violence prevention plans required for all employers (SB 553)", effective_date="2024-07-01",
              impact="All employers must create written plans and provide training"),
    LawChange(state="CA", state_name="California", category="drug_testing",
              description="Off-duty marijuana use protections (AB 2188) fully in effect", effective_date="2024-01-01",
              impact="Cannot discriminate based on off-duty marijuana use or hair follicle tests"),
    LawChange(state="CA", state_name="California", category="sick_leave",
              description="Paid sick leave expanded from 24 to 40 hours annually (SB 616)", effective_date="2024-01-01",
              impact="All employers — increased accrual cap to 80 hours"),

    # New York
    LawChange(state="NY", state_name="New York", category="minimum_wage",
              description="Minimum wage increased to $16.50 (NYC/LI/Westchester), $15.50 (rest of state)", effective_date="2026-01-01",
              impact="All employers — final year of scheduled increases before CPI indexing"),
    LawChange(state="NY", state_name="New York", category="pay_transparency",
              description="Statewide pay transparency law requires salary ranges in job postings", effective_date="2023-09-17",
              impact="Employers with 4+ employees must include salary range in all job postings"),
    LawChange(state="NY", state_name="New York", category="workplace_safety",
              description="Retail Worker Safety Act — panic buttons and de-escalation training", effective_date="2025-06-02",
              impact="Retail employers with 10+ employees must provide panic buttons"),

    # Colorado
    LawChange(state="CO", state_name="Colorado", category="minimum_wage",
              description="Minimum wage increased to $14.81/hr (CPI adjustment)", effective_date="2026-01-01",
              impact="All employers"),
    LawChange(state="CO", state_name="Colorado", category="family_leave",
              description="FAMLI paid family leave program benefits began", effective_date="2024-01-01",
              impact="Up to 12 weeks paid leave at up to 90% wage replacement"),
    LawChange(state="CO", state_name="Colorado", category="noncompete",
              description="Non-compete restrictions strengthened — income threshold $123,750+", effective_date="2022-08-10",
              impact="Non-competes void for workers earning below threshold"),

    # Washington
    LawChange(state="WA", state_name="Washington", category="minimum_wage",
              description="Minimum wage increased to $16.66/hr (CPI adjustment)", effective_date="2026-01-01",
              impact="Highest state minimum wage in the US"),
    LawChange(state="WA", state_name="Washington", category="drug_testing",
              description="Off-duty marijuana use protections enacted", effective_date="2024-01-01",
              impact="Cannot discriminate based on off-duty marijuana use"),

    # Massachusetts
    LawChange(state="MA", state_name="Massachusetts", category="minimum_wage",
              description="Minimum wage increased to $16.00/hr", effective_date="2026-01-01",
              impact="All employers"),
    LawChange(state="MA", state_name="Massachusetts", category="pay_transparency",
              description="Pay transparency law requires salary ranges in job postings", effective_date="2025-07-31",
              impact="Employers with 25+ employees must include salary range in job postings"),

    # Illinois
    LawChange(state="IL", state_name="Illinois", category="minimum_wage",
              description="Minimum wage increased to $15.00/hr", effective_date="2025-01-01",
              impact="All employers — reached $15 target"),
    LawChange(state="IL", state_name="Illinois", category="sick_leave",
              description="Paid Leave for All Workers Act — 40 hours paid leave for any reason", effective_date="2024-01-01",
              impact="All employers — leave can be used for ANY reason, not just illness"),
    LawChange(state="IL", state_name="Illinois", category="pay_transparency",
              description="Pay transparency law requires pay scale and benefits in job postings", effective_date="2025-01-01",
              impact="Employers with 15+ employees"),

    # New Jersey
    LawChange(state="NJ", state_name="New Jersey", category="minimum_wage",
              description="Minimum wage increased to $15.49/hr (CPI adjustment)", effective_date="2026-01-01",
              impact="Most employers — seasonal/small employer rate: $13.73"),
    LawChange(state="NJ", state_name="New Jersey", category="pay_transparency",
              description="Pay transparency law requires salary ranges in job postings", effective_date="2025-06-01",
              impact="Employers with 10+ employees"),

    # Oregon
    LawChange(state="OR", state_name="Oregon", category="minimum_wage",
              description="Minimum wage increased to $14.70/hr (standard), $15.95 (Portland metro)", effective_date="2026-07-01",
              impact="Three-tier regional system"),
    LawChange(state="OR", state_name="Oregon", category="family_leave",
              description="Paid Leave Oregon benefits began", effective_date="2023-09-03",
              impact="12 weeks paid leave at up to 100% of wages for low earners"),
    LawChange(state="OR", state_name="Oregon", category="pay_transparency",
              description="Pay transparency law requires salary ranges in all job postings", effective_date="2024-01-01",
              impact="All employers"),
]


def _validate_state(state: str) -> str:
    state = state.upper()
    if state not in SUPPORTED_STATES:
        supported = ", ".join(sorted(SUPPORTED_STATES))
        raise ValueError(f"State '{state}' not supported. Supported states: {supported}")
    return state


def get_recent_changes(state: str, since: str = "2024-01-01") -> list[LawChange]:
    state = _validate_state(state)
    results = [c for c in LAW_CHANGES if c.state == state and c.effective_date >= since]
    results.sort(key=lambda x: x.effective_date, reverse=True)
    return results


def get_compliance_calendar(state: str = None) -> list[LawChange]:
    results = LAW_CHANGES
    if state:
        state = _validate_state(state)
        results = [c for c in results if c.state == state]
    return sorted(results, key=lambda x: x.effective_date)


def compare_state_compliance(states: list[str], company_size: int = 50) -> dict:
    result = {}
    for state_code in states:
        state_code = state_code.upper()
        if state_code not in SUPPORTED_STATES:
            continue
        mw = wages.get_minimum_wage(state_code)
        sl = leave.get_paid_sick_leave(state_code)
        fl = leave.get_family_leave(state_code)
        vp = leave.get_vacation_payout(state_code)
        nc = compliance.get_noncompete_rules(state_code)
        pt = wages.get_pay_transparency(state_code)
        result[state_code] = {
            "state_name": mw.state_name,
            "minimum_wage": mw.minimum_wage,
            "sick_leave": {"mandated": sl.mandated, "max_annual": sl.max_annual},
            "family_leave": {"has_program": fl.has_program, "program_name": fl.program_name, "duration": fl.duration},
            "vacation_payout_required": vp.required,
            "noncompete_enforceable": nc.enforceable,
            "pay_transparency_posting_required": pt.requires_posting,
        }
    return result


def search_employment_law(query: str, state: str = None) -> list[dict]:
    query_lower = query.lower()
    results = []

    if state:
        state = _validate_state(state)

    # Search minimum wage data
    for code, mw in wages.MINIMUM_WAGE_DATA.items():
        if state and code != state:
            continue
        searchable = f"{mw.state_name} {mw.notes} minimum wage {mw.minimum_wage}".lower()
        if query_lower in searchable:
            results.append({"state": code, "category": "minimum_wage", "summary": f"Minimum wage: ${mw.minimum_wage}/hr", "details": mw.notes})

    # Search overtime data
    for code, ot in wages.OVERTIME_DATA.items():
        if state and code != state:
            continue
        searchable = f"{ot.state_name} {ot.notes} overtime".lower()
        if query_lower in searchable:
            results.append({"state": code, "category": "overtime", "summary": f"Overtime after {ot.weekly_threshold}hrs/week", "details": ot.notes})

    # Search pay transparency data
    for code, pt in wages.PAY_TRANSPARENCY_DATA.items():
        if state and code != state:
            continue
        searchable = f"{pt.state_name} {pt.details} pay transparency salary range".lower()
        if query_lower in searchable:
            results.append({"state": code, "category": "pay_transparency", "summary": f"Pay transparency: posting={'required' if pt.requires_posting else 'not required'}", "details": pt.details})

    # Search sick leave data
    for code, sl in leave.SICK_LEAVE_DATA.items():
        if state and code != state:
            continue
        searchable = f"{sl.state_name} {sl.notes} sick leave paid leave".lower()
        if query_lower in searchable:
            results.append({"state": code, "category": "sick_leave", "summary": f"Paid sick leave: {sl.max_annual}", "details": sl.notes})

    # Search family leave data
    for code, fl in leave.FAMILY_LEAVE_DATA.items():
        if state and code != state:
            continue
        searchable = f"{fl.state_name} {fl.program_name} {fl.notes} family leave paid leave parental".lower()
        if query_lower in searchable:
            results.append({"state": code, "category": "family_leave", "summary": f"{fl.program_name}: {fl.duration}", "details": fl.notes})

    # Search discrimination data
    for code, dp in compliance.DISCRIMINATION_DATA.items():
        if state and code != state:
            continue
        classes_str = " ".join(dp.protected_classes)
        searchable = f"{dp.state_name} {classes_str} {dp.notes} discrimination protected class".lower()
        if query_lower in searchable:
            results.append({"state": code, "category": "discrimination", "summary": f"{len(dp.protected_classes)} protected classes beyond federal", "details": dp.notes})

    # Search non-compete data
    for code, nc in compliance.NONCOMPETE_DATA.items():
        if state and code != state:
            continue
        searchable = f"{nc.state_name} {nc.restrictions} {nc.notes} non-compete noncompete".lower()
        if query_lower in searchable:
            results.append({"state": code, "category": "noncompete", "summary": f"Non-compete: {'not enforceable' if not nc.enforceable else 'enforceable with restrictions'}", "details": nc.restrictions})

    # Search law changes
    for change in LAW_CHANGES:
        if state and change.state != state:
            continue
        searchable = f"{change.state_name} {change.description} {change.impact} {change.category}".lower()
        if query_lower in searchable:
            results.append({"state": change.state, "category": f"change:{change.category}", "summary": change.description, "details": f"Effective: {change.effective_date}. {change.impact}"})

    # Deduplicate by state+category
    seen = set()
    unique = []
    for r in results:
        key = (r["state"], r["category"])
        if key not in seen:
            seen.add(key)
            unique.append(r)

    return unique
