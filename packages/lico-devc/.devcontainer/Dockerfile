# packages/lico-devc/.devcontainer/Dockerfile
# "Minimal Spark" - The definitive clean room for Lico.

FROM python:3.12-slim-bookworm

# 1. Install minimal system tools (The "Substance")
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    ca-certificates \
    openssh-server \
    sudo \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# 2. Install Docker CLI (Docker-out-of-Docker)
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update && apt-get install -y --no-install-recommends docker-ce-cli && \
    rm -rf /var/lib/apt/lists/*

# 3. Install Node.js & Yarn
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    npm install --global yarn && \
    rm -rf /var/lib/apt/lists/*

# 4. Install uv (The Project Engine)
ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod +x /install.sh && /install.sh && rm /install.sh

# 5. Environment configuration
ENV PATH="/root/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
WORKDIR /workspace

# Initial entrypoint is now the Provisioning System
# This script creates users and starts sshd at runtime.
CMD ["python3", "/workspace/packages/lico-devc/src/lico_devc/provision.py"]
