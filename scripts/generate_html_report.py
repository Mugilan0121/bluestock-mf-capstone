import pandas as pd

# Load fund scorecard
scorecard = pd.read_csv("data/processed/fund_scorecard.csv")

# Sort by Sharpe Ratio and select top 10 funds
top_funds = scorecard.sort_values(
    by="sharpe_ratio",
    ascending=False
).head(10)

# HTML template
html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Weekly Mutual Fund Performance Report</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f8f9fa;
        }}

        h1 {{
            color: #1f4e79;
            text-align: center;
        }}

        h2 {{
            color: #2e75b6;
        }}

        table {{
            border-collapse: collapse;
            width: 100%;
            background-color: white;
        }}

        th {{
            background-color: #ddebf7;
            border: 1px solid black;
            padding: 10px;
        }}

        td {{
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }}

        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
    </style>
</head>

<body>

    <h1>Weekly Mutual Fund Performance Report</h1>

    <h2>Top 10 Funds by Sharpe Ratio</h2>

    {top_funds.to_html(index=False)}

</body>
</html>
"""

# Save HTML report
with open(
    "reports/weekly_report.html",
    "w",
    encoding="utf-8"
) as f:
    f.write(html)

print("HTML report generated successfully!")