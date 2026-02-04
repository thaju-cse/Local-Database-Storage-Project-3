import pandas as pd
from pathlib import Path

def details():
    RAW_FILE = Path("../data/raw/netflix_tv.csv")

    df = pd.read_csv(RAW_FILE)

    print("Count:", df.count)
    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns)

    print("\nData Types:")
    print(df.dtypes)

    print("\nNull Counts:")
    print(df.isnull().sum())

    print("\nSample Rows:")
    print(df.head())

def main():
    details()

if __name__=="__main__":
    main()
