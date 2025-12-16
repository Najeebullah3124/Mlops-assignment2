#!/bin/bash
# Script to connect to EC2 instance
# Usage: ./ec2_connect.sh

EC2_IP="13.60.67.119"
KEY_FILE="Mlops.pem"
USER="ubuntu"

echo "Connecting to EC2 instance..."
echo "IP: $EC2_IP"
echo "Key: $KEY_FILE"
echo ""

# Check if key file exists
if [ ! -f "$KEY_FILE" ]; then
    echo "❌ Error: Key file $KEY_FILE not found!"
    echo "Please ensure Mlops.pem is in the current directory"
    exit 1
fi

# Set correct permissions for key file
chmod 400 "$KEY_FILE"

# Connect to EC2
ssh -i "$KEY_FILE" "$USER@$EC2_IP"

