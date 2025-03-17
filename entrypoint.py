#!/usr/bin/env python3
"""
Entrypoint script for the PayPal AU Subscription Connector MCP server.
This file imports the FastMCP instance from paypal_au_subscription_mcp.py and runs it.
"""

from paypal_au_subscription_mcp import mcp

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
