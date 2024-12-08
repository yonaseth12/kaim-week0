import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def load_data(file_path):
    """Load cleaned data for the dashboard."""
    data = pd.read_csv(file_path)
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    return data

def plot_time_series(data, columns):
    """Plot time series data for specified columns."""
    fig, ax = plt.subplots(figsize=(10, 6))
    for col in columns:
        ax.plot(data['Timestamp'], data[col], label=col)
    ax.set_title("Time Series Data")
    ax.set_xlabel("Timestamp")
    ax.legend()
    st.pyplot(fig)
