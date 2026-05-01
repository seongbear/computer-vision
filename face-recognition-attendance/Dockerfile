FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglx-mesa0 \
    libglib2.0-0 \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# Install the 'uv' package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uv

# Set the working directory
WORKDIR /app

# Copy the dependency files first (Leverages Docker caching)
COPY requirements.txt ./

# Install Python dependencies using 'uv'
RUN uv pip install --no-cache-dir -r requirements.txt

# Copy source code to the container
COPY main.py .
COPY app/ ./app/

# Run the script
CMD ["uv", "run", "main.py"]