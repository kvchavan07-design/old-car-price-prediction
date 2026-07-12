# 🚗 AI Used Car Price Prediction

A Machine Learning web application that predicts the selling price of a used car based on its specifications. The project is developed using **Python**, **Scikit-learn**, and **Streamlit**, with a **Random Forest Regressor** for prediction.

---

# 📌 Project Overview

This project predicts the resale value of used cars using Machine Learning. Users enter car details such as brand, fuel type, transmission, mileage, engine size, seats, and age, and the model estimates the selling price.

---

# 🚀 Features

- Predicts used car selling price
- Interactive Streamlit web application
- Data preprocessing and feature engineering
- One-Hot Encoding for categorical features
- Random Forest Regression model
- Clean and responsive user interface
- Fast and accurate predictions

---

# 📊 Dataset Information

- **Total Cars:** 7907
- **Brands:** 30
- **Features Used:** 46
- **Target Variable:** Selling Price

## Input Features

- Brand
- Fuel Type
- Seller Type
- Transmission
- Owner
- KM Driven
- Mileage
- Engine
- Max Power
- Seats
- Age

---

# 🧠 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Handling Missing Values
4. Exploratory Data Analysis (EDA)
5. Feature Engineering
6. One-Hot Encoding
7. Train-Test Split
8. Model Training
9. Model Evaluation
10. Web Application Development

---

# 🤖 Machine Learning Model

**Random Forest Regressor**

## Model Performance

| Metric | Score |
|---------|--------|
| Training R² Score | 0.9949 |
| Testing R² Score | 0.9827 |
| Mean Absolute Error (MAE) | 60,710 |
| Root Mean Squared Error (RMSE) | 113,564 |

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Jupyter Notebook

---

# 📂 Project Structure

```text
Old-Car-Price-Prediction/
│
├── app.py
├── Old_Car_Price_Prediction.ipynb
├── columns.pkl
├── requirements.txt
├── README.md
├── dataset.csv
└── model.pkl
```

> **Note:** If `model.pkl` is not included because of its size, generate it by running the notebook.

---

# ▶️ Installation

## Clone the Repository

```bash
git clone <repository-url>
```

## Move to the Project Folder

```bash
cd Old-Car-Price-Prediction
```

## Install Required Libraries

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

---

# 📈 Future Improvements

- XGBoost Model
- LightGBM Model
- Feature Importance Visualization
- Prediction History
- Cloud Deployment
- Better UI/UX
- Mobile-Friendly Design
- Dark Mode
- Model Comparison Dashboard

---

# 📚 Learning Outcomes

This project helped me understand:

- Data Cleaning
- Missing Value Handling
- Feature Engineering
- One-Hot Encoding
- Random Forest Regression
- Model Evaluation
- Streamlit Web Development
- End-to-End Machine Learning Projects

---

# 👨‍💻 Developer

**Aniket Chavan**

**FY MSc Data Science**

### Skills

- Python
- Machine Learning
- Data Analysis
- Streamlit
- Scikit-learn

---

# ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub.

---

# 📄 License

This project is developed for educational and learning purposes.
