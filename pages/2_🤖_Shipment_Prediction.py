import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Shipment Prediction", page_icon="🚚")

st.title("🚚 Shipment Delay Prediction")

model = joblib.load("models/shipment_model.pkl")

st.subheader("Enter Shipment Details")

distance = st.number_input("Distance (km)", 100, 3000, 1000)
previous_delay = st.number_input("Previous Delay (Days)", 0, 10, 2)

if st.button("Predict Delay"):
    prediction = model.predict([[distance, previous_delay]])
    st.success(f"Estimated Delay: {prediction[0]:.2f} Days")

st.divider()

st.subheader("Shipment Dataset")
df = pd.read_csv("data/shipments.csv")
st.dataframe(df.head(20))