#!/bin/bash

# Define the container name
CONTAINER_NAME=postgres
DATABASE_NAME=waifu-db

# Build the Docker container
sudo docker build -t $CONTAINER_NAME .

# Run the Docker container
sudo docker run -p 127.0.0.1:5432:5432 --name $DATABASE_NAME -d $CONTAINER_NAME

# Check if the container is running
if [ "$(sudo docker ps -q -f name=$DATABASE_NAME)" ]; then
    echo "PostgreSQL container \"$DATABASE_NAME\" is running"
else
    echo "Failed to start PostgreSQL container"
fi
