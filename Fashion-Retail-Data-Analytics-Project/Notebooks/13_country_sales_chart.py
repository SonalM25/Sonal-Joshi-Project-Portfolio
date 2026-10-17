
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Locate project folders
project_dir = Path(__file__).resolve().parent.parent
input_file = project_dir / "Visuals" / "merchandise_country_sales.csv"
output_file = project_dir / "Visuals" / "top_10_countries_by_revenue.png"

# Load country sales results
df = pd.read_csv(input_file)

# Select the top 10 countries by revenue
df = (
    df.sort_values("Total_Revenue", ascending=False)
    .head(10)
    .sort_values("Total_Revenue", ascending=True)
)

# Create horizontal bar chart
plt.figure(figsize=(10, 6))

plt.barh(
    df["Country"],
    df["Total_Revenue"]
)

plt.title("Top 10 Countries by Merchandise Revenue", fontsize=14)
plt.xlabel("Revenue (dataset currency units)")
plt.ylabel("Country")

plt.tight_layout()

# Save chart
plt.savefig(output_file, dpi=300, bbox_inches="tight")

print("Country sales chart saved successfully:")
print(output_file)

plt.show()
