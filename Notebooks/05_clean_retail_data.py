
from pathlib import Path
import pandas as pd

# Locate project folders
project_dir = Path(__file__).resolve().parent.parent
input_file = project_dir / "Data" / "Online Retail.xlsx"
output_file = project_dir / "Data" / "Online_Retail_Cleaned.csv"

# Load original dataset
df = pd.read_excel(input_file)

print("ORIGINAL DATASET")
print("Rows:", len(df))

# Step 1: Remove exact duplicate rows
duplicate_count = df.duplicated().sum()
df = df.drop_duplicates().copy()

print("\nExact duplicate rows removed:", duplicate_count)

# Step 2: Exclude cancelled invoices
cancelled_mask = df["InvoiceNo"].astype(str).str.startswith("C")
cancelled_count = cancelled_mask.sum()
df = df.loc[~cancelled_mask].copy()

print("Cancelled invoice rows excluded:", cancelled_count)

# Step 3: Keep positive quantities
negative_or_zero_quantity = (df["Quantity"] <= 0).sum()
df = df.loc[df["Quantity"] > 0].copy()

print("Rows with zero or negative quantities excluded:",
      negative_or_zero_quantity)

# Step 4: Keep positive unit prices
nonpositive_price_count = (df["UnitPrice"] <= 0).sum()
df = df.loc[df["UnitPrice"] > 0].copy()

print("Rows with zero or negative prices excluded:",
      nonpositive_price_count)

# Step 5: Exclude rows with missing descriptions
missing_description_count = df["Description"].isna().sum()
df = df.loc[df["Description"].notna()].copy()

print("Rows with missing descriptions excluded:",
      missing_description_count)

# Step 6: Exclude special transaction codes from merchandise analysis
special_codes = ["AMAZONFEE", "MANUAL", "DISCOUNT"]
special_mask = (
    df["StockCode"].astype(str).str.upper().isin(special_codes)
)

special_count = special_mask.sum()
df = df.loc[~special_mask].copy()

print("Special transaction rows excluded:", special_count)

# Step 7: Calculate line revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Step 8: Save cleaned dataset
df.to_csv(output_file, index=False)

print("\nCLEANING COMPLETE")
print("Cleaned rows:", len(df))
print("Cleaned columns:", len(df.columns))
print("Output file:", output_file)
print("Total merchandise revenue:", round(df["Revenue"].sum(), 2))
print("Unique countries:", df["Country"].nunique())
print("Missing customer IDs remaining:", df["CustomerID"].isna().sum())

print("\nFirst 5 cleaned rows:")
print(df.head())
