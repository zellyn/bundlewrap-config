#!/bin/bash
set -euo pipefail

# Bootstrap uv if not installed
if ! command -v uv &> /dev/null; then
    echo "uv not found. Please install it: https://docs.astral.sh/uv/getting-started/installation/"
    exit 1
fi

echo "Using uv - dependencies will be managed automatically via the bw script"
