# Fashion Retail Analytics

## Project Overview
This project analyses an online retail transaction dataset using Python and MySQL to identify sales trends, top-performing products, and country-level revenue patterns.

The analysis focuses on data quality, merchandise sales, monthly revenue trends, and business insights that can support retail decision-making.

## Business Objectives
- Calculate total merchandise revenue and sales volume.
- Identify top-performing products by revenue.
- Analyse monthly sales trends.
- Compare revenue across countries.
- Calculate average order value by country.
- Measure each country's contribution to total revenue.

## Tools and Technologies
- **Python:** Data cleaning, validation, exploratory analysis, and visualisation.
- **Pandas:** Data manipulation and aggregation.
- **MySQL:** SQL-based sales analysis.
- **Matplotlib:** Charts and visualisations.
- **VS Code:** Development environment.

## Dataset
The project uses the UCI Online Retail dataset, containing transaction records from December 2010 to December 2011.

The merchandise dataset used for analysis contains:
- 522,573 transaction rows
- 19,775 unique invoices
- 3,914 case-sensitive stock codes
- 10,247,968.18 in total merchandise revenue, in the dataset's monetary units

The data was cleaned and reviewed before analysis. Certain non-merchandise transaction codes were excluded using a provisional classification.

## Key Findings
- Total merchandise revenue was 10,247,968.18.
- The United Kingdom contributed approximately 85.14% of total merchandise revenue.
- The Netherlands had the highest average revenue per invoice among the countries analysed, at 3,052.57.
- November 2011 was the highest-revenue month, at 1,452,115.98.
- REGENCY CAKESTAND 3 TIER was the top product by revenue, generating 174,156.54.

## SQL Analysis
The SQL analysis includes:
1. Total merchandise revenue
2. Monthly sales trend
3. Top 10 products by revenue
4. Top 10 countries by revenue
5. Average order value by country
6. Country contribution to total revenue

## Visualisations
Charts created for this project:
- Monthly merchandise revenue trend
- Top 10 products by revenue
- Top 10 countries by revenue

## Project Structure
- `Data/` — Source and processed datasets
- `Notebooks/` — Python analysis scripts
- `SQL/` — SQL sales analysis queries
- `Visuals/` — Charts and exported analysis results

## Limitations
- December 2011 contains data only through December 9.
- Country-level average order values can be skewed where invoice counts are small.
- The exclusion of non-merchandise transactions is based on a provisional code review and may require further validation.
- Revenue reflects the dataset's transaction values and should not be interpreted as profit.

## Conclusion
This project demonstrates an end-to-end retail analytics workflow, including data cleaning, exploratory analysis, visualisation, SQL querying, and translating results into business insights.
