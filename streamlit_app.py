import streamlit as st
import requests

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="New Delhi House Price Prediction",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🏠 New Delhi House Price Prediction")
st.markdown(
    "Enter the house details below to estimate the **market price** using a trained **Gradient Boosting model**."
)

st.divider()

# -------------------- INPUT SECTIONS --------------------

# ===== BASIC HOUSE DETAILS =====
st.subheader("📐 Basic House Details")

col1, col2, col3, col4 = st.columns(4)

with col1:
    area = st.number_input("Area (sqft)", min_value=200, step=50)

with col2:
    bedrooms = st.number_input("No of Bedrooms", min_value=1, step=1)

with col3:
    bathrooms = st.number_input("No of Bathrooms", min_value=1, step=1)

with col4:
    stories = st.number_input("Stories", min_value=1, step=1)


# ===== AMENITIES =====
st.subheader("🏡 Amenities & Location")

col5, col6, col7, col8, col9, col10 = st.columns(6)

def yes_no(label, column):
    return 1 if column.radio(label, ["Yes", "No"], horizontal=True) == "Yes" else 0

with col5:
    mainroad = yes_no("Main Road", col5)

with col6:
    guestroom = yes_no("Guest Room", col6)

with col7:
    basement = yes_no("Basement", col7)

with col8:
    hotwaterheating = yes_no("Hot Water Heating", col8)

with col9:
    airconditioning = yes_no("Air Conditioning", col9)

with col10:
    prefarea = yes_no("Preferred Area", col10)


# ===== PARKING & FURNISHING =====
st.subheader("🪑 Parking & Furnishing")

col11, col12 = st.columns(2)

with col11:
    parking = st.number_input("Parking Spaces", min_value=0, step=1)

with col12:
    furnishing_map = {
        "Furnished": 2,
        "Semi-Furnished": 1,
        "Unfurnished": 0
    }
    furnishingstatus = furnishing_map[
        st.selectbox("Furnishing Status", furnishing_map.keys())
    ]


st.divider()

# -------------------- PREDICTION --------------------
if st.button("💰 Predict House Price", use_container_width=True):
    response = requests.post(
        "https://house-prize-prediction-backend-production.up.railway.app/predict",
        json={
            "area": area,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "stories": stories,
            "mainroad": mainroad,
            "guestroom": guestroom,
            "basement": basement,
            "hotwaterheating": hotwaterheating,
            "airconditioning": airconditioning,
            "parking": parking,
            "prefarea": prefarea,
            "furnishingstatus": furnishingstatus
        }
    )

    if response.status_code == 200:
        predicted_price = response.json()["predicted_price"]
        st.success(f"🏷️ **Estimated House Price:** ₹ {predicted_price:,.0f}")
    else:
        st.error("❌ Prediction failed. Please check inputs.")
