# EC2 Setup Guide for MLOps Project

## Prerequisites

- ✅ S3 Bucket created: `mlops-test-ass`
- ✅ Dataset uploaded: `dataset.csv`
- ✅ AWS Account with EC2 access

## Step 1: Create EC2 Instance

### Launch Instance:
1. Go to EC2 Console → Launch Instance
2. **Name**: `mlops-training-instance`
3. **AMI**: Amazon Linux 2023 (free tier eligible)
4. **Instance Type**: t2.micro (free tier)
5. **Key Pair**: Create or select existing
6. **Network Settings**: 
   - Allow SSH (port 22)
   - Allow HTTP/HTTPS if needed
7. **Configure Storage**: 8 GB (free tier)
8. **Advanced Details**: 
   - IAM instance profile (for S3 access)

## Step 2: Configure IAM Role for S3 Access

### Create IAM Role:
1. Go to IAM Console → Roles → Create Role
2. **Trusted Entity**: EC2
3. **Permissions**: 
   - `AmazonS3ReadOnlyAccess` (or custom policy)
4. **Role Name**: `mlops-ec2-s3-role`
5. **Attach to EC2**: 
   - EC2 Console → Instance → Actions → Security → Modify IAM role

### Custom Policy (if needed):
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::mlops-test-ass",
        "arn:aws:s3:::mlops-test-ass/*"
      ]
    }
  ]
}
```

## Step 3: Connect to EC2 Instance

```bash
# SSH into instance
ssh -i your-key.pem ec2-user@<instance-public-ip>

# Or use EC2 Instance Connect from AWS Console
```

## Step 4: Install Dependencies

```bash
# Update system
sudo yum update -y

# Install Python 3 and pip
sudo yum install python3 python3-pip -y

# Install AWS CLI (if not using IAM role)
pip3 install boto3 pandas scikit-learn numpy

# Or install from requirements
# First, upload requirements.txt to instance
pip3 install -r requirements.txt
```

## Step 5: Download Dataset from S3

```bash
# Using AWS CLI
aws s3 cp s3://mlops-test-ass/dataset.csv ./data/dataset.csv

# Or using Python script
python3 aws_s3_setup.py
```

## Step 6: Run Training Script

```bash
# Create project structure
mkdir -p src data models

# Upload training script (or clone from git)
# Then run:
python3 src/train.py
```

## Step 7: Verify Results

```bash
# Check model was created
ls -lh models/model.pkl

# Verify model file
file models/model.pkl
```

## Quick Setup Script for EC2

```bash
#!/bin/bash
# Run this on EC2 instance

# Install dependencies
sudo yum install python3 python3-pip -y
pip3 install boto3 pandas scikit-learn numpy

# Create directories
mkdir -p src data models

# Download dataset from S3
aws s3 cp s3://mlops-test-ass/dataset.csv ./data/dataset.csv

# Verify download
python3 -c "import pandas as pd; df = pd.read_csv('data/dataset.csv'); print(f'Dataset: {df.shape}')"
```

## Troubleshooting

### S3 Access Denied
- Check IAM role is attached to EC2
- Verify bucket policy allows access
- Check security groups allow outbound HTTPS

### Python Not Found
- Use `python3` instead of `python`
- Install: `sudo yum install python3 -y`

### Permission Denied
- Use `sudo` for system operations
- Check file permissions: `chmod +x script.sh`

## Cost Optimization (Free Tier)

- Use t2.micro instance
- Use same region (eu-north-1) for S3 and EC2
- Stop instance when not in use
- Use spot instances for training (optional)

## Next Steps

1. ✅ Create EC2 instance
2. ✅ Configure IAM role
3. ✅ Install dependencies
4. ✅ Download dataset
5. ✅ Run training
6. ✅ Verify results
7. 📸 Take screenshots

