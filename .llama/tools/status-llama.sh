#!/bin/bash

nvidia-smi --query-gpu=memory.total,memory.used,memory.free --format=csv
