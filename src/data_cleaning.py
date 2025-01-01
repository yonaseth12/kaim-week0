import pandas as pd
import numpy as np

def load_data(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return None

def check_data_quality(data):
    """
    Check for missing values, duplicates, and invalid entries.
    """
    print("Data Quality Report:")
    print(f"Shape of Data: {data.shape}")
    print(f"Missing Values:\n{data.isnull().sum()}")
    print(f"Duplicate Rows: {data.duplicated().sum()}")

def clean_data(data):
    """
    Handle missing values, outliers, and invalid entries.
    """
    # Drop entirely null columns like 'Comments'
    data = data.dropna(axis=1, how='all').copy()

    # Select numeric columns
    numeric_cols = data.select_dtypes(include=[np.number])

    # Fill missing numeric values with median
    for col in numeric_cols.columns:
        data.loc[:, col] = data[col].fillna(numeric_cols[col].median())

    # Remove outliers using Z-scores for numeric columns
    z_scores = (numeric_cols - numeric_cols.mean()) / numeric_cols.std()
    filtered_indices = (np.abs(z_scores) < 3).all(axis=1)
    data = data.loc[filtered_indices].copy()

    return data
