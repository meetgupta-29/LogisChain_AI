import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

st.title("📊 LogisChain AI Dashboard")

# Load Data
shipments = pd.read_csv("data/shipments.csv")
inventory = pd.read_csv("data/inventory.csv")
finance = pd.read_csv("data/finance.csv")
carriers = pd.read_csv("data/carriers.csv")

# KPI Cards
st.subheader("📈 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Shipments", len(shipments))
col2.metric("Products", len(inventory))
col3.metric("Finance Records", len(finance))
col4.metric("Carriers", len(carriers))

st.divider()

# Shipment Risk Distribution
st.subheader("🚚 Shipment Risk Distribution")

risk_counts = shipments["Risk_Level"].value_counts()

st.bar_chart(risk_counts)

st.divider()

# Inventory Stock
st.subheader("📦 Inventory Stock")

stock = inventory.groupby("Warehouse")["Stock"].sum()

st.bar_chart(stock)

st.divider()

# Financial Risk
st.subheader("💰 Financial Risk")

finance_risk = finance["Financial_Risk"].value_counts()

st.bar_chart(finance_risk)

st.divider()

# Carrier Ratings
st.subheader("🚛 Carrier Ratings")

st.dataframe(carriers)