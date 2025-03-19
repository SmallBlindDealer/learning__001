# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# Install dependencies
RUN pip install flask watchdog

# Run Watchdog with auto-restart
CMD ["watchmedo", "auto-restart", "--pattern=*.py", "--recursive", "--", "python", "app.py"]
