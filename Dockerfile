FROM python:3.11-slim

# Setting environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Setting work directory
WORKDIR /app

# Installing system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Installing Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copying project
COPY . .

# Running the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]