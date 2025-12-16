#!/bin/bash
# Docker Commands Helper Script
# This script provides commands for building, running, and pushing the Docker image

set -e

IMAGE_NAME="mlops-app"
DOCKER_USERNAME="${DOCKER_USERNAME:-yourusername}"  # Replace with your Docker Hub username
VERSION="v1"

echo "=== Docker Commands for MLOps Project ==="
echo ""

# Function to build the image
build_image() {
    echo "Building Docker image: ${IMAGE_NAME}"
    docker build -t ${IMAGE_NAME} .
    echo "✅ Build complete!"
}

# Function to run the container
run_container() {
    echo "Running Docker container: ${IMAGE_NAME}"
    docker run --rm ${IMAGE_NAME}
    echo "✅ Container execution complete!"
}

# Function to tag the image
tag_image() {
    echo "Tagging image for Docker Hub..."
    docker tag ${IMAGE_NAME} ${DOCKER_USERNAME}/${IMAGE_NAME}:${VERSION}
    docker tag ${IMAGE_NAME} ${DOCKER_USERNAME}/${IMAGE_NAME}:latest
    echo "✅ Image tagged!"
}

# Function to push the image
push_image() {
    echo "Pushing image to Docker Hub..."
    echo "Make sure you're logged in: docker login"
    docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${VERSION}
    docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:latest
    echo "✅ Image pushed!"
}

# Function to show all commands
show_commands() {
    echo "Available commands:"
    echo "  ./docker-commands.sh build    - Build the Docker image"
    echo "  ./docker-commands.sh run      - Run the Docker container"
    echo "  ./docker-commands.sh tag      - Tag image for Docker Hub"
    echo "  ./docker-commands.sh push     - Push image to Docker Hub"
    echo "  ./docker-commands.sh all      - Build, tag, and push"
    echo ""
    echo "Manual commands:"
    echo "  docker build -t ${IMAGE_NAME} ."
    echo "  docker run ${IMAGE_NAME}"
    echo "  docker tag ${IMAGE_NAME} ${DOCKER_USERNAME}/${IMAGE_NAME}:${VERSION}"
    echo "  docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${VERSION}"
}

# Main script logic
case "$1" in
    build)
        build_image
        ;;
    run)
        run_container
        ;;
    tag)
        tag_image
        ;;
    push)
        push_image
        ;;
    all)
        build_image
        tag_image
        echo "Ready to push. Run: ./docker-commands.sh push"
        ;;
    *)
        show_commands
        ;;
esac

