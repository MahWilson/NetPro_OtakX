#!/bin/bash

echo "Starting NetPilot setup..."

docker compose build
docker compose up -d

echo "Waiting for container..."
sleep 5

docker exec -it netpilot-controller bash