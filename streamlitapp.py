import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Shopping Data Dashboard")

csv_file = "shopping_behavior_updated.csv"

try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    st.error(f"File not found: {csv_file}. Please check the file path.")
    st.stop()  # Stop execution here

# Debug: show all column names so you can confirm 'Category' exists exactly in the data
st.write("Columns found in data:", df.columns.tolist())

if 'Category' not in df.columns:
    st.error("Error: Column 'Category' not found in dataset. Please check spelling and capitalization.")
    st.stop()  # Stop execution here if column is missing

# Now we can safely create categories list
categories = df['Category'].dropna().unique()
selected_category = st.selectbox("Select Category", options=["All"] + list(categories))

if selected_category != "All":
    df = df[df['Category'] == selected_category]

st.write(f"Filtered records: {len(df)}")
st.dataframe(df)

chart_data = df.groupby('Category')['Purchase Amount (USD)'].sum().reset_index()
fig = px.bar(chart_data, x='Category', y='Purchase Amount (USD)', title='Total Purchase Amount by Category')
st.plotly_chart(fig)

# Retail Customer Insights Dashboard

## Project Summary

This project presents an interactive data analytics dashboard built with Streamlit to analyze retail customer shopping behavior. It leverages real transactional data, including product categories (e.g., blouse, footwear), purchase locations, payment modes, and customer preferences.

The dashboard enables users to filter and explore the dataset by various dimensions to uncover shopping patterns and trends. Visualizations provide actionable insights for retail businesses, e-commerce platforms, and marketers aiming to optimize their product offerings, targeted campaigns, and customer experience.

## Project Description

This data dashboard project focuses on retail customer behavior analysis using real-world transactional data. The key features include:

- Loading and cleaning shopping behavior data from CSV files.  
- Interactive filters for product categories, location, and payment methods.  
- Data tables displaying detailed transaction records after filtering.  
- Visual charts (bar charts, pie charts) showing purchase trends by category and payment methods.  
- Insights that help retail companies understand customer preferences, regional buying patterns, and payment habits.

This project demonstrates practical skills in Python data processing, Streamlit app development, and data visualization with Plotly, designed to support data-driven decision-making in retail and consumer goods sectors.
