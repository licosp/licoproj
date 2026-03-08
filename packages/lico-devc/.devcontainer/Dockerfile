# packages/lico-devc/.devcontainer/Dockerfile
# "Minimal Spark" - The definitive clean room for Lico.

FROM python:3.12-slim-bookworm

# 1. Install minimal system tools (The "Substance")
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# 2. Install uv (The Project Engine)
# We pipe the official installer to sh for the latest stable version
ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod +x /install.sh && /install.sh && rm /install.sh

# Ensure uv is available in the PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# 3. Environment configuration
WORKDIR /workspace

# Default to bash for the initial launcher intent
CMD ["/bin/bash"]
