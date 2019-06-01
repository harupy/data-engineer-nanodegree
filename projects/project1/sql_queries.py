# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
  timestamp bigint NOT NULL,
  user_id int NOT NULL,
  level varchar NOT NULL,
  song_id varchar,
  artist_id varchar,
  session_id int NOT NULL,
  location varchar,
  user_agent varchar
)
""")


user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
  user_id int NOT NULL,
  first_name varchar,
  last_name varchar,
  gender varchar,
  level varchar
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
  song_id varchar NOT NULL,
  title varchar NOT NULL,
  artist_id varchar NOT NULL,
  year int NOT NULL,
  duration float NOT NULL
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
  artist_id varchar NOT NULL,
  artist_name varchar NOT NULL,
  artist_location varchar,
  artist_latitude float,
  artist_longitude float
)
""")

# timestamp	hour	day	week_of_year	month	year	weekday

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
  timestamp bigint NOT NULL,
  hour int NOT NULL,
  day int NOT NULL,
  week_of_year int NOT NULL,
  month int NOT NULL,
  year int NOT NULL,
  weekday int NOT NULL
)
""")


def create_insert_query(table_name, columns):
  """
  Create an insert query

  Args:
    table_name (str): Table name to insert data into
    columns (list of str): Columns of the table

  Returns:
    str: Insert query

  Examples:
  >>> create_insert_query('table', ['col1', 'col2'])
  'INSERT INTO table (col1, col2) VALUES (%s, %s)'

  """
  cols = f"{', '.join(columns)}"
  vals = f"({', '.join(['%s'] * len(columns))})"
  return f"INSERT INTO {table_name} ({cols}) VALUES {vals}"


# INSERT RECORDS
songplay_table_insert = create_insert_query(
  'songplays',
  ['timestamp', 'user_id', 'level', 'song_id', 'artist_id', 'session_id', 'location', 'user_agent']
)

song_table_insert = create_insert_query(
  'songs',
  ['song_id', 'title', 'artist_id', 'year', 'duration']
)

artist_table_insert = create_insert_query(
  'artists',
  ['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']
)

time_table_insert = create_insert_query(
  'time',
  ['timestamp', 'hour', 'day', 'week_of_year', 'month', 'year', 'weekday']
)

user_table_insert = create_insert_query(
  'users',
  ['user_id', 'first_name', 'last_name', 'gender', 'level']
)


# FIND SONGS

song_select = ("""
  SELECT song_id, s.artist_id
  FROM songs s
  LEFT JOIN artists a ON s.artist_id = a.artist_id
  WHERE title=%s AND artist_name=%s AND duration=%s
""")

#

# QUERY LISTS

# create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
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


if __name__ == '__main__':
  import doctest
  doctest.testmod()
