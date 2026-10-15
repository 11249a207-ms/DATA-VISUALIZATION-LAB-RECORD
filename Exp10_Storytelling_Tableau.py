# Experiment No. 10: Storytelling in Tableau
# Aim: Present insights as a sequence of visualizations.
# This Python sample creates the chart views; arrange them as story points in Tableau.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

# Story Step 1: Category performance
category_sales = data.groupby("Category")["Sales"].sum()
category_sales.plot(kind="bar")
plt.title("Story 1: Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Story Step 2: Regional contribution
region_sales = data.groupby("Region")["Sales"].sum()
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Story 2: Regional Contribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Story Step 3: Relationship between quantity and sales
plt.plot(data["Quantity"], data["Sales"], marker="o")
plt.title("Story 3: Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# In Tableau Public, add these views as story points and write a caption for each.
