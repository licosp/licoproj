#!/bin/sh
set -e

echo "--- Lico Container Bootstrapper (Shell Spark) ---"

if ! docker compose version >/dev/null 2>&1; then
    echo "[Error] 'docker compose' not found. Please install Docker."
    exit 1
fi

# Run the Python bootstrapper (Source of Truth)
python3 packages/lico-devc/src/lico_devc/boot.py "$@"
