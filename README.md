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
