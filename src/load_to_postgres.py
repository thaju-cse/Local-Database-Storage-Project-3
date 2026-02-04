'''import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# Database config
DB_USER = "de_user"
DB_PASSWORD = "de_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "de_project"

TABLE_NAME = "netflix_tv"

CSV_FILE = Path("../data/processed/netflix_tv_cleaned.csv")

def load_data():
    df = pd.read_csv(CSV_FILE)

    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Batch insert
    df.to_sql(
        TABLE_NAME,
        engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=1000
    )

    print("Data successfully loaded into PostgreSQL")

if __name__ == "__main__":
    load_data()
'''
'''
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# DB config
DB_USER = "de_user"
DB_PASSWORD = "de_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "de_project"
TABLE_NAME = "netflix_tv"

# File path
CSV_FILE = Path("../data/processed/netflix_tv_cleaned.csv")

# Columns to load (explicit control)
COLUMNS_TO_LOAD = [
	"show_id", 
	"type",
	"title",
	"country", 
	"date_added",
	"release_year",
	"description"
]

def load_selected_columns():
    # Load only required columns
    df = pd.read_csv(CSV_FILE, usecols=COLUMNS_TO_LOAD)

    # Optional: final safety checks
    df = df.drop_duplicates()
    # Remove duplicate primary keys
    df = df.drop_duplicates(subset=["show_id"])

    # df["age"] = pd.to_numeric(df["age"], errors="coerce")

    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    df.to_sql(
        TABLE_NAME,
        engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=1000
    )

    print(f"{len(df)} rows inserted into {TABLE_NAME}")

if __name__ == "__main__":
    load_selected_columns()
'''
'''
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.dialects.postgresql import insert

# -----------------------
# CONFIG
# -----------------------
DB_USER = "de_user"
DB_PASSWORD = "de_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "de_project"
TABLE_NAME = "netflix_tv"

CSV_FILE = Path("../data/processed/netflix_tv_cleaned.csv")

COLUMNS_TO_LOAD = [
    "show_id",
    "type",
    "title",
    "country",
    "date_added",
    "release_year",
    "description",
]

# -----------------------
# LOAD + CLEAN DATA
# -----------------------
def load_dataframe():
    df = pd.read_csv(CSV_FILE, usecols=COLUMNS_TO_LOAD)

    # deduplicate primary key
    df = df.drop_duplicates(subset=["show_id"])

    # type fixes
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce")

    return df


# -----------------------
# UPSERT INTO POSTGRES
# -----------------------
def upsert_dataframe(df):
    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    metadata = MetaData()
    metadata.reflect(bind=engine)

    table = Table(TABLE_NAME, metadata, autoload_with=engine)

    with engine.begin() as conn:
        for _, row in df.iterrows():
            stmt = insert(table).values(**row.to_dict())

            # ignore duplicates (PRIMARY KEY conflict)
            stmt = stmt.on_conflict_do_nothing(
                index_elements=["show_id"]
            )

            conn.execute(stmt)

    print(f"Load completed. Rows processed: {len(df)}")


# -----------------------
# MAIN
# -----------------------
if __name__ == "__main__":
    df = load_dataframe()
    upsert_dataframe(df)

'''


import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.dialects.postgresql import insert

# ---------------- CONFIG ----------------
DB_USER = "de_user"
DB_PASSWORD = "de_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "de_project"
TABLE_NAME = "netflix_tv"

CSV_FILE = Path("../data/processed/netflix_tv_cleaned.csv")

COLUMNS = [
    "show_id",
    "type",
    "title",
    "country",
    "date_added",
    "release_year",
    "description",
]

# ---------------- LOAD DATA ----------------
def load_dataframe():
    df = pd.read_csv(CSV_FILE, usecols=COLUMNS)

    # Deduplicate PK
    df = df.drop_duplicates(subset=["show_id"])

    return df


# ---------------- UPSERT ----------------
def upsert_dataframe(df):
    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    metadata = MetaData()
    table = Table(TABLE_NAME, metadata, autoload_with=engine)

    with engine.begin() as conn:
        for row in df.to_dict(orient="records"):
            stmt = (
                insert(table)
                .values(**row)
                .on_conflict_do_nothing(index_elements=["show_id"])
            )
            conn.execute(stmt)

    print(f"Load successful. Rows processed: {len(df)}")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    df = load_dataframe()
    upsert_dataframe(df)

