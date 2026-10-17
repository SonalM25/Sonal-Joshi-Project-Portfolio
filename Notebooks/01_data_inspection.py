
from pathlib import Path
import pandas as pd

# Locate the project folder
project_dir = Path(__file__).resolve().parent.parent
file_path = project_dir / "Data" / "Online Retail.xlsx"

# Load the Excel dataset
df = pd.read_excel(file_path)

print("Dataset loaded successfully!")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values by column:")
print(df.isnull().sum())
