"""
DNSDumpster MCP Server implementation.

This module contains the main MCP server implementation for interacting with the DNSDumpster API.
"""
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("example")


def main():
    """Entry point for the MCP server."""
    return mcp.run()


if __name__ == "__main__":
    main()
