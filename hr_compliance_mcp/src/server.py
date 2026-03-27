from typing import Optional

from fastmcp import FastMCP

from . import config
from . import wages
from . import leave
from . import compliance
from . import intelligence

mcp = FastMCP(
    name="HR Compliance MCP Server",
    instructions=(
        "You are connected to a 50-state employment law intelligence MCP server. "
        "Use these tools to look up minimum wages, overtime rules, paid leave mandates, "
        "pay transparency requirements, discrimination protections, background check laws, "
        "non-compete rules, and more across US states. "
        "Currently covers 8 priority states: CA, NY, CO, WA, MA, IL, NJ, OR."
    ),
)

SUPPORTED_STATES = sorted(wages.SUPPORTED_STATES)


def _check_pro_tier() -> Optional[dict]:
    """Check if current tier allows Pro features."""
    if config.TIER == "starter":
        return {
            "status": "error",
            "message": "This feature requires the Pro plan ($99/mo). Upgrade at https://mcpize.com/hr-compliance-mcp",
        }
    return None


# ============================================================
# Tier 1 — Wage & Hour (Starter)
# ============================================================

@mcp.tool
async def get_minimum_wage(state: str, include_local: bool = True) -> dict:
    """Get current minimum wage for a state/city, including tipped wage and scheduled increases.

    Args:
        state: Two-letter state code (e.g., CA, NY, CO)
        include_local: Include local/city minimum wage rates (default: True)
    """
    try:
        result = wages.get_minimum_wage(state)
        d = result.to_dict()
        if not include_local:
            d.pop("local_rates", None)
        return {"status": "success", "data": d}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@mcp.tool
async def get_overtime_rules(state: str) -> dict:
    """Get overtime thresholds, rates, exemptions, and daily vs weekly rules by state.

    Args:
        state: Two-letter state code (e.g., CA, NY, CO)
    """
    try:
        result = wages.get_overtime_rules(state)
        return {"status": "success", "data": result.to_dict()}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@mcp.tool
async def get_pay_frequency_requirements(state: str) -> dict:
    """Get how often employers must pay employees by state.

    Args:
        state: Two-letter state code (e.g., CA, NY, CO)
    """
    try:
        result = wages.get_pay_frequency(state)
        return {"status": "success", "data": result.to_dict()}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@mcp.tool
async def compare_wages_across_states(states: list[str]) -> dict:
    """Side-by-side minimum wage comparison for multi-state employers.

    Args:
        states: List of two-letter state codes to compare (e.g., ["CA", "NY", "IL"])
    """
    try:
        results = wages.compare_wages(states)
        return {
            "status": "success",
            "comparison": [r.to_dict() for r in results],
            "highest": results[0].to_dict() if results else None,
            "lowest": results[-1].to_dict() if results else None,
        }
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@mcp.tool
async def get_pay_transparency_rules(state: str) -> dict:
    """Get salary range disclosure requirements by state.

    Args:
        state: Two-letter state code (e.g., CA, CO, WA)
    """
    try:
        result = wages.get_pay_transparency(state)
        return {"status": "success", "data": result.to_dict()}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


# ============================================================
# Tier 2 — Leave Laws (Starter)
# ============================================================

@mcp.tool
async def get_paid_sick_leave(state: str) -> dict:
    """Get sick leave mandates: accrual rate, max hours, eligibility by state.

    Args:
        state: Two-letter state code (e.g., CA, NY, NJ)
    """
    try:
        result = leave.get_paid_sick_leave(state)
        return {"status": "success", "data": result.to_dict()}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@mcp.tool
async def get_family_leave(state: str) -> dict:
    """Get paid family/medical leave programs by state (beyond federal FMLA).

    Args:
        state: Two-letter state code (e.g., CA, NY, WA)
    """
    try:
        result = leave.get_family_leave(state)
        return {"status": "success", "data": result.to_dict()}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@mcp.tool
async def get_vacation_payout_rules(state: str) -> dict:
    """Get whether unused PTO must be paid out at termination by state.

    Args:
        state: Two-letter state code (e.g., CA, CO, MA)
    """
    try:
        result = leave.get_vacation_payout(state)
        return {"status": "success", "data": result.to_dict()}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@mcp.tool
async def get_voting_leave(state: str) -> dict:
    """Get time-off-to-vote requirements by state.

    Args:
        state: Two-letter state code (e.g., CA, NY, IL)
    """
    try:
        result = leave.get_voting_leave(state)
        return {"status": "success", "data": result.to_dict()}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@mcp.tool
async def get_bereavement_leave(state: str) -> dict:
    """Get bereavement leave mandates by state.

    Args:
        state: Two-letter state code (e.g., CA, IL, OR)
    """
    try:
        result = leave.get_bereavement_leave(state)
        return {"status": "success", "data": result.to_dict()}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


# ============================================================
# Tier 3 — Compliance & Protections (Pro)
# ============================================================

@mcp.tool
async def get_discrimination_protections(state: str) -> dict:
    """Get protected classes beyond federal law (sexual orientation, gender identity, criminal history, etc.).

    Args:
        state: Two-letter state code (e.g., CA, NY, NJ)
    """
    tier_check = _check_pro_tier()
    if tier_check:
        return tier_check
    try:
        result = compliance.get_discrimination_protections(state)
        return {"status": "success", "data": result.to_dict()}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@mcp.tool
async def get_background_check_laws(state: str) -> dict:
    """Get ban-the-box, fair chance hiring, and background check restrictions by state.

    Args:
        state: Two-letter state code (e.g., CA, NY, MA)
    """
    tier_check = _check_pro_tier()
    if tier_check:
        return tier_check
    try:
        result = compliance.get_background_check_laws(state)
        return {"status": "success", "data": result.to_dict()}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@mcp.tool
async def get_drug_testing_rules(state: str) -> dict:
    """Get pre-employment and workplace drug testing laws by state, including marijuana protections.

    Args:
        state: Two-letter state code (e.g., CA, NY, NJ)
    """
    tier_check = _check_pro_tier()
    if tier_check:
        return tier_check
    try:
        result = compliance.get_drug_testing_rules(state)
        return {"status": "success", "data": result.to_dict()}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@mcp.tool
async def get_noncompete_rules(state: str) -> dict:
    """Get non-compete enforceability and restrictions by state.

    Args:
        state: Two-letter state code (e.g., CA, CO, WA)
    """
    tier_check = _check_pro_tier()
    if tier_check:
        return tier_check
    try:
        result = compliance.get_noncompete_rules(state)
        return {"status": "success", "data": result.to_dict()}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@mcp.tool
async def get_workplace_safety(state: str) -> dict:
    """Get state OSHA plans and unique workplace safety requirements.

    Args:
        state: Two-letter state code (e.g., CA, WA, OR)
    """
    tier_check = _check_pro_tier()
    if tier_check:
        return tier_check
    try:
        result = compliance.get_workplace_safety(state)
        return {"status": "success", "data": result.to_dict()}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


# ============================================================
# Tier 4 — Intelligence (Pro)
# ============================================================

@mcp.tool
async def get_recent_changes(state: str, since: str = "2024-01-01") -> dict:
    """Get recent employment law changes for a state since a given date.

    Args:
        state: Two-letter state code (e.g., CA, NY, WA)
        since: ISO date string to filter changes from (default: 2024-01-01)
    """
    tier_check = _check_pro_tier()
    if tier_check:
        return tier_check
    try:
        results = intelligence.get_recent_changes(state, since=since)
        return {
            "status": "success",
            "state": state.upper(),
            "changes": [r.to_dict() for r in results],
            "count": len(results),
        }
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@mcp.tool
async def compare_state_compliance(states: list[str], company_size: int = 50) -> dict:
    """Full compliance comparison across multiple states for a given company size.

    Args:
        states: List of two-letter state codes (e.g., ["CA", "NY", "IL"])
        company_size: Number of employees (affects which laws apply)
    """
    tier_check = _check_pro_tier()
    if tier_check:
        return tier_check
    try:
        result = intelligence.compare_state_compliance(states, company_size=company_size)
        return {"status": "success", "company_size": company_size, "comparison": result}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@mcp.tool
async def get_compliance_calendar(state: str = None) -> dict:
    """Get upcoming effective dates and compliance deadlines.

    Args:
        state: Optional two-letter state code to filter (e.g., CA). Omit for all states.
    """
    tier_check = _check_pro_tier()
    if tier_check:
        return tier_check
    try:
        results = intelligence.get_compliance_calendar(state=state)
        return {"status": "success", "calendar": [r.to_dict() for r in results], "count": len(results)}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


@mcp.tool
async def search_employment_law(query: str, state: str = None) -> dict:
    """Free-text search across all state employment law data.

    Args:
        query: Search terms (e.g., "minimum wage increase", "paid leave", "non-compete ban")
        state: Optional two-letter state code to limit search scope
    """
    tier_check = _check_pro_tier()
    if tier_check:
        return tier_check
    try:
        results = intelligence.search_employment_law(query, state=state)
        return {"status": "success", "query": query, "results": results, "count": len(results)}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


# ============================================================
# Resources
# ============================================================

@mcp.resource("hr://states/supported")
def supported_states_resource() -> str:
    """Reference: all supported states and their key compliance highlights."""
    lines = ["# Supported States for HR Compliance MCP\n"]
    for code in SUPPORTED_STATES:
        mw = wages.MINIMUM_WAGE_DATA[code]
        sl = leave.SICK_LEAVE_DATA[code]
        lines.append(f"## {mw.state_name} ({code})")
        lines.append(f"- Minimum Wage: ${mw.minimum_wage:.2f}/hr")
        lines.append(f"- Paid Sick Leave: {'Mandated' if sl.mandated else 'Not mandated'} ({sl.max_annual})")
        lines.append("")
    return "\n".join(lines)


@mcp.resource("hr://categories/all")
def categories_resource() -> str:
    """Reference: all employment law categories covered by this server."""
    return """# HR Compliance MCP — Law Categories

## Tier 1: Wage & Hour (Starter)
- Minimum Wage — State/local rates, tipped wages, scheduled increases
- Overtime Rules — Weekly/daily thresholds, exemptions
- Pay Frequency — How often employers must pay
- Pay Transparency — Salary range disclosure requirements
- Wage Comparison — Side-by-side multi-state comparison

## Tier 2: Leave Laws (Starter)
- Paid Sick Leave — Accrual rates, maximums, eligibility
- Family/Medical Leave — State-level paid leave programs beyond FMLA
- Vacation Payout — Use-it-or-lose-it vs mandatory payout rules
- Voting Leave — Time-off-to-vote requirements
- Bereavement Leave — Mandated bereavement leave

## Tier 3: Compliance & Protections (Pro)
- Discrimination Protections — State protected classes beyond federal
- Background Check Laws — Ban-the-box, fair chance hiring
- Drug Testing Rules — Pre-employment, random, marijuana protections
- Non-Compete Rules — Enforceability, income thresholds
- Workplace Safety — State OSHA plans, unique requirements

## Tier 4: Intelligence (Pro)
- Recent Changes — Law changes since a given date
- State Compliance Comparison — Full multi-state comparison
- Compliance Calendar — Upcoming effective dates
- Employment Law Search — Free-text search across all data
"""


def main():
    try:
        mcp.run()
    except KeyboardInterrupt:
        pass
