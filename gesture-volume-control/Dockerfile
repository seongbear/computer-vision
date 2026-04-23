# Use a slim Python image
FROM python:3.10-slim

# Install system dependencies for MediaPipe and OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install uv using the official binary explorer
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set work directory
WORKDIR /app

# Copy lockfiles first to leverage Docker layer caching
COPY pyproject.toml uv.lock ./

# Install dependencies into the system environment
# --frozen ensures uv uses the exact versions in uv.lock
RUN uv sync --frozen --no-install-project --no-dev

# Copy the source code
COPY src/ ./src/

# Run the application
# We use 'uv run' to ensure the environment is correctly loaded
CMD ["uv", "run", "src/VolumeControl.py"]