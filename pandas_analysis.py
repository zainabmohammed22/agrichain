import pandas as pd

df = pd.read_csv("data/transactions.csv")
print(df.head())
print("Shape:", df.shape)
print(df.columns.tolist())

quantity = df["quantity"]
print("Average:", round(quantity.mean(), 1))
print("Highest:", quantity.max())
print("Lowest:", quantity.min())
# Task 3: Show describe() of the WHOLE table
print(df.describe())

# Task 4: Show the column type and shape of the table
print(df["type"].head(5))
print(df.shape)