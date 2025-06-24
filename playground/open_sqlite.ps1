# Get the last (most recent) CONTAINER ID from `docker ps`
$containerId = docker ps -q | Select-Object -First 1

# If no container is running, exit
if ([string]::IsNullOrEmpty($containerId)) {
    Write-Host "No running Docker containers found."
    exit 1
}

# Open an interactive sqlite3 shell inside the container
docker exec -it $containerId sh -c "sqlite3 /var/task/database/SSMD.db"