-- Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average 1 Year Return

SELECT
    AVG(return_1yr_pct) AS avg_return
FROM fact_performance;

-- Funds with Expense Ratio Less Than 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Transaction Count by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- Total Investment Amount

SELECT
    SUM(amount_inr) AS total_amount
FROM fact_transactions;

-- Average NAV

SELECT
    AVG(nav) AS average_nav
FROM fact_nav;

-- Top 5 Funds by 1-Year Return

SELECT
    scheme_name,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- Transactions by Type

SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

-- Number of Funds per Category

SELECT
    category,
    COUNT(*) AS total_funds
FROM dim_fund
GROUP BY category;

-- Average Expense Ratio

SELECT
    AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance;

