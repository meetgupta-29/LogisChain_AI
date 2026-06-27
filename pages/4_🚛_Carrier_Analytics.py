import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Carrier Analytics", page_icon="🚛")

st.title("🚛 Carrier Analytics")

df = pd.read_csv("data/carriers.csv")

st.subheader("Carrier Performance")

st.dataframe(df)

st.subheader("On-Time Delivery %")

fig = px.bar(
    df,
    x="Carrier",
    y="On_Time_Percentage",
    color="Rating"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Average Delay")

fig2 = px.bar(
    df,
    x="Carrier",
    y="Average_Delay",
    color="Rating"
)

st.plotly_chart(fig2, use_container_width=True)