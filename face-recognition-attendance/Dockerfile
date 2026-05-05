FROM python:3.10-slim

# Install System Dependencies (Need these for OpenCV and dlib)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglx-mesa0 \
    libglib2.0-0 \
    cmake \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install 'uv' EXACTLY HERE (Must be before you try to run it!)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Set working directory
WORKDIR /app

# Copy your requirements file
COPY requirements.txt .

# Install dependencies (Now Docker knows what 'uv' is!)
RUN uv pip install --system --no-cache -r requirements.txt

# Copy the rest of your code
COPY . .

# Run the app
CMD ["python", "app/main.py"]