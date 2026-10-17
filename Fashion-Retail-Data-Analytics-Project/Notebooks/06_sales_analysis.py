
from pathlib import Path
import pandas as pd

# Locate project folders
project_dir = Path(__file__).resolve().parent.parent
input_file = project_dir / "Data" / "Online_Retail_Cleaned.csv"

# Load cleaned dataset
df = pd.read_csv(input_file, parse_dates=["InvoiceDate"])

print("=" * 50)
print("ONLINE RETAIL SALES ANALYSIS")
print("=" * 50)

# 1. Overall sales summary
print("\n1. OVERALL SUMMARY")
print("Total transactions (rows):", len(df))
print("Total revenue:", round(df["Revenue"].sum(), 2))
print("Total quantity sold:", df["Quantity"].sum())
print("Unique products:", df["StockCode"].nunique())
print("Unique countries:", df["Country"].nunique())
print("Invoices:", df["InvoiceNo"].nunique())

# 2. Top 10 products by revenue
top_products = (
    df.groupby("Description", as_index=False)
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Quantity=("Quantity", "sum")
    )
    .sort_values("Total_Revenue", ascending=False)
    .head(10)
)

print("\n2. TOP 10 PRODUCTS BY REVENUE")
print(top_products.to_string(index=False))

# 3. Top 10 countries by revenue
country_sales = (
    df.groupby("Country", as_index=False)
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Invoice_Count=("InvoiceNo", "nunique")
    )
    .sort_values("Total_Revenue", ascending=False)
    .head(10)
)

print("\n3. TOP 10 COUNTRIES BY REVENUE")
print(country_sales.to_string(index=False))

# 4. Monthly revenue trend
df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

monthly_sales = (
    df.groupby("Month", as_index=False)
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Invoice_Count=("InvoiceNo", "nunique")
    )
    .sort_values("Month")
)

print("\n4. MONTHLY SALES TREND")
print(monthly_sales.to_string(index=False))

# 5. Save analysis tables
output_dir = project_dir / "Visuals"
output_dir.mkdir(exist_ok=True)

top_products.to_csv(output_dir / "top_10_products.csv", index=False)
country_sales.to_csv(output_dir / "top_10_countries.csv", index=False)
monthly_sales.to_csv(output_dir / "monthly_sales_trend.csv", index=False)

print("\n" + "=" * 50)
print("SALES ANALYSIS COMPLETE")
print("Analysis files saved in:", output_dir)
print("=" * 50)
