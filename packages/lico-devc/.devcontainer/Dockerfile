FROM mcr.microsoft.com/devcontainers/python:3.11-bookworm

# Installing required system tools.
RUN apt-get update && apt-get install -y \
    git \
    vim \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Installing Google Gemini SDK and the monitoring library (watchdog).
RUN pip install --no-cache-dir \
    google-generativeai \
    watchdog

# Git user settings for AI.
# (so that it is clear at a glance in the history that this is AI action)
RUN git config --global user.email "ai-agent@example.com" \
    && git config --global user.name "Lico-Agent" \
    && git config --global init.defaultBranch main

WORKDIR /workspace
