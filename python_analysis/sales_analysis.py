import pandas as pd

# Load dataset
df = pd.read_csv("Ecommerce_Sales_Data_2024_2025.csv")

print("Dataset Shape:", df.shape)
print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
