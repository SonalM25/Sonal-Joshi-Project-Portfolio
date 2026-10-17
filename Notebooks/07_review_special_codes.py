
from pathlib import Path
import pandas as pd

# Locate the cleaned dataset
project_dir = Path(__file__).resolve().parent.parent
input_file = project_dir / "Data" / "Online_Retail_Cleaned.csv"

df = pd.read_csv(input_file, dtype={"InvoiceNo": str}, low_memory=False)

print("=" * 60)
print("SPECIAL TRANSACTION CODE REVIEW")
print("=" * 60)

# 1. Review the most common stock codes
print("\n1. TOP 30 STOCK CODES BY ROW COUNT")

stock_summary = (
    df.groupby("StockCode", dropna=False)
    .agg(
        Row_Count=("StockCode", "size"),
        Total_Revenue=("Revenue", "sum"),
        Description=("Description", "first")
    )
    .sort_values("Row_Count", ascending=False)
    .head(30)
    .reset_index()
)

print(stock_summary.to_string(index=False))

# 2. Search descriptions for possible non-merchandise entries
keywords = [
    "POSTAGE", "DOTCOM", "MANUAL", "DISCOUNT",
    "BANK CHARGES", "AMAZON", "FEE", "CARRIAGE",
    "ADJUST", "CRUK", "COMMISSION"
]

pattern = "|".join(keywords)

special_rows = df[
    df["Description"].fillna("").str.upper().str.contains(
        pattern, regex=True
    )
].copy()

print("\n2. POSSIBLE SPECIAL TRANSACTIONS")
print("Matching rows:", len(special_rows))

special_summary = (
    special_rows.groupby("Description", dropna=False)
    .agg(
        Row_Count=("Description", "size"),
        Total_Quantity=("Quantity", "sum"),
        Total_Revenue=("Revenue", "sum")
    )
    .sort_values("Total_Revenue", ascending=False)
    .reset_index()
)

print(special_summary.to_string(index=False))

# 3. Save results for review
output_dir = project_dir / "Visuals"
output_dir.mkdir(exist_ok=True)

stock_summary.to_csv(
    output_dir / "stock_code_review.csv", index=False
)
special_summary.to_csv(
    output_dir / "special_transaction_review.csv", index=False
)

print("\n3. FILES SAVED")
print("1. Visuals/stock_code_review.csv")
print("2. Visuals/special_transaction_review.csv")

print("\nReview complete. Do not remove flagged rows automatically.")
