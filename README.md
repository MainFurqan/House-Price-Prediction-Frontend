# House Price Prediction – Full Stack ML Application

This repository represents a **production‑ready, end‑to‑end Machine Learning project** for predicting house prices. It covers the complete lifecycle of a data science application: **Exploratory Data Analysis (EDA), preprocessing, model training & evaluation, serialization, backend API development, frontend UI development, and cloud deployment**.

The application is split into two independent services:

* **Backend** → FastAPI + trained ML model (deployed on Railway)
* **Frontend** → Streamlit web application (deployed on Streamlit Cloud)

---

## 🔗 Live Application

**Frontend (Streamlit UI):**
[https://house-prize-prediction-frontend-ni2vyx76kgojvxxv7szyfg.streamlit.app/](https://house-prize-prediction-frontend-ni2vyx76kgojvxxv7szyfg.streamlit.app/)

The frontend communicates with the backend API to fetch predictions in real time.

---

## 🧠 Problem Statement

The goal of this project is to **predict house prices** based on multiple numerical and categorical features using supervised machine learning. Accurate price prediction helps buyers, sellers, and stakeholders make informed decisions.

---

## 🗂️ Project Architecture

```
House-Price-Prediction
│
├── Backend (FastAPI + ML Model)
│   ├── model/
│   │   ├── EDA_to_serialization.ipynb
│   │   ├── Housing.csv
│   │   └── house_price_gb_model.pkl
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── Frontend (Streamlit)
│   ├── streamlit_app.py
│   ├── requirements.txt
│   └── Dockerfile
```

the both repository is include ( House-Price-Prediction-Backend + House-Price-Prediction-Frontend)

---

## 📊 1. Data Exploration & Analysis (EDA)

All data exploration and experimentation is performed in:

```
model/EDA_to_serialization.ipynb
```

### Key EDA Steps

* Analyzed **distribution of numerical features**
* Checked **balance and imbalance** in categorical/discrete features
* Identified and handled **outliers**
* Studied **feature–target relationships**
* Documented all assumptions and decisions inside the notebook

The dataset used is:

```
model/Housing.csv
```

---

## 🔄 2. Data Preprocessing

The preprocessing pipeline includes:

* Encoding **binary categorical features** → `0 / 1`
* Encoding **ordinal categorical features** into ordered numeric values
* Ensuring consistent preprocessing for training and inference
* Separating features and target variable

**Target Variable:**

```
price
```

---

## 🤖 3. Model Training & Evaluation

Multiple models were trained and evaluated. The final selected model is:

### ✅ Gradient Boosting Regressor

**Performance on test data:**

* **RMSE:** ~0.25
* **R² Score:** ~0.66

This model provided the best bias‑variance tradeoff and generalization performance.

---

## 💾 4. Model Serialization

After finalizing the model:

* The trained model was serialized using `pickle`
* Saved as:

```
model/house_price_gb_model.pkl
```

This serialized model is loaded directly by the FastAPI backend for inference.

---

## ⚙️ 5. Backend – FastAPI (Model Serving)

### Purpose

The backend exposes the trained ML model as a **REST API** for real‑time predictions.

### Key File

```
main.py
```

### Responsibilities

* Load serialized model at startup
* Accept structured input features via API request
* Perform prediction using the trained model
* Return predicted house price as JSON response

### Tech Stack

* FastAPI
* Uvicorn
* Scikit‑learn
* NumPy / Pandas

### Containerization

The backend is fully containerized using Docker:

```
Dockerfile
```

### Deployment

* Deployed on **Railway**
* Connected directly to the GitHub backend repository

---

## 🎨 6. Frontend – Streamlit (User Interface)

### Purpose

Provides a simple, interactive UI for users to:

* Input house features
* Send data to backend API
* Display predicted house price

### Key File

```
streamlit_app.py
```

### Features

* User‑friendly input fields
* Real‑time API communication
* Error handling for invalid inputs
* Clean and minimal UI

### Tech Stack

* Streamlit
* Requests
* Python

### Deployment

* Deployed on **Streamlit Cloud**
* Connected to GitHub frontend repository

---

## 🔁 7. Frontend–Backend Communication

Flow:

1. User enters input features in Streamlit UI
2. Frontend sends HTTP request to FastAPI endpoint
3. Backend loads model and generates prediction
4. Prediction returned as JSON
5. Frontend displays result to user

---

## 🚀 8. End‑to‑End Deployment Summary

| Component | Platform        |
| --------- | --------------- |
| Backend   | Railway         |
| Frontend  | Streamlit Cloud |
| Model     | Pickle (.pkl)   |
| API       | FastAPI         |

---

## 📌 Key Highlights

* Complete **end‑to‑end ML pipeline**
* Production‑ready deployment
* Clear separation of concerns (EDA, model, API, UI)
* Scalable architecture
* Real‑time inference

---

## 👤 Author

**Main Furqan**
Machine Learning Engineer

---
