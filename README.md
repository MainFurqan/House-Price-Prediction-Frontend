# 🏠 New Delhi House Price Prediction

**End-to-End Machine Learning Deployment Application**

🔗 **Live Application (Streamlit Frontend)**
[https://house-prize-prediction-frontend-ni2vyx76kgojvxxv7szyfg.streamlit.app/](https://house-prize-prediction-frontend-ni2vyx76kgojvxxv7szyfg.streamlit.app/)

---

## 📌 Project Overview

This repository contains a **production-ready, end-to-end Machine Learning application** for predicting **house prices in New Delhi** using structured housing data.

The project demonstrates the **complete ML lifecycle**, including:

* Exploratory Data Analysis (EDA)
* Data preprocessing & feature engineering
* Model training, evaluation & selection
* Model serialization
* Backend API development
* Frontend UI development
* Cloud deployment using Docker

The system follows a **clean separation of concerns** with independent backend and frontend services.

---

## 🧠 Problem Statement

House price prediction is challenging due to:

* High feature variability
* Skewed target distributions
* Presence of outliers
* Non-linear relationships between features and price

The goal of this project is to build a **robust regression model** that accurately predicts house prices while handling skewness, outliers, and feature interactions effectively.

---

## 🗂️ Project Structure

```
New Delhi Home Price Prediction/
│
├── backend/
│   ├── model/
│   │   ├── EDA_to_Serialization.ipynb
│   │   ├── housing.csv
│   │   └── home_price_GD_model.pkl
│   │
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── streamlit_app.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── README.md
```

> The backend and frontend are deployed as **separate services**:
>
> * Backend → Railway
> * Frontend → Streamlit Cloud

---

## 🔍 Exploratory Data Analysis (EDA)

All exploratory analysis and experimentation were performed in:

```
backend/model/EDA_to_Serialization.ipynb
```

### EDA Highlights

* Analysis of **numerical feature distributions**
* Balance and imbalance analysis of **categorical variables**
* Identification of **skewness and extreme values**
* Outlier detection using statistical techniques and visualizations
* Univariate and multivariate analysis to study feature–target relationships
* Clear documentation of assumptions and decisions

The dataset used:

```
backend/model/housing.csv
```

---

## ⚙️ Data Preprocessing

The preprocessing pipeline includes:

* Encoding **categorical features** using appropriate strategies
* Encoding **ordinal variables** with meaningful numeric order
* Handling outliers and inconsistencies
* Feature–target separation
* Ensuring consistency between training and inference pipelines

### Target Variable Transformation

* Applied **log transformation** on the target variable (`price`) to:

  * Reduce extreme skewness
  * Stabilize variance
  * Improve model generalization

---

## 🤖 Model Training & Selection

The following tree-based regression models were trained and evaluated:

* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor

### ✅ Final Model

**Gradient Boosting Regressor** was selected based on superior generalization performance.

### 📊 Model Performance (Test Data)

| Metric | Value    |
| ------ | -------- |
| RMSE   | **0.25** |
| R²     | **0.66** |

---

## 💾 Model Serialization

* The finalized model was serialized using **Pickle**
* Saved as:

```
backend/model/home_price_GD_model.pkl
```

This model is directly loaded by the backend API during runtime.

---

## 🚀 Backend – FastAPI (Model Serving)

### Purpose

The backend exposes the trained ML model as a **RESTful API** for real-time predictions.

### Key File

```
backend/main.py
```

### Responsibilities

* Load serialized model at application startup
* Accept structured feature inputs via HTTP requests
* Perform inference using the trained model
* Return predictions in JSON format

### Tech Stack

* FastAPI
* Uvicorn
* Scikit-learn
* Pandas & NumPy

### Containerization & Deployment

* Fully containerized using **Docker**
* Deployed on **Railway**

---

## 🎨 Frontend – Streamlit (User Interface)

### Purpose

Provides an interactive web interface for users to:

* Input house features
* Trigger predictions
* View predicted house prices in real time

### Key File

```
frontend/streamlit_app.py
```

### Features

* Clean and intuitive UI
* Real-time API communication
* Input validation and error handling
* Lightweight and responsive design

### Deployment

* Deployed on **Streamlit Cloud**
* Communicates with FastAPI backend over HTTP

---

## 🔁 Frontend–Backend Workflow

1. User enters housing features in Streamlit UI
2. Frontend sends request to FastAPI endpoint
3. Backend performs prediction using serialized model
4. Prediction returned as JSON
5. Frontend displays result to the user

---

## 🐳 Deployment Architecture

| Component      | Technology         | Platform        |
| -------------- | ------------------ | --------------- |
| Model Training | Scikit-learn       | Local           |
| Backend API    | FastAPI + Docker   | Railway         |
| Frontend UI    | Streamlit + Docker | Streamlit Cloud |

This **hybrid deployment architecture** ensures modularity, scalability, and clean system design.

---

## 🏗️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* FastAPI
* Streamlit
* Docker
* Railway
* Streamlit Cloud

---

## 👤 Author

**Main Furqan**
Machine Learning & Data Science

---
