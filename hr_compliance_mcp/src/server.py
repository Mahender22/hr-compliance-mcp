from fastmcp import FastMCP

mcp = FastMCP(
    name="HR Compliance MCP Server",
    instructions=(
        "You are connected to a 50-state employment law intelligence MCP server. "
        "Use these tools to look up minimum wages, overtime rules, paid leave mandates, "
        "pay transparency requirements, discrimination protections, background check laws, "
        "non-compete rules, and more across all US states."
    ),
)


def main():
    try:
        mcp.run()
    except KeyboardInterrupt:
        pass
