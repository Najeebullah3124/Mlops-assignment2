# Task 6 - AWS S3 Bucket Setup

## ✅ Your Current S3 Setup

Based on the information provided, you have:

### S3 Bucket Details:
- **Bucket Name**: `mlops-test-ass`
- **Region**: Europe (Stockholm) - `eu-north-1`
- **Object**: `dataset.csv`
- **Size**: 114.7 KB
- **S3 URI**: `s3://mlops-test-ass/dataset.csv`
- **Object URL**: `https://mlops-test-ass.s3.eu-north-1.amazonaws.com/dataset.csv`
- **Last Modified**: December 16, 2025, 11:42:37 (UTC+05:00)

## ✅ Task 6.1 Requirements Checklist

### 1. Create Bucket ✅
- **Status**: ✅ Complete
- **Bucket Name**: `mlops-test-ass`
- **Region**: `eu-north-1` (Europe - Stockholm)

### 2. Upload Dataset ✅
- **Status**: ✅ Complete
- **File**: `dataset.csv`
- **Size**: 114.7 KB
- **Location**: Uploaded to S3 bucket

### 3. Configure Permissions ⚠️
- **Status**: ⚠️ Needs Verification
- **Action Required**: Verify bucket permissions are set correctly

### 4. Generate Bucket URL ✅
- **Status**: ✅ Complete
- **Object URL**: `https://mlops-test-ass.s3.eu-north-1.amazonaws.com/dataset.csv`

## 📋 Permissions Configuration Guide

### Recommended Permissions for MLOps Project:

#### Option 1: Public Read (for testing)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::mlops-test-ass/*"
    }
  ]
}
```

#### Option 2: EC2 Instance Access (recommended for production)
- Use IAM roles to allow EC2 instances to access S3
- No public access needed
- More secure

### Steps to Configure Permissions:

1. **Go to S3 Console** → Your bucket `mlops-test-ass`
2. **Click "Permissions" tab**
3. **Block Public Access**: 
   - For testing: Turn OFF (allow public read)
   - For production: Keep ON, use IAM roles
4. **Bucket Policy**: Add policy if needed
5. **Access Control List (ACL)**: Set if required

## 📸 Screenshots Needed

### Screenshot 1: S3 Bucket Overview
- Show the S3 bucket list
- Highlight your bucket `mlops-test-ass`
- Show bucket details (region, creation date)

### Screenshot 2: Uploaded Dataset
- Show the bucket contents
- Highlight `dataset.csv`
- Show file details (size, last modified, type)

### Screenshot 3: Permissions Configuration (Optional)
- Show Permissions tab
- Show bucket policy or ACL settings
- Verify public access settings

## ✅ Verification Checklist

- [x] Bucket created successfully
- [x] Dataset uploaded (114.7 KB)
- [x] Object URL generated
- [ ] Permissions configured (verify)
- [ ] Screenshots captured

## 🔍 Quick Verification

Test if the dataset is accessible:

```bash
# Test URL access (if public)
curl https://mlops-test-ass.s3.eu-north-1.amazonaws.com/dataset.csv | head -5

# Or download using AWS CLI
aws s3 cp s3://mlops-test-ass/dataset.csv ./data/dataset_s3.csv
```

## 📝 Summary

**Your setup is 95% complete!** 

✅ **What's Done:**
- Bucket created
- Dataset uploaded
- URL generated

⚠️ **What to Verify:**
- Permissions configuration
- Access from EC2 (for Task 6.2)

## Next Steps for Task 6.2 (EC2 Deployment)

1. **Create EC2 Instance**
2. **Configure IAM Role** (for S3 access)
3. **Install dependencies** on EC2
4. **Download dataset** from S3
5. **Run training script** on EC2
6. **Upload results** back to S3 (optional)

Your S3 setup looks good! Just verify the permissions and you're ready for EC2 deployment.

