"""
Train a Linear Regression model for house price prediction
and save it as a pickle file.
"""

import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("Housing.csv")

# Preprocessing
df['date'] = pd.to_datetime(df['date']).dt.year
df.drop('street', axis=1, inplace=True)
df = pd.get_dummies(df, columns=['city', 'statezip', 'country'], drop_first=True)

# Features and target
X = df.drop('price', axis=1)
y = df['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model/house_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully")
