import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import utils

# Page setup
st.set_page_config(page_title="MoonLight Energy Solutions Dashboard", layout="wide")
st.title("🌞 MoonLight Energy Solutions Dashboard")

# Load data
data = utils.load_data("../data/processed/cleaned_data.csv")

# Sidebar filters
st.sidebar.header("Filters")
month_filter = st.sidebar.selectbox("Select Month", options=sorted(data['Timestamp'].dt.month.unique()))
variables_filter = st.sidebar.multiselect("Select Variables for Analysis", options=data.columns[1:], default=["GHI", "DNI", "DHI", "Tamb"])

# Apply filters
filtered_data = data[data['Timestamp'].dt.month == month_filter]

# Time Series Analysis
st.subheader("📈 Time Series Analysis")
if variables_filter:
    utils.plot_time_series(filtered_data, variables_filter)

# Correlation Heatmap
st.subheader("📊 Correlation Heatmap")
utils.plot_correlation_heatmap(filtered_data)

# Histograms
st.subheader("📂 Distribution Analysis")
selected_hist_column = st.selectbox("Select Variable for Histogram", options=data.columns[1:])
if selected_hist_column:
    utils.plot_histogram(filtered_data, selected_hist_column)

# Wind Rose Plot
st.subheader("🌬️ Wind Analysis")
if "WS" in data.columns and "WD" in data.columns:
    utils.plot_wind_rose(filtered_data)

# Insights and Recommendations
st.subheader("📌 Insights and Recommendations")
st.text("""
- High correlation between solar radiation components and temperature.
- Patterns observed in wind speed and direction.
- Peak solar irradiance during midday; consider installation efficiency around these times.
""")
