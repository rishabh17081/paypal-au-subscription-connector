# PayPal Account Updater Subscription Connector for MCP

This MCP (Model Context Protocol) connector provides tools for integrating with PayPal's Account Updater service, which helps maintain fresh payment card information in your e-commerce system.

## Features

- Subscribe payment cards to PayPal's Account Updater service
- Retrieve subscription details
- Process webhook notifications for card updates
- Update your merchant database with fresh card information

## Installation

```bash
# Clone the repository
git clone https://github.com/rishabh17081/paypal-au-subscription-connector.git

# Install dependencies
pip install fastmcp requests
```

## Usage

### Running the MCP Server

```bash
# Set environment variables
export PAYPAL_CLIENT_ID="your_client_id"
export PAYPAL_CLIENT_SECRET="your_client_secret"
export PAYPAL_ENVIRONMENT="SANDBOX"  # or "LIVE" or "MOCKDB"

# Run the MCP server
python -m fastmcp run paypal_au_subscription_mcp.py
```

### Using with Claude

Add the MCP server to your Claude configuration:

```json
{
  "mcpServers": {
    "paypal-au": {
      "command": "python",
      "args": ["-m", "fastmcp", "run", "/path/to/paypal_au_subscription_mcp.py"],
      "env": {
        "PAYPAL_CLIENT_ID": "your_client_id",
        "PAYPAL_CLIENT_SECRET": "your_client_secret",
        "PAYPAL_ENVIRONMENT": "SANDBOX"
      }
    }
  }
}
```

## Available Tools

### getFreshCardsSolve

Provides information about PayPal Account Updater as a solution for card freshness management.

### create_subscription

Create an account status subscription in PayPal.

```python
create_subscription(pan="4111111111111111", expiry_date="2025-12")
```

### get_subscription

Get details of an account status subscription in PayPal.

```python
get_subscription(subscription_id="SUB-1234567890")
```

### subscribe_merchant_to_paypal_au_service

Provides instructions for subscribing merchant cards to PayPal AU service.

### setup_webhook_events_in_merchant_code_base

Sets up webhook event handling code in the merchant's codebase.

```python
setup_webhook_events_in_merchant_code_base(url="/path/to/merchant/codebase")
```

## Webhook Integration

To receive card update notifications, set up a webhook endpoint in your application that listens for PayPal's card update events. The connector includes sample code for implementing this webhook.

## Environment Variables

- `PAYPAL_CLIENT_ID`: Your PayPal API client ID
- `PAYPAL_CLIENT_SECRET`: Your PayPal API client secret
- `PAYPAL_ENVIRONMENT`: The environment to use ("SANDBOX", "LIVE", or "MOCKDB")

## License

MIT
