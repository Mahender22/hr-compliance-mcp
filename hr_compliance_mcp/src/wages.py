from .models import MinimumWage, OvertimeRules, PayFrequency, PayTransparency

SUPPORTED_STATES = {
    "CA", "NY", "CO", "WA", "MA", "IL", "NJ", "OR",
}

# --- Minimum Wage Data ---

MINIMUM_WAGE_DATA = {
    "CA": MinimumWage(
        state="CA", state_name="California", minimum_wage=16.50, tipped_wage=16.50,
        tip_credit=False, effective_date="2026-01-01",
        notes="Annual CPI adjustment. No tip credit. Fast food workers: $20.00/hr.",
        scheduled_increases=[{"date": "2027-01-01", "rate": "CPI adjusted"}],
        local_rates=[
            {"jurisdiction": "San Francisco", "rate": 18.67, "effective": "2026-07-01"},
            {"jurisdiction": "Los Angeles (City)", "rate": 17.28, "effective": "2026-07-01"},
            {"jurisdiction": "San Jose", "rate": 17.55, "effective": "2026-01-01"},
            {"jurisdiction": "Berkeley", "rate": 18.67, "effective": "2026-07-01"},
            {"jurisdiction": "Emeryville", "rate": 19.36, "effective": "2026-07-01"},
        ],
    ),
    "NY": MinimumWage(
        state="NY", state_name="New York", minimum_wage=16.50, tipped_wage=11.00,
        tip_credit=True, effective_date="2026-01-01",
        notes="NYC, Long Island, Westchester: $16.50. Rest of state: $15.50. Tipped varies by industry.",
        scheduled_increases=[{"date": "2027-01-01", "rate": "Indexed to CPI starting 2027"}],
        local_rates=[
            {"jurisdiction": "NYC", "rate": 16.50, "effective": "2026-01-01"},
            {"jurisdiction": "Long Island & Westchester", "rate": 16.50, "effective": "2026-01-01"},
            {"jurisdiction": "Rest of State", "rate": 15.50, "effective": "2026-01-01"},
        ],
    ),
    "CO": MinimumWage(
        state="CO", state_name="Colorado", minimum_wage=14.81, tipped_wage=11.79,
        tip_credit=True, effective_date="2026-01-01",
        notes="Annual CPI adjustment. Tip credit max $3.02.",
        local_rates=[{"jurisdiction": "Denver", "rate": 18.29, "effective": "2026-01-01"}],
    ),
    "WA": MinimumWage(
        state="WA", state_name="Washington", minimum_wage=16.66, tipped_wage=16.66,
        tip_credit=False, effective_date="2026-01-01",
        notes="Annual CPI adjustment. No tip credit. Highest state minimum wage.",
        local_rates=[
            {"jurisdiction": "Seattle (large employers)", "rate": 20.76, "effective": "2026-01-01"},
            {"jurisdiction": "Seattle (small employers)", "rate": 18.76, "effective": "2026-01-01"},
            {"jurisdiction": "SeaTac (hospitality/transport)", "rate": 19.71, "effective": "2026-01-01"},
        ],
    ),
    "MA": MinimumWage(
        state="MA", state_name="Massachusetts", minimum_wage=16.00, tipped_wage=7.00,
        tip_credit=True, effective_date="2026-01-01",
        notes="Scheduled increase to $16.00. Tipped wage $7.00. Service rate: $7.00.",
    ),
    "IL": MinimumWage(
        state="IL", state_name="Illinois", minimum_wage=15.00, tipped_wage=9.00,
        tip_credit=True, effective_date="2026-01-01",
        notes="Tip credit: 40% of minimum wage. Youth wage (under 18): $13.00.",
        local_rates=[
            {"jurisdiction": "Chicago", "rate": 16.20, "effective": "2026-07-01"},
            {"jurisdiction": "Cook County", "rate": 14.50, "effective": "2026-07-01"},
        ],
    ),
    "NJ": MinimumWage(
        state="NJ", state_name="New Jersey", minimum_wage=15.49, tipped_wage=5.26,
        tip_credit=True, effective_date="2026-01-01",
        notes="Annual CPI adjustment. Seasonal/small employer: $13.73.",
    ),
    "OR": MinimumWage(
        state="OR", state_name="Oregon", minimum_wage=14.70, tipped_wage=14.70,
        tip_credit=False, effective_date="2026-07-01",
        notes="Three-tier system based on region. No tip credit.",
        local_rates=[
            {"jurisdiction": "Portland metro", "rate": 15.95, "effective": "2026-07-01"},
            {"jurisdiction": "Standard (rest of state)", "rate": 14.70, "effective": "2026-07-01"},
            {"jurisdiction": "Nonurban counties", "rate": 13.20, "effective": "2026-07-01"},
        ],
    ),
}

# --- Overtime Data ---

OVERTIME_DATA = {
    "CA": OvertimeRules(
        state="CA", state_name="California", weekly_threshold=40, weekly_rate=1.5,
        daily_threshold=8, daily_rate=1.5,
        exemptions=["Executive", "Administrative", "Professional", "Computer professional ($55.58/hr min)"],
        notes="2x pay after 12 hrs/day. 1.5x first 8 hrs on 7th consecutive day, 2x after that. PAGA private enforcement.",
    ),
    "NY": OvertimeRules(
        state="NY", state_name="New York", weekly_threshold=40, weekly_rate=1.5,
        exemptions=["Executive ($1,200/week min)", "Administrative ($1,200/week min)", "Professional"],
        notes="No daily overtime. Residential employees: OT after 44 hrs.",
    ),
    "CO": OvertimeRules(
        state="CO", state_name="Colorado", weekly_threshold=40, weekly_rate=1.5,
        daily_threshold=12, daily_rate=1.5,
        exemptions=["Executive ($1,057.69/week)", "Administrative", "Professional", "Highly compensated ($128,506/yr)"],
        notes="Both daily (12hr) AND weekly (40hr) overtime apply. Whichever gives more OT.",
    ),
    "WA": OvertimeRules(
        state="WA", state_name="Washington", weekly_threshold=40, weekly_rate=1.5,
        exemptions=["Executive (2x state minimum)", "Administrative", "Professional", "Computer professional ($62.35/hr)"],
        notes="Agricultural workers phasing in: OT after 40hrs by 2024.",
    ),
    "MA": OvertimeRules(
        state="MA", state_name="Massachusetts", weekly_threshold=40, weekly_rate=1.5,
        exemptions=["Executive", "Administrative", "Professional", "Outside sales"],
        notes="Sunday/holiday premium pay phased out by 2023.",
    ),
    "IL": OvertimeRules(
        state="IL", state_name="Illinois", weekly_threshold=40, weekly_rate=1.5,
        exemptions=["Executive ($684/week)", "Administrative", "Professional", "Outside sales"],
        notes="No daily overtime. One Day Rest in Seven Act requires 24hrs off per 7-day period.",
    ),
    "NJ": OvertimeRules(
        state="NJ", state_name="New Jersey", weekly_threshold=40, weekly_rate=1.5,
        exemptions=["Executive", "Administrative", "Professional", "Outside sales"],
        notes="No daily overtime.",
    ),
    "OR": OvertimeRules(
        state="OR", state_name="Oregon", weekly_threshold=40, weekly_rate=1.5,
        exemptions=["Executive ($767.60/week)", "Administrative", "Professional"],
        notes="Manufacturing: OT after 10 hrs/day. Agricultural workers: OT after 55hrs/week (decreasing to 40).",
    ),
}

# --- Pay Frequency Data ---

PAY_FREQUENCY_DATA = {
    "CA": PayFrequency(state="CA", state_name="California", frequency="semi-monthly",
        details="Wages earned 1st-15th paid by 26th; 16th-last paid by 10th of next month.",
        exceptions="Weekly for certain agricultural and domestic workers."),
    "NY": PayFrequency(state="NY", state_name="New York", frequency="varies by industry",
        details="Manual workers: weekly. Clerical/other: semi-monthly. Railroad workers: semi-monthly.",
        exceptions="Manual workers at nonprofits may request semi-monthly."),
    "CO": PayFrequency(state="CO", state_name="Colorado", frequency="monthly",
        details="At least monthly. Most employers pay semi-monthly or bi-weekly.",
        exceptions="Executive, administrative, and professional employees may be paid monthly."),
    "WA": PayFrequency(state="WA", state_name="Washington", frequency="monthly",
        details="At least monthly on established regular paydays.",
        exceptions="None significant."),
    "MA": PayFrequency(state="MA", state_name="Massachusetts", frequency="bi-weekly",
        details="Weekly or bi-weekly. Exempt salaried employees: semi-monthly or monthly.",
        exceptions="Exempt employees may be paid monthly."),
    "IL": PayFrequency(state="IL", state_name="Illinois", frequency="semi-monthly",
        details="At least semi-monthly. Executive, administrative, professional: monthly allowed.",
        exceptions="Monthly for executive/admin/professional employees."),
    "NJ": PayFrequency(state="NJ", state_name="New Jersey", frequency="semi-monthly",
        details="At least semi-monthly.", exceptions="None significant."),
    "OR": PayFrequency(state="OR", state_name="Oregon", frequency="monthly",
        details="At least monthly, within 35 days of end of pay period.",
        exceptions="None significant."),
}

# --- Pay Transparency Data ---

PAY_TRANSPARENCY_DATA = {
    "CA": PayTransparency(state="CA", state_name="California", requires_posting=True, requires_on_request=True,
        effective_date="2023-01-01", employer_threshold=15,
        details="Employers with 15+ employees must include pay scale in all job postings. Must provide pay scale to current employees on request.",
        penalties="$100-$10,000 per violation."),
    "NY": PayTransparency(state="NY", state_name="New York", requires_posting=True, requires_on_request=True,
        effective_date="2023-09-17", employer_threshold=4,
        details="Statewide: employers with 4+ employees must include salary range in job postings. NYC law also applies.",
        penalties="Up to $1,000 first violation, $5,000 subsequent."),
    "CO": PayTransparency(state="CO", state_name="Colorado", requires_posting=True, requires_on_request=True,
        effective_date="2021-01-01", employer_threshold=1,
        details="First state to require salary ranges in ALL job postings. Must also include benefits description. Applies to remote jobs that could be performed in CO.",
        penalties="$500-$10,000 per violation."),
    "WA": PayTransparency(state="WA", state_name="Washington", requires_posting=True, requires_on_request=True,
        effective_date="2023-01-01", employer_threshold=15,
        details="Must include salary range and benefits description in all job postings for employers with 15+ employees.",
        penalties="Up to $500 first violation, $1,000+ repeat."),
    "MA": PayTransparency(state="MA", state_name="Massachusetts", requires_posting=True, requires_on_request=True,
        effective_date="2025-07-31", employer_threshold=25,
        details="Employers with 25+ employees must include pay range in job postings. Must provide pay range to applicants and current employees on request.",
        penalties="Warning first, then $500-$25,000."),
    "IL": PayTransparency(state="IL", state_name="Illinois", requires_posting=True, requires_on_request=False,
        effective_date="2025-01-01", employer_threshold=15,
        details="Employers with 15+ employees must include pay scale and benefits in job postings.",
        penalties="$500 first, $2,500-$10,000 repeat."),
    "NJ": PayTransparency(state="NJ", state_name="New Jersey", requires_posting=False, requires_on_request=True,
        effective_date="2025-06-01", employer_threshold=10,
        details="Employers with 10+ employees must disclose pay range in job postings and to current employees upon request. Jersey City has a local ordinance.",
        penalties="$1,000 first, up to $10,000 subsequent."),
    "OR": PayTransparency(state="OR", state_name="Oregon", requires_posting=True, requires_on_request=True,
        effective_date="2024-01-01", employer_threshold=1,
        details="All employers must include pay range in job postings. Must provide pay range to employees on request.",
        penalties="$1,000 per violation."),
}


# --- Query Functions ---

def get_minimum_wage(state: str) -> MinimumWage:
    """Get minimum wage data for a state."""
    state = state.upper()
    if state not in MINIMUM_WAGE_DATA:
        supported = ", ".join(sorted(SUPPORTED_STATES))
        raise ValueError(f"State '{state}' not supported. Supported states: {supported}")
    return MINIMUM_WAGE_DATA[state]


def get_overtime_rules(state: str) -> OvertimeRules:
    """Get overtime rules for a state."""
    state = state.upper()
    if state not in OVERTIME_DATA:
        supported = ", ".join(sorted(SUPPORTED_STATES))
        raise ValueError(f"State '{state}' not supported. Supported states: {supported}")
    return OVERTIME_DATA[state]


def get_pay_frequency(state: str) -> PayFrequency:
    """Get pay frequency requirements for a state."""
    state = state.upper()
    if state not in PAY_FREQUENCY_DATA:
        supported = ", ".join(sorted(SUPPORTED_STATES))
        raise ValueError(f"State '{state}' not supported. Supported states: {supported}")
    return PAY_FREQUENCY_DATA[state]


def get_pay_transparency(state: str) -> PayTransparency:
    """Get pay transparency rules for a state."""
    state = state.upper()
    if state not in PAY_TRANSPARENCY_DATA:
        supported = ", ".join(sorted(SUPPORTED_STATES))
        raise ValueError(f"State '{state}' not supported. Supported states: {supported}")
    return PAY_TRANSPARENCY_DATA[state]


def compare_wages(states: list[str]) -> list[MinimumWage]:
    """Compare minimum wages across states, sorted by wage descending."""
    results = []
    for state in states:
        results.append(get_minimum_wage(state))
    results.sort(key=lambda x: x.minimum_wage, reverse=True)
    return results
