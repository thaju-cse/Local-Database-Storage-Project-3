# Local Database Storage (SQL Basics)

Used a Dataset(Netflix Movies and TV Shows) from Kaggle to do cleaning, transformation and loading into a database od Postgresql DBMS.

---

## Overview
Selelcted a data set from kaggle to clean and transform it  using 3 functions of python the loaded into a database located in local postgresql database.

---

## Features
1. Download kaggle data set from website using python.
2. Inspect the dataset by using basic info (meta data).
3. Cleaned and transformed by converting csv into pandad dataframe.
4. Finally validate the transformed clean data.
5. Then loaded into a database of postgresql DBMS.

---

## Tech Stack
```
|-----------------|-----------------------------|
|Category         |Tools                        |
|-----------------------------------------------|
|Language         |Python                       |
|Libraries        |Pandas, kagglehub,sqlalchemy |
|OS               |Ubuntu(WSL)                  |
|-----------------------------------------------|
```

---

## Project Architecture
- Download kaggle data set.
- Basic cleaning and transformations.
- Saving into a csv file as transformed clean data.
- Storing the csv as structured table into a Postgresql database.

---

## Installation / Setup
```
git clone https://github.com/thaju-cse/Local-Database-Storage-Project-3
cd Local-Database-Storage-Project-3
pip install -r requirements.txt
```

---

## Usage
```
python3 main.py
```
---

## Folder Structure
```
|-- data/
|    |-- raw/
|    |-- processed/
|-- src/
|    |-- inspect_data.py
|    |-- clean_transform.py
|    |-- validate.py
|    |-- load_to_postgres.py
|-- README.md
|-- requirements.txt
```
---

## Learning Outcomes
- Creating virtual environments of python
- Installing packages in linux
- Understanding the errors
- Uploading csv data into a database of Postgres

---

## Future Enhancements
- Automating the whole process
- Capacity incrementing upto Giga Bytes of Data
- Optimized Data types management

---

## Challenges
- Installation of modules
- Finding the actual environment of python running in the background
- Writing Readme.md file
- Matching the data types to upload data

---

## Author
**Shaik Thajuddhin**
---
**Aspiring Data Engineer**
