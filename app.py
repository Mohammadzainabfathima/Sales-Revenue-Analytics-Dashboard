import streamlit as st
import pandas as pd
from src.data_processing import load_data, preprocess, summarize
from src.visualization import plot_revenue_trend, plot_top_products, plot_region_sales

st.title("📊 Sales & Revenue Analytics Dashboard")

uploaded_file = st.file_uploader("Upload sales CSV file", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)
    df = preprocess(df)

    st.subheader("Summary Metrics")
    summary = summarize(df)
    st.metric("Total Revenue", f"${summary['total_revenue']:.2f}")
    st.metric("Total Quantity Sold", summary['total_quantity'])
    st.metric("Unique Products", summary['unique_products'])

    st.subheader("Revenue Trend")
    st.plotly_chart(plot_revenue_trend(df))

    st.subheader("Top Products by Revenue")
    st.plotly_chart(plot_top_products(df))

    st.subheader("Revenue by Region")
    st.plotly_chart(plot_region_sales(df))

else:
    st.info("Please upload a CSV file to begin analysis.")
