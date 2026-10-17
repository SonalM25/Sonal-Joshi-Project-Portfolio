
from pathlib import Path
import pandas as pd

# Find the project folder
project_dir = Path(__file__).resolve().parent.parent
file_path = project_dir / "Data" / "Online Retail.xlsx"

# Load the original dataset
df = pd.read_excel(file_path)

print("DATA QUALITY INVESTIGATION")
print("=" * 40)

# 1. Investigate cancelled invoices
cancelled = df[
    df["InvoiceNo"].astype(str).str.startswith("C")
]

print("\n1. Cancelled invoice examples:")
print(cancelled.head(10).to_string(index=False))
print("Total cancelled invoice rows:", len(cancelled))

# 2. Investigate zero or negative prices
unusual_prices = df[df["UnitPrice"] <= 0]

print("\n2. Zero or negative price examples:")
print(unusual_prices.head(10).to_string(index=False))
print("Total rows with zero or negative prices:", len(unusual_prices))

# 3. Investigate negative quantities
negative_quantities = df[df["Quantity"] < 0]

print("\n3. Negative quantity examples:")
print(negative_quantities.head(10).to_string(index=False))
print("Total rows with negative quantities:", len(negative_quantities))

# 4. Summarise quantities and prices
print("\n4. Quantity and price summary:")
print(df[["Quantity", "UnitPrice"]].describe())

print("\nInvestigation complete.")
