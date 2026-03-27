from hr_compliance_mcp.src.wages import (
    get_minimum_wage, get_overtime_rules, get_pay_frequency,
    get_pay_transparency, compare_wages, SUPPORTED_STATES,
)


def test_get_minimum_wage_ca():
    result = get_minimum_wage("CA")
    assert result.state == "CA"
    assert result.minimum_wage >= 16.0
    assert result.tip_credit is False
    assert len(result.local_rates) > 0


def test_get_minimum_wage_ny():
    result = get_minimum_wage("NY")
    assert result.state == "NY"
    assert result.minimum_wage >= 15.0
    assert len(result.local_rates) > 0


def test_get_minimum_wage_case_insensitive():
    result = get_minimum_wage("ca")
    assert result.state == "CA"


def test_get_minimum_wage_unsupported_state():
    try:
        get_minimum_wage("ZZ")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "not supported" in str(e).lower()


def test_get_overtime_rules_ca():
    result = get_overtime_rules("CA")
    assert result.daily_threshold == 8
    assert result.weekly_threshold == 40


def test_get_overtime_rules_ny():
    result = get_overtime_rules("NY")
    assert result.weekly_threshold == 40
    assert result.daily_threshold is None


def test_get_pay_frequency_ca():
    result = get_pay_frequency("CA")
    assert result.state == "CA"
    assert result.frequency != ""


def test_get_pay_transparency_co():
    result = get_pay_transparency("CO")
    assert result.requires_posting is True


def test_get_pay_transparency_nj():
    result = get_pay_transparency("NJ")
    assert result.requires_posting is False


def test_compare_wages():
    result = compare_wages(["CA", "NY", "IL"])
    assert len(result) == 3
    assert result[0].state in ("CA", "NY", "IL")


def test_compare_wages_sorts_descending():
    result = compare_wages(["CA", "IL"])
    assert result[0].minimum_wage >= result[1].minimum_wage


def test_supported_states_has_8():
    assert len(SUPPORTED_STATES) >= 8
    for code in ["CA", "NY", "CO", "WA", "MA", "IL", "NJ", "OR"]:
        assert code in SUPPORTED_STATES
