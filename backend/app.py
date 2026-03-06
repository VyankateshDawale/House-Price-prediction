"""
Flask backend for house price prediction
"""

import pickle
import numpy as np
import pandas as pd
import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='template', static_folder='static')

# 🔥 THIS LINE FIXES YOUR PROBLEM
CORS(app, supports_credentials=True)

# Get the absolute path to the model file
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, "..", "model", "house_model.pkl")
feature_names_path = os.path.join(base_dir, "..", "model", "feature_names.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(feature_names_path, "rb") as f:
    feature_names = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        print("Received:", data)
        
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Create a DataFrame with the input data
        input_data = {
            'date': '2014-01-01',  # Date string that will be converted
            'bedrooms': float(data["bedrooms"]),
            'bathrooms': float(data["bathrooms"]),
            'sqft_living': float(data["sqft_living"]),
            'sqft_lot': float(data["sqft_lot"]),
            'floors': 1.0,
            'waterfront': 0.0,
            'view': 0.0,
            'condition': 3.0,
            'sqft_above': float(data["sqft_living"]),
            'sqft_basement': 0.0,
            'yr_built': float(data["yr_built"]),
            'yr_renovated': 0.0,
            'city': 'Shoreline',  # Default city (from training data)
            'statezip': 'WA 98133',  # Default statezip (from training data)
            'country': 'USA'  # Default country
        }
        
        # Create DataFrame
        df = pd.DataFrame([input_data])
        
        # Apply same preprocessing as training
        df['date'] = pd.to_datetime(df['date']).dt.year
        df.drop('street', axis=1, errors='ignore', inplace=True)
        df = pd.get_dummies(df, columns=['city', 'statezip', 'country'], drop_first=True)
        
        # Ensure all feature columns exist (fill missing with 0)
        for col in feature_names:
            if col not in df.columns:
                df[col] = 0
        
        # Reorder columns to match training order
        df = df[feature_names]
        
        # Make prediction
        features = df.values
        prediction = model.predict(features)[0]
        return jsonify({"predicted_price": round(float(prediction), 2)})
    except Exception as e:
        import traceback
        error_msg = f"{str(e)}\n{traceback.format_exc()}"
        print(f"Error: {error_msg}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)