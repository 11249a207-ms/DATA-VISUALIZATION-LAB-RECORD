# Experiment No. 6: Data Aggregation and Statistical Functions
# Aim: Calculate summary statistics and aggregate sales data.

import pandas as pd

data = pd.read_csv("sales_data.csv")

print("Summary statistics:")
print(data[["Sales", "Quantity"]].describe())

print("\nTotal sales by category:")
print(data.groupby("Category")["Sales"].sum())

print("\nAverage sales by region:")
print(data.groupby("Region")["Sales"].mean())

print("\nTotal sales by region:")
print(data.groupby("Region")["Sales"].sum())
