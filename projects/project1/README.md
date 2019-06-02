# Project 1: Data Modeling with Postgres

## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

## Project Description

In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Install Dependencies

```console
# pip
pip install -r requirements.txt

# pipenv
pipenv install
```

## Initialize Tables

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
| sql_queries.py   | Contains all the SQL queries for ETL                       |
| query_utils.py   | Contains utility functions to create SQL queries           |
| create_tables.py | Initialize tables                                          |
| etl.py           | Processes files in `data` and inserts the data into tables |
| test.ipynb       | A notebook to check if the queries work correctly          |
| etl.ipynb        | A notebook to test the ETL processes                       |
| data             | A directory containing song and log data                   |
| requirements.txt | Dependencies required for this project                     |

## Data

`song_data` Example

```json
{
  "num_songs": 1,
  "artist_id": "ARD7TVE1187B99BFB1",
  "artist_latitude": null,
  "artist_longitude": null,
  "artist_location": "California - LA",
  "artist_name": "Casual",
  "song_id": "SOMZWCG12A8C13C480",
  "title": "I Didn't Mean To",
  "duration": 218.93179,
  "year": 0
}
```

`log_data` Example

```json
{
  "artist": null,
  "auth": "Logged In",
  "firstName": "Walter",
  "gender": "M",
  "itemInSession": 0,
  "lastName": "Frye",
  "length": null,
  "level": "free",
  "location": "San Francisco-Oakland-Hayward, CA",
  "method": "GET",
  "page": "Home",
  "registration": 1540919166796.0,
  "sessionId": 38,
  "song": null,
  "status": 200,
  "ts": 1541105830796,
  "userAgent": "\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36\"",
  "userId": "39"
}, ...
```

## Table Schemas

`songs` table

| Column    | Datatype | Constraint  |
| --------- | -------- | ----------- |
| song_id   | varchar  | PRIMARY KEY |
| artist_id | varchar  | NOT NULL    |
| title     | varchar  | NOT NULL    |
| year      | int      | -           |
| duration  | float    | NOT NULL    |

`artists` table

| Column           | Datatype | Constraint  |
| ---------------- | -------- | ----------- |
| artist_id        | varchar  | PRIMARY KEY |
| artist_name      | varchar  | NOT NULL    |
| artist_location  | varchar  | -           |
| artist_latitude  | float    | -           |
| artist_longitude | float    | -           |

`time` table

| Column       | Datatype  | Constraint  |
| ------------ | --------- | ----------- |
| time_id      | serial    | PRIMARY KEY |
| ts           | timestamp | NOT NULL    |
| hour         | int       | NOT NULL    |
| day          | int       | NOT NULL    |
| week_of_year | int       | NOT NULL    |
| month        | int       | NOT NULL    |
| year         | int       | NOT NULL    |
| weekday      | int       | NOT NULL    |

`users` table

| Column     | Datatype | Constraint  |
| ---------- | -------- | ----------- |
| user_id    | int      | PRIMARY KEY |
| first_name | varchar  | NOT NULL    |
| last_name  | varchar  | NOT NULL    |
| gender     | varchar  | NOT NULL    |
| level      | varchar  | NOT NULL    |

`songplays` table

| Column      | Datatype  | Constraint  |
| ----------- | --------- | ----------- |
| songplay_id | serial    | PRIMARY KEY |
| ts          | timestamp | NOT NULL    |
| user_id     | int       | NOT NULL    |
| level       | varchar   | NOT NULL    |
| song_id     | varchar   | -           |
| artist_id   | varchar   | -           |
| session_id  | int       | -           |
| location    | varchar   | -           |
| user_agent  | varchar   | -           |

## Data Sources

| Table Name | Data Source            | Preprocess                     |
| ---------- | ---------------------- | ------------------------------ |
| songs      | song_data              | -                              |
| artists    | song_data              | -                              |
| time       | log_data               | Filter logs by NextPage Action |
| users      | log_data               | Filter logs by NextPage Action |
| songplays  | song_data and log_data | Filter logs by NextPage Action |

## ETL Pipeline

`songs` table

Extract and insert the following data from `song_data`

- `song_data`
- `song_id`,`title`
- `artist_id`
- `year`
- `duration`

---

`artists` table

Extract and insert the following data from `song_data`

- `artist_id`
- `artist_name`
- `artist_location`
- `artist_latitude`
- `artist_longitude`

---

`time` table

1. Convert timestamp to datetime
2. Extract and insert the following data from `log_data`
   - `timestamp`
   - `hour`
   - `day`
   - `week of year`
   - `month`
   - `year`
   - `weekday`

---

`users` table

Extract and insert the following data from `log_data`

- `userId`
- `firstName`
- `lastName`
- `gender`
- `level`

---

`songplays` table

1. Find `song_id` and `artist_id` from `songs` and `artists` tables using `song`, `artist` and `length`
2. Extract and insert the following data
   - `timestamp`
   - `userId`
   - `level`
   - `song_id`
   - `artist_id`
   - `session_id`
   - `location`
   - `userAgent`
