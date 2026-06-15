#!/bin/bash

.llama/tools/status-llama.sh

pkill -9 -f llama-server
kill -9 $(pgrep -f llama-server)
