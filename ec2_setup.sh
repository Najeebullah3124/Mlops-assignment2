#!/bin/bash
# EC2 Setup Script - Run this ON the EC2 instance
# This script installs all dependencies and sets up the environment

set -e

echo "=========================================="
echo "EC2 Instance Setup for MLOps Project"
echo "=========================================="
echo ""

# Update system
echo "📦 Updating system packages..."
sudo apt update
sudo apt upgrade -y

# Install Docker
echo ""
echo "🐳 Installing Docker..."
sudo apt install -y docker.io docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Install Python and pip
echo ""
echo "🐍 Installing Python and pip..."
sudo apt install -y python3 python3-pip python3-venv

# Install AWS CLI
echo ""
echo "☁️  Installing AWS CLI..."
sudo apt install -y awscli

# Install Git (if not already installed)
echo ""
echo "📥 Installing Git..."
sudo apt install -y git

# Install additional build tools
echo ""
echo "🔧 Installing build tools..."
sudo apt install -y build-essential gcc

# Verify installations
echo ""
echo "=========================================="
echo "Verifying Installations"
echo "=========================================="
echo ""

echo "Docker version:"
docker --version || echo "⚠️  Docker not working (may need to log out/in)"

echo ""
echo "Python version:"
python3 --version

echo ""
echo "Pip version:"
pip3 --version

echo ""
echo "AWS CLI version:"
aws --version

echo ""
echo "=========================================="
echo "✅ Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Log out and log back in (for Docker group to take effect)"
echo "2. Clone your project or upload files"
echo "3. Install Python dependencies: pip3 install -r requirements.txt"
echo "4. Download dataset from S3: aws s3 cp s3://mlops-test-ass/dataset.csv ./data/dataset.csv"
echo "5. Run training: python3 src/train.py"

