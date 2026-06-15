#!/bin/bash

.llama/tools/status-llama.sh

OLLAMA_DEBUG=1
OLLAMA_HOST=127.0.0.1:11434
OLLAMA_CONTEXT_LENGTH=32k
OLLAMA_KEEP_ALIVE="1m"
OLLAMA_MAX_LOADED_MODELS=1
OLLAMA_MODELS=~/develop/.ollama/models
OLLAMA_NUM_PARALLEL=1
OLLAMA_FLASH_ATTENTION=1
OLLAMA_KV_CACHE_TYPE=q8_0

ollama serve \
    2>&1 | tee .temp/ollama/logs/debug-server.log
