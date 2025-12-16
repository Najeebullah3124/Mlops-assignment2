# Task 6.3 - API Deployment on EC2

## ✅ API Deployment Complete!

### What Was Deployed:

1. **Flask API** (`api/app.py`)
   - Home endpoint: `/`
   - Health check: `/health`
   - Single prediction: `/predict` (POST)
   - Batch prediction: `/predict/batch` (POST)

2. **Docker Image**
   - Built on EC2: `mlops-api:v1`
   - Running on port 8000

3. **Container Status**
   - Container name: `mlops-api`
   - Port mapping: `8000:8000`
   - Status: Running

## API Endpoints

### Base URL
```
http://13.60.67.119:8000
```

### Available Endpoints:

1. **GET /** - API information
   ```bash
   curl http://13.60.67.119:8000/
   ```

2. **GET /health** - Health check
   ```bash
   curl http://13.60.67.119:8000/health
   ```

3. **POST /predict** - Single prediction
   ```bash
   curl -X POST http://13.60.67.119:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [0.5, -0.1, 0.6, 1.5, -0.2]}'
   ```

4. **POST /predict/batch** - Batch predictions
   ```bash
   curl -X POST http://13.60.67.119:8000/predict/batch \
     -H "Content-Type: application/json" \
     -d '{"features": [[0.5, -0.1, 0.6, 1.5, -0.2], [0.3, 0.2, -0.4, 0.8, 0.1]]}'
   ```

## Screenshots Needed

### 1. Docker Logs Screenshot
```bash
# On EC2 or via SSH:
docker logs mlops-api
```

**What to capture:**
- Container startup logs
- Model loading confirmation
- Flask server starting message

### 2. Running Container Screenshot
```bash
# On EC2 or via SSH:
docker ps | grep mlops-api
# Or
docker ps -a
```

**What to capture:**
- Container ID
- Image name: `mlops-api:v1`
- Status: Up
- Ports: `0.0.0.0:8000->8000/tcp`

### 3. Public Endpoint Test Screenshot

**Option A: Browser**
- Open: `http://13.60.67.119:8000/`
- Or: `http://13.60.67.119:8000/health`

**Option B: Postman**
- Method: GET
- URL: `http://13.60.67.119:8000/health`
- Or POST to `/predict` with JSON body

**Option C: curl (Terminal)**
```bash
curl http://13.60.67.119:8000/health
curl http://13.60.67.119:8000/
curl -X POST http://13.60.67.119:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [0.5, -0.1, 0.6, 1.5, -0.2]}'
```

## Container Management Commands

### View Logs
```bash
docker logs mlops-api
docker logs -f mlops-api  # Follow logs
```

### Check Status
```bash
docker ps | grep mlops-api
docker inspect mlops-api
```

### Stop Container
```bash
docker stop mlops-api
```

### Start Container
```bash
docker start mlops-api
```

### Restart Container
```bash
docker restart mlops-api
```

### Remove Container
```bash
docker stop mlops-api
docker rm mlops-api
```

## Testing the API

### Test 1: Health Check
```bash
curl http://13.60.67.119:8000/health
```
**Expected Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### Test 2: API Info
```bash
curl http://13.60.67.119:8000/
```
**Expected Response:**
```json
{
  "message": "MLOps API - Model Inference Service",
  "version": "1.0",
  "endpoints": {...}
}
```

### Test 3: Prediction
```bash
curl -X POST http://13.60.67.119:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [0.5, -0.1, 0.6, 1.5, -0.2]}'
```
**Expected Response:**
```json
{
  "prediction": 0.4198,
  "features": [0.5, -0.1, 0.6, 1.5, -0.2],
  "model_type": "LinearRegression"
}
```

## Troubleshooting

### Container Not Starting
```bash
# Check logs
docker logs mlops-api

# Check if port is in use
sudo netstat -tulpn | grep 8000
```

### Cannot Access from Browser
- Verify security group allows port 8000
- Check container is running: `docker ps`
- Test locally on EC2: `curl http://localhost:8000/health`

### Model Not Loading
- Verify model file exists in container
- Check Dockerfile copies models directory
- View container logs for errors

## Next Steps (Optional)

### Push to Docker Hub
```bash
# Tag image
docker tag mlops-api:v1 yourusername/mlops-api:v1

# Push to Docker Hub
docker push yourusername/mlops-api:v1
```

### Use Docker Hub Image
```bash
# Pull from Docker Hub
docker pull yourusername/mlops-api:v1

# Run
docker run -d -p 8000:8000 yourusername/mlops-api:v1
```

## ✅ Deployment Summary

- **API**: Flask application deployed
- **Container**: Running on port 8000
- **Status**: Operational
- **Public URL**: http://13.60.67.119:8000

**Ready for screenshots!** 📸

