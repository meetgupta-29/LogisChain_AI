import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Finance Analytics", page_icon="💰")

st.title("💰 Finance Analytics")

df = pd.read_csv("data/finance.csv")

st.subheader("Financial Dataset")
st.dataframe(df)

st.subheader("Revenue by Company")

fig = px.bar(
    df,
    x="Company",
    y="Revenue",
    color="Financial_Risk"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Working Capital")

fig2 = px.bar(
    df,
    x="Company",
    y="Working_Capital",
    color="Financial_Risk"
)

st.plotly_chart(fig2, use_container_width=True)