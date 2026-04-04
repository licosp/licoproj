# !/bin/sh

# Minimal Spark: Find our ground and handover to Python

SCRIPT_DIR=$(dirname "$(realpath "$0")")
exec python3 "$SCRIPT_DIR/src/lico_devc/boot.py" "$@"
