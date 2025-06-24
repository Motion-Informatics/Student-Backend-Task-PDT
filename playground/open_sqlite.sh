#!/bin/bash
# Get the last (most recent) CONTAINER ID from `docker ps`
CONTAINER_ID=$(docker ps -q | head -n 1)

# If no container is running, exit
if [ -z "$CONTAINER_ID" ]; then
  echo "No running Docker containers found."
  exit 1
fi

# Open an interactive sqlite3 shell inside the container
docker exec -it "$CONTAINER_ID" sh -c "sqlite3 /var/task/database/SSMD.db"