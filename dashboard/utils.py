import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from windrose import WindroseAxes

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

def plot_correlation_heatmap(data):
    """Plot a correlation heatmap of numerical data."""
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    ax.set_title("Correlation Heatmap")
    st.pyplot(fig)

def plot_histogram(data, column):
    """Plot a histogram for a selected column."""
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(data[column], kde=True, bins=30, color='skyblue')
    ax.set_title(f"Distribution of {column}")
    st.pyplot(fig)

def plot_wind_rose(data):
    """Plot a wind rose using wind speed and direction."""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax = WindroseAxes.from_ax()
    ax.bar(data['WD'], data['WS'], normed=True, opening=0.8, edgecolor='white')
    ax.set_title("Wind Rose")
    st.pyplot(fig)
