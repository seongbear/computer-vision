# Use a slim Python 3.10 image
FROM python:3.10-slim

# Install system dependencies required by OpenCV to render video
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglx-mesa0 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install the 'uv' package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy dependency files first (for Docker caching)
COPY pyproject.toml uv.lock ./

# Install dependencies strictly from the lockfile
RUN uv sync --frozen --no-install-project --no-dev

# Copy your source code
COPY main.py .
COPY app/ ./app/

# Run the script
CMD ["uv", "run", "main.py"]