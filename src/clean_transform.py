import pandas as pd
import numpy as np
from pathlib import Path

RAW_FILE = Path("../data/raw/netflix_tv.csv")
PROCESSED_DIR = Path("../data/processed")
PROCESSED_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = PROCESSED_DIR / "netflix_tv_cleaned.csv"

def clean_data():
    df = pd.read_csv(RAW_FILE)

    # 1. Standardize column names
    print("Standardizing column names...")
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # 2. Drop duplicates
    print("Dropping duplicates...")
    df = df.drop_duplicates()
    
    print("Removing columns having too many null values")
    # 3. Remove columns with too many nulls
    null_ratio = df.isnull().mean()
    df = df.loc[:, null_ratio < 0.4]

    
    # 4. Strip string columns
    #for col in df.select_dtypes(include="object"):
    #   df[col] = df[col].str.strip()

    # 5. Convert date columns (best guess)
    #for col in df.columns:
    #    if "date" in col:
    #        df[col] = pd.to_datetime(df[col], errors="coerce")

    # 6. Numeric coercion
    #for col in df.select_dtypes(include="object"):
    #    df[col] = pd.to_numeric(df[col], errors="ignore")

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Cleaned data saved → {OUTPUT_FILE}")

def main():
    clean_data()

if __name__ == "__main__":
    main()
