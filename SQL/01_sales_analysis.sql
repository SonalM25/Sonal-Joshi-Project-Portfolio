


-- Query 1: Calculate total merchandise revenue

SELECT
    ROUND(SUM(Revenue), 2) AS total_revenue
FROM fashion_retail.online_retail_merchandise;


-- Query 2: Calculate monthly merchandise revenue

SELECT
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS sales_month,
    ROUND(SUM(Revenue), 2) AS monthly_revenue
FROM fashion_retail.online_retail_merchandise
GROUP BY DATE_FORMAT(InvoiceDate, '%Y-%m')
ORDER BY sales_month;


-- Query 3: Top 10 products by revenue

SELECT
    StockCode,
    Description,
    ROUND(SUM(Revenue), 2) AS total_revenue,
    SUM(Quantity) AS total_quantity_sold
FROM fashion_retail.online_retail_merchandise
GROUP BY StockCode, Description
ORDER BY total_revenue DESC
LIMIT 10;


-- Query 4: Top 10 countries by revenue

SELECT
    Country,
    ROUND(SUM(Revenue), 2) AS total_revenue,
    SUM(Quantity) AS total_quantity_sold,
    COUNT(DISTINCT InvoiceNo) AS total_invoices
FROM fashion_retail.online_retail_merchandise
GROUP BY Country
ORDER BY total_revenue DESC
LIMIT 10;


-- Query 5: Average order value by country

SELECT
    Country,
    COUNT(DISTINCT InvoiceNo) AS total_invoices,
    ROUND(SUM(Revenue), 2) AS total_revenue,
    ROUND(
        SUM(Revenue) / COUNT(DISTINCT InvoiceNo),
        2
    ) AS average_order_value
FROM fashion_retail.online_retail_merchandise
GROUP BY Country
ORDER BY average_order_value DESC;


-- Query 6: Country contribution to total revenue

SELECT
    Country,
    ROUND(SUM(Revenue), 2) AS total_revenue,
    ROUND(
        SUM(Revenue) * 100.0 /
        (SELECT SUM(Revenue)
         FROM fashion_retail.online_retail_merchandise),
        2
    ) AS revenue_percentage
FROM fashion_retail.online_retail_merchandise
GROUP BY Country
ORDER BY revenue_percentage DESC;
