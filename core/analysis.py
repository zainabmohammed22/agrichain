import pandas as pd

def stock_status(txns: pd.DataFrame, opening: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = txns.copy()
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0.0)
    signed = df.copy()
    signed["signed_qty"] = signed.apply(
        lambda r: r["quantity"] if str(r["type"]).strip().lower() == "supply" else -r["quantity"],
        axis=1,
    )
    net_flow = signed.groupby("product_id", as_index=False)["signed_qty"].sum().rename(columns={"signed_qty": "net_change"})

    daily_cons = (
        df[df["type"].astype(str).str.strip().str.lower() == "consumption"]
        .groupby("product_id")["quantity"]
        .mean()
        .rename("avg_daily_consumption")
    )

    out = products.merge(opening, on="product_id", how="left").merge(net_flow, on="product_id", how="left")
    out["opening_stock"] = pd.to_numeric(out["opening_stock"], errors="coerce").fillna(0.0)
    out["net_change"] = out["net_change"].fillna(0.0)
    out["current_stock"] = (out["opening_stock"] + out["net_change"]).round(2)

    out = out.merge(daily_cons, on="product_id", how="left")
    out["avg_daily_consumption"] = out["avg_daily_consumption"].fillna(0.0)
    out["days_left"] = out.apply(
        lambda r: round(r["current_stock"] / r["avg_daily_consumption"], 1) if r["avg_daily_consumption"] > 0 else 999.0,
        axis=1,
    )

    out["min_stock"] = pd.to_numeric(out["min_stock"], errors="coerce").fillna(0.0)
    out["status"] = out.apply(
        lambda r: "Low" if r["current_stock"] < r["min_stock"] else "OK",
        axis=1,
    )
    return out
