#!/bin/bash
# Airflow Setup Script

set -e

echo "=== Setting up Apache Airflow ==="
echo ""

# Set AIRFLOW_UID
echo "Setting AIRFLOW_UID..."
echo -e "AIRFLOW_UID=$(id -u)" > .env
echo "✅ AIRFLOW_UID set to $(id -u)"

# Create necessary directories
echo "Creating directories..."
mkdir -p airflow/dags airflow/logs airflow/plugins airflow/config
mkdir -p data models
echo "✅ Directories created"

# Initialize Airflow
echo "Initializing Airflow..."
docker compose up airflow-init
echo "✅ Airflow initialized"

echo ""
echo "=== Setup Complete ==="
echo ""
echo "To start Airflow, run:"
echo "  docker compose up"
echo ""
echo "Then access Airflow UI at: http://localhost:8080"
echo "Username: airflow"
echo "Password: airflow"

