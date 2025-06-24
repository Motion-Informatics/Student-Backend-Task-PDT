#!/bin/bash

# Exit immediately on any error
set -e

echo "🔨 Building Docker image: PDT-Backend-Task"

# Build the image
docker build -t pdt-backend-task .

echo "✅ Build completed successfully!"