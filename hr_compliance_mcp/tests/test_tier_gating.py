import pytest
from unittest.mock import patch
from hr_compliance_mcp.src import config


@pytest.mark.asyncio
async def test_starter_tier_allows_minimum_wage():
    from hr_compliance_mcp.src.server import get_minimum_wage
    with patch.object(config, "TIER", "starter"):
        result = await get_minimum_wage("CA")
        assert result["status"] == "success"


@pytest.mark.asyncio
async def test_starter_tier_allows_sick_leave():
    from hr_compliance_mcp.src.server import get_paid_sick_leave
    with patch.object(config, "TIER", "starter"):
        result = await get_paid_sick_leave("CA")
        assert result["status"] == "success"


@pytest.mark.asyncio
async def test_starter_tier_blocks_discrimination():
    from hr_compliance_mcp.src.server import get_discrimination_protections
    with patch.object(config, "TIER", "starter"):
        result = await get_discrimination_protections("CA")
        assert result["status"] == "error"
        assert "Pro plan" in result["message"]


@pytest.mark.asyncio
async def test_starter_tier_blocks_noncompete():
    from hr_compliance_mcp.src.server import get_noncompete_rules
    with patch.object(config, "TIER", "starter"):
        result = await get_noncompete_rules("CA")
        assert result["status"] == "error"


@pytest.mark.asyncio
async def test_starter_tier_blocks_recent_changes():
    from hr_compliance_mcp.src.server import get_recent_changes
    with patch.object(config, "TIER", "starter"):
        result = await get_recent_changes("CA")
        assert result["status"] == "error"


@pytest.mark.asyncio
async def test_starter_tier_blocks_search():
    from hr_compliance_mcp.src.server import search_employment_law
    with patch.object(config, "TIER", "starter"):
        result = await search_employment_law("minimum wage")
        assert result["status"] == "error"


@pytest.mark.asyncio
async def test_pro_tier_allows_discrimination():
    from hr_compliance_mcp.src.server import get_discrimination_protections
    with patch.object(config, "TIER", "pro"):
        result = await get_discrimination_protections("CA")
        assert result["status"] == "success"


@pytest.mark.asyncio
async def test_pro_tier_allows_search():
    from hr_compliance_mcp.src.server import search_employment_law
    with patch.object(config, "TIER", "pro"):
        result = await search_employment_law("minimum wage")
        assert result["status"] == "success"


@pytest.mark.asyncio
async def test_unsupported_state_returns_error():
    from hr_compliance_mcp.src.server import get_minimum_wage
    result = await get_minimum_wage("ZZ")
    assert result["status"] == "error"
    assert "not supported" in result["message"].lower()
