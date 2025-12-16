#!/bin/bash
# Script to upload project files to EC2 instance
# Usage: ./upload_to_ec2.sh

EC2_IP="13.60.67.119"
KEY_FILE="Mlops.pem"
USER="ubuntu"
REMOTE_DIR="~/mlops-project"

echo "Uploading project files to EC2..."
echo "IP: $EC2_IP"
echo ""

# Check if key file exists
if [ ! -f "$KEY_FILE" ]; then
    echo "❌ Error: Key file $KEY_FILE not found!"
    exit 1
fi

# Set correct permissions
chmod 400 "$KEY_FILE"

# Create remote directory
echo "Creating remote directory..."
ssh -i "$KEY_FILE" "$USER@$EC2_IP" "mkdir -p $REMOTE_DIR"

# Upload key files
echo "Uploading files..."
scp -i "$KEY_FILE" -r \
    src/ \
    tests/ \
    requirements.txt \
    create_dataset.py \
    aws_s3_setup.py \
    "$USER@$EC2_IP:$REMOTE_DIR/"

echo ""
echo "✅ Upload complete!"
echo ""
echo "Next steps on EC2:"
echo "1. cd ~/mlops-project"
echo "2. pip3 install -r requirements.txt"
echo "3. aws s3 cp s3://mlops-test-ass/dataset.csv ./data/dataset.csv"
echo "4. python3 src/train.py"

