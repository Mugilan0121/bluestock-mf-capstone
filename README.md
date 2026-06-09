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

# Day 5 - Power BI Dashboard

Built an interactive Mutual Fund Analytics Dashboard using Power BI.

### Dashboard Pages

1. Industry Overview

   * AUM Growth Trend
   * Top Fund Houses
   * Industry KPIs

2. Fund Performance

   * Risk vs Return Analysis
   * NAV vs Benchmark Comparison
   * Fund Scorecard

3. Investor Analytics

   * Transaction Analysis by State
   * SIP vs Lumpsum Distribution
   * Age Group Analysis
   * Monthly Transaction Trends

4. SIP & Market Trends

   * SIP Inflow vs NIFTY 50 Trend
   * Category Inflow Heat Map
   * Top Categories by Net Inflow
   * SIP Growth KPIs

### Tools Used

* Power BI
* DAX
* Power Query
* Data Modeling
* Interactive Slicers and KPIs


## Day 6 – Advanced Analytics & Risk Metrics

### Tasks Completed

* Calculated **Value at Risk (VaR)** and **Conditional VaR (CVaR)** for mutual funds.
* Performed **90-Day Rolling Sharpe Ratio** analysis and generated performance charts.
* Conducted **Investor Cohort Analysis** based on transaction history.
* Identified SIP discontinuation risk through **SIP Continuity Analysis**.
* Built a simple **Fund Recommendation Engine** using risk grades and Sharpe Ratio.
* Computed **Herfindahl-Hirschman Index (HHI)** to measure portfolio concentration and diversification.

### Deliverables

* Advanced_Analytics.ipynb
* var_cvar_report.csv
* rolling_sharpe_chart.png
* cohort_analysis.csv
* sip_continuity.csv
* recommender.py
* sector_hhi.csv


## Bonus Challenges Completed
### B1 - Streamlit Web App
- Built a Streamlit-based Mutual Fund Intelligence Platform with interactive dashboards, KPIs, filters, and visualizations.

### B2 – Monte Carlo Simulation
- Simulated 100 future NAV paths over 5 years.
- Generated uncertainty bands and projection charts.

### B3 – Markowitz Portfolio Optimization
- Optimized a portfolio of 5 mutual funds.
- Maximized Sharpe Ratio using Modern Portfolio Theory.

### B4 – Automated HTML Reporting
- Generated automated HTML performance reports.
- Summarized top-performing mutual funds.