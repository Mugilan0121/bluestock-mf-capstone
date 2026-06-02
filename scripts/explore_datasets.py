import pandas as pd
import os

folder = "data/raw"

files = os.listdir(folder)

for file in files:

    if file.endswith(".csv"):

        print("\n" + "="*60)
        print("FILE:", file)

        df = pd.read_csv(f"{folder}/{file}")

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())