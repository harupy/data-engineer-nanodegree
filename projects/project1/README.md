# Project 1: Data Modeling with Postgres

## Project Description

In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Install dependencies

```
# pip
pip install -r requirements.txt

# pipenv
pipenv install
```

## Initialize tables

```
python create_tables.py
```

## Execute ETL

```
python etl.py
```

## Files

| File Name        | Description                                                |
| ---------------- | ---------------------------------------------------------- |
| sql_queries.py   | Contains all the SQL queries for this project              |
| query_utils.py   | Contains utility functions to create SQL queries           |
| create_tables.py | Initialize tables                                          |
| etl.py           | Processes files in `data` and inserts the data into tables |
| test.ipynb       | A notebook to check if the queries work correctly          |
| etl.ipynb        | A notebook to test the ETL processes                       |
| data             | A directory containing song and log data                   |
| requirements.txt | Dependencies required for this project                     |
