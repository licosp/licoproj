#!/bin/bash

.llama/tools/status-llama.sh

pkill -9 -f ollama
kill -9 $(pgrep -f ollama)
