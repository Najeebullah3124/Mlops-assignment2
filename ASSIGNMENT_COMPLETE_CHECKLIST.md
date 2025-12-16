# Assignment 02 - Complete Checklist

**Deadline: 14-12-2025**

## ✅ Task 1 - Project Setup + Version Control (Git + DVC)

### 1.1 Create Project Structure ✅
- [x] Git initialized
- [x] .gitignore created
- [x] Python environment (requirements.txt)
- [x] Project structure created
- [ ] **Screenshot**: Folder structure
- [ ] **Screenshot**: git init output

### 1.2 Initialize DVC ✅
**Commands Executed:**
```bash
✅ dvc init
✅ dvc remote add -d myremote ./dvcstore
✅ dvc add data/dataset.csv
✅ git add data/dataset.csv.dvc .dvc .dvcignore
✅ git commit -m "Add dataset with DVC"
```

**Files Created:**
- ✅ `.dvc/` directory
- ✅ `data/dataset.csv.dvc`
- ✅ `.dvcignore`

- [ ] **Screenshot**: DVC commands output
- [ ] **Screenshot**: `.dvc` file (data/dataset.csv.dvc)
- [ ] **Screenshot**: DVC status/output logs

### 1.3 Create Training Pipeline ✅
**Commands Executed:**
```bash
✅ dvc stage add -n train_model -d src/train.py -d data/dataset.csv -o models/model.pkl python3 src/train.py
✅ dvc repro train_model
```

**Files Created:**
- ✅ `dvc.yaml`
- ✅ `dvc.lock`

**Pipeline Executed:**
- ✅ Model trained successfully
- ✅ MSE: 0.0097, R²: 0.9985

- [ ] **Screenshot**: Successful DVC pipeline run
- [ ] **Screenshot**: dvc.yaml file

---

## ✅ Task 2 - CI/CD Pipeline (GitHub Actions)

### 2.1 Create Workflow File ✅
**File Created:**
- ✅ `.github/workflows/ci.yml`

**Workflow Includes:**
- ✅ Setup Python
- ✅ Install requirements
- ✅ Run unit tests
- ✅ Run linting (flake8, pylint)
- ✅ Verify training script runs

- [ ] **Screenshot**: Workflow file
- [ ] **Screenshot**: GitHub Actions successful run
- [ ] **Screenshot**: (Optional) Failing workflow

**Action Needed:**
- [ ] Push code to GitHub repository
- [ ] Screenshot workflow run

### 2.2 Add Tests ✅
**File Created:**
- ✅ `tests/test_train.py`

**Tests Include:**
- ✅ Data loading (4 tests)
- ✅ Model training (3 tests)
- ✅ Shape validation (2 tests)
- ✅ Model evaluation (4 tests)
- ✅ Data preparation (3 tests)

**Total: 16 tests, all passing**

- [ ] **Screenshot**: Test results

---

## ✅ Task 3 - Docker

### 3.1 Create Dockerfile ✅
**File Created:**
- ✅ `Dockerfile`

**Commands Executed:**
```bash
✅ docker build -t mlops-app .
✅ docker run mlops-app
```

**Results:**
- ✅ Image built successfully (1.12GB)
- ✅ Container runs successfully
- ✅ Training completes in container

- [ ] **Screenshot**: Dockerfile
- [ ] **Screenshot**: Build logs
- [ ] **Screenshot**: Running container

### 3.2 Push Docker Image to Docker Hub ⚠️
**Action Needed:**
```bash
# Replace 'yourusername' with your Docker Hub username
docker tag mlops-app yourusername/mlops-app:v1
docker login
docker push yourusername/mlops-app:v1
```

- [ ] **Screenshot**: Docker Hub repository page
- [ ] **Screenshot**: Push logs

---

## ✅ Task 4 - Airflow Pipeline

### 4.1 Install Airflow Locally ✅
**Files Created:**
- ✅ `docker-compose.yaml`
- ✅ `airflow/dags/train_pipeline.py`
- ✅ `.env` (AIRFLOW_UID=501)

**Commands Executed:**
```bash
✅ docker compose up airflow-init
✅ docker compose up -d
```

**Services Running:**
- ✅ PostgreSQL (healthy)
- ✅ Airflow Webserver (port 8080)
- ✅ Airflow Scheduler

**DAG Created:**
- ✅ `train_pipeline` with 4 tasks:
  1. load_data
  2. train_model
  3. save_model
  4. log_results

**Access:**
- URL: http://localhost:8080
- Username: airflow
- Password: airflow

- [ ] **Screenshot**: Airflow UI
- [ ] **Screenshot**: DAG graph
- [ ] **Screenshot**: Successful job run

**Action Needed:**
- [ ] Access Airflow UI
- [ ] Trigger DAG
- [ ] Capture screenshots

---

## ✅ Task 5 - RESTful API

### 5.1 Build ML Inference API ✅
**File Created:**
- ✅ `api/app.py` (Flask API)

**Endpoints:**
- ✅ `/` - API information
- ✅ `/health` - Health check
- ✅ `/predict` - Model prediction (POST)
- ✅ `/predict/batch` - Batch prediction (POST)

**API Deployed:**
- ✅ Running on EC2: http://13.60.67.119:8000

- [ ] **Screenshot**: API running
- [ ] **Screenshot**: Testing using Postman/cURL
- [ ] **Screenshot**: Sample prediction outputs

### 5.2 Containerize the API ✅
**Files Created:**
- ✅ `api/Dockerfile`
- ✅ `api/requirements.txt`

**Commands Executed:**
```bash
✅ docker build -t mlops-api:v1 (on EC2)
✅ docker run -d -p 8000:8000 mlops-api:v1 (on EC2)
```

**Status:**
- ✅ API containerized
- ✅ Running on EC2 port 8000

- [ ] **Screenshot**: API running in Docker

---

## ✅ Task 6 - AWS EC2 + S3 Deployment

### 6.1 Create AWS S3 Bucket ✅
**Bucket Details:**
- ✅ Name: `mlops-test-ass`
- ✅ Region: eu-north-1
- ✅ Dataset uploaded: `dataset.csv` (114.7 KB)
- ✅ URL: https://mlops-test-ass.s3.eu-north-1.amazonaws.com/dataset.csv

- [ ] **Screenshot**: S3 bucket
- [ ] **Screenshot**: Uploaded data

### 6.2 Launch EC2 Instance ✅
**Instance Details:**
- ✅ Public IP: 13.60.67.119
- ✅ OS: Ubuntu 22.04
- ✅ Port 8000: Open
- ✅ Port 22 (SSH): Open

**Dependencies Installed:**
- ✅ Docker
- ✅ Python3 & pip3
- ✅ AWS CLI

- [ ] **Screenshot**: EC2 instance dashboard
- [ ] **Screenshot**: Instance SSH terminal

### 6.3 Deploy API Using Docker on EC2 ✅
**Deployment:**
- ✅ API image built on EC2
- ✅ Container running: `mlops-api`
- ✅ Port 8000 mapped
- ✅ API accessible: http://13.60.67.119:8000

**Commands Executed:**
```bash
✅ docker build -t mlops-api:v1 (on EC2)
✅ docker run -d -p 8000:8000 --name mlops-api mlops-api:v1 (on EC2)
```

- [ ] **Screenshot**: Logs
- [ ] **Screenshot**: Running container
- [ ] **Screenshot**: Public endpoint test (browser/Postman)

---

## 📊 Completion Status

| Task | Code | Deployment | Screenshots |
|------|------|------------|-------------|
| 1.1 Project Structure | ✅ 100% | ✅ 100% | ⚠️ Need |
| 1.2 DVC Init | ✅ 100% | ✅ 100% | ⚠️ Need |
| 1.3 DVC Pipeline | ✅ 100% | ✅ 100% | ⚠️ Need |
| 2.1 Workflow File | ✅ 100% | ⚠️ Need GitHub | ⚠️ Need |
| 2.2 Tests | ✅ 100% | ✅ 100% | ⚠️ Need |
| 3.1 Dockerfile | ✅ 100% | ✅ 100% | ⚠️ Need |
| 3.2 Docker Hub | ✅ 100% | ⚠️ Need Push | ⚠️ Need |
| 4.1 Airflow | ✅ 100% | ✅ 100% | ⚠️ Need |
| 5.1 API | ✅ 100% | ✅ 100% | ⚠️ Need |
| 5.2 Containerize | ✅ 100% | ✅ 100% | ⚠️ Need |
| 6.1 S3 | ✅ 100% | ✅ 100% | ⚠️ Need |
| 6.2 EC2 | ✅ 100% | ✅ 100% | ⚠️ Need |
| 6.3 Deploy | ✅ 100% | ✅ 100% | ⚠️ Need |

**Code & Deployment: ~95% Complete**  
**Screenshots: Need to capture**

---

## 📝 Submission Requirements

### PDF/Word Report Needs:
- [x] Explanation + Commands used (all documented)
- [x] Terminal logs (can be captured)
- [ ] Screenshots of outputs (need to capture)
- [ ] GitHub repository link (need to create/push)
- [x] AWS public endpoint URL: http://13.60.67.119:8000

### Zipped Project Folder:
- [x] All source code ready
- [x] Configuration files ready
- [x] Documentation ready
- [ ] Need to exclude large files (.git, __pycache__, .dvc/cache, etc.)

---

## 🎯 What's Complete

### ✅ 100% Complete:
1. **DVC Setup** - All commands executed, pipeline working
2. **Docker Build & Run** - Image built, container tested
3. **Airflow Setup** - Services running, DAG ready
4. **API Development** - Created and deployed
5. **EC2 Deployment** - Instance configured, API running
6. **S3 Setup** - Bucket created, dataset uploaded

### ⚠️ Needs Action:
1. **GitHub Push** - Push code to GitHub (10 min)
2. **Docker Hub Push** - Tag and push image (10 min)
3. **Screenshots** - Capture all required screenshots (1 hour)
4. **Report Writing** - Compile report with screenshots (1-2 hours)

---

## ✅ Summary

**Code & Deployment: 95% Complete** ✅  
**Screenshots & Documentation: Need to capture** ⚠️

**Everything is built and working!** You just need to:
1. Push to GitHub
2. Push to Docker Hub
3. Capture screenshots
4. Write the report

**Estimated time to complete: 2-3 hours**

All the hard work is done! 🎉

