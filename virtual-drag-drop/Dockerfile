# Use a slim Python 3.11 image 
FROM python:3.11-slim

# Install system dependencies 
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglx-mesa0 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install the 'uv' package manager 
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory
WORKDIR /app

# Copy the dependency files first (Leverages Docker caching)
COPY pyproject.toml uv.lock ./

# Install Python dependencies using 'uv'
RUN uv sync --frozen --no-install-project --no-dev

# Copy source code to the container
COPY main.py .
COPY app/ ./app/

# Run the script 
CMD ["uv", "run", "main.py"]