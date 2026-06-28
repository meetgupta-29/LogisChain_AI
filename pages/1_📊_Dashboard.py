import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("""
<style>
div[data-testid="metric-container"] {
    background-color: #1f2937;
    border: 2px solid #4CAF50;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.4);
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

st.title("📊 LogisChain AI Dashboard")

# Load Data
shipments = pd.read_csv("data/shipments.csv")
inventory = pd.read_csv("data/inventory.csv")
finance = pd.read_csv("data/finance.csv")
carriers = pd.read_csv("data/carriers.csv")

# Sidebar Filters
st.sidebar.header("🔍 Filters")

origin = st.sidebar.selectbox(
    "Origin",
    ["All"] + sorted(shipments["Origin"].unique().tolist())
)

carrier = st.sidebar.selectbox(
    "Carrier",
    ["All"] + sorted(shipments["Carrier"].unique().tolist())
)

risk = st.sidebar.selectbox(
    "Risk Level",
    ["All"] + sorted(shipments["Risk_Level"].unique().tolist())
)

filtered_df = shipments.copy()

if origin != "All":
    filtered_df = filtered_df[filtered_df["Origin"] == origin]

if carrier != "All":
    filtered_df = filtered_df[filtered_df["Carrier"] == carrier]

if risk != "All":
    filtered_df = filtered_df[filtered_df["Risk_Level"] == risk]

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

risk_counts = filtered_df["Risk_Level"].value_counts()

fig = px.bar(x=risk_counts.index, y=risk_counts.values)
st.plotly_chart(fig)

# Inventory Stock
st.subheader("📦 Inventory Stock")

st.write(inventory.columns)
st.dataframe(inventory.head())

# Financial Risk
st.subheader("💰 Financial Risk")

finance_risk = finance["Financial_Risk"].value_counts()

fig = px.pie(
    values=finance_risk.values,
    names=finance_risk.index,
    title="Financial Risk Distribution"
)

st.plotly_chart(fig, width="stretch")

# Carrier Ratings
st.subheader("🚛 Carrier Ratings")

st.dataframe(carriers)

st.divider()

st.download_button(
    label="📥 Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_shipments.csv",
    mime="text/csv"
)