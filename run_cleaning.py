from pathlib import Path
import pandas as pd
from core.cleaning import clean_data

Path("output").mkdir(exist_ok=True)

real_df = pd.read_csv("data/transactions.csv")
clean_real = clean_data(real_df)
print(f"real file: {len(real_df)} rows -> {len(clean_real)} rows after cleaning")
clean_real.to_csv("output/transactions_cleaned.csv", index=False)

edge_df = pd.read_csv("data/AgriChain_edge_cases.csv")
clean_edge = clean_data(edge_df)
print(f"test file: {len(edge_df)} rows -> {len(clean_edge)} rows after cleaning")
clean_edge.to_csv("output/AgriChain_edge_cases_cleaned.csv", index=False)

print("Saved the cleaned files in the output folder")
