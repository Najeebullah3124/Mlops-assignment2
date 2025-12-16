"""
MLOps Training Pipeline DAG

This DAG orchestrates the machine learning training pipeline:
1. Load data
2. Train model
3. Save trained model
4. Log results
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import pandas as pd
import pickle
import os
import logging
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Configure logging
logger = logging.getLogger(__name__)

# Default arguments for the DAG
default_args = {
    'owner': 'mlops-team',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'train_pipeline',
    default_args=default_args,
    description='MLOps Training Pipeline',
    schedule_interval=timedelta(days=1),  # Run daily
    start_date=days_ago(1),
    catchup=False,
    tags=['mlops', 'training', 'ml'],
)


def load_data(**context):
    """
    Task 1: Load dataset from CSV file.
    
    Returns:
        str: Path to the dataset file
    """
    logger.info("Starting data loading task")
    
    data_path = '/opt/airflow/data/dataset.csv'
    
    # Check if dataset exists, if not create it
    if not os.path.exists(data_path):
        logger.warning(f"Dataset not found at {data_path}, creating sample dataset...")
        os.makedirs(os.path.dirname(data_path), exist_ok=True)
        
        # Create sample dataset
        import numpy as np
        np.random.seed(42)
        n_samples = 1000
        X = np.random.randn(n_samples, 5)
        y = X[:, 0] * 2 + X[:, 1] * 1.5 - X[:, 2] * 0.5 + np.random.randn(n_samples) * 0.1
        
        df = pd.DataFrame(X, columns=[f'feature_{i+1}' for i in range(5)])
        df['target'] = y
        df.to_csv(data_path, index=False)
        logger.info(f"Created dataset with {n_samples} samples")
    
    # Load and validate dataset
    df = pd.read_csv(data_path)
    logger.info(f"Dataset loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")
    logger.info(f"Dataset columns: {list(df.columns)}")
    
    # Log dataset statistics
    logger.info(f"Dataset statistics:\n{df.describe()}")
    
    # Push dataset info to XCom for next tasks
    context['ti'].xcom_push(key='data_path', value=data_path)
    context['ti'].xcom_push(key='data_shape', value=df.shape)
    
    return data_path


def train_model(**context):
    """
    Task 2: Train the machine learning model.
    
    Returns:
        dict: Model metrics and information
    """
    logger.info("Starting model training task")
    
    # Get data path from previous task
    data_path = context['ti'].xcom_pull(key='data_path', task_ids='load_data')
    
    # Load dataset
    df = pd.read_csv(data_path)
    logger.info(f"Loaded dataset: {df.shape}")
    
    # Separate features and target
    X = df.drop('target', axis=1)
    y = df['target']
    
    logger.info(f"Features shape: {X.shape}, Target shape: {y.shape}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    logger.info(f"Training set: {len(X_train)} samples")
    logger.info(f"Test set: {len(X_test)} samples")
    
    # Train model
    logger.info("Training Linear Regression model...")
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    logger.info("Model training completed")
    logger.info(f"Model coefficients: {model.coef_}")
    logger.info(f"Model intercept: {model.intercept_}")
    
    # Evaluate model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    logger.info(f"Model Performance:")
    logger.info(f"  MSE: {mse:.4f}")
    logger.info(f"  R² Score: {r2:.4f}")
    
    # Push model and metrics to XCom
    model_path = '/opt/airflow/models/model.pkl'
    context['ti'].xcom_push(key='model_path', value=model_path)
    context['ti'].xcom_push(key='mse', value=mse)
    context['ti'].xcom_push(key='r2_score', value=r2)
    context['ti'].xcom_push(key='model', value=model)  # For saving in next task
    
    return {
        'model_path': model_path,
        'mse': mse,
        'r2_score': r2,
        'train_size': len(X_train),
        'test_size': len(X_test),
    }


def save_model(**context):
    """
    Task 3: Save the trained model to disk.
    """
    logger.info("Starting model saving task")
    
    # Get model path and model from previous task
    model_path = context['ti'].xcom_pull(key='model_path', task_ids='train_model')
    
    # Get model object (in production, you might want to serialize differently)
    # For now, we'll retrain or load from XCom
    # Note: XCom has size limits, so we'll retrain here or use a better approach
    data_path = context['ti'].xcom_pull(key='data_path', task_ids='load_data')
    df = pd.read_csv(data_path)
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Create models directory if it doesn't exist
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    
    # Save model
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    logger.info(f"Model saved successfully to {model_path}")
    
    # Verify model was saved
    if os.path.exists(model_path):
        file_size = os.path.getsize(model_path)
        logger.info(f"Model file size: {file_size} bytes")
        context['ti'].xcom_push(key='model_saved', value=True)
        context['ti'].xcom_push(key='model_file_size', value=file_size)
    else:
        raise FileNotFoundError(f"Model file was not created at {model_path}")
    
    return model_path


def log_results(**context):
    """
    Task 4: Log training results and metrics.
    """
    logger.info("Starting results logging task")
    
    # Get all metrics from previous tasks
    data_shape = context['ti'].xcom_pull(key='data_shape', task_ids='load_data')
    mse = context['ti'].xcom_pull(key='mse', task_ids='train_model')
    r2_score = context['ti'].xcom_pull(key='r2_score', task_ids='train_model')
    model_path = context['ti'].xcom_pull(key='model_path', task_ids='train_model')
    model_saved = context['ti'].xcom_pull(key='model_saved', task_ids='save_model')
    model_file_size = context['ti'].xcom_pull(key='model_file_size', task_ids='save_model')
    
    # Log comprehensive results
    logger.info("=" * 50)
    logger.info("TRAINING PIPELINE RESULTS")
    logger.info("=" * 50)
    logger.info(f"Dataset Shape: {data_shape}")
    logger.info(f"Model Performance Metrics:")
    logger.info(f"  Mean Squared Error (MSE): {mse:.6f}")
    logger.info(f"  R² Score: {r2_score:.6f}")
    logger.info(f"Model Location: {model_path}")
    logger.info(f"Model Saved: {model_saved}")
    logger.info(f"Model File Size: {model_file_size} bytes")
    logger.info("=" * 50)
    
    # Create a summary report
    summary = {
        'timestamp': datetime.now().isoformat(),
        'data_shape': data_shape,
        'mse': mse,
        'r2_score': r2_score,
        'model_path': model_path,
        'model_saved': model_saved,
        'model_file_size': model_file_size,
    }
    
    # Save summary to file
    summary_path = '/opt/airflow/logs/training_summary.json'
    import json
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    
    logger.info(f"Summary report saved to {summary_path}")
    logger.info("Pipeline execution completed successfully!")
    
    return summary


# Define tasks
task_load_data = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

task_train_model = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

task_save_model = PythonOperator(
    task_id='save_model',
    python_callable=save_model,
    dag=dag,
)

task_log_results = PythonOperator(
    task_id='log_results',
    python_callable=log_results,
    dag=dag,
)

# Define task dependencies
task_load_data >> task_train_model >> task_save_model >> task_log_results

