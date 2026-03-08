#!/bin/sh
set -e

echo "--- Lico Container Bootstrapper (Shell Spark) ---"

if ! docker compose version >/dev/null 2>&1; then
    echo "[Error] 'docker compose' not found. Please install Docker."
    exit 1
fi

echo "[Action] Starting lico-resident container via docker compose..."
docker compose -f packages/lico-devc/.devcontainer/docker-compose.yml up -d --build

echo "[Success] Lico container 'lico-resident' is now active."
echo "You can now join the conversation from inside the container."
