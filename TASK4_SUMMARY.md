# Task 4 - Airflow Pipeline Summary

## ✅ Completed Setup

### 4.1 Airflow Installation with Docker Compose

**All Required Files Created:**

1. **docker-compose.yaml** ✅
   - PostgreSQL database for Airflow metadata
   - Airflow webserver (UI on port 8080)
   - Airflow scheduler
   - Airflow init service
   - Volume mounts for dags, logs, plugins, config
   - Mounts for data and models directories

2. **airflow/Dockerfile** ✅
   - Based on Apache Airflow 2.9.0
   - Installs system dependencies (gcc)
   - Installs Python requirements

3. **airflow/dags/train_pipeline.py** ✅
   - Complete DAG with 4 tasks
   - All required functionality implemented

4. **Setup Scripts** ✅
   - `airflow/setup_airflow.sh` - Automated setup
   - Environment configuration

### 4.2 DAG: train_pipeline.py

**DAG Structure:**
```
load_data → train_model → save_model → log_results
```

**Task Details:**

#### Task 1: load_data
- ✅ Loads dataset from CSV file
- ✅ Creates dataset if it doesn't exist
- ✅ Validates dataset structure
- ✅ Logs dataset statistics
- ✅ Pushes data info to XCom for next tasks

#### Task 2: train_model
- ✅ Loads data from previous task
- ✅ Splits into train/test sets (80/20)
- ✅ Trains Linear Regression model
- ✅ Evaluates model (MSE, R² score)
- ✅ Logs model performance metrics
- ✅ Pushes metrics to XCom

#### Task 3: save_model
- ✅ Creates models directory if needed
- ✅ Saves trained model as pickle file
- ✅ Verifies model was saved successfully
- ✅ Logs file size
- ✅ Pushes save status to XCom

#### Task 4: log_results
- ✅ Collects all metrics from previous tasks
- ✅ Logs comprehensive summary
- ✅ Saves summary report to JSON file
- ✅ Provides execution summary

## Setup Instructions

### Quick Start (3 Commands)

```bash
# 1. Set environment variable
echo -e "AIRFLOW_UID=$(id -u)" > .env

# 2. Initialize Airflow
docker compose up airflow-init

# 3. Start Airflow
docker compose up -d
```

### Access Airflow UI

1. Open browser: **http://localhost:8080**
2. Login:
   - Username: `airflow`
   - Password: `airflow`

### Run the Pipeline

1. In Airflow UI, find **`train_pipeline`** DAG
2. Toggle it **ON** (switch on the left)
3. Click on the DAG name
4. Click **"Trigger DAG"** button (play icon)
5. Watch execution in **Graph View**

## Screenshots Checklist

### Required Screenshots:

1. **Airflow UI Screenshot**
   - Main DAGs page showing `train_pipeline` DAG
   - DAG should be visible and enabled
   - Show the DAG list view

2. **DAG Graph Screenshot**
   - Click on `train_pipeline` DAG
   - Go to "Graph" view
   - Show all 4 tasks connected:
     - load_data
     - train_model
     - save_model
     - log_results
   - All tasks should show green (success) status

3. **Successful Job Run Screenshot**
   - After triggering the DAG
   - Show "Tree" or "Graph" view
   - All tasks completed successfully (green)
   - Show execution times
   - Can also show task logs

## Project Structure

```
Mlops-Project/
├── docker-compose.yaml          # Airflow services configuration
├── airflow/
│   ├── Dockerfile              # Custom Airflow image
│   ├── setup_airflow.sh        # Setup automation script
│   ├── dags/
│   │   └── train_pipeline.py  # ✅ Training pipeline DAG
│   ├── logs/                   # Airflow execution logs
│   ├── plugins/                # Airflow plugins (empty)
│   └── config/                 # Airflow config (empty)
├── data/                       # Dataset directory (mounted)
├── models/                     # Model output (mounted)
└── src/                        # Source code (mounted)
```

## DAG Features

### ✅ All Requirements Met:

- **Loads data** - Task 1: `load_data`
- **Trains model** - Task 2: `train_model`
- **Saves trained model** - Task 3: `save_model`
- **Logs results** - Task 4: `log_results`

### Additional Features:

- Comprehensive logging at each step
- Error handling and validation
- Data passing between tasks via XCom
- Model performance metrics tracking
- Summary report generation
- Automatic dataset creation if missing

## Useful Commands

### Start/Stop
```bash
# Start Airflow
docker compose up -d

# Stop Airflow
docker compose down

# View logs
docker compose logs -f
```

### Troubleshooting
```bash
# Check DAG syntax
python3 -m py_compile airflow/dags/train_pipeline.py

# View scheduler logs
docker compose logs airflow-scheduler

# Restart services
docker compose restart
```

## Verification Steps

Before taking screenshots, verify:

- [ ] Airflow UI is accessible at http://localhost:8080
- [ ] Can login with airflow/airflow
- [ ] `train_pipeline` DAG appears in the UI
- [ ] DAG can be enabled (toggle switch works)
- [ ] DAG can be triggered
- [ ] All 4 tasks execute successfully
- [ ] Model file is created in models/ directory
- [ ] Logs show detailed execution information

## Next Steps

1. **Start Airflow**: `docker compose up -d`
2. **Access UI**: http://localhost:8080
3. **Enable DAG**: Toggle `train_pipeline` ON
4. **Trigger DAG**: Click "Trigger DAG" button
5. **Monitor**: Watch execution in Graph View
6. **Screenshot**: Capture required screenshots

## Documentation Files

- `TASK4_AIRFLOW.md` - Detailed setup guide
- `AIRFLOW_QUICK_START.md` - Quick reference
- `TASK4_SUMMARY.md` - This file

All setup is complete and ready to use! 🚀

