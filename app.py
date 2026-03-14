import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

model = joblib.load(os.path.join(os.path.dirname(__file__), "house_price_model.pkl"))

st.title("House Price Prediction")

st.write("Enter house details")

# numeric inputs
area = st.number_input("Area (Square Feet)", min_value=300)
bedrooms = st.number_input("Number of Bedrooms", min_value=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1)
floors = st.number_input("Number of Floors", min_value=1)
year = st.number_input("Year Built", min_value=1900, max_value=2025)

# categorical inputs
location = st.selectbox("Location", ["Downtown","Suburban","Rural"])
condition = st.selectbox("Condition", ["Excellent","Good","Fair","Poor"])
garage = st.selectbox("Garage", ["Yes","No"])

if st.button("Predict Price"):

    data = pd.DataFrame({
        "Area":[area],
        "Bedrooms":[bedrooms],
        "Bathrooms":[bathrooms],
        "Floors":[floors],
        "YearBuilt":[year],
        "Location":[location],
        "Condition":[condition],
        "Garage":[garage]
    })

    data = pd.get_dummies(data)
    data = data.reindex(columns=model.feature_names_in_, fill_value=0)

    prediction = model.predict(data)

    price = prediction[0]   # define price here
    price_lakh = price / 100000

    st.success(f"Predicted Price: ₹{price:,.0f} (~{price_lakh:.2f} Lakhs)")