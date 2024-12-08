import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def summary_statistics(data):
    """
    Display summary statistics for numerical columns.
    """
    print("Summary Statistics:")
    print(data.describe())

def time_series_analysis(data, columns, time_column="Timestamp"):
    """
    Plot time series data for selected columns.
    """
    data[time_column] = pd.to_datetime(data[time_column])
    data = data.set_index(time_column)
    data[columns].plot(subplots=True, figsize=(10, 8), title="Time Series Analysis")
    plt.tight_layout()
    plt.show()

def correlation_analysis(data):
    """
    Visualize correlations between numeric features using a heatmap.
    """
    corr = data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()

def wind_analysis(data):
    """
    Generate a wind rose plot (uses matplotlib).
    """
    from windrose import WindroseAxes
    ax = WindroseAxes.from_ax()
    ax.bar(data['WD'], data['WS'], normed=True, opening=0.8, edgecolor='white')
    ax.set_title("Wind Rose")
    plt.show()
