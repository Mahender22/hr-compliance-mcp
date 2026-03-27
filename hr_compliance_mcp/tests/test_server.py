from hr_compliance_mcp.src.server import mcp


def test_server_has_name():
    assert mcp.name == "HR Compliance MCP Server"


def test_server_has_instructions():
    assert "employment law" in mcp.instructions.lower()
