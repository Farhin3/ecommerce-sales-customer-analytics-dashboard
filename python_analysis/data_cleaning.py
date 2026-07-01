import pandas as pd

# Load dataset
df = pd.read_csv("../data/Ecommerce_Sales_Data_2024_2025.csv")

# Dataset overview
print("Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Data types
print("\nData Types:")
print(df.dtypes)
