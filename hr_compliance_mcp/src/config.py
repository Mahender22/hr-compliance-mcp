import os

DEMO_MODE = os.environ.get("HR_MCP_DEMO", "").lower() in ("1", "true", "yes")
TIER = os.environ.get("HR_MCP_TIER", "pro").lower()  # "starter" or "pro"
