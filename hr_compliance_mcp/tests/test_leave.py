from hr_compliance_mcp.src.leave import (
    get_paid_sick_leave, get_family_leave, get_vacation_payout,
    get_voting_leave, get_bereavement_leave,
)


def test_get_paid_sick_leave_ca():
    result = get_paid_sick_leave("CA")
    assert result.mandated is True
    assert "30 hours" in result.accrual_rate.lower() or "1 hour" in result.accrual_rate.lower()

def test_get_paid_sick_leave_il():
    result = get_paid_sick_leave("IL")
    assert result.mandated is True

def test_get_paid_sick_leave_case_insensitive():
    result = get_paid_sick_leave("ca")
    assert result.state == "CA"

def test_get_paid_sick_leave_unsupported():
    try:
        get_paid_sick_leave("ZZ")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

def test_get_family_leave_ca():
    result = get_family_leave("CA")
    assert result.has_program is True
    assert "PFL" in result.program_name or "Paid Family" in result.program_name

def test_get_family_leave_nj():
    result = get_family_leave("NJ")
    assert result.has_program is True

def test_get_vacation_payout_ca():
    result = get_vacation_payout("CA")
    assert result.required is True

def test_get_vacation_payout_il():
    result = get_vacation_payout("IL")
    assert result.required is True

def test_get_voting_leave_ca():
    result = get_voting_leave("CA")
    assert result.required is True
    assert result.paid is True

def test_get_voting_leave_nj():
    result = get_voting_leave("NJ")
    assert result.required is False

def test_get_bereavement_leave_ca():
    result = get_bereavement_leave("CA")
    assert result.mandated is True

def test_get_bereavement_leave_ny():
    result = get_bereavement_leave("NY")
    assert result.mandated is False
