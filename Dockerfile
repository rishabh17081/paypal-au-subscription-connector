FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python files individually to ensure they exist
COPY entrypoint.py ./
COPY paypal_au_subscription_mcp.py ./
COPY setup.py ./

# Make the entrypoint script executable
RUN chmod +x entrypoint.py

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PAYPAL_ENVIRONMENT=MOCKDB

# Run the MCP server using the stdio transport
CMD ["python", "entrypoint.py"]
