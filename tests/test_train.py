#!/usr/bin/env python3
"""
Unit tests for the training script.
"""
import unittest
import os
import sys
import pandas as pd
import numpy as np
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from train import load_data, prepare_data, train_model, evaluate_model, save_model


class TestDataLoading(unittest.TestCase):
    """Test data loading functionality."""
    
    def test_load_data_exists(self):
        """Test that dataset file exists and can be loaded."""
        data_path = 'data/dataset.csv'
        self.assertTrue(os.path.exists(data_path), 
                       f"Dataset file {data_path} does not exist")
        
        df = load_data(data_path)
        self.assertIsInstance(df, pd.DataFrame, 
                             "load_data should return a DataFrame")
    
    def test_load_data_not_empty(self):
        """Test that loaded dataset is not empty."""
        df = load_data('data/dataset.csv')
        self.assertGreater(len(df), 0, "Dataset should not be empty")
    
    def test_load_data_has_target(self):
        """Test that dataset has a target column."""
        df = load_data('data/dataset.csv')
        self.assertIn('target', df.columns, 
                     "Dataset should have a 'target' column")
    
    def test_load_data_shape(self):
        """Test that dataset has expected shape (features + target)."""
        df = load_data('data/dataset.csv')
        # Should have at least 1 feature column + target column
        self.assertGreaterEqual(len(df.columns), 2, 
                               "Dataset should have at least 2 columns")
        # Should have multiple rows
        self.assertGreater(len(df), 10, 
                          "Dataset should have multiple rows")


class TestDataPreparation(unittest.TestCase):
    """Test data preparation functionality."""
    
    def setUp(self):
        """Set up test data."""
        self.df = load_data('data/dataset.csv')
    
    def test_prepare_data_returns_two_objects(self):
        """Test that prepare_data returns X and y."""
        X, y = prepare_data(self.df)
        self.assertIsNotNone(X, "X should not be None")
        self.assertIsNotNone(y, "y should not be None")
    
    def test_prepare_data_X_shape(self):
        """Test that X has correct shape (no target column)."""
        X, y = prepare_data(self.df)
        # X should have one less column than original df
        self.assertEqual(X.shape[1], self.df.shape[1] - 1,
                        "X should have one less column than original dataframe")
        self.assertEqual(X.shape[0], self.df.shape[0],
                        "X should have same number of rows as original dataframe")
    
    def test_prepare_data_y_shape(self):
        """Test that y has correct shape (1D array)."""
        X, y = prepare_data(self.df)
        # y should be a Series with same number of rows
        self.assertEqual(len(y), self.df.shape[0],
                       "y should have same number of rows as original dataframe")
        self.assertEqual(y.ndim, 1, "y should be 1-dimensional")


class TestModelTraining(unittest.TestCase):
    """Test model training functionality."""
    
    def setUp(self):
        """Set up test data."""
        self.df = load_data('data/dataset.csv')
        self.X, self.y = prepare_data(self.df)
        # Use a subset for faster testing
        self.X_train = self.X.iloc[:100]
        self.y_train = self.y.iloc[:100]
    
    def test_train_model_returns_model(self):
        """Test that train_model returns a model object."""
        model = train_model(self.X_train, self.y_train)
        self.assertIsNotNone(model, "train_model should return a model")
        # Check it's a LinearRegression model
        from sklearn.linear_model import LinearRegression
        self.assertIsInstance(model, LinearRegression,
                             "Model should be a LinearRegression instance")
    
    def test_train_model_has_coefficients(self):
        """Test that trained model has coefficients."""
        model = train_model(self.X_train, self.y_train)
        self.assertIsNotNone(model.coef_, "Model should have coefficients")
        self.assertEqual(len(model.coef_), self.X_train.shape[1],
                        "Number of coefficients should match number of features")
    
    def test_train_model_can_predict(self):
        """Test that trained model can make predictions."""
        model = train_model(self.X_train, self.y_train)
        X_test = self.X.iloc[100:110]
        predictions = model.predict(X_test)
        self.assertEqual(len(predictions), len(X_test),
                        "Predictions should have same length as test data")


class TestModelEvaluation(unittest.TestCase):
    """Test model evaluation functionality."""
    
    def setUp(self):
        """Set up test data and model."""
        self.df = load_data('data/dataset.csv')
        self.X, self.y = prepare_data(self.df)
        self.X_train = self.X.iloc[:100]
        self.y_train = self.y.iloc[:100]
        self.X_test = self.X.iloc[100:120]
        self.y_test = self.y.iloc[100:120]
        self.model = train_model(self.X_train, self.y_train)
    
    def test_evaluate_model_returns_metrics(self):
        """Test that evaluate_model returns metrics."""
        mse, r2, y_pred = evaluate_model(self.model, self.X_test, self.y_test)
        self.assertIsNotNone(mse, "MSE should not be None")
        self.assertIsNotNone(r2, "R² should not be None")
        self.assertIsNotNone(y_pred, "Predictions should not be None")
    
    def test_evaluate_model_mse_is_positive(self):
        """Test that MSE is a positive number."""
        mse, r2, y_pred = evaluate_model(self.model, self.X_test, self.y_test)
        self.assertGreaterEqual(mse, 0, "MSE should be non-negative")
        self.assertIsInstance(mse, (int, float), "MSE should be a number")
    
    def test_evaluate_model_r2_is_valid(self):
        """Test that R² is a valid score."""
        mse, r2, y_pred = evaluate_model(self.model, self.X_test, self.y_test)
        # R² can be negative for bad models, but should be a number
        self.assertIsInstance(r2, (int, float), "R² should be a number")
        self.assertLessEqual(r2, 1.0, "R² should be <= 1.0")
    
    def test_evaluate_model_predictions_shape(self):
        """Test that predictions have correct shape."""
        mse, r2, y_pred = evaluate_model(self.model, self.X_test, self.y_test)
        self.assertEqual(len(y_pred), len(self.y_test),
                       "Predictions should have same length as test labels")


class TestShapeValidation(unittest.TestCase):
    """Test shape validation across the pipeline."""
    
    def test_data_shapes_consistent(self):
        """Test that data shapes are consistent throughout pipeline."""
        df = load_data('data/dataset.csv')
        X, y = prepare_data(df)
        
        # Check original dataframe
        self.assertGreater(df.shape[0], 0, "Dataframe should have rows")
        self.assertGreater(df.shape[1], 1, "Dataframe should have columns")
        
        # Check X and y shapes
        self.assertEqual(X.shape[0], df.shape[0], 
                        "X should have same rows as original")
        self.assertEqual(X.shape[1], df.shape[1] - 1,
                        "X should have one less column (no target)")
        self.assertEqual(len(y), df.shape[0],
                        "y should have same rows as original")
    
    def test_model_input_output_shapes(self):
        """Test that model input/output shapes are correct."""
        df = load_data('data/dataset.csv')
        X, y = prepare_data(df)
        
        X_train = X.iloc[:100]
        y_train = y.iloc[:100]
        X_test = X.iloc[100:110]
        
        model = train_model(X_train, y_train)
        predictions = model.predict(X_test)
        
        # Model should accept X_test and produce predictions
        self.assertEqual(len(predictions), len(X_test),
                        "Predictions should match test data length")
        self.assertEqual(model.coef_.shape[0], X_train.shape[1],
                        "Model coefficients should match feature count")


if __name__ == '__main__':
    unittest.main()

