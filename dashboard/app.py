import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import utils

# Set page title
st.title("MoonLight Energy Solutions Dashboard")

# Load data
data = utils.load_data("../data/processed/cleaned_data.csv")

# Sidebar filters
st.sidebar.header("Filters")
month_filter = st.sidebar.selectbox("Select Month", options=sorted(data['Timestamp'].dt.month.unique()))

# Apply filters
filtered_data = data[data['Timestamp'].dt.month == month_filter]

# EDA visualizations
st.subheader("Time Series Analysis")
utils.plot_time_series(filtered_data, ["GHI", "DNI", "DHI", "Tamb"])

st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(filtered_data.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)
