"""API key auth + per-key tier enforcement.

Keys are loaded from the HR_API_KEYS env var as JSON:
    HR_API_KEYS='{"hrk_starter_demo": "starter", "hrk_pro_demo": "pro"}'

Tier values: "starter" (Tier 1+2 only) or "pro" (all tiers).

For dev/onboarding the first 5-10 customers, env-var-backed keys are
sufficient. When we have >20 customers or need self-serve signup, swap the
loader for a SQLite/Postgres-backed table without changing call sites.
"""

import json
import os
import time
from collections import defaultdict, deque
from typing import Literal

from fastapi import Header, HTTPException, status

Tier = Literal["starter", "pro"]


def _load_keys() -> dict[str, Tier]:
    raw = os.environ.get("HR_API_KEYS", "").strip()
    if not raw:
        # Dev fallback so local curl works without env config.
        return {"hrk_dev_starter": "starter", "hrk_dev_pro": "pro"}
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"HR_API_KEYS is not valid JSON: {exc}") from exc
    return {k: v.lower() for k, v in parsed.items()}


_KEYS = _load_keys()


# Sliding-window rate limit: per-key, last 60 seconds. Each tier has its
# own ceiling. In-memory only — fine for single-instance deploys; swap for
# Redis when we go multi-instance.
_REQ_LOG: dict[str, deque] = defaultdict(deque)
_RATE_LIMITS = {"starter": 60, "pro": 300}  # requests per minute
_WINDOW_SECONDS = 60


def _check_rate_limit(api_key: str, tier: Tier) -> None:
    now = time.monotonic()
    log = _REQ_LOG[api_key]
    while log and log[0] < now - _WINDOW_SECONDS:
        log.popleft()
    limit = _RATE_LIMITS[tier]
    if len(log) >= limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded: {limit} requests/minute for tier '{tier}'",
        )
    log.append(now)


def require_starter(x_api_key: str | None = Header(default=None)) -> Tier:
    """FastAPI dependency: any valid key (Starter or Pro) passes."""
    if not x_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing X-API-Key header",
        )
    tier = _KEYS.get(x_api_key)
    if tier is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key",
        )
    _check_rate_limit(x_api_key, tier)
    return tier


def require_pro(x_api_key: str | None = Header(default=None)) -> Tier:
    """FastAPI dependency: only Pro keys pass; Starter gets 402."""
    tier = require_starter(x_api_key)
    if tier != "pro":
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail="This endpoint requires the Pro plan ($99/mo). Upgrade at https://hrcompliance.dev/waitlist",
        )
    return tier


# Test seam — pytest fixtures call this to inject keys without env mutation.
def _set_keys_for_testing(keys: dict[str, Tier]) -> None:
    global _KEYS
    _KEYS = keys
    _REQ_LOG.clear()
