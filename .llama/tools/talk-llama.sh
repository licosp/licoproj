#!/bin/bash

.llama/tools/status-llama.sh

DEBUG_CLIENT=".temp/llama/logs/debug-client.jsonl"
REQUEST=".llama/assets/llama-request.json"
FILTER=".llama/assets/llama-parse.jq"

DEFAULT_PROMPT=".llama/assets/prompt-talk.md"
DEFAULT_MODEL="gemma-4-12B-it-qat-128K-subj-mtp"
DEFAULT_URL="http://localhost:8080/v1/chat/completions"

usage() {
  echo "Usage: $0 [-m <model>] [-u <url>] [-p <prompt-file>]"
  echo "  -p  prompt file (default: ${DEFAULT_PROMPT})"
  echo "  -m  model name  (default: ${DEFAULT_MODEL})"
  echo "  -u  url         (default: ${DEFAULT_URL})"
  echo ""
  echo "Example:"
  echo "  $0 -p .llama/assets/prompt-talk.md"
  echo "  $0 -m gemma-4-12B-it-qat-128K-subj-mtp"
  echo "  $0 -u http://localhost:8080/v1/chat/completions"
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

mkdir -p "$(dirname "${DEBUG_CLIENT}")"

UUID="$(uuidgen)"

PATCHED_REQ="$(jq \
  --compact-output \
  --sort-keys \
  --arg uuid "${UUID}" \
  --arg model "${MODEL}" \
  --rawfile prompt "${PROMPT_FILE}" \
  '.uuid = $uuid | .model = $model | .messages[0].content = $prompt' \
  "${REQUEST}")"

echo "${PATCHED_REQ}" >> \
  "${DEBUG_CLIENT}"

RESPONSE=$(curl -X POST \
  -H "Content-Type: application/json" \
  --data-binary "${PATCHED_REQ}" \
  "${URL}")

PATCHED_RES="$(echo "${RESPONSE}" | jq \
  --compact-output \
  --sort-keys \
  --argjson req "${PATCHED_REQ}" \
  --from-file "${FILTER}")"

echo "${PATCHED_RES}" >> \
  "${DEBUG_CLIENT}"
