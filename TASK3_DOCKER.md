# Task 3 - Docker Setup Guide

## ✅ Completed Tasks

### 3.1 Dockerfile Created

**Location**: `Dockerfile`

**Features:**
- ✅ Based on Python 3.10-slim
- ✅ Installs all dependencies from requirements.txt
- ✅ Copies project files
- ✅ Creates necessary directories (data, models)
- ✅ Generates dataset automatically
- ✅ Runs training script by default

**Dockerfile Contents:**
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p data models
RUN python create_dataset.py
CMD ["python", "src/train.py"]
```

### 3.2 Additional Files Created

- `.dockerignore` - Excludes unnecessary files from Docker build context
- `docker-commands.sh` - Helper script for Docker operations
- `TASK3_DOCKER.md` - This documentation file

## Commands to Execute

### 3.1 Build and Run Container

```bash
# Build the Docker image
docker build -t mlops-app .

# Run the container
docker run mlops-app
```

**Expected Output:**
- Build logs showing layer creation
- Container runs training script
- Model is created in models/model.pkl

### 3.2 Push to Docker Hub

**Prerequisites:**
1. Create a Docker Hub account at https://hub.docker.com
2. Login to Docker Hub:
   ```bash
   docker login
   ```

**Commands:**
```bash
# Tag the image (replace 'yourusername' with your Docker Hub username)
docker tag mlops-app yourusername/mlops-app:v1

# Push to Docker Hub
docker push yourusername/mlops-app:v1
```

**Alternative: Tag as latest:**
```bash
docker tag mlops-app yourusername/mlops-app:latest
docker push yourusername/mlops-app:latest
```

## Screenshots Needed

### 3.1 Deliverables:
1. **Dockerfile screenshot** - Show the Dockerfile content
2. **Build logs** - Screenshot of `docker build -t mlops-app .` output
3. **Running container screenshot** - Screenshot of `docker run mlops-app` output

### 3.2 Deliverables:
1. **Docker Hub repository page** - Screenshot of your image on Docker Hub
2. **Push logs** - Screenshot of `docker push` command output

## Using the Helper Script

The `docker-commands.sh` script provides convenient commands:

```bash
# Build image
./docker-commands.sh build

# Run container
./docker-commands.sh run

# Tag image (set DOCKER_USERNAME environment variable first)
export DOCKER_USERNAME=yourusername
./docker-commands.sh tag

# Push image
./docker-commands.sh push
```

## Manual Step-by-Step

### Step 1: Build the Image
```bash
docker build -t mlops-app .
```

**What to screenshot:**
- The entire build process
- Final "Successfully tagged" message

### Step 2: Run the Container
```bash
docker run mlops-app
```

**What to screenshot:**
- Container output showing training process
- Model creation confirmation

### Step 3: Login to Docker Hub
```bash
docker login
```
Enter your Docker Hub username and password.

### Step 4: Tag the Image
```bash
# Replace 'yourusername' with your actual Docker Hub username
docker tag mlops-app yourusername/mlops-app:v1
```

### Step 5: Push to Docker Hub
```bash
docker push yourusername/mlops-app:v1
```

**What to screenshot:**
- Push progress logs
- Final "pushed" confirmation

### Step 6: Verify on Docker Hub
1. Go to https://hub.docker.com
2. Navigate to your repository
3. Screenshot the repository page showing your image

## Troubleshooting

### Build Issues
- **Error: requirements.txt not found**
  - Make sure you're in the project root directory
  - Check that requirements.txt exists

- **Error: Permission denied**
  - On Linux/Mac, you might need `sudo` (not recommended)
  - Better: Add your user to docker group

### Push Issues
- **Error: denied: requested access to the resource is denied**
  - Make sure you're logged in: `docker login`
  - Verify your username is correct in the tag command

- **Error: tag does not exist**
  - Make sure you tagged the image before pushing
  - Check image exists: `docker images`

## Verification Commands

```bash
# List all Docker images
docker images

# Check if container runs successfully
docker run --rm mlops-app

# Inspect image
docker inspect mlops-app

# View image history
docker history mlops-app
```

## Docker Image Details

- **Base Image**: python:3.10-slim
- **Working Directory**: /app
- **Default Command**: python src/train.py
- **Exposed Ports**: None (training script only)
- **Size**: ~500-800 MB (depending on dependencies)

## Next Steps

After pushing to Docker Hub, you can:
1. Pull the image on any machine: `docker pull yourusername/mlops-app:v1`
2. Run it: `docker run yourusername/mlops-app:v1`
3. Use it in Kubernetes, Docker Compose, or other orchestration tools

