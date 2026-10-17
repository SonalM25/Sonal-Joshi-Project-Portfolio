
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Locate the project folders
project_dir = Path(__file__).resolve().parent.parent
input_file = project_dir / "Visuals" / "merchandise_monthly_sales.csv"
output_file = project_dir / "Visuals" / "monthly_merchandise_revenue.png"

# Load monthly sales results
df = pd.read_csv(input_file)

# Create the chart
plt.figure(figsize=(12, 6))

plt.plot(
    df["Month"],
    df["Total_Revenue"],
    marker="o",
    linewidth=2
)

plt.title("Monthly Merchandise Revenue Trend", fontsize=15)
plt.xlabel("Month", fontsize=11)
plt.ylabel("Revenue (dataset currency units)", fontsize=11)

plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

# Save chart
plt.savefig(output_file, dpi=300, bbox_inches="tight")

print("Monthly revenue chart saved successfully:")
print(output_file)

# Display chart
plt.show()
