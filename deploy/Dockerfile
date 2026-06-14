# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy the demo code into the container
COPY code/ ./code

# Expose a port for UI or API extensions if required
EXPOSE 8080

# Default command to run the AIoT demo
CMD ["python3", "code/aiot_demo.py", "--scenario", "smart_mattress"]
