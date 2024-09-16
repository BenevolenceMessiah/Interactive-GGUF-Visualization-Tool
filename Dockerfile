# Dockerfile

# Use the official Python 3.10 slim image as the base
FROM python:3.10-slim

# Set environment variables to prevent Python from writing .pyc files and buffer outputs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    build-essential \
    cmake \
    wget \
    curl \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Clone and install llama-cpp-python
RUN git clone https://github.com/ggerganov/llama-cpp-python.git && \
    cd llama-cpp-python && \
    LLAMA_CUBLAS=1 pip install . && \
    cd ..

# Copy the rest of the application code
COPY . /app

# Set the working directory
WORKDIR /app

# Expose the ports Gradio runs on
# EXPOSE 7933 7934
EXPOSE 7934

# Define the default command to run your application
CMD ["python", "main.py"]
