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
    data = data.dropna(axis=1, how='all')

    # Fill missing numeric values with median
    for col in data.select_dtypes(include=[np.number]):
        data[col] = data[col].fillna(data[col].median())

    # Remove outliers using Z-scores for numeric columns
    z_scores = np.abs((data.select_dtypes(include=[np.number]) - data.mean()) / data.std())
    data = data[(z_scores < 3).all(axis=1)]
    
    return data
