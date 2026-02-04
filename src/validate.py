import pandas as pd

def validate():
    df = pd.read_csv("../data/processed/netflix_tv_cleaned.csv")
    print(df.info())
    print(df.isnull().sum())

def main():
    validate()

if __name__=="__main__":
    main()
