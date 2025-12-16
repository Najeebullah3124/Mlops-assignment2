# Start Docker Desktop and Complete Setup

## Step 1: Start Docker Desktop

1. **Open Docker Desktop** application
   - Find it in Applications or Spotlight
   - Or run: `open -a Docker`

2. **Wait for Docker to Start**
   - Look for Docker whale icon in menu bar
   - Wait until it shows "Docker Desktop is running"
   - This may take 1-2 minutes

3. **Verify Docker is Running**
   ```bash
   docker ps
   ```
   Should return empty list (not an error)

## Step 2: Build Docker Image

Once Docker Desktop is running, execute:

```bash
cd /Users/harris/Downloads/F22311_Lab15/Mlops-Project
docker build -t mlops-app .
```

**Expected Output:**
- Multiple build steps
- "Successfully built" message
- "Successfully tagged mlops-app:latest"

## Step 3: Run Docker Container

```bash
docker run --rm mlops-app
```

**Expected Output:**
```
Loading dataset...
Training set size: 800
Test set size: 200
Training model...
Model performance:
  MSE: 0.0097
  R²: 0.9985
Model saved to models/model.pkl
```

## Step 4: Initialize Airflow

```bash
cd /Users/harris/Downloads/F22311_Lab15/Mlops-Project
docker compose up airflow-init
```

**Expected Output:**
- Database initialization
- User creation
- "Airflow is ready!" message

## Step 5: Start Airflow Services

```bash
docker compose up -d
```

**Expected Output:**
- Services starting (postgres, airflow-webserver, airflow-scheduler)
- All services should show "Up"

## Step 6: Verify Airflow

```bash
# Check services
docker compose ps

# Access UI
open http://localhost:8080
```

**Login:**
- Username: `airflow`
- Password: `airflow`

## Step 7: Trigger DAG

1. In Airflow UI, find `train_pipeline` DAG
2. Toggle it ON (switch on left)
3. Click on DAG name
4. Click "Trigger DAG" button
5. Watch execution in Graph View

## Quick Commands Script

Save this as `complete_setup.sh` and run:

```bash
#!/bin/bash
# Complete Docker and Airflow Setup

echo "Step 1: Building Docker image..."
docker build -t mlops-app .

echo ""
echo "Step 2: Testing Docker container..."
docker run --rm mlops-app

echo ""
echo "Step 3: Initializing Airflow..."
docker compose up airflow-init

echo ""
echo "Step 4: Starting Airflow..."
docker compose up -d

echo ""
echo "Step 5: Waiting for services..."
sleep 15

echo ""
echo "Step 6: Checking status..."
docker compose ps

echo ""
echo "✅ Setup Complete!"
echo "Access Airflow: http://localhost:8080"
echo "Username: airflow"
echo "Password: airflow"
```

## Troubleshooting

### Docker Desktop Not Starting
- Check system requirements
- Restart Docker Desktop
- Check Docker Desktop preferences

### Port 8080 Already in Use
```bash
# Change port in docker-compose.yaml
# Or stop conflicting service
lsof -ti:8080 | xargs kill
```

### Airflow Services Not Starting
```bash
# Check logs
docker compose logs

# Restart services
docker compose restart
```

## Screenshots to Capture

### Docker:
1. Docker build output
2. Docker run output
3. `docker images` showing mlops-app

### Airflow:
1. `docker compose ps` showing all services
2. Airflow UI login page
3. DAG list showing train_pipeline
4. DAG graph view
5. Successful job run

## Current Status

✅ **DVC**: 100% Complete
⚠️ **Docker**: Ready (start Docker Desktop)
⚠️ **Airflow**: Ready (start Docker Desktop)

Once Docker Desktop is running, all commands will work!

