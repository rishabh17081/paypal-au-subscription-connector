FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Make the entrypoint script executable
RUN chmod +x entrypoint.py

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PAYPAL_ENVIRONMENT=MOCKDB

# Run the MCP server
CMD ["python", "entrypoint.py"]
