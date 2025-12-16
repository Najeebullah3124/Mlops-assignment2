# EC2 Instance - Ready to Use! ✅

## ✅ Security Group Configuration Complete

- **Port 22 (SSH)**: ✅ Open - Can connect to instance
- **Port 8000 (API)**: ✅ Open - API will be accessible

## Your EC2 Details

- **Public IP**: 13.60.67.119
- **Key File**: Mlops.pem
- **User**: ubuntu
- **OS**: Ubuntu 22.04

## Quick Start - Connect Now!

### Step 1: Connect to EC2

```bash
cd /Users/harris/Downloads/F22311_Lab15/Mlops-Project
chmod 400 Mlops.pem
./ec2_connect.sh
```

Or manually:
```bash
ssh -i Mlops.pem ubuntu@13.60.67.119
```

### Step 2: Install Dependencies (On EC2)

Once connected, run:

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

### Step 3: Set Up Project (On EC2)

```bash
# Create project structure
mkdir -p ~/mlops-project/{src,data,models}
cd ~/mlops-project

# Download dataset from S3
aws s3 cp s3://mlops-test-ass/dataset.csv ./data/dataset.csv

# Install Python dependencies
pip3 install pandas scikit-learn numpy boto3
```

### Step 4: Upload Project Files (From Local Machine)

In a new terminal (keep SSH session open):

```bash
cd /Users/harris/Downloads/F22311_Lab15/Mlops-Project
./upload_to_ec2.sh
```

### Step 5: Run Training (On EC2)

Back in your SSH session:

```bash
cd ~/mlops-project
python3 src/train.py
```

### Step 6: Verify Everything Works

```bash
# Check Docker
docker --version

# Check Python
python3 --version

# Check AWS CLI
aws --version

# Check dataset
ls -lh data/dataset.csv

# Check model
ls -lh models/model.pkl
```

## All-in-One Setup Script

You can also upload and run the setup script:

```bash
# From local machine, upload setup script
scp -i Mlops.pem ec2_setup.sh ubuntu@13.60.67.119:~/

# On EC2, run it
chmod +x ec2_setup.sh
./ec2_setup.sh
```

## Testing API on Port 8000

If you want to test port 8000:

```bash
# Simple HTTP server test
cd ~/mlops-project
python3 -m http.server 8000
```

Then test from your browser:
```
http://13.60.67.119:8000
```

## Screenshots Checklist

- [x] Security Group configured (ports 22 & 8000)
- [ ] EC2 Instance Dashboard screenshot
- [ ] SSH connection successful
- [ ] Dependencies installed
- [ ] Dataset downloaded from S3
- [ ] Training script executed
- [ ] Model file created

## Troubleshooting

### Cannot Connect via SSH
- Verify key file permissions: `chmod 400 Mlops.pem`
- Check security group has SSH (port 22) open
- Verify instance is running

### Docker Permission Denied
- Add user to docker group: `sudo usermod -aG docker $USER`
- Log out and log back in
- Or use `sudo docker` commands

### AWS CLI Access Denied
- Configure credentials: `aws configure`
- Or attach IAM role to EC2 instance
- Verify IAM permissions for S3

## Next Steps

1. ✅ Connect to EC2
2. ✅ Install dependencies
3. ✅ Download dataset
4. ✅ Run training
5. 📸 Take screenshots
6. ✅ Complete Task 6.2

**You're all set! Connect and start setting up your EC2 instance.** 🚀

