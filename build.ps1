# Stop execution on any errors
$ErrorActionPreference = "Stop"

Write-Host "Building Docker image: PDT-Backend-Task"

# Build Docker image
docker build -t pdt-backend-task .

Write-Host "Build completed successfully!"