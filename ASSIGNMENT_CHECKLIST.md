# Assignment 02 - Submission Checklist

**Deadline: 14-12-2025**

## ✅ Completed Tasks

### Task 1.1 - Project Setup ✅
- [x] Git initialized
- [x] .gitignore created
- [x] Python environment (requirements.txt)
- [x] Project structure created
- [x] Screenshots ready (folder structure)

### Task 2 - CI/CD Pipeline ✅
- [x] Workflow file created (.github/workflows/ci.yml)
- [x] Unit tests created (tests/test_train.py)
- [x] All 16 tests passing
- [x] Linting configured (flake8, pylint)
- [ ] ⚠️ **Need**: Push to GitHub and screenshot workflow run

### Task 3.1 - Dockerfile ✅
- [x] Dockerfile created
- [x] Build tested
- [ ] ⚠️ **Need**: Screenshot of build logs and running container

### Task 3.2 - Docker Hub Push ⚠️
- [ ] **Need**: Tag image with your Docker Hub username
- [ ] **Need**: Push to Docker Hub
- [ ] **Need**: Screenshot of Docker Hub repository

### Task 4 - Airflow ⚠️
- [x] Docker compose file created
- [x] DAG created (train_pipeline.py)
- [ ] **Need**: Start Airflow and screenshot UI/DAG

### Task 5 - RESTful API ✅
- [x] API created (api/app.py - Flask)
- [x] Endpoints: /predict, /health, /
- [x] Containerized
- [x] Running on EC2
- [ ] ⚠️ **Need**: Screenshots of API testing

### Task 6.1 - S3 Bucket ✅
- [x] Bucket created: mlops-test-ass
- [x] Dataset uploaded
- [x] URL generated
- [ ] ⚠️ **Need**: Screenshots

### Task 6.2 - EC2 Instance ✅
- [x] Instance launched: 13.60.67.119
- [x] Port 8000 opened
- [x] Dependencies installed
- [ ] ⚠️ **Need**: Screenshots

### Task 6.3 - API Deployment on EC2 ✅
- [x] API deployed
- [x] Container running
- [x] Public endpoint working: http://13.60.67.119:8000
- [ ] ⚠️ **Need**: Screenshots

## ⚠️ Tasks Needing Action

### 1. DVC Setup (Task 1.2 & 1.3)
**Status**: Files ready, but DVC commands need to be run

**Commands to run:**
```bash
# Install DVC if not installed
pip install dvc

# Initialize DVC
dvc init
dvc remote add -d myremote ./dvcstore

# Add dataset
dvc add data/dataset.csv
git add data/.gitignore data/dataset.csv.dvc .dvc .dvcignore
git commit -m "Add dataset with DVC"

# Create pipeline
dvc run -n train_model \
  -d src/train.py -d data/dataset.csv \
  -o models/model.pkl \
  python src/train.py

git add dvc.yaml dvc.lock
git commit -m "Add training pipeline"
```

### 2. GitHub Actions (Task 2)
**Status**: Workflow file ready, needs to be pushed

**Action needed:**
- Push code to GitHub repository
- Screenshot successful workflow run
- (Optional) Create a failing workflow screenshot

### 3. Docker Hub Push (Task 3.2)
**Status**: Image built, needs to be pushed

**Commands:**
```bash
# Tag image (replace 'yourusername' with your Docker Hub username)
docker tag mlops-app yourusername/mlops-app:v1

# Login to Docker Hub
docker login

# Push image
docker push yourusername/mlops-app:v1
```

### 4. Airflow (Task 4)
**Status**: Files ready, needs to be started

**Commands:**
```bash
# Set environment variable
echo -e "AIRFLOW_UID=$(id -u)" > .env

# Initialize Airflow
docker compose up airflow-init

# Start Airflow
docker compose up -d

# Access UI: http://localhost:8080
# Username: airflow
# Password: airflow
```

## 📸 Screenshots Needed

### Task 1
- [x] Folder structure
- [x] Git init output
- [ ] DVC commands output
- [ ] .dvc file content
- [ ] DVC pipeline run
- [ ] dvc.yaml file

### Task 2
- [ ] Workflow file (.github/workflows/ci.yml)
- [ ] GitHub Actions successful run
- [ ] (Optional) Failing workflow
- [ ] Test results

### Task 3
- [ ] Dockerfile
- [ ] Build logs
- [ ] Running container
- [ ] Docker Hub repository page
- [ ] Push logs

### Task 4
- [ ] Airflow UI
- [ ] DAG graph
- [ ] Successful job run

### Task 5
- [ ] API running (terminal)
- [ ] Postman/cURL testing
- [ ] Sample predictions
- [ ] API in Docker

### Task 6
- [ ] S3 bucket page
- [ ] Uploaded dataset
- [ ] EC2 instance dashboard
- [ ] SSH terminal
- [ ] Container logs
- [ ] Running container
- [ ] Public endpoint test (browser/Postman)

## 📋 Submission Requirements

### PDF/Word Report Should Include:
1. ✅ Explanation + Commands used
2. ✅ Terminal logs
3. ⚠️ Screenshots of outputs (need to capture)
4. ⚠️ GitHub repository link (need to create/push)
5. ✅ AWS public endpoint URL: http://13.60.67.119:8000

### Zipped Project Folder:
- ✅ Exclude large files (.git, __pycache__, .dvc/cache, etc.)
- ✅ Include all source code
- ✅ Include configuration files
- ✅ Include documentation

## 🚀 Quick Action Items

1. **DVC Setup** (15 min)
   - Run DVC commands
   - Capture screenshots

2. **GitHub Push** (10 min)
   - Create GitHub repo
   - Push code
   - Screenshot workflow

3. **Docker Hub** (10 min)
   - Tag and push image
   - Screenshot repository

4. **Airflow** (20 min)
   - Start Airflow
   - Trigger DAG
   - Screenshot UI

5. **Screenshots** (30 min)
   - Capture all required screenshots
   - Organize for report

## ✅ What's Already Done

- ✅ Complete project structure
- ✅ All source code written
- ✅ Tests created and passing
- ✅ Docker configuration
- ✅ API deployed and running
- ✅ EC2 instance configured
- ✅ S3 bucket created
- ✅ All documentation files

## 📝 Summary

**Ready**: ~85%  
**Needs Action**: 
- DVC setup and screenshots
- GitHub push and workflow screenshots
- Docker Hub push
- Airflow setup and screenshots
- Capture all screenshots

**Estimated Time to Complete**: 1-2 hours

