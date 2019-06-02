from query_utils import build_insert_query

# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
songplay_table_create = """
CREATE TABLE IF NOT EXISTS songplays (
  songplay_id serial PRIMARY KEY,
  ts timestamp NOT NULL,
  user_id int NOT NULL,
  level varchar NOT NULL,
  song_id varchar,
  artist_id varchar,
  session_id int,
  location varchar,
  user_agent varchar
)
"""


user_table_create = """
CREATE TABLE IF NOT EXISTS users (
  user_id varchar PRIMARY KEY,
  first_name varchar NOT NULL,
  last_name varchar NOT NULL,
  gender varchar,
  level varchar NOT NULL
)
"""

song_table_create = """
CREATE TABLE IF NOT EXISTS songs (
  song_id varchar PRIMARY KEY,
  title varchar NOT NULL,
  artist_id varchar NOT NULL,
  year int,
  duration float NOT NULL
)
"""

artist_table_create = """
CREATE TABLE IF NOT EXISTS artists (
  artist_id varchar PRIMARY KEY,
  artist_name varchar,
  artist_location varchar,
  artist_latitude float,
  artist_longitude float
)
"""

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
  time_id serial PRIMARY KEY,
  ts timestamp NOT NULL,
  hour int NOT NULL,
  day int NOT NULL,
  week_of_year int NOT NULL,
  month int NOT NULL,
  year int NOT NULL,
  weekday int NOT NULL
)
""")


# INSERT RECORDS
songplay_table_insert = build_insert_query(
  'songplays',
  ['ts', 'user_id', 'level', 'song_id', 'artist_id', 'session_id', 'location', 'user_agent'],
)

song_table_insert = build_insert_query(
  'songs',
  ['song_id', 'title', 'artist_id', 'year', 'duration'],
  'ON CONFLICT (song_id) DO NOTHING'
)

artist_table_insert = build_insert_query(
  'artists',
  ['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude'],
  'ON CONFLICT (artist_id) DO NOTHING'
)

time_table_insert = build_insert_query(
  'time',
  ['ts', 'hour', 'day', 'week_of_year', 'month', 'year', 'weekday']
)

user_table_insert = build_insert_query(
  'users',
  ['user_id', 'first_name', 'last_name', 'gender', 'level'],
  'ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level'
)


# FIND SONGS
song_select = """
  SELECT song_id, s.artist_id
  FROM songs s
  LEFT JOIN artists a ON s.artist_id = a.artist_id
  WHERE title=%s AND artist_name=%s AND duration=%s
"""

# QUERY LISTS

create_table_queries = [
  song_table_create,
  artist_table_create,
  time_table_create,
  user_table_create,
  songplay_table_create,
]

drop_table_queries = [
  song_table_drop,
  artist_table_drop,
  time_table_drop,
  user_table_drop,
  songplay_table_drop,
]
