# Mutual Fund Analytics Capstone

## Objective
Analyze mutual fund NAV data using Python, SQL and Power BI.

## Funds Used
- HDFC Top 100
- SBI Bluechip
- ICICI Bluechip
- Nippon Large Cap
- Axis Bluechip
- Kotak Bluechip

## Day 1 Deliverables
- Project setup
- Data ingestion
- CSV generation
- Data validation

AMFI Codes Used:

HDFC Top 100 - 125497
SBI Bluechip - 119551
ICICI Bluechip - 120503
Nippon Large Cap - 118632
Axis Bluechip - 119092
Kotak Bluechip - 120841

Each AMFI code uniquely identifies a mutual fund scheme and is used to fetch NAV history through the MFAPI endpoint.

## Day 2 - Data Cleaning & SQL Database Design

### Completed Tasks

* Cleaned NAV history dataset
* Cleaned investor transactions dataset
* Cleaned scheme performance dataset
* Created processed datasets
* Designed SQLite star schema
* Loaded datasets into SQLite database
* Created analytical SQL queries
* Created data dictionary documentation

### Files Generated

* data/processed/02_nav_history_cleaned.csv
* data/processed/07_scheme_performance_cleaned.csv
* data/processed/08_investor_transactions_cleaned.csv
* sql/schema.sql
* sql/queries.sql
* reports/data_dictionary.md
* bluestock_mf.db

### Key Technologies

* Python
* Pandas
* SQLite
* SQLAlchemy
* Jupyter Notebook
* Git & GitHub

## Day 3 – Exploratory Data Analysis

- Performed EDA on mutual fund datasets
- Created 16+ visualizations using Plotly, Matplotlib, and Seaborn
- Exported PNG charts for reporting
- Documented 10 key EDA findings
- Analyzed NAV trends, SIP inflows, investor demographics, folio growth, and sector 

# Day 4 – Fund Performance Analytics

Completed advanced mutual fund performance analysis using NAV history and benchmark indices.

Tasks completed:
- Calculated daily returns for all schemes
- Computed CAGR for each mutual fund
- Calculated Sharpe Ratio using annualized returns and volatility
- Calculated Sortino Ratio using downside deviation
- Computed Alpha and Beta against NIFTY100 benchmark
- Calculated Maximum Drawdown for each scheme
- Built a composite Fund Scorecard
- Compared top-performing funds against NIFTY50 and NIFTY100 benchmarks

Deliverables generated:
- Performance_Analytics.ipynb
- fund_scorecard.csv
- alpha_beta.csv
- benchmark_comparison.png