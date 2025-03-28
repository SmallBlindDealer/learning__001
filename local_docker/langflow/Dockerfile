# Use an official Python image as base
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Install Langflow
RUN pip install langflow

# Expose the port
EXPOSE 7860

# Default command to run Langflow
CMD ["langflow", "run", "--host", "0.0.0.0"]

# docker build -t langflow-app .
# docker run -p 7860:7860 langflow-app
