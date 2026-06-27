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

# INVENTORY DATASET

products = [
    "Laptop", "Mobile", "Tablet", "Monitor",
    "Printer", "Keyboard", "Mouse", "Smart Watch"
]

warehouses = [
    "Mumbai", "Delhi", "Bengaluru",
    "Hyderabad", "Chennai"
]

inventory_data = []

for i in range(1, 501):

    stock = random.randint(50, 1000)
    demand = random.randint(30, 900)
    safety_stock = random.randint(20, 100)

    inventory_data.append({
        "Product_ID": f"P{i:04}",
        "Product_Name": random.choice(products),
        "Warehouse": random.choice(warehouses),
        "Stock": stock,
        "Demand": demand,
        "Safety_Stock": safety_stock,
        "Reorder_Level": safety_stock + 30
    })

inventory_df = pd.DataFrame(inventory_data)

inventory_df.to_csv("data/inventory.csv", index=False)

print("\nInventory dataset created successfully!")
print(inventory_df.head())


# FINANCE DATASET

companies = [
    "Samsung", "Apple", "Dell", "HP",
    "Lenovo", "Sony", "LG", "Asus"
]

finance_data = []

for i in range(1, 301):

    revenue = random.randint(500000, 5000000)

    expenses = random.randint(200000, revenue)

    working_capital = revenue - expenses

    credit_score = random.randint(600, 900)

    if credit_score >= 800:
        risk = "Low"
    elif credit_score >= 700:
        risk = "Medium"
    else:
        risk = "High"

    finance_data.append({

        "Company": random.choice(companies),

        "Revenue": revenue,

        "Expenses": expenses,

        "Working_Capital": working_capital,

        "Credit_Score": credit_score,

        "Financial_Risk": risk

    })

finance_df = pd.DataFrame(finance_data)

finance_df.to_csv("data/finance.csv", index=False)

print("\nFinance dataset created successfully!")

print(finance_df.head())


# CARRIER DATASET

carrier_data = []

for carrier in carriers:

    carrier_data.append({

        "Carrier": carrier,

        "On_Time_Percentage": random.randint(80,99),

        "Average_Delay": round(random.uniform(0.5,5),2),

        "Completed_Shipments": random.randint(1000,10000),

        "Rating": round(random.uniform(3.5,5.0),1)

    })

carrier_df = pd.DataFrame(carrier_data)

carrier_df.to_csv("data/carriers.csv", index=False)

print("\nCarrier dataset created successfully!")

print(carrier_df)