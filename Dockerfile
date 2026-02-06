# Use official Python slim image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install system-level dependencies for numpy, pandas, sklearn
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole project
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Use uvicorn to serve the app
CMD ["uvicorn", "application:app", "--host", "0.0.0.0", "--port", "8000"]
