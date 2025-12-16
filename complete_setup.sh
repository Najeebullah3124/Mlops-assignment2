#!/bin/bash
# Complete Docker and Airflow Setup Script

echo "=== Complete Setup Script ==="
echo ""

# Check if Docker is running
if ! docker ps &>/dev/null; then
    echo "❌ Docker Desktop is not running!"
    echo "Please start Docker Desktop first, then run this script again."
    exit 1
fi

echo "✅ Docker is running"
echo ""

echo "Step 1: Building Docker image..."
docker build -t mlops-app . 2>&1 | tail -5

echo ""
echo "Step 2: Testing Docker container..."
docker run --rm mlops-app 2>&1 | tail -10

echo ""
echo "Step 3: Initializing Airflow..."
docker compose up airflow-init 2>&1 | tail -10

echo ""
echo "Step 4: Starting Airflow services..."
docker compose up -d 2>&1

echo ""
echo "Step 5: Waiting for services to start..."
sleep 15

echo ""
echo "Step 6: Checking service status..."
docker compose ps

echo ""
echo "✅ Setup Complete!"
echo ""
echo "Access Airflow UI: http://localhost:8080"
echo "Username: airflow"
echo "Password: airflow"
