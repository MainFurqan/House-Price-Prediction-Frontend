import streamlit as st
import requests

st.title("New Delhi House Price Prediction")

# User inputs
area = st.number_input("Area (sqft)")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("bathrooms")
stories = st.number_input("stories")
mainroad = st.number_input("mainroad")
guestroom = st.number_input("guestroom")
basement = st.number_input("basement")
hotwaterheating = st.number_input("hotwaterheating")
airconditioning = st.number_input("airconditioning")
parking = st.number_input("parking")
prefarea = st.number_input("prefarea")
furnishingstatus = st.number_input("furnishingstatus")


if st.button("Predict Price"):
    # Send data to backend
    response = requests.post(
        "https://house-prize-prediction-backend-production.up.railway.app/predict",
        json={
            "area": area,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "stories" : stories,
            "mainroad" : mainroad,
            "guestroom" : guestroom,
            "basement" : basement,
            "hotwaterheating" : hotwaterheating,
            "airconditioning" : airconditioning,
            "parking" : parking,
            "prefarea" : prefarea,
            "furnishingstatus" : furnishingstatus
        }
    )
    if response.status_code == 200:
        predicted_price = response.json()["predicted_price"]
        st.success(f"Estimated House Price: {predicted_price:,.0f}")
    else:
        st.error("Prediction failed. Please check inputs.")
