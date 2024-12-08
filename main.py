from src.data_cleaning import load_data, check_data_quality, clean_data
from src.eda import summary_statistics, time_series_analysis, correlation_analysis, wind_analysis
import pandas as pd

def main():
    # File paths
    file_paths = ["data/raw/benin-malanville.csv", "data/raw/sierraleone-bumbuna.csv", "data/raw/togo-dapaong_qc.csv"]
    datasets = []

    # Load datasets
    for file_path in file_paths:
        print(f"Loading {file_path}...")
        data = load_data(file_path)
        if data is not None:
            datasets.append(data)

    # Combine datasets if needed
    combined_data = pd.concat(datasets, ignore_index=True)

    # Data Quality Check
    check_data_quality(combined_data)

    # Clean Data
    print("Cleaning data...")
    cleaned_data = clean_data(combined_data)
    
    # Save cleaned data
    cleaned_data.to_csv("data/processed/cleaned_data.csv", index=False)
    print("Cleaned data saved at data/processed/cleaned_data.csv")

    # Exploratory Data Analysis (EDA)
    print("Performing EDA...")
    summary_statistics(cleaned_data)
    time_series_analysis(cleaned_data, ["GHI", "DNI", "DHI", "Tamb"])
    correlation_analysis(cleaned_data)
    wind_analysis(cleaned_data)

if __name__ == "__main__":
    main()
