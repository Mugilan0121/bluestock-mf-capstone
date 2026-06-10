# Bluestock Mutual Fund Analytics Capstone Project

## Project Overview

The Bluestock Mutual Fund Analytics Capstone Project is an end-to-end data analytics solution developed to analyze, evaluate, and visualize mutual fund performance using Python, SQLite, SQL, and Power BI.

The project follows a complete analytics workflow, starting from data collection and cleaning, followed by database creation, exploratory data analysis (EDA), performance metric calculation, and dashboard development. The objective is to transform raw mutual fund data into meaningful insights that support investment analysis and decision-making.

---

## Objectives

* Collect and organize mutual fund data.
* Build a structured SQLite database.
* Perform data cleaning and preprocessing.
* Conduct exploratory data analysis (EDA).
* Calculate performance metrics such as Alpha and Beta.
* Generate fund scorecards and risk classifications.
* Develop an interactive Power BI dashboard.
* Extract business insights from mutual fund data.

---

## Technologies Used

| Technology       | Purpose                     |
| ---------------- | --------------------------- |
| Python           | Data Processing & Analytics |
| Pandas           | Data Manipulation           |
| SQLite           | Database Management         |
| SQL              | Data Querying               |
| Matplotlib       | Data Visualization          |
| Jupyter Notebook | Development Environment     |
| Power BI         | Dashboard Development       |
| GitHub           | Version Control             |

---

## Project Architecture

Raw Mutual Fund Data

↓

Data Cleaning & Validation

↓

SQLite Database Storage

↓

SQL Querying & Data Retrieval

↓

Exploratory Data Analysis (EDA)

↓

Performance Analytics

↓

Power BI Dashboard

↓

Business Insights & Reporting

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
```

### 2. Navigate to Project Folder

```bash
cd BLUESTOCK_MF_CAPSTONE
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## File Descriptions

### data/

Contains raw and processed mutual fund datasets used throughout the project.

### notebooks/

Contains Jupyter notebooks for data ingestion, cleaning, exploratory analysis, performance analytics, and advanced financial analysis.

### dashboard/

Contains Power BI dashboard files and dashboard screenshots.

### reports/

Contains generated reports, visualizations, and analytical outputs.

### sql/

Contains SQL queries used for database operations and data retrieval.

### docs/

Contains the final project report and presentation deck.

### bluestock_mf.db

SQLite database containing processed mutual fund information.

### run_pipeline.py

Master script representing the overall project workflow.

---

## ETL Workflow

The ETL (Extract, Transform, Load) process follows these steps:

### Extract

* Import mutual fund dataset.
* Load data into the Python environment.

### Transform

* Handle missing values.
* Remove duplicate records.
* Standardize column formats.
* Validate data quality.

### Load

* Store cleaned data into SQLite database.
* Enable SQL-based querying and analysis.

---

## How to Run the Project

### Step 1 – Data Ingestion

Open and run:

```text
notebooks/01_data_ingestion.ipynb
```

### Step 2 – Data Cleaning

Open and run:

```text
notebooks/02_data_cleaning.ipynb
```

### Step 3 – Exploratory Data Analysis

Open and run:

```text
notebooks/EDA_Analysis.ipynb
```

### Step 4 – Performance Analytics

Open and run:

```text
notebooks/Performance_Analytics.ipynb
```

### Step 5 – Advanced Analytics (Optional)

Open and run:

```text
notebooks/Advanced_Analytics.ipynb
```

---

## Running the Master Pipeline

Execute:

```bash
python run_pipeline.py
```

Expected Output:

```text
Bluestock Mutual Fund Analytics Pipeline
Step 1: Data Ingestion Completed
Step 2: EDA Completed
Step 3: Performance Analytics Completed
Step 4: Dashboard Created
Project Execution Successful
```

---

## Dashboard

The Power BI dashboard provides:

* Mutual Fund Performance Monitoring
* Category-wise Analysis
* Risk Assessment
* Fund Comparison
* Interactive Filtering
* Performance Insights

### How to Open Dashboard

1. Open Power BI Desktop.
2. Navigate to the dashboard folder.
3. Open the Power BI dashboard file (.pbix).
4. Refresh data if required.
5. Explore dashboard visuals and filters.

---

## Key Deliverables

* SQLite Database
* Data Cleaning Pipeline
* Exploratory Data Analysis
* Alpha & Beta Metrics
* Fund Scorecard
* Risk Classification
* Power BI Dashboard
* Final Report
* Presentation Deck

---

## Key Findings

* Mutual fund categories exhibit varying levels of representation.
* Performance varies significantly across funds and categories.
* Risk-adjusted metrics provide deeper insights than returns alone.
* Benchmark comparisons improve fund evaluation accuracy.
* Interactive dashboards simplify complex financial analysis.

---

## Future Improvements

* Integration with real-time market data.
* Automated ETL scheduling.
* Predictive analytics for fund performance forecasting.
* Enhanced portfolio optimization models.
* Cloud deployment of analytical workflows.

---

## Author

**Mugilan M**

Bluestock Mutual Fund Analytics Capstone Project

June 2026
