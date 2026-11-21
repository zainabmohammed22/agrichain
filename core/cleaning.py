import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df = df[df["quantity"] > 0]
    df = df[df["type"].isin(["supply", "consumption"])]
    return df
