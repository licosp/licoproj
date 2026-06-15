#!/bin/bash

.llama/tools/status-llama.sh

LOG=".temp/ollama/ollama-debug.jsonl"
REQUEST=".ollama/assets/ollama-request.json"
FILTER=".ollama/assets/ollama-parse.jq"

DEFAULT_PROMPT=".llama/assets/prompt-talk.md"
DEFAULT_MODEL="gemma4:12b-it-qat-128K-subj"
DEFAULT_URL="http://localhost:11434/api/generate"

usage() {
  echo "Usage: $0 -m <model> [-u <url>] [-p <prompt-file>]"
  echo "  -p  prompt file (default: ${DEFAULT_PROMPT})"
  echo "  -m  model name (default: ${DEFAULT_MODEL})"
  echo "  -u  url        (default: ${DEFAULT_URL})"
  echo ""
  echo "Example:"
  echo "  $0 -p .llama/assets/prompt-talk.md"
  echo "  $0 -m gemma4:12b-it-qat-128K-subj"
  echo "  $0 -u http://localhost:11434/api/generate"
  exit 1
}

MODEL="${DEFAULT_MODEL}"
URL="${DEFAULT_URL}"
PROMPT_FILE="${DEFAULT_PROMPT}"

while getopts "m:u:p:" opt; do
  case ${opt} in
  m) MODEL="${OPTARG}" ;;
  u) URL="${OPTARG}" ;;
  p) PROMPT_FILE="${OPTARG}" ;;
  *) usage ;;
  esac
done

if [ ! -f "${PROMPT_FILE}" ]; then
  echo "Error: prompt file not found: ${PROMPT_FILE}"
  exit 1
fi

mkdir -p "$(dirname "${LOG}")"

PATCHED_REQ="$(jq \
  --arg model "${MODEL}" \
  --rawfile prompt "${PROMPT_FILE}" \
  '.model = $model | .prompt = $prompt' \
  "${REQUEST}")"

curl -X POST \
  -H "Content-Type: application/json" \
  --data-binary "${PATCHED_REQ}" \
  "${URL}" |
  jq --argjson req "${PATCHED_REQ}" \
    -f "${FILTER}" >>"${LOG}"
