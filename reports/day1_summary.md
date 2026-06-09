# Day 1 – Project Setup & Data Ingestion (ETL)

## Objective

Set up the project environment, ingest mutual fund datasets, validate data quality, and establish the foundation for further analytics.

## Project Setup

### Folder Structure Created

bluestock_mf_capstone/

├── data/

│   ├── raw/

│   ├── processed/

│   └── db/

├── scripts/

├── notebooks/

├── sql/

├── dashboard/

├── reports/

├── requirements.txt

└── README.md

### Environment Setup

- Python Virtual Environment created and activated
- Required libraries installed:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - plotly
  - sqlalchemy
  - requests
  - scipy
  - jupyter
- requirements.txt generated successfully


## Datasets Loaded

### Core Project Datasets

1. Fund Master Dataset
2. NAV History Dataset
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

### Live NAV Datasets Collected

1. HDFC Top 100
2. SBI Bluechip
3. ICICI Prudential Bluechip
4. Nippon India Large Cap
5. Axis Bluechip
6. Kotak Bluechip


## Data Exploration

All 10 CSV datasets were loaded and explored using Pandas.

The following checks were performed:

- Dataset Shape
- Column Names
- Data Types
- First Five Records
- Missing Value Analysis

All datasets loaded successfully without errors. :contentReference[oaicite:0]{index=0}


## Live NAV Fetching

Successfully connected to MFAPI and fetched live NAV data using API requests.

### API Used

https://api.mfapi.in/mf/125497

### Deliverable

- live_nav_fetch.py


## Data Validation Results

### Mutual Fund NAV Datasets

| Scheme | Rows | Missing Values |
|----------|--------:|---------------:|
| HDFC Top 100 | 3090 | 0 |
| ICICI Bluechip | 3306 | 0 |
| Axis Bluechip | 3564 | 0 |
| Nippon Large Cap | 3297 | 0 |
| SBI Bluechip | 3235 | 0 |
| Kotak Bluechip | 3300 | 0 |

All datasets passed quality checks with no missing values detected. :contentReference[oaicite:1]{index=1}


## Fund Master Analysis

### Unique Fund Houses

Total Fund Houses Identified: 10

Examples:

- SBI Mutual Fund
- HDFC Mutual Fund
- ICICI Prudential Mutual Fund
- Nippon India Mutual Fund
- Axis Mutual Fund
- Kotak Mahindra Mutual Fund
- Aditya Birla Sun Life Mutual Fund
- Mirae Asset Mutual Fund
- UTI Mutual Fund
- DSP Mutual Fund

### Categories Identified

- Equity
- Debt

### Sub-Categories Identified

Total Sub-Categories: 12

Examples:

- Large Cap
- Mid Cap
- Small Cap
- Value
- Index
- Liquid
- Gilt
- ELSS
- Short Duration

### Risk Categories Identified

Total Risk Categories: 5

- Low
- Moderate
- High
- Very High
- Moderately High

Fund master analysis successfully completed. :contentReference[oaicite:2]{index=2}


## AMFI Code Validation

Validation performed between:

- fund_master.csv
- nav_history.csv

### Results

- Total Fund Master Codes: 40
- Total NAV History Codes: 40
- Missing Codes: 0

### Outcome

✓ All AMFI codes present in fund_master exist in nav_history

✓ No missing scheme references found

✓ Dataset relationships validated successfully :contentReference[oaicite:3]{index=3}

## Deliverables Completed

### Scripts

- data_ingestion.py
- live_nav_fetch.py
- validate_data.py
- explore_datasets.py
- fund_master_analysis.py
- amfi_validation.py

### Reports

- Day 1 Summary Report
- Data Quality Summary Report

### Configuration

- requirements.txt
- README.md

## Key Findings

- All project datasets were loaded successfully.
- No missing values detected in NAV datasets.
- 10 mutual fund houses identified.
- 2 primary investment categories identified.
- 12 sub-categories identified.
- 5 risk classifications identified.
- All 40 AMFI scheme codes validated successfully.
- Live NAV fetching from MFAPI implemented successfully.

## Conclusion

Day 1 objectives for Project Setup and Data Ingestion (ETL) were completed successfully. The project environment has been configured, datasets have been ingested and validated, live NAV integration has been established, and the data is ready for Day 2 activities involving Data Cleaning, SQL Database Loading, and Advanced Analysis.