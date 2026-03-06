"""
Train a Linear Regression model for house price prediction
and save it as a pickle file.
"""

import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("Housing.csv")

# Clean Data (Improve Accuracy)
df = df[df['price'] > 0]
upper_bound = df['price'].quantile(0.99)
df = df[df['price'] <= upper_bound]

# Preprocessing
df['date'] = pd.to_datetime(df['date']).dt.year
df.drop('street', axis=1, inplace=True)
df = pd.get_dummies(df, columns=['city', 'statezip', 'country'], drop_first=True)

# Features and target (Log transform target)
import numpy as np
X = df.drop('price', axis=1)
y = np.log1p(df['price'])

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model and feature names
with open("model/house_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save feature names to ensure prediction dataframe matches training
import os
os.makedirs('model', exist_ok=True)
with open("model/feature_names.pkl", "wb") as f:
    pickle.dump(list(X.columns), f)

print("Model trained and saved successfully")
