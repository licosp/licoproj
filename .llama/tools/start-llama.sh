#!/bin/bash

.llama/tools/stop-llama.sh

llama-server \
    --models-dir ~/develop/.llama/models \
    --models-preset .llama/assets/models.ini \
    2>&1 | tee .temp/llama/logs/debug-server.log
