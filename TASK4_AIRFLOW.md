# Task 4 - Airflow Pipeline Setup Guide

## ✅ Completed Tasks

### 4.1 Airflow Installation with Docker Compose

**Files Created:**
- ✅ `docker-compose.yaml` - Airflow services configuration
- ✅ `airflow/Dockerfile` - Custom Airflow image with dependencies
- ✅ `airflow/dags/train_pipeline.py` - Training pipeline DAG
- ✅ `.env` - Environment variables
- ✅ `airflow/setup_airflow.sh` - Setup script

### 4.2 DAG: train_pipeline.py

The DAG includes 4 tasks:

1. **load_data** - Loads dataset from CSV file
   - Checks if dataset exists, creates if not
   - Validates dataset structure
   - Logs dataset statistics
   - Pushes data info to XCom

2. **train_model** - Trains the machine learning model
   - Loads data from previous task
   - Splits into train/test sets
   - Trains Linear Regression model
   - Evaluates model (MSE, R²)
   - Logs model performance
   - Pushes metrics to XCom

3. **save_model** - Saves trained model to disk
   - Creates models directory if needed
   - Saves model as pickle file
   - Verifies model was saved
   - Logs file size

4. **log_results** - Logs comprehensive results
   - Collects all metrics from previous tasks
   - Logs detailed summary
   - Saves summary report to JSON file
   - Provides execution summary

## Setup Instructions

### Step 1: Set Environment Variables

```bash
# Set AIRFLOW_UID (important for file permissions)
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

Or use the setup script:
```bash
./airflow/setup_airflow.sh
```

### Step 2: Initialize Airflow

```bash
docker compose up airflow-init
```

This will:
- Initialize the Airflow database
- Create the admin user (airflow/airflow)
- Set up necessary tables

### Step 3: Start Airflow Services

```bash
docker compose up -d
```

This starts:
- **PostgreSQL** - Airflow metadata database
- **Airflow Webserver** - UI at http://localhost:8080
- **Airflow Scheduler** - Executes DAGs

### Step 4: Access Airflow UI

1. Open browser: http://localhost:8080
2. Login:
   - Username: `airflow`
   - Password: `airflow`

### Step 5: Enable and Trigger DAG

1. In Airflow UI, find `train_pipeline` DAG
2. Toggle it ON (switch on the left)
3. Click on the DAG name
4. Click "Trigger DAG" button (play icon)
5. Watch the execution in Graph View

## Commands Reference

### Start Airflow
```bash
docker compose up -d
```

### Stop Airflow
```bash
docker compose down
```

### View Logs
```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f airflow-webserver
docker compose logs -f airflow-scheduler
```

### Restart Services
```bash
docker compose restart
```

### Clean Start (removes volumes)
```bash
docker compose down -v
docker compose up airflow-init
docker compose up -d
```

## DAG Details

**DAG ID:** `train_pipeline`

**Schedule:** Daily (`timedelta(days=1)`)

**Tasks:**
```
load_data → train_model → save_model → log_results
```

**Task Dependencies:**
- Each task depends on the previous one
- Uses XCom to pass data between tasks

## Screenshots Needed

### 4.1 Deliverables:

1. **Airflow UI Screenshot**
   - Show the main DAGs page
   - Highlight the `train_pipeline` DAG
   - Show DAG status (green/running)

2. **DAG Graph Screenshot**
   - Click on `train_pipeline` DAG
   - Go to "Graph" view
   - Screenshot showing all 4 tasks and their connections
   - Show task statuses (success/failed)

3. **Successful Job Run Screenshot**
   - After triggering the DAG
   - Show "Tree" or "Graph" view with all tasks completed
   - All tasks should show green (success)
   - Show task execution times

## Troubleshooting

### Issue: Permission Denied
**Solution:**
```bash
# Make sure AIRFLOW_UID is set correctly
echo -e "AIRFLOW_UID=$(id -u)" > .env
docker compose down -v
docker compose up airflow-init
docker compose up -d
```

### Issue: DAG Not Appearing
**Solution:**
- Check DAG file is in `airflow/dags/` directory
- Check for syntax errors: `python -m py_compile airflow/dags/train_pipeline.py`
- Check scheduler logs: `docker compose logs airflow-scheduler`
- Wait a few seconds for DAG to be parsed

### Issue: Tasks Failing
**Solution:**
- Check task logs in Airflow UI
- Click on failed task → "Log" button
- Check if data/model directories exist
- Verify Python dependencies are installed

### Issue: Port 8080 Already in Use
**Solution:**
```bash
# Change port in docker-compose.yaml
# Under airflow-webserver, change:
ports:
  - "8080:8080"
# To:
ports:
  - "8081:8080"  # Access at http://localhost:8081
```

## Project Structure

```
Mlops-Project/
├── docker-compose.yaml          # Airflow services
├── .env                         # Environment variables
├── airflow/
│   ├── Dockerfile              # Custom Airflow image
│   ├── setup_airflow.sh        # Setup script
│   ├── dags/
│   │   └── train_pipeline.py  # Training pipeline DAG
│   ├── logs/                   # Airflow logs
│   ├── plugins/                # Airflow plugins
│   └── config/                 # Airflow config
├── data/                       # Dataset directory
├── models/                     # Model output directory
└── src/                        # Source code
```

## DAG Features

### Logging
- Comprehensive logging at each step
- Logs dataset statistics
- Logs model performance metrics
- Logs file operations

### Error Handling
- Validates dataset existence
- Verifies model saving
- Provides clear error messages

### Data Flow
- Uses XCom to pass data between tasks
- Stores metrics for logging
- Maintains data paths

### Monitoring
- All tasks are visible in Airflow UI
- Task logs available for debugging
- Execution history tracked

## Next Steps

After successful setup:

1. **Monitor DAG Execution**
   - Check Airflow UI regularly
   - Review task logs
   - Monitor execution times

2. **Customize DAG**
   - Modify schedule interval
   - Add more tasks
   - Add email notifications
   - Add retry logic

3. **Production Deployment**
   - Use external database
   - Set up proper authentication
   - Configure email alerts
   - Use CeleryExecutor for scaling

## Verification Checklist

- [ ] Airflow UI accessible at http://localhost:8080
- [ ] Can login with airflow/airflow
- [ ] `train_pipeline` DAG appears in UI
- [ ] DAG can be enabled (toggled ON)
- [ ] DAG can be triggered
- [ ] All 4 tasks execute successfully
- [ ] Model file created in models/ directory
- [ ] Logs show detailed execution information

