#!/bin/bash

# Check if the version parameter is provided
if [ "$1" = "-v" ] && [ -n "$2" ]; then
    VERSION="$2"
else
    echo "Error: Version parameter (-v) is mandatory."
    exit 1
fi

# Export requirements
poetry export -f requirements.txt --output requirements.txt
# Consider adding error handling for this command

# Build Docker image with the version
docker build -t 192.168.0.15:32000/local_storage_exporter:$VERSION .
# Consider adding error handling for this command

# Push Docker image with the version
docker push 192.168.0.15:32000/local_storage_exporter:$VERSION
# Consider adding error handling for this command

# Check if the restart parameter is provided
if [ "$3" = "-r" ]; then
    echo "Restarting deployment..."
    kubectl rollout restart deployment/local_storage_exporter -n local_storage_exporter || { echo "Deployment restart failed"; exit 1; }
fi
