# Data Dictionary

## dim_fund

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique fund identifier |
| fund_house | TEXT | Mutual fund company |
| scheme_name | TEXT | Fund scheme name |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |
| plan | TEXT | Regular/Direct plan |

## fact_nav

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Fund identifier |
| nav_date | DATE | NAV date |
| nav | REAL | Net Asset Value |

## fact_transactions

| Column | Type | Description |
|----------|----------|----------|
| investor_id | INTEGER | Investor identifier |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |

## fact_performance

| Column | Type | Description |
|----------|----------|----------|
| return_1yr_pct | REAL | 1 year return |
| return_3yr_pct | REAL | 3 year return |
| return_5yr_pct | REAL | 5 year return |
| expense_ratio_pct | REAL | Expense ratio |

## fact_aum

| Column | Type | Description |
|----------|----------|----------|
| fund_house | TEXT | Fund company |
| aum_crore | REAL | Assets under management |