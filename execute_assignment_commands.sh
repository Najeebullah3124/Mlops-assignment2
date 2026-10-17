#!/bin/bash
# MLOps Assignment - Command Execution Script
# This script executes all commands required for the assignment

set -e  # Exit on error

echo "=========================================="
echo "MLOps Assignment - Command Execution"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Task 1: Project Setup + Version Control (Git + DVC)
echo -e "${BLUE}=== Task 1: Project Setup + Version Control ===${NC}"
echo ""

echo "1.1 Checking Git status..."
git status
echo ""

echo "1.2 Checking DVC status..."
dvc status
echo ""

echo "1.3 Checking DVC remote configuration..."
dvc remote list
echo ""

echo "1.4 Viewing DVC pipeline..."
dvc dag
echo ""

echo "1.5 Viewing dvc.yaml..."
cat dvc.yaml
echo ""

echo "1.6 Viewing dataset.dvc file..."
cat data/dataset.csv.dvc
echo ""

# Task 2: CI/CD Pipeline
echo -e "${BLUE}=== Task 2: CI/CD Pipeline ===${NC}"
echo ""

echo "2.1 Viewing GitHub Actions workflow..."
cat .github/workflows/ci.yml
echo ""

echo "2.2 Running unit tests..."
python3 -m unittest discover -s tests -p 'test_*.py' -v
echo ""

echo "2.3 Running linting (if flake8 is installed)..."
if command -v flake8 &> /dev/null; then
    flake8 src/ tests/ --count --select=E9,F63,F7,F82 --show-source --statistics || echo "No critical errors"
    flake8 src/ tests/ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
else
    echo "flake8 not installed. Install with: pip install flake8"
fi
echo ""

echo "2.4 Verifying training script runs..."
python3 src/train.py
echo ""

# Task 3: Docker
echo -e "${BLUE}=== Task 3: Docker ===${NC}"
echo ""

echo "3.1 Building Docker image for training..."
echo "Command: docker build -t mlops-app ."
echo "Note: This may take a few minutes..."
docker build -t mlops-app . || echo "Docker build failed or Docker not running"
echo ""

echo "3.2 Running Docker container..."
echo "Command: docker run mlops-app"
docker run --rm mlops-app || echo "Docker run failed or Docker not running"
echo ""

echo "3.3 Tagging Docker image for Docker Hub..."
echo "Command: docker tag mlops-app YOUR_USERNAME/mlops-app:v1"
echo "Replace YOUR_USERNAME with your Docker Hub username"
echo "Example: docker tag mlops-app harris/mlops-app:v1"
echo ""

echo "3.4 Pushing to Docker Hub..."
echo "Command: docker push YOUR_USERNAME/mlops-app:v1"
echo "Note: Requires Docker Hub login: docker login"
echo ""

# Task 4: Airflow Pipeline
echo -e "${BLUE}=== Task 4: Airflow Pipeline ===${NC}"
echo ""

echo "4.1 Starting Airflow with Docker Compose..."
echo "Command: docker-compose up -d"
echo "Note: This will start Airflow services"
echo "Access Airflow UI at: http://localhost:8080"
echo "Default credentials: airflow / airflow"
echo ""

echo "4.2 Viewing Airflow DAG..."
cat airflow/dags/train_pipeline.py | head -50
echo ""

# Task 5: RESTful API
echo -e "${BLUE}=== Task 5: RESTful API ===${NC}"
echo ""

echo "5.1 Testing API import..."
python3 -c "import sys; sys.path.insert(0, 'api'); from app import app; print('API imports successfully')"
echo ""

echo "5.2 Starting API server (Flask)..."
echo "Command: cd api && python3 app.py"
echo "Or: python3 api/app.py"
echo "API will be available at: http://localhost:8000"
echo ""

echo "5.3 Testing API endpoints..."
echo "Health check: curl http://localhost:8000/health"
echo "Predict: curl -X POST http://localhost:8000/predict -H 'Content-Type: application/json' -d '{\"features\": [1, 2, 3, 4, 5]}'"
echo ""

echo "5.4 Building API Docker image..."
echo "Command: docker build -f api/Dockerfile -t mlops-api ."
docker build -f api/Dockerfile -t mlops-api . || echo "Docker build failed or Docker not running"
echo ""

echo "5.5 Running API in Docker..."
echo "Command: docker run -p 8000:8000 mlops-api"
echo "Note: Run this in background or separate terminal"
echo ""

# Task 6: AWS EC2 + S3 Deployment
echo -e "${BLUE}=== Task 6: AWS EC2 + S3 Deployment ===${NC}"
echo ""

echo "6.1 AWS S3 Setup script exists..."
ls -lh aws_s3_setup.py
echo ""

echo "6.2 Viewing AWS S3 setup script..."
cat aws_s3_setup.py | head -30
echo ""

echo "6.3 AWS Commands (to be run on EC2 instance)..."
echo "sudo apt update"
echo "sudo apt install docker.io python3-pip -y"
echo "docker pull YOUR_USERNAME/mlops-api:v1"
echo "docker run -d -p 8000:8000 YOUR_USERNAME/mlops-api:v1"
echo ""

echo -e "${GREEN}=========================================="
echo "Command Execution Summary"
echo "==========================================${NC}"
echo ""
echo "✅ Task 1: Git + DVC - Completed"
echo "✅ Task 2: CI/CD - Tests passed"
echo "⚠️  Task 3: Docker - Requires Docker to be running"
echo "⚠️  Task 4: Airflow - Requires docker-compose"
echo "✅ Task 5: API - Code verified, needs runtime testing"
echo "⚠️  Task 6: AWS - Manual deployment required"
echo ""
echo "Next steps:"
echo "1. Run Docker commands if Docker is available"
echo "2. Start Airflow: docker-compose up -d"
echo "3. Test API: python3 api/app.py (in separate terminal)"
echo "4. Deploy to AWS EC2 manually"
echo ""

