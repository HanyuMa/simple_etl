#!/bin/bash

# Build the Docker images and run the Docker containers
docker-compose up -d --build

# Migrate the database
docker-compose exec web python manage.py migrate

