
from pathlib import Path
import pandas as pd

project_dir = Path(__file__).resolve().parent.parent
input_file = project_dir / "Data" / "Online_Retail_Merchandise.csv"

df = pd.read_csv(
    input_file,
    parse_dates=["InvoiceDate"],
    dtype={"InvoiceNo": str, "StockCode": str},
    low_memory=False
)

print("=" * 55)
print("MERCHANDISE SALES ANALYSIS")
print("=" * 55)

# 1. Overall summary
print("\n1. OVERALL SUMMARY")
print("Rows analysed:", len(df))
print("Merchandise revenue:", round(df["Revenue"].sum(), 2))
print("Quantity sold:", df["Quantity"].sum())
print("Unique stock codes:", df["StockCode"].nunique())
print("Countries:", df["Country"].nunique())
print("Unique invoices:", df["InvoiceNo"].nunique())

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

# 3. Country sales
country_sales = (
    df.groupby("Country", as_index=False)
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Invoice_Count=("InvoiceNo", "nunique")
    )
    .sort_values("Total_Revenue", ascending=False)
)

print("\n3. TOP 10 COUNTRIES BY REVENUE")
print(country_sales.head(10).to_string(index=False))

# 4. Monthly trend
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

print("\n4. MONTHLY MERCHANDISE REVENUE")
print(monthly_sales.to_string(index=False))

# 5. Save results
output_dir = project_dir / "Visuals"
output_dir.mkdir(exist_ok=True)

top_products.to_csv(
    output_dir / "merchandise_top_products.csv", index=False
)
country_sales.to_csv(
    output_dir / "merchandise_country_sales.csv", index=False
)
monthly_sales.to_csv(
    output_dir / "merchandise_monthly_sales.csv", index=False
)

print("\nAnalysis files saved in:", output_dir)
print("MERCHANDISE SALES ANALYSIS COMPLETE")
