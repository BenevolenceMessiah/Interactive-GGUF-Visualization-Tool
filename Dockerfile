# Dockerfile

# Use NVIDIA's CUDA base image
FROM nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu20.04

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    python3.10 \
    python3-pip \
    python3.10-dev \
    build-essential \
    cmake \
    wget \
    curl \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Install pip and upgrade
RUN python3.10 -m pip install --upgrade pip

# Install PyTorch with CUDA 12.1 support
RUN pip install --upgrade --force-reinstall torch==2.2.0 --index-url https://download.pytorch.org/whl/cu121

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies excluding torch
RUN pip install -r requirements.txt

# Build and install llama-cpp-python with CUDA support
RUN git clone https://github.com/ggerganov/llama-cpp-python.git
WORKDIR /app/llama-cpp-python
RUN LLAMA_CUBLAS=1 pip install .

# Return to app directory
WORKDIR /app

# Copy application code
COPY . /app

# Expose port
EXPOSE 7934

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python3.10", "main.py"]
