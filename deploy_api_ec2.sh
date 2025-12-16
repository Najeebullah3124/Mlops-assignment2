#!/bin/bash
# Script to deploy API on EC2
# Usage: ./deploy_api_ec2.sh

EC2_IP="13.60.67.119"
KEY_FILE="Mlops.pem"
USER="ubuntu"
DOCKER_USERNAME="${DOCKER_USERNAME:-yourusername}"
IMAGE_NAME="mlops-api"
VERSION="v1"

echo "=== Deploying API on EC2 ==="
echo ""

# Check if key file exists
if [ ! -f "$KEY_FILE" ]; then
    echo "❌ Error: Key file $KEY_FILE not found!"
    exit 1
fi

# Set permissions
chmod 400 "$KEY_FILE"

echo "Step 1: Uploading API files to EC2..."
scp -i "$KEY_FILE" -r api/ "$USER@$EC2_IP:~/mlops-project/"

echo ""
echo "Step 2: Building Docker image on EC2..."
ssh -i "$KEY_FILE" "$USER@$EC2_IP" << 'ENDSSH'
cd ~/mlops-project/api
docker build -t mlops-api:v1 .
echo "✅ Docker image built"
ENDSSH

echo ""
echo "Step 3: Stopping existing container (if any)..."
ssh -i "$KEY_FILE" "$USER@$EC2_IP" "docker stop mlops-api 2>/dev/null || true && docker rm mlops-api 2>/dev/null || true"

echo ""
echo "Step 4: Running API container..."
ssh -i "$KEY_FILE" "$USER@$EC2_IP" "docker run -d -p 8000:8000 --name mlops-api mlops-api:v1"

echo ""
echo "Step 5: Waiting for API to start..."
sleep 5

echo ""
echo "Step 6: Checking container status..."
ssh -i "$KEY_FILE" "$USER@$EC2_IP" "docker ps | grep mlops-api"

echo ""
echo "Step 7: Testing API endpoint..."
ssh -i "$KEY_FILE" "$USER@$EC2_IP" "curl -s http://localhost:8000/health | head -20"

echo ""
echo "=== Deployment Complete ==="
echo ""
echo "API is running at: http://$EC2_IP:8000"
echo ""
echo "Test endpoints:"
echo "  - Health: http://$EC2_IP:8000/health"
echo "  - Home: http://$EC2_IP:8000/"
echo "  - Predict: POST http://$EC2_IP:8000/predict"
echo ""
echo "Example prediction:"
echo 'curl -X POST http://'$EC2_IP':8000/predict -H "Content-Type: application/json" -d '"'"'{"features": [0.5, -0.1, 0.6, 1.5, -0.2]}'"'"

