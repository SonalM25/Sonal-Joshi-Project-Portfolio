
from pathlib import Path
import pandas as pd

project_dir = Path(__file__).resolve().parent.parent
input_file = project_dir / "Data" / "Online_Retail_Cleaned.csv"

df = pd.read_csv(
    input_file,
    dtype={"InvoiceNo": str, "StockCode": str},
    low_memory=False
)

print("=" * 65)
print("SPECIAL STOCK CODE INVESTIGATION")
print("=" * 65)

# Stock codes identified for closer review
codes_to_check = [
    "POST", "DOT", "M", "BANK CHARGES",
    "AMAZONFEE", "CRUK", "C2", "D"
]

# 1. Summarise selected stock codes
print("\n1. SELECTED STOCK CODES")

selected = df[
    df["StockCode"].str.upper().isin(codes_to_check)
].copy()

if selected.empty:
    print("No matching stock codes found.")
else:
    code_summary = (
        selected.groupby("StockCode", dropna=False)
        .agg(
            Rows=("StockCode", "size"),
            Revenue=("Revenue", "sum"),
            Quantity=("Quantity", "sum"),
            Descriptions=("Description", "nunique")
        )
        .sort_values("Revenue", ascending=False)
        .reset_index()
    )
    print(code_summary.to_string(index=False))

# 2. Investigate Manual descriptions separately
print("\n2. MANUAL DESCRIPTION DETAILS")

manual = df[
    df["Description"].fillna("").str.strip().str.upper()
    == "MANUAL"
].copy()

if manual.empty:
    print("No exact MANUAL descriptions found.")
else:
    manual_summary = (
        manual.groupby("StockCode", dropna=False)
        .agg(
            Rows=("StockCode", "size"),
            Revenue=("Revenue", "sum"),
            Quantity=("Quantity", "sum")
        )
        .sort_values("Revenue", ascending=False)
        .reset_index()
    )
    print(manual_summary.to_string(index=False))

# 3. Show examples for closer inspection
print("\n3. SAMPLE SPECIAL TRANSACTIONS")

examples = df[
    df["StockCode"].str.upper().isin(codes_to_check)
    | df["Description"].fillna("").str.upper().isin(
        ["MANUAL", "ADJUST BAD DEBT", "BANK CHARGES"]
    )
]

columns_to_show = [
    "InvoiceNo", "StockCode", "Description",
    "Quantity", "UnitPrice", "Revenue", "Country"
]

print(examples[columns_to_show].head(25).to_string(index=False))

# 4. Save results
output_dir = project_dir / "Visuals"
output_dir.mkdir(exist_ok=True)

if not selected.empty:
    code_summary.to_csv(
        output_dir / "selected_stock_code_summary.csv",
        index=False
    )

if not manual.empty:
    manual_summary.to_csv(
        output_dir / "manual_description_summary.csv",
        index=False
    )

print("\nInvestigation complete.")
print("Review the tables before deciding which rows to exclude.")
