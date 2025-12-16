#!/usr/bin/env python3
"""
MLOps API - Flask application for model inference
"""
from flask import Flask, request, jsonify
import pickle
import os
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model
MODEL_PATH = 'models/model.pkl'
model = None

def load_model():
    """Load the trained model."""
    global model
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        print(f"Model loaded from {MODEL_PATH}")
    else:
        print(f"Warning: Model file not found at {MODEL_PATH}")

@app.route('/')
def home():
    """Home endpoint."""
    return jsonify({
        'message': 'MLOps API - Model Inference Service',
        'version': '1.0',
        'endpoints': {
            '/': 'API information',
            '/health': 'Health check',
            '/predict': 'Model prediction (POST)',
            '/predict/batch': 'Batch prediction (POST)'
        }
    })

@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Single prediction endpoint."""
    try:
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 500
        
        data = request.get_json()
        
        if not data or 'features' not in data:
            return jsonify({'error': 'Invalid input. Expected {"features": [f1, f2, f3, f4, f5]}'}), 400
        
        features = data['features']
        
        if len(features) != 5:
            return jsonify({'error': 'Expected 5 features'}), 400
        
        # Convert to numpy array and reshape for prediction
        features_array = np.array(features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features_array)[0]
        
        return jsonify({
            'prediction': float(prediction),
            'features': features,
            'model_type': 'LinearRegression'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict/batch', methods=['POST'])
def predict_batch():
    """Batch prediction endpoint."""
    try:
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 500
        
        data = request.get_json()
        
        if not data or 'features' not in data:
            return jsonify({'error': 'Invalid input. Expected {"features": [[f1, f2, ...], ...]}'}), 400
        
        features_list = data['features']
        
        if not isinstance(features_list, list) or len(features_list) == 0:
            return jsonify({'error': 'Features must be a non-empty list'}), 400
        
        # Convert to numpy array
        features_array = np.array(features_list)
        
        if features_array.shape[1] != 5:
            return jsonify({'error': 'Each sample must have 5 features'}), 400
        
        # Make predictions
        predictions = model.predict(features_array).tolist()
        
        return jsonify({
            'predictions': predictions,
            'count': len(predictions),
            'model_type': 'LinearRegression'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Load model on startup
    load_model()
    
    # Run Flask app
    app.run(host='0.0.0.0', port=8000, debug=False)

