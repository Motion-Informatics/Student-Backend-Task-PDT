#!/bin/bash
set -e

echo "🚀 Starting container with volume mount"

docker run -p 9000:8080 \
  -v "$(pwd)/database:/var/task/database" \
  pdt-backend-task