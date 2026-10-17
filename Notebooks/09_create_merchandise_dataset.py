
from pathlib import Path
import pandas as pd

project_dir = Path(__file__).resolve().parent.parent
input_file = project_dir / "Data" / "Online_Retail_Cleaned.csv"

output_file = project_dir / "Data" / "Online_Retail_Merchandise.csv"
excluded_file = project_dir / "Data" / "Excluded_NonMerchandise_Transactions.csv"

df = pd.read_csv(
    input_file,
    dtype={"InvoiceNo": str, "StockCode": str},
    low_memory=False
)

# Identify transaction types that should not count as merchandise sales
non_merchandise_codes = {
    "DOT", "POST", "M", "C2", "BANK CHARGES"
}

code_mask = df["StockCode"].str.upper().isin(non_merchandise_codes)

description_mask = (
    df["Description"]
    .fillna("")
    .str.strip()
    .str.upper()
    .isin(["ADJUST BAD DEBT", "BANK CHARGES"])
)

exclude_mask = code_mask | description_mask

excluded = df.loc[exclude_mask].copy()
merchandise = df.loc[~exclude_mask].copy()

# Save both datasets
merchandise.to_csv(output_file, index=False)
excluded.to_csv(excluded_file, index=False)

print("=" * 55)
print("MERCHANDISE DATASET CREATED")
print("=" * 55)

print("\nBEFORE SEPARATING NON-MERCHANDISE TRANSACTIONS")
print("Rows:", len(df))
print("Revenue:", round(df["Revenue"].sum(), 2))

print("\nEXCLUDED FOR SEPARATE REVIEW")
print("Rows:", len(excluded))
print("Revenue:", round(excluded["Revenue"].sum(), 2))

print("\nMERCHANDISE-ONLY DATASET")
print("Rows:", len(merchandise))
print("Revenue:", round(merchandise["Revenue"].sum(), 2))
print("Unique products:", merchandise["StockCode"].nunique())
print("Countries:", merchandise["Country"].nunique())

print("\nFILES SAVED:")
print(output_file)
print(excluded_file)

print("\nNote: This is a working classification, not a final audit.")
print("Other unusual codes and gift vouchers may need further review.")
