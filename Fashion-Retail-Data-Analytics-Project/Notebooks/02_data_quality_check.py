
from pathlib import Path
import pandas as pd

project_dir = Path(__file__).resolve().parent.parent
file_path = project_dir / "Data" / "Online Retail.xlsx"

df = pd.read_excel(file_path)

print("1. Duplicate rows:", df.duplicated().sum())

print("\n2. Cancelled invoices:",
      df["InvoiceNo"].astype(str).str.startswith("C").sum())

print("\n3. Negative quantities:", (df["Quantity"] < 0).sum())

print("\n4. Zero or negative prices:",
      (df["UnitPrice"] <= 0).sum())

print("\n5. Transaction date range:")
print("Start:", df["InvoiceDate"].min())
print("End:", df["InvoiceDate"].max())

print("\n6. Countries represented:", df["Country"].nunique())

print("\n7. Top 10 countries by number of records:")
print(df["Country"].value_counts().head(10))
