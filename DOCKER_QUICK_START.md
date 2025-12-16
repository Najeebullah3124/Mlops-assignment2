# Docker Quick Start Guide

## Quick Commands

### Build Image
```bash
docker build -t mlops-app .
```

### Run Container
```bash
docker run mlops-app
```

### Push to Docker Hub
```bash
# 1. Login first
docker login

# 2. Tag image (replace 'yourusername' with your Docker Hub username)
docker tag mlops-app yourusername/mlops-app:v1

# 3. Push
docker push yourusername/mlops-app:v1
```

## Complete Workflow

```bash
# Step 1: Build
docker build -t mlops-app .

# Step 2: Test locally
docker run mlops-app

# Step 3: Login to Docker Hub
docker login

# Step 4: Tag
docker tag mlops-app yourusername/mlops-app:v1

# Step 5: Push
docker push yourusername/mlops-app:v1
```

## What Gets Built

The Dockerfile:
1. Uses Python 3.10-slim base image
2. Installs system dependencies (gcc)
3. Installs Python packages from requirements.txt
4. Copies all project files
5. Creates data/ and models/ directories
6. Generates the dataset
7. Runs the training script

## Screenshot Checklist

- [ ] Dockerfile content
- [ ] `docker build` output (build logs)
- [ ] `docker run` output (running container)
- [ ] `docker push` output (push logs)
- [ ] Docker Hub repository page

