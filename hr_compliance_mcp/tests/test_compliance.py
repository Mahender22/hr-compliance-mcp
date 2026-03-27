from hr_compliance_mcp.src.compliance import (
    get_discrimination_protections, get_background_check_laws,
    get_drug_testing_rules, get_noncompete_rules, get_workplace_safety,
)

def test_get_discrimination_protections_ca():
    result = get_discrimination_protections("CA")
    assert result.state == "CA"
    assert "Sexual orientation" in result.protected_classes
    assert "Gender identity" in result.protected_classes
    assert len(result.protected_classes) > 5

def test_get_discrimination_protections_ny():
    result = get_discrimination_protections("NY")
    assert len(result.protected_classes) > 5

def test_get_discrimination_unsupported():
    try:
        get_discrimination_protections("ZZ")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

def test_get_background_check_ca():
    result = get_background_check_laws("CA")
    assert result.ban_the_box is True
    assert result.fair_chance is True

def test_get_background_check_nj():
    result = get_background_check_laws("NJ")
    assert result.ban_the_box is True

def test_get_drug_testing_ca():
    result = get_drug_testing_rules("CA")
    assert result.state == "CA"
    assert "marijuana" in result.marijuana_protections.lower()

def test_get_noncompete_ca():
    result = get_noncompete_rules("CA")
    assert result.enforceable is False

def test_get_noncompete_ma():
    result = get_noncompete_rules("MA")
    assert result.enforceable is True
    assert result.income_threshold != ""

def test_get_workplace_safety_ca():
    result = get_workplace_safety("CA")
    assert result.has_state_plan is True
    assert "Cal/OSHA" in result.agency

def test_get_workplace_safety_ny():
    result = get_workplace_safety("NY")
    assert result.has_state_plan is True
