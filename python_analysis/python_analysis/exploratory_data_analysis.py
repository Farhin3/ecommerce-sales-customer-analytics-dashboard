import pandas as pd

df = pd.read_csv("../data/Ecommerce_Sales_Data_2024_2025.csv")

# Total Sales
print("Total Sales:", df["Sales"].sum())

# Total Profit
print("Total Profit:", df["Profit"].sum())

# Sales by Category
print("\nSales by Category")
print(df.groupby("Category")["Sales"].sum())

# Profit by Category
print("\nProfit by Category")
print(df.groupby("Category")["Profit"].sum())

# Sales by Region
print("\nSales by Region")
print(df.groupby("Region")["Sales"].sum())
