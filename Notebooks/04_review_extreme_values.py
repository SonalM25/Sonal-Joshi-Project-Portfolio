
from pathlib import Path
import pandas as pd

project_dir = Path(__file__).resolve().parent.parent
file_path = project_dir / "Data" / "Online Retail.xlsx"

df = pd.read_excel(file_path)

# 1. Check negative unit prices
negative_prices = df[df["UnitPrice"] < 0]

print("1. NEGATIVE UNIT PRICE RECORDS")
print("Total:", len(negative_prices))
print(negative_prices.head(10).to_string(index=False))

# 2. Check zero unit prices
zero_prices = df[df["UnitPrice"] == 0]

print("\n2. ZERO UNIT PRICE RECORDS")
print("Total:", len(zero_prices))
print(zero_prices.head(10).to_string(index=False))

# 3. Check unusually large quantities
extreme_quantities = df[df["Quantity"].abs() > 10000]

print("\n3. RECORDS WITH ABSOLUTE QUANTITY ABOVE 10,000")
print("Total:", len(extreme_quantities))
print(extreme_quantities.head(10).to_string(index=False))

# 4. Check unusually high positive unit prices
high_prices = df[df["UnitPrice"] > 1000]

print("\n4. RECORDS WITH UNIT PRICE ABOVE 1,000")
print("Total:", len(high_prices))
print(high_prices.head(10).to_string(index=False))

print("\nReview complete. Original data has not been changed.")
