import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Shipment Prediction", page_icon="🚚")

st.title("🚚 Shipment Delay Prediction")

saved = joblib.load("models/shipment_model.pkl")

model = saved["model"]
encoders = saved["encoders"]

st.subheader("Enter Shipment Details")

supplier = st.selectbox(
    "Supplier",
    ["Asus", "Lenovo", "Samsung", "Apple", "LG", "Dell", "HP", "Sony"]
)

origin = st.selectbox(
    "Origin",
    ["Mumbai", "Hyderabad", "Delhi", "Kolkata", "Chennai"]
)

destination = st.selectbox(
    "Destination",
    ["Pune", "Ahmedabad", "Jaipur", "Bengaluru", "Lucknow"]
)

carrier = st.selectbox(
    "Carrier",
    ["DHL", "FedEx", "Blue Dart", "Delhivery", "UPS"]
)

distance = st.number_input("Distance (km)", 100, 3000, 1000)

weather = st.selectbox(
    "Weather",
    ["Fog","Clear","Storm","Rain"]
)

risk = st.selectbox("Risk Level", ["Low", "Medium", "High"])

if st.button("Predict Delay"):
    # Encode categorical variables
    supplier_encoded = encoders["Supplier"].transform([supplier])[0]
    origin_encoded = encoders["Origin"].transform([origin])[0]
    destination_encoded = encoders["Destination"].transform([destination])[0]
    carrier_encoded = encoders["Carrier"].transform([carrier])[0]
    weather_encoded = encoders["Weather"].transform([weather])[0]
    risk_encoded = encoders["Risk_Level"].transform([risk])[0]

    prediction = model.predict([[supplier_encoded, origin_encoded, destination_encoded, carrier_encoded, distance, weather_encoded, risk_encoded]])
    st.success(f"Estimated Delay: {prediction[0]:.2f} Days")

st.divider()

st.subheader("Shipment Dataset")
df = pd.read_csv("data/shipments.csv")
st.dataframe(df.head(20))