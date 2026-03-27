from .models import PaidSickLeave, FamilyLeave, VacationPayout, VotingLeave, BereavementLeave

SUPPORTED_STATES = {"CA", "NY", "CO", "WA", "MA", "IL", "NJ", "OR"}

SICK_LEAVE_DATA = {
    "CA": PaidSickLeave(state="CA", state_name="California", mandated=True,
        accrual_rate="1 hour per 30 hours worked", max_annual="40 hours", max_carryover="80 hours",
        eligibility="All employees after 30 days of employment", effective_date="2024-01-01",
        notes="Expanded from 24 to 40 hours in 2024. Applies to all employers regardless of size."),
    "NY": PaidSickLeave(state="NY", state_name="New York", mandated=True,
        accrual_rate="1 hour per 30 hours worked", max_annual="40-56 hours based on employer size",
        max_carryover="40-56 hours", eligibility="All private-sector employees", effective_date="2020-09-30",
        notes="5-99 employees: 40hrs paid. 100+ employees: 56hrs paid. 1-4 employees: 40hrs unpaid (under $1M net income)."),
    "CO": PaidSickLeave(state="CO", state_name="Colorado", mandated=True,
        accrual_rate="1 hour per 30 hours worked", max_annual="48 hours", max_carryover="48 hours",
        eligibility="All employees from day one", effective_date="2021-01-01",
        notes="Healthy Families and Workplaces Act. Additional 80hrs for public health emergencies."),
    "WA": PaidSickLeave(state="WA", state_name="Washington", mandated=True,
        accrual_rate="1 hour per 40 hours worked", max_annual="No annual cap (accrual based)",
        max_carryover="40 hours", eligibility="All employees from day one", effective_date="2018-01-01",
        notes="Can use after 90 days. Applies to all employers including small businesses."),
    "MA": PaidSickLeave(state="MA", state_name="Massachusetts", mandated=True,
        accrual_rate="1 hour per 30 hours worked", max_annual="40 hours", max_carryover="40 hours",
        eligibility="All employees after 90 days", effective_date="2015-07-01",
        notes="Employers with 11+ employees: paid. Under 11: unpaid sick leave."),
    "IL": PaidSickLeave(state="IL", state_name="Illinois", mandated=True,
        accrual_rate="1 hour per 40 hours worked", max_annual="40 hours",
        max_carryover="Employer may limit to 40 hours", eligibility="All employees after 90 days",
        effective_date="2024-01-01",
        notes="Paid Leave for All Workers Act — can be used for ANY reason, not just illness."),
    "NJ": PaidSickLeave(state="NJ", state_name="New Jersey", mandated=True,
        accrual_rate="1 hour per 30 hours worked", max_annual="40 hours", max_carryover="40 hours",
        eligibility="All employees from day one", effective_date="2018-10-29",
        notes="New Jersey Earned Sick Leave Law. Applies to all employers regardless of size."),
    "OR": PaidSickLeave(state="OR", state_name="Oregon", mandated=True,
        accrual_rate="1 hour per 30 hours worked", max_annual="40 hours", max_carryover="40 hours",
        eligibility="All employees after 90 days", effective_date="2016-01-01",
        notes="10+ employees in Portland, 6+ elsewhere: paid. Smaller employers: unpaid protected leave."),
}

FAMILY_LEAVE_DATA = {
    "CA": FamilyLeave(state="CA", state_name="California", has_program=True,
        program_name="CA Paid Family Leave (PFL)", duration="8 weeks",
        wage_replacement="60-70% of weekly wages (up to ~$1,620/week)",
        eligibility="Employees who paid into SDI. No employer size requirement.",
        effective_date="2004-07-01",
        notes="Also: CA Family Rights Act (CFRA) provides 12 weeks job-protected unpaid leave for 5+ employee employers."),
    "NY": FamilyLeave(state="NY", state_name="New York", has_program=True,
        program_name="NY Paid Family Leave (PFL)", duration="12 weeks",
        wage_replacement="67% of average weekly wage (max $1,151.16/week)",
        eligibility="Full-time: 26+ consecutive weeks. Part-time: 175+ days.",
        effective_date="2018-01-01",
        notes="Funded through employee payroll deductions. Job protection included."),
    "CO": FamilyLeave(state="CO", state_name="Colorado", has_program=True,
        program_name="CO Family and Medical Leave Insurance (FAMLI)",
        duration="12 weeks (16 for pregnancy complications)",
        wage_replacement="Up to 90% of wages (max ~$1,100/week)",
        eligibility="Employees who earned $2,500+ in base period", effective_date="2024-01-01",
        notes="One of the most generous programs. Premiums split 50/50 employer/employee."),
    "WA": FamilyLeave(state="WA", state_name="Washington", has_program=True,
        program_name="WA Paid Family and Medical Leave (PFML)",
        duration="12 weeks family + 12 weeks medical (16-18 combined max)",
        wage_replacement="Up to 90% of wages (max ~$1,456/week)",
        eligibility="820+ hours worked in qualifying period", effective_date="2020-01-01",
        notes="Premiums: 0.74% of wages split employer/employee. Employers with 50+ employees pay employer share."),
    "MA": FamilyLeave(state="MA", state_name="Massachusetts", has_program=True,
        program_name="MA Paid Family and Medical Leave (PFML)",
        duration="12 weeks family + 20 weeks medical (26 combined max)",
        wage_replacement="80% of wages up to 50% state avg weekly wage, then 50% above that (max ~$1,149/week)",
        eligibility="Meet financial eligibility (earnings threshold)", effective_date="2021-01-01",
        notes="Most generous duration (26 weeks combined). Funded through payroll tax."),
    "IL": FamilyLeave(state="IL", state_name="Illinois", has_program=False,
        program_name="None (federal FMLA only)", duration="12 weeks unpaid (FMLA)",
        wage_replacement="None (unpaid)",
        eligibility="FMLA: 50+ employees, 12 months employed, 1,250 hours",
        effective_date="N/A",
        notes="No state paid family leave program as of 2026. Paid Leave for All Workers Act covers sick leave only."),
    "NJ": FamilyLeave(state="NJ", state_name="New Jersey", has_program=True,
        program_name="NJ Family Leave Insurance (FLI)", duration="12 weeks",
        wage_replacement="85% of weekly wage (max ~$1,055/week)",
        eligibility="20+ weeks of covered employment OR $12,000+ in earnings",
        effective_date="2009-07-01",
        notes="One of the first state programs. Also NJ Family Leave Act provides 12 weeks job-protected leave (30+ employees)."),
    "OR": FamilyLeave(state="OR", state_name="Oregon", has_program=True,
        program_name="OR Paid Leave Oregon", duration="12 weeks (14 for pregnancy)",
        wage_replacement="Up to 100% of wages for low earners (max ~$1,523/week)",
        eligibility="$1,000+ in wages during base year", effective_date="2023-09-03",
        notes="Most generous wage replacement for low-income workers. 1% payroll tax split 60/40 employee/employer."),
}

VACATION_PAYOUT_DATA = {
    "CA": VacationPayout(state="CA", state_name="California", required=True,
        conditions="All accrued, unused vacation must be paid at termination. No use-it-or-lose-it policies allowed. Vacation is considered earned wages."),
    "NY": VacationPayout(state="NY", state_name="New York", required=False,
        conditions="Not required by state law unless employer has a policy or practice of paying out. If employer has a written forfeiture policy, they may not pay out.",
        notes="Check employer's written policy."),
    "CO": VacationPayout(state="CO", state_name="Colorado", required=True,
        conditions="All accrued vacation must be paid at separation. No forfeiture or use-it-or-lose-it policies. Vacation is earned wages under Colorado Wage Claim Act."),
    "WA": VacationPayout(state="WA", state_name="Washington", required=False,
        conditions="Not required by state law unless employer's policy states otherwise. If employer policy promises payout, it must be honored.",
        notes="Employers may adopt use-it-or-lose-it policies."),
    "MA": VacationPayout(state="MA", state_name="Massachusetts", required=True,
        conditions="All accrued, unused vacation must be paid upon termination. Treble damages for violations under MA Wage Act."),
    "IL": VacationPayout(state="IL", state_name="Illinois", required=True,
        conditions="All earned vacation must be paid at termination. IL Wage Payment and Collection Act prohibits use-it-or-lose-it. Applies to all employers."),
    "NJ": VacationPayout(state="NJ", state_name="New Jersey", required=False,
        conditions="Not required by state law unless employer has established policy. Follow employer policy/agreement.",
        notes="Employer policy controls."),
    "OR": VacationPayout(state="OR", state_name="Oregon", required=False,
        conditions="Not required by state law. Employer policy governs. If employer policy promises payout, it is enforceable.",
        notes="Employers may adopt use-it-or-lose-it with proper notice."),
}

VOTING_LEAVE_DATA = {
    "CA": VotingLeave(state="CA", state_name="California", required=True, paid=True,
        duration="Up to 2 hours at beginning or end of shift", notice_required="2 working days before election"),
    "NY": VotingLeave(state="NY", state_name="New York", required=True, paid=True,
        duration="Up to 2 hours if insufficient non-working time to vote", notice_required="2-10 working days before election"),
    "CO": VotingLeave(state="CO", state_name="Colorado", required=True, paid=True,
        duration="Up to 2 hours", notice_required="Prior to election day",
        notes="All-mail ballot state, but leave still available for in-person voting."),
    "WA": VotingLeave(state="WA", state_name="Washington", required=False, paid=False,
        duration="N/A — all-mail ballot state", notice_required="N/A",
        notes="Washington uses all-mail voting. No specific voting leave law needed."),
    "MA": VotingLeave(state="MA", state_name="Massachusetts", required=True, paid=False,
        duration="First 2 hours polls are open (manufacturing/mechanical employees only)",
        notice_required="Reasonable notice",
        notes="Very limited — applies mainly to manufacturing workers. Most employees not covered."),
    "IL": VotingLeave(state="IL", state_name="Illinois", required=True, paid=True,
        duration="Up to 2 hours", notice_required="Prior to election day",
        notes="Employer may specify which 2 hours."),
    "NJ": VotingLeave(state="NJ", state_name="New Jersey", required=False, paid=False,
        duration="N/A", notice_required="N/A", notes="No state voting leave law. Polls open 6am-8pm."),
    "OR": VotingLeave(state="OR", state_name="Oregon", required=False, paid=False,
        duration="N/A — all-mail ballot state", notice_required="N/A",
        notes="Oregon uses all-mail voting since 2000."),
}

BEREAVEMENT_LEAVE_DATA = {
    "CA": BereavementLeave(state="CA", state_name="California", mandated=True, duration="5 days",
        qualifying_relationships="Spouse, child, parent, sibling, grandparent, grandchild, domestic partner, parent-in-law",
        notes="AB 1949 (2023). Applies to employers with 5+ employees. Unpaid but can use accrued PTO."),
    "NY": BereavementLeave(state="NY", state_name="New York", mandated=False, duration="No state mandate",
        qualifying_relationships="N/A", notes="No state law requiring bereavement leave. Governed by employer policy."),
    "CO": BereavementLeave(state="CO", state_name="Colorado", mandated=True, duration="4 days",
        qualifying_relationships="Spouse, domestic partner, child, parent, sibling, grandparent, grandchild, parent-in-law",
        notes="Can also be used for miscarriage, failed adoption/fertility, or stillbirth."),
    "WA": BereavementLeave(state="WA", state_name="Washington", mandated=False, duration="No state mandate",
        qualifying_relationships="N/A", notes="No specific bereavement law. May use PFML for qualifying events."),
    "MA": BereavementLeave(state="MA", state_name="Massachusetts", mandated=False, duration="No state mandate",
        qualifying_relationships="N/A", notes="No state law requiring bereavement leave. PFML may apply for grief-related conditions."),
    "IL": BereavementLeave(state="IL", state_name="Illinois", mandated=True, duration="10 days (unpaid, job-protected)",
        qualifying_relationships="Child (including miscarriage, stillbirth, failed adoption/surrogacy, unsuccessful fertility treatment, diagnosis impacting fertility)",
        notes="Child Bereavement Leave Act + Child Extended Bereavement Leave Act. 50+ employees only."),
    "NJ": BereavementLeave(state="NJ", state_name="New Jersey", mandated=False, duration="No state mandate",
        qualifying_relationships="N/A", notes="No state law. May use NJ earned sick leave for bereavement."),
    "OR": BereavementLeave(state="OR", state_name="Oregon", mandated=True, duration="2 weeks",
        qualifying_relationships="Spouse, domestic partner, child, parent, parent-in-law, grandparent, grandchild, sibling",
        notes="Oregon Family Leave Act covers bereavement. 25+ employees. Can use Paid Leave Oregon benefits."),
}


def _validate_state(state: str) -> str:
    state = state.upper()
    if state not in SUPPORTED_STATES:
        supported = ", ".join(sorted(SUPPORTED_STATES))
        raise ValueError(f"State '{state}' not supported. Supported states: {supported}")
    return state

def get_paid_sick_leave(state: str) -> PaidSickLeave:
    return SICK_LEAVE_DATA[_validate_state(state)]

def get_family_leave(state: str) -> FamilyLeave:
    return FAMILY_LEAVE_DATA[_validate_state(state)]

def get_vacation_payout(state: str) -> VacationPayout:
    return VACATION_PAYOUT_DATA[_validate_state(state)]

def get_voting_leave(state: str) -> VotingLeave:
    return VOTING_LEAVE_DATA[_validate_state(state)]

def get_bereavement_leave(state: str) -> BereavementLeave:
    return BEREAVEMENT_LEAVE_DATA[_validate_state(state)]
