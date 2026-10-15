# Experiment No. 5: Connecting to Data and Preparing Data for Visualization
# Aim: Load, inspect, clean and save a CSV dataset.

import pandas as pd

data = pd.read_csv("sales_data.csv")
print("First five rows:")
print(data.head())

print("\nMissing values:")
print(data.isnull().sum())

data = data.drop_duplicates()
data["Sales"] = pd.to_numeric(data["Sales"], errors="coerce")
data = data.dropna(subset=["Sales"])
data.to_csv("cleaned_sales_data.csv", index=False)

print("\nData prepared successfully.")
