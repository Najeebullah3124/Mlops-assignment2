# Task 6.2 - EC2 Instance Setup Guide

## ✅ Your EC2 Instance Details

- **Public IPv4**: `13.60.67.119`
- **AMI**: Ubuntu 22.04 LTS
- **Key File**: `Mlops.pem`
- **User**: `ubuntu`
- **Port to Open**: 8000 (for API)

## Step 1: Configure Security Group

### Open Port 8000 in AWS Console:

1. Go to **EC2 Console** → **Instances**
2. Select your instance
3. Click **Security** tab → **Security groups**
4. Click on the security group
5. Click **Edit inbound rules**
6. Click **Add rule**:
   - **Type**: Custom TCP
   - **Port**: 8000
   - **Source**: 0.0.0.0/0 (or your IP for security)
   - **Description**: MLOps API
7. Click **Save rules**

### Also ensure SSH (port 22) is open:
- **Type**: SSH
- **Port**: 22
- **Source**: Your IP or 0.0.0.0/0

## Step 2: Connect to EC2 Instance

### Option 1: Using the provided script
```bash
# Make script executable
chmod +x ec2_connect.sh

# Connect
./ec2_connect.sh
```

### Option 2: Manual SSH connection
```bash
# Set correct permissions for key file
chmod 400 Mlops.pem

# Connect to EC2
ssh -i Mlops.pem ubuntu@13.60.67.119
```

## Step 3: Install Dependencies

### Run on EC2 instance:

```bash
# Update system
sudo apt update

# Install Docker
sudo apt install -y docker.io docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Install Python and pip
sudo apt install -y python3 python3-pip

# Install AWS CLI
sudo apt install -y awscli

# Install Git
sudo apt install -y git
```

### Or use the setup script:

```bash
# Upload ec2_setup.sh to EC2, then:
chmod +x ec2_setup.sh
./ec2_setup.sh
```

## Step 4: Verify Installations

```bash
# Check Docker
docker --version
sudo docker ps

# Check Python
python3 --version
pip3 --version

# Check AWS CLI
aws --version
```

## Step 5: Set Up Project on EC2

### Option 1: Clone from Git (if you have a repo)
```bash
git clone <your-repo-url>
cd Mlops-Project
```

### Option 2: Upload files using SCP
```bash
# From your local machine:
scp -i Mlops.pem -r /path/to/Mlops-Project ubuntu@13.60.67.119:~/
```

### Option 3: Manual setup
```bash
# Create project structure
mkdir -p ~/mlops-project/{src,data,models,tests}
cd ~/mlops-project

# Upload files individually or create them
```

## Step 6: Configure AWS Credentials

### Option 1: IAM Role (Recommended)
1. Create IAM role with S3 read permissions
2. Attach role to EC2 instance
3. No credentials needed!

### Option 2: AWS CLI Configure
```bash
aws configure
# Enter your Access Key ID
# Enter your Secret Access Key
# Region: eu-north-1
# Output format: json
```

## Step 7: Download Dataset from S3

```bash
# Create data directory
mkdir -p data

# Download dataset
aws s3 cp s3://mlops-test-ass/dataset.csv ./data/dataset.csv

# Verify download
ls -lh data/dataset.csv
head -5 data/dataset.csv
```

## Step 8: Install Python Dependencies

```bash
# Install from requirements.txt
pip3 install -r requirements.txt

# Or install individually
pip3 install pandas scikit-learn numpy boto3
```

## Step 9: Run Training Script

```bash
# Run training
python3 src/train.py

# Verify model was created
ls -lh models/model.pkl
```

## Step 10: Test API (if you have one)

```bash
# If you have an API server
python3 -m http.server 8000

# Or using Flask/FastAPI
# python3 api.py
```

## Quick Setup Commands (All in One)

```bash
# Run these commands on EC2 instance:

# 1. Update and install
sudo apt update
sudo apt install -y docker.io python3-pip awscli git

# 2. Start Docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# 3. Create project structure
mkdir -p ~/mlops-project/{src,data,models}
cd ~/mlops-project

# 4. Download dataset
aws s3 cp s3://mlops-test-ass/dataset.csv ./data/dataset.csv

# 5. Install Python packages
pip3 install pandas scikit-learn numpy boto3

# 6. Verify
python3 --version
docker --version
aws --version
```

## Troubleshooting

### Cannot connect via SSH
- Check security group allows SSH (port 22)
- Verify key file permissions: `chmod 400 Mlops.pem`
- Check instance is running

### Docker permission denied
- Add user to docker group: `sudo usermod -aG docker $USER`
- Log out and log back in
- Or use `sudo docker` commands

### AWS CLI access denied
- Configure credentials: `aws configure`
- Or attach IAM role to instance
- Check IAM permissions for S3 access

### Port 8000 not accessible
- Check security group inbound rules
- Verify application is listening on 0.0.0.0:8000 (not 127.0.0.1)
- Check firewall: `sudo ufw status`

## Screenshots Needed

1. **EC2 Instance Dashboard**
   - Show instance in EC2 console
   - Instance ID, status, public IP visible
   - Security groups shown

2. **SSH Connection**
   - Terminal showing successful SSH connection
   - Or EC2 Instance Connect screenshot

3. **Dependencies Installed**
   - Show `docker --version`
   - Show `python3 --version`
   - Show `pip3 --version`

4. **Dataset Downloaded**
   - Show `ls -lh data/dataset.csv`
   - Or show file in S3 and local

5. **Training Completed**
   - Show training script output
   - Show model file created

## Security Best Practices

1. **Limit SSH Access**: Only allow your IP in security group
2. **Use IAM Roles**: Instead of access keys when possible
3. **Close Unused Ports**: Only open ports you need
4. **Regular Updates**: `sudo apt update && sudo apt upgrade`
5. **Firewall**: Consider using `ufw` for additional security

## Cost Optimization (Free Tier)

- Use t2.micro or t3.micro instance
- Stop instance when not in use
- Use same region as S3 (eu-north-1)
- Monitor usage in AWS Cost Explorer

## Next Steps

After setup:
1. ✅ EC2 instance running
2. ✅ Dependencies installed
3. ✅ Dataset downloaded
4. ✅ Training script ready
5. 📸 Take screenshots
6. 🚀 Run training pipeline

