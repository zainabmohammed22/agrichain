import pandas as pd

df = pd.read_csv("data/AgriChain_edge_cases.csv")

print("Rows:", len(df))
print(df.isna().sum())
print(df["type"].unique().tolist())

df = df.dropna()
print("After missing:", len(df))

df = df[df["quantity"] > 0]
print("Positive quantities:", len(df))

df = df[df["type"].isin(["supply", "consumption"])]
print(df)