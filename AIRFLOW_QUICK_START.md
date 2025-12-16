# Airflow Quick Start Guide

## Quick Setup (3 Steps)

### 1. Set Environment Variable
```bash
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

### 2. Initialize Airflow
```bash
docker compose up airflow-init
```

### 3. Start Airflow
```bash
docker compose up -d
```

## Access Airflow UI

- **URL:** http://localhost:8080
- **Username:** `airflow`
- **Password:** `airflow`

## Run the Training Pipeline

1. Open Airflow UI
2. Find `train_pipeline` DAG
3. Toggle it ON (switch on left)
4. Click DAG name → Click "Trigger DAG" (play icon)
5. Watch execution in Graph View

## Stop Airflow

```bash
docker compose down
```

## View Logs

```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f airflow-scheduler
```

## Common Issues

**DAG not appearing?**
- Wait 30 seconds for scheduler to parse
- Check: `docker compose logs airflow-scheduler`

**Permission errors?**
- Run: `echo -e "AIRFLOW_UID=$(id -u)" > .env`
- Restart: `docker compose down && docker compose up -d`

**Port 8080 in use?**
- Change port in `docker-compose.yaml` (line with `8080:8080`)

