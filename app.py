import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="LogisChain AI",
    page_icon="🚚",
    layout="wide"
)

# Sidebar
st.sidebar.title("🚚 LogisChain AI")
st.sidebar.success("Navigation")

# Main Title
st.title("🚚 LogisChain AI Dashboard")

st.markdown("""
Welcome to the **LogisChain AI Dashboard**.

This project helps analyze:

- 📦 Shipments
- 📊 Inventory
- 💰 Financial Risk
- 🚛 Carrier Performance
- 🤖 AI Shipment Delay Prediction
""")

st.divider()

col1, col2, col3 = st.columns(3)

col1.metric("Shipments", "1000")
col2.metric("Products", "500")
col3.metric("Carriers", "5")

st.divider()

st.success("✅ Project setup completed successfully!")