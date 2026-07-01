import pandas as pd

df = pd.read_csv("../data/Ecommerce_Sales_Data_2024_2025.csv")

top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(top_customers.head(120))
