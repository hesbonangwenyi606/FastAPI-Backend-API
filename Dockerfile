# ================================
# Stage 1 — Build Environment
# ================================
FROM python:3.11-slim AS builder

LABEL maintainer="hesbonmanyinsa96@gmail.com"

# Prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies and build wheels
RUN pip install --no-cache-dir --upgrade pip && \
    pip wheel --no-cache-dir --no-deps -r requirements.txt -w /wheels && \
    pip wheel "pydantic[email]" -w /wheels

# ================================
# Stage 2 — Runtime Environment
# ================================
FROM python:3.11-slim

WORKDIR /app

# Copy built wheels from builder stage
COPY --from=builder /wheels /wheels

# Install dependencies (including pydantic[email])
RUN pip install --no-cache-dir /wheels/*

# Copy app files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
