#!/usr/bin/env python3
"""
Training script for the MLOps project.
Loads dataset, trains a model, and saves it.
"""
import pandas as pd
import pickle
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def load_data(data_path='data/dataset.csv'):
    """Load dataset from CSV file."""
    df = pd.read_csv(data_path)
    return df


def prepare_data(df):
    """Separate features and target from dataframe."""
    X = df.drop('target', axis=1)
    y = df['target']
    return X, y


def train_model(X_train, y_train):
    """Train a linear regression model."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """Evaluate model performance."""
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2, y_pred


def save_model(model, model_path='models/model.pkl'):
    """Save trained model to file."""
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)


def main():
    # Load dataset
    print("Loading dataset...")
    df = load_data('data/dataset.csv')
    
    # Separate features and target
    X, y = prepare_data(df)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"Training set size: {len(X_train)}")
    print(f"Test set size: {len(X_test)}")
    
    # Train model
    print("Training model...")
    model = train_model(X_train, y_train)
    
    # Evaluate model
    mse, r2, y_pred = evaluate_model(model, X_test, y_test)
    
    print(f"Model performance:")
    print(f"  MSE: {mse:.4f}")
    print(f"  R²: {r2:.4f}")
    
    # Save model
    model_path = 'models/model.pkl'
    save_model(model, model_path)
    
    print(f"Model saved to {model_path}")

if __name__ == '__main__':
    main()

