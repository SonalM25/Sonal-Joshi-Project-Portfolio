
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Locate project folders
project_dir = Path(__file__).resolve().parent.parent
input_file = project_dir / "Visuals" / "merchandise_top_products.csv"
output_file = project_dir / "Visuals" / "top_10_products_by_revenue.png"

# Load product analysis
df = pd.read_csv(input_file)

# Reverse order so the highest revenue appears at the top
df = df.sort_values("Total_Revenue", ascending=True)

# Create horizontal bar chart
plt.figure(figsize=(12, 7))

plt.barh(
    df["Description"],
    df["Total_Revenue"]
)

plt.title("Top 10 Products by Revenue", fontsize=15)
plt.xlabel("Revenue (dataset currency units)")
plt.ylabel("Product")

plt.tight_layout()

# Save chart
plt.savefig(output_file, dpi=300, bbox_inches="tight")

print("Top products chart saved successfully:")
print(output_file)

plt.show()
