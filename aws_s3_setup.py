#!/usr/bin/env python3
"""
Script to download dataset from S3 and verify access.
Use this on EC2 instance to test S3 connectivity.
"""

import boto3
import pandas as pd
import os
from botocore.exceptions import ClientError

# S3 Configuration
BUCKET_NAME = 'mlops-test-ass'
OBJECT_KEY = 'dataset.csv'
LOCAL_PATH = 'data/dataset.csv'

def download_from_s3():
    """Download dataset from S3 bucket."""
    try:
        # Create S3 client
        s3_client = boto3.client('s3', region_name='eu-north-1')
        
        # Create local directory if it doesn't exist
        os.makedirs(os.path.dirname(LOCAL_PATH), exist_ok=True)
        
        # Download file
        print(f"Downloading {OBJECT_KEY} from s3://{BUCKET_NAME}...")
        s3_client.download_file(BUCKET_NAME, OBJECT_KEY, LOCAL_PATH)
        
        print(f"✅ Successfully downloaded to {LOCAL_PATH}")
        
        # Verify file
        df = pd.read_csv(LOCAL_PATH)
        print(f"✅ Dataset verified: {df.shape[0]} rows, {df.shape[1]} columns")
        
        return True
        
    except ClientError as e:
        print(f"❌ Error downloading from S3: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def verify_s3_access():
    """Verify S3 bucket access."""
    try:
        s3_client = boto3.client('s3', region_name='eu-north-1')
        
        # Check if bucket exists and is accessible
        print(f"Checking access to bucket: {BUCKET_NAME}...")
        s3_client.head_bucket(Bucket=BUCKET_NAME)
        print(f"✅ Bucket is accessible")
        
        # Check if object exists
        print(f"Checking for object: {OBJECT_KEY}...")
        s3_client.head_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY)
        print(f"✅ Object exists in bucket")
        
        # Get object metadata
        response = s3_client.head_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY)
        size = response['ContentLength']
        print(f"✅ Object size: {size / 1024:.2f} KB")
        
        return True
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':
            print(f"❌ Bucket or object not found")
        elif error_code == '403':
            print(f"❌ Access denied. Check IAM permissions or bucket policy")
        else:
            print(f"❌ Error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == '__main__':
    print("=" * 50)
    print("S3 Access Verification")
    print("=" * 50)
    print()
    
    # Verify access first
    if verify_s3_access():
        print()
        # Download if access is verified
        download_from_s3()
    else:
        print("\n⚠️  Cannot download. Please check:")
        print("   1. AWS credentials are configured")
        print("   2. IAM role/permissions allow S3 access")
        print("   3. Bucket policy allows access")
        print("   4. Region is correct (eu-north-1)")

