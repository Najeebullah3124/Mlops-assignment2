#!/usr/bin/env python3
"""
Script to create a sample dataset for the MLOps project.
"""
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample data
n_samples = 1000
X = np.random.randn(n_samples, 5)
y = X[:, 0] * 2 + X[:, 1] * 1.5 - X[:, 2] * 0.5 + np.random.randn(n_samples) * 0.1

# Create DataFrame
df = pd.DataFrame(X, columns=[f'feature_{i+1}' for i in range(5)])
df['target'] = y

# Save to CSV
df.to_csv('data/dataset.csv', index=False)
print(f"Dataset created with {n_samples} samples and saved to data/dataset.csv")

