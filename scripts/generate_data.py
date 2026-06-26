import pandas as pd
import random
from datetime import datetime, timedelta


# Sample Data

suppliers = [
    "Samsung",
    "Apple",
    "Dell",
    "HP",
    "Lenovo",
    "Sony",
    "LG",
    "Asus"
]

origins = [
    "Mumbai",
    "Delhi",
    "Chennai",
    "Hyderabad",
    "Kolkata"
]

destinations = [
    "Pune",
    "Bengaluru",
    "Ahmedabad",
    "Jaipur",
    "Lucknow"
]

carriers = [
    "DHL",
    "FedEx",
    "Blue Dart",
    "Delhivery",
    "UPS"
]

weather_conditions = [
    "Clear",
    "Rain",
    "Storm",
    "Fog"
]

risk_levels = [
    "Low",
    "Medium",
    "High"
]


# Generate Shipment Records

shipment_data = []

for i in range(1, 1001):

    shipment_date = datetime(2026, 1, 1) + timedelta(days=random.randint(0,180))

    expected_delivery = shipment_date + timedelta(days=random.randint(2,7))

    delay = random.randint(0,5)

    actual_delivery = expected_delivery + timedelta(days=delay)

    shipment_data.append({

        "Shipment_ID": f"SHP{i:04}",

        "Supplier": random.choice(suppliers),

        "Origin": random.choice(origins),

        "Destination": random.choice(destinations),

        "Carrier": random.choice(carriers),

        "Distance_km": random.randint(100,2500),

        "Weather": random.choice(weather_conditions),

        "Shipment_Date": shipment_date.date(),

        "Expected_Delivery": expected_delivery.date(),

        "Actual_Delivery": actual_delivery.date(),

        "Delay_Days": delay,

        "Risk_Level": random.choice(risk_levels)

    })


# Create DataFrame

shipment_df = pd.DataFrame(shipment_data)

shipment_df.to_csv("data/shipments.csv", index=False)

print("Shipment dataset created successfully!")
print(shipment_df.head())