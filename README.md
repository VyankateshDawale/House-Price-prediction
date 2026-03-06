# 🏠 House Price Prediction

A machine learning web application that predicts house prices based on key property features using **Linear Regression**. Built with a **Flask** backend and a clean HTML/CSS/JS frontend.

---

## 📌 Features

- Predict house prices based on:
  - Number of Bedrooms
  - Number of Bathrooms
  - Square Footage (Living Area)
  - Square Footage (Lot)
  - Year Built
- Pre-trained Linear Regression model
- Simple, responsive web interface
- REST API endpoint for predictions

---

## 🛠️ Tech Stack

| Component       | Technology                  |
| --------------- | --------------------------- |
| **Frontend**    | HTML, CSS, JavaScript       |
| **Backend**     | Python, Flask, Flask-CORS   |
| **ML Model**    | scikit-learn (Linear Regression) |
| **Data Processing** | Pandas, NumPy          |

---

## 📁 Project Structure

```
House_Price_Prediction/
├── backend/
│   ├── app.py                 # Flask server & prediction API
│   ├── static/
│   │   ├── style.css          # Frontend styling
│   │   └── script.js          # Frontend logic (AJAX calls)
│   └── template/
│       └── index.html         # Main web page
├── model/
│   ├── house_model.pkl        # Trained Linear Regression model
│   └── feature_names.pkl      # Feature column names for prediction
├── Housing.csv                # Dataset (4600+ records)
├── train_model.py             # Script to train and save the model
├── requirements.txt           # Python dependencies
└── README.md
```

---

## 📊 Dataset

The dataset (`Housing.csv`) contains **4,600+ house sale records** from Washington state (USA) with features including:

- `date`, `price`, `bedrooms`, `bathrooms`
- `sqft_living`, `sqft_lot`, `floors`, `waterfront`
- `view`, `condition`, `sqft_above`, `sqft_basement`
- `yr_built`, `yr_renovated`, `street`, `city`, `statezip`, `country`

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/VyankateshDawale/House-Price-prediction.git
cd House-Price-prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. (Optional) Retrain the Model

If you want to retrain the model from scratch:

```bash
python train_model.py
```

This will regenerate `model/house_model.pkl`.

### 4. Run the Application

```bash
cd backend
python app.py
```

The app will start at **http://127.0.0.1:5000**

### 5. Use the Application

1. Open your browser and go to `http://127.0.0.1:5000`
2. Enter the property details:
   - **Bedrooms** – Number of bedrooms
   - **Bathrooms** – Number of bathrooms
   - **Sqft Living** – Living area in square feet
   - **Sqft Lot** – Lot size in square feet
   - **Year Built** – Year the house was built
3. Click **Predict**
4. The estimated house price will be displayed

---

## 🔌 API Reference

### `POST /predict`

**Request Body (JSON):**

```json
{
  "bedrooms": 3,
  "bathrooms": 2,
  "sqft_living": 2000,
  "sqft_lot": 8000,
  "yr_built": 1990
}
```

**Response (JSON):**

```json
{
  "predicted_price": 450000.00
}
```

---

## 🧠 Model Details

- **Algorithm:** Linear Regression
- **Library:** scikit-learn
- **Preprocessing:**
  - Date converted to year
  - Street column dropped
  - One-hot encoding for `city`, `statezip`, and `country`
- **Target Variable:** `price`

---

## 📝 License

This project is open-source and available for educational purposes.

---

## 👤 Author

**Vyankatesh Dawale**

- GitHub: [@VyankateshDawale](https://github.com/VyankateshDawale)
