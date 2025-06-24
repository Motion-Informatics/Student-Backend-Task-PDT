# # Stop execution on any error
# $ErrorActionPreference = "Stop"

# Write-Host " Starting container with volume mount"

# # Get the absolute path to the ./database directory
# $databasePath = Resolve-Path "./database"

# # Run Docker container
# docker run -p 9000:8080 `
#   -v "$($databasePath):/var/task/database" `
#   pdt-backend-task


# Stop execution on any error
$ErrorActionPreference = "Stop"

Write-Host "Ensuring database folder exists..."

# Create the database folder if it doesn't exist
if (-Not (Test-Path -Path "./database")) {
    New-Item -ItemType Directory -Path "./database" | Out-Null
    Write-Host "Created ./database directory"
} else {
    Write-Host "./database directory already exists"
}

Write-Host "Starting container with volume mount"

# Get the absolute path to the ./database directory
$databasePath = Resolve-Path "./database"

# Run Docker container
docker run -d -p 9000:8080 `
  -v "$($databasePath):/var/task/database" `
  pdt-backend-task