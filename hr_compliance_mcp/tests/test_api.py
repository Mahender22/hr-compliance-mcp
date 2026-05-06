"""End-to-end tests for the REST API.

Uses FastAPI's TestClient — no live server needed. Auth is exercised through
real HTTP request flow (header in, dependency runs, route fires) so a future
swap from env-var auth to DB-backed auth doesn't silently break.
"""

import pytest
from fastapi.testclient import TestClient

from hr_compliance_mcp.api import auth
from hr_compliance_mcp.api.app import app


@pytest.fixture(autouse=True)
def _seed_keys():
    auth._set_keys_for_testing(
        {"hrk_test_starter": "starter", "hrk_test_pro": "pro"}
    )
    yield
    auth._set_keys_for_testing({})


@pytest.fixture
def client():
    return TestClient(app)


# --- Health + meta ----------------------------------------------------------

def test_healthz_no_auth(client):
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_supported_states_no_auth(client):
    r = client.get("/v1/states")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "success"
    assert "ME" in body["states"]
    assert "CA" in body["states"]


# --- Auth -------------------------------------------------------------------

def test_starter_endpoint_requires_key(client):
    r = client.get("/v1/wage/CA")
    assert r.status_code == 401


def test_starter_endpoint_rejects_bad_key(client):
    r = client.get("/v1/wage/CA", headers={"X-API-Key": "hrk_bogus"})
    assert r.status_code == 403


def test_starter_key_can_hit_starter_endpoint(client):
    r = client.get("/v1/wage/CA", headers={"X-API-Key": "hrk_test_starter"})
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "success"
    assert body["data"]["state"] == "CA"


def test_starter_key_blocked_from_pro_endpoint(client):
    r = client.get(
        "/v1/compliance/discrimination/CA",
        headers={"X-API-Key": "hrk_test_starter"},
    )
    assert r.status_code == 402
    assert "Pro plan" in r.json()["detail"]


def test_pro_key_can_hit_pro_endpoint(client):
    r = client.get(
        "/v1/compliance/discrimination/CA",
        headers={"X-API-Key": "hrk_test_pro"},
    )
    assert r.status_code == 200
    assert r.json()["status"] == "success"


# --- Tier 1 routes ----------------------------------------------------------

def test_overtime_endpoint(client):
    r = client.get("/v1/overtime/CA", headers={"X-API-Key": "hrk_test_pro"})
    assert r.status_code == 200
    assert r.json()["data"]["state"] == "CA"


def test_pay_transparency_returns_maine(client):
    r = client.get("/v1/pay-transparency/ME", headers={"X-API-Key": "hrk_test_pro"})
    assert r.status_code == 200
    body = r.json()
    assert body["data"]["state"] == "ME"
    assert body["data"]["effective_date"] == "2026-07-29"


def test_unknown_state_returns_error_payload(client):
    r = client.get("/v1/wage/ZZ", headers={"X-API-Key": "hrk_test_pro"})
    # The endpoint returns 200 with status=error to keep error handling
    # uniform across the API surface (pattern matches MCP server.py).
    assert r.status_code == 200
    assert r.json()["status"] == "error"
    assert "not supported" in r.json()["message"].lower()


# --- Tier 2 routes ----------------------------------------------------------

def test_sick_leave_endpoint(client):
    r = client.get("/v1/leave/sick/CA", headers={"X-API-Key": "hrk_test_starter"})
    assert r.status_code == 200
    assert r.json()["status"] == "success"


# --- Tier 4 routes (Pro) ----------------------------------------------------

def test_compliance_calendar_pro_only(client):
    starter = client.get("/v1/intel/calendar", headers={"X-API-Key": "hrk_test_starter"})
    assert starter.status_code == 402

    pro = client.get("/v1/intel/calendar", headers={"X-API-Key": "hrk_test_pro"})
    assert pro.status_code == 200
    assert pro.json()["status"] == "success"


def test_search_pro_endpoint(client):
    r = client.get(
        "/v1/intel/search",
        params={"query": "minimum wage"},
        headers={"X-API-Key": "hrk_test_pro"},
    )
    assert r.status_code == 200
    assert r.json()["status"] == "success"


# --- Rate limiting ----------------------------------------------------------

def test_rate_limit_blocks_starter_after_60_requests(client):
    headers = {"X-API-Key": "hrk_test_starter"}
    last_status = 200
    for _ in range(70):
        last_status = client.get("/v1/wage/CA", headers=headers).status_code
        if last_status == 429:
            break
    assert last_status == 429
