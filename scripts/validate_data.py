import pandas as pd
import os

folder = "data/raw"

files = os.listdir(folder)

for file in files:

    df = pd.read_csv(f"{folder}/{file}")

    print("\n")
    print("=" * 50)
    print(file)

    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    print("Missing Values:")
    print(df.isnull().sum())