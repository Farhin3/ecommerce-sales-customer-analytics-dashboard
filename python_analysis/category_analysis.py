import pandas as pd

df = pd.read_csv("../data/Ecommerce_Sales_Data_2024_2025.csv")

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values()
)

print(category_profit)
