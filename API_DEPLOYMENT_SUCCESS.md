# ✅ API Deployment Successfully Completed!

## Deployment Status

- **Container**: `mlops-api` ✅ Running
- **Image**: `mlops-api:v1` ✅ Built
- **Port**: 8000 ✅ Mapped
- **Public URL**: http://13.60.67.119:8000 ✅ Accessible

## Container Information

**Container ID**: `b58236aa5563`  
**Status**: Up and running  
**Port Mapping**: `0.0.0.0:8000->8000/tcp`  
**Image**: `mlops-api:v1`

## API Endpoints

### Base URL
```
http://13.60.67.119:8000
```

### 1. Health Check
```bash
GET http://13.60.67.119:8000/health
```
**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### 2. API Information
```bash
GET http://13.60.67.119:8000/
```

### 3. Single Prediction
```bash
POST http://13.60.67.119:8000/predict
Content-Type: application/json

{
  "features": [0.5, -0.1, 0.6, 1.5, -0.2]
}
```

**Response:**
```json
{
  "prediction": 0.5461435276434738,
  "features": [0.5, -0.1, 0.6, 1.5, -0.2],
  "model_type": "LinearRegression"
}
```

### 4. Batch Prediction
```bash
POST http://13.60.67.119:8000/predict/batch
Content-Type: application/json

{
  "features": [[0.5, -0.1, 0.6, 1.5, -0.2], [0.3, 0.2, -0.4, 0.8, 0.1]]
}
```

## Screenshots Required

### 1. Docker Logs Screenshot

**Command to run:**
```bash
docker logs mlops-api
```

**What to capture:**
- Model loading: "Model loaded from models/model.pkl"
- Flask server starting: "Running on all addresses (0.0.0.0)"
- Server running on port 8000
- Recent request logs

**Expected output:**
```
Model loaded from models/model.pkl
 * Serving Flask app 'app'
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://172.17.0.2:8000
```

### 2. Running Container Screenshot

**Command to run:**
```bash
docker ps | grep mlops-api
# Or
docker ps -a
```

**What to capture:**
- Container ID: `b58236aa5563`
- Image: `mlops-api:v1`
- Status: `Up`
- Ports: `0.0.0.0:8000->8000/tcp`
- Container name: `mlops-api`

**Expected output:**
```
CONTAINER ID   IMAGE           COMMAND         STATUS         PORTS
b58236aa5563   mlops-api:v1   "python app.py" Up X minutes   0.0.0.0:8000->8000/tcp
```

### 3. Public Endpoint Test Screenshot

**Option A: Browser**
1. Open browser
2. Navigate to: `http://13.60.67.119:8000/health`
3. Or: `http://13.60.67.119:8000/`
4. Screenshot the JSON response

**Option B: Postman**
1. Method: GET
2. URL: `http://13.60.67.119:8000/health`
3. Or POST to `/predict` with JSON body
4. Screenshot the response

**Option C: Terminal/curl**
```bash
# Health check
curl http://13.60.67.119:8000/health

# API info
curl http://13.60.67.119:8000/

# Prediction
curl -X POST http://13.60.67.119:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [0.5, -0.1, 0.6, 1.5, -0.2]}'
```

## Quick Test Commands

### From Local Machine
```bash
# Health check
curl http://13.60.67.119:8000/health

# API info
curl http://13.60.67.119:8000/

# Prediction
curl -X POST http://13.60.67.119:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [0.5, -0.1, 0.6, 1.5, -0.2]}'
```

### From EC2 (via SSH)
```bash
# View logs
docker logs mlops-api

# Check status
docker ps | grep mlops-api

# Test locally
curl http://localhost:8000/health
```

## Container Management

### View Logs
```bash
docker logs mlops-api
docker logs -f mlops-api  # Follow logs in real-time
docker logs --tail 50 mlops-api  # Last 50 lines
```

### Check Status
```bash
docker ps | grep mlops-api
docker inspect mlops-api
```

### Stop/Start/Restart
```bash
docker stop mlops-api
docker start mlops-api
docker restart mlops-api
```

## Verification Checklist

- [x] Docker image built successfully
- [x] Container running
- [x] Port 8000 mapped correctly
- [x] Model loaded in container
- [x] API responding to requests
- [x] Health endpoint working
- [x] Prediction endpoint working
- [x] Public access working (security group configured)

## ✅ Deployment Complete!

Your API is now live and accessible at:
**http://13.60.67.119:8000**

Ready for screenshots! 📸

