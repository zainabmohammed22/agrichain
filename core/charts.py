import matplotlib.pyplot as plt

def plot_consumption_line(df, path, product="P01"):
    one = df[(df["product_id"] == product) & (df["type"] == "consumption")].head(15)
    plt.figure(figsize=(8, 4.5))
    plt.plot(one["date"], one["quantity"], marker="o")
    plt.xticks(rotation=45, ha="right")
    plt.title("Consumption of Product " + product)
    plt.xlabel("Date")
    plt.ylabel("Quantity")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path

def plot_supply_vs_consumption(df, path):
    totals = df.groupby("type")["quantity"].sum()
    plt.figure(figsize=(8, 4.5))
    plt.bar(totals.index, totals.values)
    plt.title("Supply vs Consumption")
    plt.xlabel("Transaction type")
    plt.ylabel("Total quantity")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path

def plot_quantity_hist(df, path, bins=5):
    plt.figure(figsize=(8, 4.5))
    plt.hist(df["quantity"], bins=bins)
    plt.title("Distribution of Quantities")
    plt.xlabel("Quantity")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path

def plot_two_products(df, path, a="P01", b="P04"):
    df_a = df[(df["product_id"] == a) & (df["type"] == "consumption")].head(15)
    df_b = df[(df["product_id"] == b) & (df["type"] == "consumption")].head(15)
    plt.figure(figsize=(8, 4.5))
    plt.plot(range(len(df_a)), df_a["quantity"], label=a)
    plt.plot(range(len(df_b)), df_b["quantity"], label=b)
    plt.title(f"Comparison: {a} vs {b}")
    plt.xlabel("Record")
    plt.ylabel("Quantity")
    plt.legend()
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path
