from hr_compliance_mcp.src.models import (
    MinimumWage, OvertimeRules, PayFrequency, PayTransparency,
    PaidSickLeave, FamilyLeave, VacationPayout, VotingLeave,
    BereavementLeave, DiscriminationProtections, BackgroundCheckLaw,
    DrugTestingRules, NonCompeteRules, WorkplaceSafety, LawChange,
)


def test_minimum_wage_to_dict():
    mw = MinimumWage(
        state="CA", state_name="California", minimum_wage=16.50, tipped_wage=16.50,
        tip_credit=False, effective_date="2026-01-01", notes="Annual CPI adjustment",
    )
    d = mw.to_dict()
    assert d["state"] == "CA"
    assert d["minimum_wage"] == 16.50
    assert d["tip_credit"] is False
    assert "notes" in d


def test_minimum_wage_to_dict_excludes_empty_lists():
    mw = MinimumWage(
        state="IL", state_name="Illinois", minimum_wage=15.00, tipped_wage=9.00,
        tip_credit=True, effective_date="2026-01-01",
    )
    d = mw.to_dict()
    assert "scheduled_increases" not in d
    assert "local_rates" not in d


def test_overtime_rules_to_dict():
    ot = OvertimeRules(
        state="CA", state_name="California", weekly_threshold=40, weekly_rate=1.5,
        daily_threshold=8, daily_rate=1.5,
        exemptions=["Executive", "Administrative", "Professional"],
        notes="Also 2x after 12 hrs/day",
    )
    d = ot.to_dict()
    assert d["daily_threshold"] == 8
    assert len(d["exemptions"]) == 3


def test_pay_transparency_to_dict():
    pt = PayTransparency(
        state="CO", state_name="Colorado", requires_posting=True, requires_on_request=True,
        effective_date="2021-01-01", employer_threshold=1,
        details="Must include salary range + benefits in all job postings",
    )
    d = pt.to_dict()
    assert d["requires_posting"] is True
    assert d["employer_threshold"] == 1


def test_paid_sick_leave_to_dict():
    sl = PaidSickLeave(
        state="CA", state_name="California", mandated=True,
        accrual_rate="1 hour per 30 hours worked", max_annual="40 hours",
        max_carryover="80 hours", eligibility="All employees after 30 days",
        effective_date="2024-01-01",
    )
    d = sl.to_dict()
    assert d["mandated"] is True
    assert "40 hours" in d["max_annual"]


def test_family_leave_to_dict():
    fl = FamilyLeave(
        state="NJ", state_name="New Jersey", has_program=True,
        program_name="NJ Family Leave Insurance", duration="12 weeks",
        wage_replacement="85% of weekly wage, max $1,055/week",
        eligibility="20+ weeks of covered employment", effective_date="2009-07-01",
    )
    d = fl.to_dict()
    assert d["has_program"] is True


def test_discrimination_protections_to_dict():
    dp = DiscriminationProtections(
        state="CA", state_name="California",
        protected_classes=["Sexual orientation", "Gender identity", "Gender expression",
            "Marital status", "Medical condition", "Military/veteran status",
            "Political activities", "Reproductive health decisions"],
        enforcing_agency="California Civil Rights Department (CRD)",
    )
    d = dp.to_dict()
    assert len(d["protected_classes"]) == 8


def test_noncompete_rules_to_dict():
    nc = NonCompeteRules(
        state="CA", state_name="California", enforceable=False,
        restrictions="Non-competes are void and unenforceable",
        notes="Cal. Bus. & Prof. Code 16600",
    )
    d = nc.to_dict()
    assert d["enforceable"] is False


def test_law_change_to_dict():
    lc = LawChange(
        state="CA", state_name="California", category="minimum_wage",
        description="Minimum wage increased to $16.50/hr via CPI adjustment",
        effective_date="2026-01-01", impact="Affects all employers regardless of size",
    )
    d = lc.to_dict()
    assert d["category"] == "minimum_wage"
    assert "16.50" in d["description"]
