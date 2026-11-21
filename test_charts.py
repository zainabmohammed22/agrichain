from pathlib import Path
import pandas as pd
from core.charts import (
    plot_consumption_line,
    plot_supply_vs_consumption,
    plot_quantity_hist,
    plot_two_products,
)

df = pd.read_csv("output/transactions_cleaned.csv")
out_dir = Path("output/charts")
out_dir.mkdir(parents=True, exist_ok=True)

charts = [
    plot_consumption_line(df, out_dir / "agrichain_consumption.png"),
    plot_supply_vs_consumption(df, out_dir / "agrichain_supply_vs_consumption.png"),
    plot_quantity_hist(df, out_dir / "agrichain_quantity_hist.png"),
    plot_two_products(df, out_dir / "agrichain_two_products.png"),
]

created = 0
for p in charts:
    if Path(p).exists():
        print(f"PASS - {p}")
        created += 1
    else:
        print(f"FAIL - {p}")

print(f"{created} of {len(charts)} charts created")
