# Experiment No. 9: Basic Dashboards
# The following charts are examples of views that can be combined in a Tableau dashboard.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

data.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.tight_layout()
plt.show()

data.groupby("Region")["Sales"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales by Region")
plt.ylabel("")
plt.tight_layout()
plt.show()

plt.plot(data["Quantity"], data["Sales"], marker="o")
plt.title("Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# In Tableau, add the worksheets to a Dashboard and arrange them as required.
