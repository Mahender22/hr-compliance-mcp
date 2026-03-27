from hr_compliance_mcp.src.intelligence import (
    get_recent_changes, get_compliance_calendar,
    compare_state_compliance, search_employment_law,
)

def test_get_recent_changes_ca():
    results = get_recent_changes("CA")
    assert len(results) > 0
    assert all(r.state == "CA" for r in results)

def test_get_recent_changes_since_date():
    results = get_recent_changes("CA", since="2025-01-01")
    assert len(results) > 0

def test_get_recent_changes_unsupported():
    try:
        get_recent_changes("ZZ")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

def test_get_compliance_calendar():
    results = get_compliance_calendar()
    assert len(results) > 0
    dates = [r.effective_date for r in results]
    assert dates == sorted(dates)

def test_get_compliance_calendar_state_filter():
    results = get_compliance_calendar(state="CA")
    assert all(r.state == "CA" for r in results)

def test_compare_state_compliance():
    result = compare_state_compliance(["CA", "NY"], company_size=50)
    assert "CA" in result
    assert "NY" in result
    assert "minimum_wage" in result["CA"]
    assert "sick_leave" in result["CA"]

def test_search_employment_law():
    results = search_employment_law("minimum wage")
    assert len(results) > 0

def test_search_employment_law_state():
    results = search_employment_law("paid leave", state="CA")
    assert len(results) > 0
    assert all(r["state"] == "CA" for r in results)

def test_search_employment_law_no_results():
    results = search_employment_law("xyznonexistent123")
    assert len(results) == 0
