import pandas as pd
from pathlib import Path

# Locate project root
project_root = Path(__file__).resolve().parent.parent

# Load fund scorecard
scorecard_path = project_root / "data" / "processed" / "fund_scorecard.csv"

scorecard = pd.read_csv(scorecard_path)

# User input
risk = input(
    "Enter Risk Level (Low / Moderate / High / Moderately High / Very High): "
).strip().lower()

# Make comparison case-insensitive
scorecard["risk_grade_clean"] = (
    scorecard["risk_grade"]
    .astype(str)
    .str.strip()
    .str.lower()
)

# Filter matching funds
filtered = scorecard[
    scorecard["risk_grade_clean"] == risk
]

# No matches found
if filtered.empty:

    print("\nNo funds found for this risk level.")
    print("\nAvailable Risk Levels:")

    for level in scorecard["risk_grade"].unique():
        print("-", level)

# Show recommendations
else:

    recommendations = (
        filtered
        .sort_values(
            by="sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    print("\nTop 3 Recommended Funds:\n")

    columns_to_show = [
        "scheme_name",
        "risk_grade",
        "sharpe_ratio",
        "fund_score"
    ]

    available_columns = [
        col
        for col in columns_to_show
        if col in recommendations.columns
    ]

    print(
        recommendations[
            available_columns
        ]
    )