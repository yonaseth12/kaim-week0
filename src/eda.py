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

def pairplot_analysis(data):
    selected_columns = ['GHI', 'DNI', 'DHI', 'WS', 'TModA', 'TModB']
    sns.pairplot(data[selected_columns], diag_kind='kde', plot_kws={'alpha':0.5})
    plt.suptitle("Pairwise Relationship of Variables", y=1.02)
    plt.show()

def distribution_analysis(data):
    selected_columns = ['GHI', 'DNI', 'DHI', 'WS', 'TModA', 'TModB']
    for col in selected_columns:
        plt.figure(figsize=(8, 6))
        plt.hist(data[col].dropna(), bins=30, color='skyblue', edgecolor='black', alpha=0.7)
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.show()


def boxplot_analysis(data):
    selected_columns = ['GHI', 'DNI', 'DHI', 'WS', 'TModA', 'TModB']
    for col in selected_columns:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=data[col], color='lightgreen')
        plt.title(f"Boxplot of {col}")
        plt.xlabel(col)
        plt.show()

def missing_data_analysis(data):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.isnull(), cbar=False, cmap="viridis", yticklabels=False)
    plt.title("Missing Data Heatmap")
    plt.show()

def facet_grid_analysis(data):
    g = sns.FacetGrid(data, col="Cleaning", height=6)
    g.map(sns.lineplot, "Timestamp", "GHI", color="blue")
    g.set_axis_labels("Timestamp", "GHI (W/m²)")
    plt.suptitle("GHI over Time Grouped by Cleaning Status", y=1.02)
    plt.show()

def pairwise_correlation_analysis(data):
    corr = data[['GHI', 'DNI', 'TModA', 'WS']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title("Correlation Matrix of Key Variables")
    plt.show()