#!/bin/sh
# Minimal Spark: Handover to Python orchestration.
exec python3 packages/lico-devc/src/lico_devc/boot.py "$@"
