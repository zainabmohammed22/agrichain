from pathlib import Path
import pandas as pd
import streamlit as st
from core.charts import (
    plot_consumption_line,
    plot_supply_vs_consumption,
    plot_quantity_hist,
    plot_two_products,
)
from core.analysis import stock_status

st.set_page_config(page_title="AgriChain - Inventory & Supply", layout="wide")
st.title("AgriChain — Inventory & Supply Dashboard")

# === STUDENT PART 1 START ===
st.subheader("1. The cleaned transactions")
df = pd.read_csv("output/transactions_cleaned.csv")
c1, c2, c3 = st.columns(3)
c1.metric("Rows", len(df))
c2.metric("Products", df["product_id"].nunique())
c3.metric("Total supply", round(float(df[df["type"] == "supply"]["quantity"].sum()), 1))
st.dataframe(df.head(10))
# === STUDENT PART 1 END ===

# === STUDENT PART 2 START ===
st.subheader("2. Charts from Lecture 4")
charts_dir = Path("output/charts")
charts_dir.mkdir(parents=True, exist_ok=True)
left, right = st.columns(2)
left.image(str(plot_supply_vs_consumption(df, charts_dir / "agrichain_supply_vs_consumption.png")))
right.image(str(plot_quantity_hist(df, charts_dir / "agrichain_quantity_hist.png")))
# === STUDENT PART 2 END ===

# === STUDENT PART 3 START ===
st.subheader("3. Interactive Product Views")
product_list = sorted(df["product_id"].dropna().unique().tolist())
product = st.selectbox("Product", product_list)
st.image(str(plot_consumption_line(df, charts_dir / "agrichain_consumption_selected.png", product=product)))

col_a, col_b = st.columns(2)
prod_a = col_a.selectbox("Product A", product_list, index=0)
prod_b = col_b.selectbox(
    "Product B",
    product_list,
    index=1 if len(product_list) > 1 else 0,
)
st.image(str(plot_two_products(df, charts_dir / "agrichain_two_products_selected.png", a=prod_a, b=prod_b)))
# === STUDENT PART 3 END ===

# === STUDENT PART 4 START ===
st.subheader("4. Stock Levels and Low-Stock Alerts")
products_path = Path("data/products.csv")
opening_path = Path("data/opening_stock.csv")
if products_path.exists() and opening_path.exists():
    products = pd.read_csv(products_path)
    opening = pd.read_csv(opening_path)
    table = stock_status(df, opening, products)
    days = st.slider("Warn when days left is below", min_value=1, max_value=90, value=20)
    needs = table[(table["status"] == "Low") | (table["days_left"] < days)]
    st.metric("Products needing attention", len(needs))
    if len(needs) > 0:
        st.warning("Products needing attention: " + ", ".join(needs["product_id"].astype(str).tolist()))
    st.dataframe(table)
    st.download_button(
        label="Download stock table (CSV)",
        data=table.to_csv(index=False).encode("utf-8"),
        file_name="stock_status.csv",
        mime="text/csv",
    )
else:
    st.info("Add data/products.csv and data/opening_stock.csv to enable the stock table.")
# === STUDENT PART 4 END ===
