# Experiment No. 8: Data Visualizations - Charts, Graphs and Data Mapping

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

# Bar chart: sales by category
data.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Pie chart: sales by region
data.groupby("Region")["Sales"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales by Region")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Line chart: sales versus quantity
plt.plot(data["Quantity"], data["Sales"], marker="o")
plt.title("Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
