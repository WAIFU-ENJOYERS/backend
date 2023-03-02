#!/bin/bash

filename="docker-compose.yml"

directory=$(sudo find . -type f -name "$filename" -exec dirname {} \;)

cd "$directory"

sudo docker compose up -d