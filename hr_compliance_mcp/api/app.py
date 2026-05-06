"""FastAPI surface mirroring the MCP tools.

The MCP server (server.py) is the canonical home of the tool definitions —
this module wraps the same data layer (wages.py, leave.py, compliance.py,
intelligence.py) for HTTP clients who can't speak MCP. Auth lives in auth.py;
keep this file focused on routing.

Tier mapping mirrors server.py's _check_pro_tier exactly:
  - Tier 1 (Wage & Hour) and Tier 2 (Leave) → Starter
  - Tier 3 (Compliance) and Tier 4 (Intelligence) → Pro

Run locally:
    pip install -e ".[api,dev]"
    HR_API_KEYS='{"hrk_dev": "pro"}' uvicorn hr_compliance_mcp.api.app:app --reload

Then visit http://127.0.0.1:8000/docs for OpenAPI explorer.
"""

from fastapi import Depends, FastAPI

from ..src import compliance, intelligence, leave, wages
from .auth import require_pro, require_starter


def _ok(data) -> dict:
    return {"status": "success", "data": data}


def _err(message: str, code: int = 400) -> dict:
    return {"status": "error", "message": message}


app = FastAPI(
    title="HR Compliance API",
    description=(
        "REST surface for the HR Compliance MCP. 50-state US employment law — "
        "minimum wage, overtime, leave, pay transparency, discrimination, "
        "background checks, and more. Same data layer as the open-source MCP server."
    ),
    version="0.1.0",
    contact={
        "name": "HR Compliance",
        "url": "https://hrcompliance.dev",
    },
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
)


# ---------------------------------------------------------------------------
# Health + meta — no auth, useful for uptime checks and load balancers.
# ---------------------------------------------------------------------------

@app.get("/healthz", tags=["meta"])
def healthz() -> dict:
    return {"status": "ok"}


@app.get("/v1/states", tags=["meta"])
def supported_states() -> dict:
    return {"status": "success", "states": sorted(wages.SUPPORTED_STATES)}


# ---------------------------------------------------------------------------
# Tier 1 — Wage & Hour (Starter+)
# ---------------------------------------------------------------------------

@app.get("/v1/wage/{state}", tags=["wage"], dependencies=[Depends(require_starter)])
def get_minimum_wage(state: str, include_local: bool = True) -> dict:
    try:
        d = wages.get_minimum_wage(state).to_dict()
        if not include_local:
            d.pop("local_rates", None)
        return _ok(d)
    except ValueError as exc:
        return _err(str(exc))


@app.get("/v1/overtime/{state}", tags=["wage"], dependencies=[Depends(require_starter)])
def get_overtime(state: str) -> dict:
    try:
        return _ok(wages.get_overtime_rules(state).to_dict())
    except ValueError as exc:
        return _err(str(exc))


@app.get("/v1/pay-frequency/{state}", tags=["wage"], dependencies=[Depends(require_starter)])
def get_pay_frequency(state: str) -> dict:
    try:
        return _ok(wages.get_pay_frequency(state).to_dict())
    except ValueError as exc:
        return _err(str(exc))


@app.get("/v1/pay-transparency/{state}", tags=["wage"], dependencies=[Depends(require_starter)])
def get_pay_transparency(state: str) -> dict:
    try:
        return _ok(wages.get_pay_transparency(state).to_dict())
    except ValueError as exc:
        return _err(str(exc))


@app.get("/v1/wage/compare", tags=["wage"], dependencies=[Depends(require_starter)])
def compare_wages(states: str) -> dict:
    """Compare minimum wages across states. `states` is a comma-separated list, e.g. ?states=CA,NY,IL"""
    state_list = [s.strip() for s in states.split(",") if s.strip()]
    try:
        results = wages.compare_wages(state_list)
        return {
            "status": "success",
            "comparison": [r.to_dict() for r in results],
            "highest": results[0].to_dict() if results else None,
            "lowest": results[-1].to_dict() if results else None,
        }
    except ValueError as exc:
        return _err(str(exc))


# ---------------------------------------------------------------------------
# Tier 2 — Leave Laws (Starter+)
# ---------------------------------------------------------------------------

@app.get("/v1/leave/sick/{state}", tags=["leave"], dependencies=[Depends(require_starter)])
def get_sick_leave(state: str) -> dict:
    try:
        return _ok(leave.get_paid_sick_leave(state).to_dict())
    except ValueError as exc:
        return _err(str(exc))


@app.get("/v1/leave/family/{state}", tags=["leave"], dependencies=[Depends(require_starter)])
def get_family_leave(state: str) -> dict:
    try:
        return _ok(leave.get_family_leave(state).to_dict())
    except ValueError as exc:
        return _err(str(exc))


@app.get("/v1/leave/vacation-payout/{state}", tags=["leave"], dependencies=[Depends(require_starter)])
def get_vacation_payout(state: str) -> dict:
    try:
        return _ok(leave.get_vacation_payout(state).to_dict())
    except ValueError as exc:
        return _err(str(exc))


@app.get("/v1/leave/voting/{state}", tags=["leave"], dependencies=[Depends(require_starter)])
def get_voting_leave(state: str) -> dict:
    try:
        return _ok(leave.get_voting_leave(state).to_dict())
    except ValueError as exc:
        return _err(str(exc))


@app.get("/v1/leave/bereavement/{state}", tags=["leave"], dependencies=[Depends(require_starter)])
def get_bereavement_leave(state: str) -> dict:
    try:
        return _ok(leave.get_bereavement_leave(state).to_dict())
    except ValueError as exc:
        return _err(str(exc))


# ---------------------------------------------------------------------------
# Tier 3 — Compliance & Protections (Pro)
# ---------------------------------------------------------------------------

@app.get("/v1/compliance/discrimination/{state}", tags=["compliance"], dependencies=[Depends(require_pro)])
def get_discrimination(state: str) -> dict:
    try:
        return _ok(compliance.get_discrimination_protections(state).to_dict())
    except ValueError as exc:
        return _err(str(exc))


@app.get("/v1/compliance/background-check/{state}", tags=["compliance"], dependencies=[Depends(require_pro)])
def get_background_check(state: str) -> dict:
    try:
        return _ok(compliance.get_background_check_laws(state).to_dict())
    except ValueError as exc:
        return _err(str(exc))


@app.get("/v1/compliance/drug-testing/{state}", tags=["compliance"], dependencies=[Depends(require_pro)])
def get_drug_testing(state: str) -> dict:
    try:
        return _ok(compliance.get_drug_testing_rules(state).to_dict())
    except ValueError as exc:
        return _err(str(exc))


@app.get("/v1/compliance/noncompete/{state}", tags=["compliance"], dependencies=[Depends(require_pro)])
def get_noncompete(state: str) -> dict:
    try:
        return _ok(compliance.get_noncompete_rules(state).to_dict())
    except ValueError as exc:
        return _err(str(exc))


@app.get("/v1/compliance/safety/{state}", tags=["compliance"], dependencies=[Depends(require_pro)])
def get_safety(state: str) -> dict:
    try:
        return _ok(compliance.get_workplace_safety(state).to_dict())
    except ValueError as exc:
        return _err(str(exc))


# ---------------------------------------------------------------------------
# Tier 4 — Intelligence (Pro)
# ---------------------------------------------------------------------------

@app.get("/v1/intel/recent-changes/{state}", tags=["intel"], dependencies=[Depends(require_pro)])
def recent_changes(state: str, since: str = "2024-01-01") -> dict:
    try:
        results = intelligence.get_recent_changes(state, since=since)
        return {
            "status": "success",
            "state": state.upper(),
            "changes": [r.to_dict() for r in results],
            "count": len(results),
        }
    except ValueError as exc:
        return _err(str(exc))


@app.get("/v1/intel/compare", tags=["intel"], dependencies=[Depends(require_pro)])
def compare_compliance(states: str, company_size: int = 50) -> dict:
    state_list = [s.strip() for s in states.split(",") if s.strip()]
    try:
        result = intelligence.compare_state_compliance(state_list, company_size=company_size)
        return {"status": "success", "company_size": company_size, "comparison": result}
    except ValueError as exc:
        return _err(str(exc))


@app.get("/v1/intel/calendar", tags=["intel"], dependencies=[Depends(require_pro)])
def compliance_calendar(state: str | None = None) -> dict:
    try:
        results = intelligence.get_compliance_calendar(state=state)
        return {"status": "success", "calendar": [r.to_dict() for r in results], "count": len(results)}
    except ValueError as exc:
        return _err(str(exc))


@app.get("/v1/intel/search", tags=["intel"], dependencies=[Depends(require_pro)])
def search(query: str, state: str | None = None) -> dict:
    try:
        results = intelligence.search_employment_law(query, state=state)
        return {"status": "success", "query": query, "results": results, "count": len(results)}
    except ValueError as exc:
        return _err(str(exc))


def main() -> None:
    """Console-script entrypoint: `hr-compliance-api`."""
    import os
    import uvicorn
    uvicorn.run(
        "hr_compliance_mcp.api.app:app",
        host=os.environ.get("HOST", "0.0.0.0"),
        port=int(os.environ.get("PORT", "8000")),
    )
