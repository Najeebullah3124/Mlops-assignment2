#!/bin/bash
# Script to push Docker image to Docker Hub
# Usage: ./push_to_dockerhub.sh <your-dockerhub-username>

if [ -z "$1" ]; then
    echo "Usage: ./push_to_dockerhub.sh <your-dockerhub-username>"
    echo "Example: ./push_to_dockerhub.sh johndoe"
    exit 1
fi

DOCKER_USERNAME="$1"
IMAGE_NAME="mlops-app"
VERSION="v1"

echo "=== Pushing to Docker Hub ==="
echo "Username: $DOCKER_USERNAME"
echo "Image: $IMAGE_NAME"
echo ""

# Check if image exists
if ! docker images | grep -q "$IMAGE_NAME"; then
    echo "❌ Image $IMAGE_NAME not found!"
    echo "Building image first..."
    docker build -t $IMAGE_NAME .
fi

# Tag image
echo "Tagging image..."
docker tag $IMAGE_NAME $DOCKER_USERNAME/$IMAGE_NAME:$VERSION
docker tag $IMAGE_NAME $DOCKER_USERNAME/$IMAGE_NAME:latest

# Login to Docker Hub
echo ""
echo "Logging in to Docker Hub..."
echo "Please enter your Docker Hub credentials:"
docker login

if [ $? -ne 0 ]; then
    echo "❌ Docker Hub login failed!"
    exit 1
fi

# Push image
echo ""
echo "Pushing image to Docker Hub..."
docker push $DOCKER_USERNAME/$IMAGE_NAME:$VERSION
docker push $DOCKER_USERNAME/$IMAGE_NAME:latest

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Successfully pushed to Docker Hub!"
    echo "Image URL: https://hub.docker.com/r/$DOCKER_USERNAME/$IMAGE_NAME"
else
    echo ""
    echo "❌ Push failed. Please check your Docker Hub credentials."
fi

