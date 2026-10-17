# MLOps Assignment - Commands Execution Summary

## ✅ Executed Commands and Results

### Task 1: Project Setup + Version Control (Git + DVC)

#### Git Status
```bash
git status
```
**Result:** Repository is initialized and on `main` branch

#### DVC Status
```bash
dvc status
```
**Result:** 
```
Data and pipelines are up to date.
```

#### DVC Remote Configuration
```bash
dvc remote list
```
**Result:**
```
myremote        /Users/harris/Downloads/F22311_Lab15/Mlops-Project/dvcstore     (default)
```

#### DVC Pipeline
```bash
dvc dag
```
**Result:**
```
+----------------------+ 
| data/dataset.csv.dvc | 
+----------------------+ 
            *            
            *            
            *            
    +-------------+      
    | train_model |      
    +-------------+      
```

#### DVC Pipeline Configuration (dvc.yaml)
```yaml
stages:
  train_model:
    cmd: python3 src/train.py
    deps:
    - data/dataset.csv
    - src/train.py
    outs:
    - models/model.pkl
```

#### Dataset DVC File (data/dataset.csv.dvc)
```yaml
outs:
- md5: a01a018c30d5786b1ea4f7e1a2de3eab
  size: 117422
  hash: md5
  path: dataset.csv
```

---

### Task 2: CI/CD Pipeline (GitHub Actions)

#### Unit Tests
```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```
**Result:** ✅ All 16 tests passed
```
test_load_data_exists ... ok
test_load_data_has_target ... ok
test_load_data_not_empty ... ok
test_load_data_shape ... ok
test_prepare_data_X_shape ... ok
test_prepare_data_returns_two_objects ... ok
test_prepare_data_y_shape ... ok
test_evaluate_model_mse_is_positive ... ok
test_evaluate_model_predictions_shape ... ok
test_evaluate_model_r2_is_valid ... ok
test_evaluate_model_returns_metrics ... ok
test_train_model_can_predict ... ok
test_train_model_has_coefficients ... ok
test_train_model_returns_model ... ok
test_data_shapes_consistent ... ok
test_model_input_output_shapes ... ok

----------------------------------------------------------------------
Ran 16 tests in 0.032s

OK
```

#### Training Script Verification
```bash
python3 src/train.py
```
**Result:** ✅ Training completed successfully
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

#### Model File Verification
```bash
ls -lh models/model.pkl
```
**Result:**
```
-rw-r--r--@ 1 harris  staff   646B Dec 16 15:20 models/model.pkl
```

#### GitHub Actions Workflow
**File:** `.github/workflows/ci.yml`
**Status:** ✅ Configured with:
- Python setup
- Dependency installation
- Unit tests
- Linting (flake8 & pylint)
- Training script verification

---

### Task 3: Docker

#### Docker Version
```bash
docker --version
```
**Result:** Docker version 28.5.2, build ecc6942

#### Commands to Execute (when ready):
```bash
# Build training image
docker build -t mlops-app .

# Run training container
docker run mlops-app

# Tag for Docker Hub (replace YOUR_USERNAME)
docker tag mlops-app YOUR_USERNAME/mlops-app:v1

# Push to Docker Hub (requires login)
docker login
docker push YOUR_USERNAME/mlops-app:v1
```

---

### Task 4: Airflow Pipeline

#### Airflow DAG
**File:** `airflow/dags/train_pipeline.py`
**Status:** ✅ Complete with 4 tasks:
1. `load_data` - Loads dataset
2. `train_model` - Trains model
3. `save_model` - Saves model
4. `log_results` - Logs results

#### Docker Compose Configuration
**File:** `docker-compose.yaml`
**Status:** ✅ Configured with:
- PostgreSQL database
- Airflow webserver (port 8080)
- Airflow scheduler
- Volume mounts for DAGs, logs, data, models

#### Commands to Execute:
```bash
# Start Airflow
docker-compose up -d

# Access Airflow UI
# URL: http://localhost:8080
# Credentials: airflow / airflow

# View logs
docker-compose logs -f

# Stop Airflow
docker-compose down
```

---

### Task 5: RESTful API

#### API Import Test
```bash
python3 -c "import sys; sys.path.insert(0, 'api'); from app import app; print('API imports successfully')"
```
**Result:** ✅ API imports successfully
**Available routes:**
- `/` - API information
- `/health` - Health check
- `/predict` - Single prediction (POST)
- `/predict/batch` - Batch prediction (POST)

#### API File
**File:** `api/app.py`
**Status:** ✅ Flask application with all required endpoints

#### Commands to Execute:
```bash
# Run API locally
cd api && python3 app.py
# Or: python3 api/app.py

# Test health endpoint
curl http://localhost:8000/health

# Test predict endpoint
curl -X POST http://localhost:8000/predict \
  -H 'Content-Type: application/json' \
  -d '{"features": [1, 2, 3, 4, 5]}'

# Build API Docker image
docker build -f api/Dockerfile -t mlops-api .

# Run API in Docker
docker run -p 8000:8000 mlops-api
```

---

### Task 6: AWS EC2 + S3 Deployment

#### AWS S3 Setup Script
**File:** `aws_s3_setup.py`
**Status:** ✅ Available

#### Commands for EC2 Instance:
```bash
# Update system
sudo apt update

# Install Docker and Python
sudo apt install docker.io python3-pip -y

# Pull Docker image
docker pull YOUR_USERNAME/mlops-api:v1

# Run API container
docker run -d -p 8000:8000 YOUR_USERNAME/mlops-api:v1

# Test API
curl http://EC2_PUBLIC_IP:8000/health
```

#### Security Group Configuration:
- Open port 8000 for API access
- Open port 22 for SSH access

---

## 📋 Summary

### ✅ Completed
- [x] Git repository initialized
- [x] DVC initialized and configured
- [x] Dataset tracked with DVC
- [x] DVC pipeline created
- [x] All unit tests passing (16/16)
- [x] Training script verified
- [x] Model file generated
- [x] GitHub Actions workflow configured
- [x] Airflow DAG created
- [x] API code complete with all endpoints
- [x] Dockerfiles created

### ⚠️ Requires Manual Execution
- [ ] Docker build and run (Docker available, commands ready)
- [ ] Docker Hub push (requires Docker Hub account)
- [ ] Airflow startup (docker-compose up)
- [ ] API runtime testing (start server and test endpoints)
- [ ] AWS EC2 deployment (manual setup required)
- [ ] AWS S3 bucket creation (manual setup required)

### 📝 Next Steps
1. Run Docker commands when ready
2. Start Airflow: `docker-compose up -d`
3. Test API: `python3 api/app.py` (in separate terminal)
4. Deploy to AWS EC2 manually
5. Capture screenshots for report
6. Create PDF/Word report with screenshots and logs

---

## 🚀 Quick Start Commands

### Run All Tests
```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

### Train Model
```bash
python3 src/train.py
```

### Start API
```bash
python3 api/app.py
```

### Start Airflow
```bash
docker-compose up -d
```

### Build Docker Images
```bash
# Training
docker build -t mlops-app .

# API
docker build -f api/Dockerfile -t mlops-api .
```

---

**Generated:** December 16, 2025
**Project:** MLOps Assignment
**Status:** All code complete, ready for execution and documentation

