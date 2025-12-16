# EC2 Quick Start Guide

## Your EC2 Details
- **IP**: 13.60.67.119
- **Key**: Mlops.pem
- **User**: ubuntu
- **OS**: Ubuntu 22.04

## Quick Setup (3 Steps)

### 1. Connect to EC2
```bash
chmod 400 Mlops.pem
ssh -i Mlops.pem ubuntu@13.60.67.119
```

### 2. Install Dependencies
```bash
sudo apt update
sudo apt install -y docker.io python3-pip awscli
sudo systemctl start docker
sudo usermod -aG docker $USER
```

### 3. Set Up Project
```bash
mkdir -p ~/mlops-project/{src,data,models}
cd ~/mlops-project
aws s3 cp s3://mlops-test-ass/dataset.csv ./data/dataset.csv
pip3 install pandas scikit-learn numpy boto3
```

## Using Helper Scripts

### Connect to EC2
```bash
./ec2_connect.sh
```

### Upload Project Files
```bash
./upload_to_ec2.sh
```

## Security Group Setup

**Important**: Open port 8000 in AWS Console:
1. EC2 → Instances → Your instance
2. Security → Security groups
3. Edit inbound rules
4. Add: TCP, Port 8000, Source: 0.0.0.0/0

## Verify Setup
```bash
docker --version
python3 --version
pip3 --version
aws --version
```

