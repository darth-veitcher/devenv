#!/bin/bash
# This script is executed when the devcontainer starts.
set -e
echo "Starting devcontainer setup..."
echo "Current directory: $(pwd)"
echo "Current user: $(whoami)"
echo "------------------------------"
cd /workspace
# Ensure the workspace is clean and up-to-date
git submodule update --init --recursive
git submodule foreach --recursive git fetch
# Run the docker compose file to set up the environment
docker compose -f .devcontainer/compose.yml up -d redis searxng crawl4ai context7-mcp
# Wait for the services to be ready and then update claude and superclaude
claude update
uvx superclaude update --quiet --yes --components commands core mcp || uvx SuperClaude install --profile developer --yes --quiet || true

echo "\n------------------------------"
echo "Devcontainer setup completed successfully."
