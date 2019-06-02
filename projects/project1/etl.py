import os
import glob
import psycopg2

import pandas as pd
from sql_queries import (
  song_table_insert,
  artist_table_insert,
  time_table_insert,
  user_table_insert,
  songplay_table_insert,
  song_select,
)


def process_song_file(cur, filepath):
  """
  Read a song JSON file and insert the data into time, user and songplay table

  Args:
    cur (cursor): A cursor object to execute SQL queries
    filepath (str): A path to a JSON file

  Returns:
    None
  """

  # open song file
  df = pd.read_json(filepath, lines=True)

  # insert song record
  song_cols = [
    'song_id',
    'title',
    'artist_id',
    'year',
    'duration',
  ]
  song_data = df[song_cols].values.tolist()[0]
  cur.execute(song_table_insert, song_data)

  # insert artist record
  artist_cols = [
    'artist_id',
    'artist_name',
    'artist_location',
    'artist_latitude',
    'artist_longitude',
  ]
  artist_data = df[artist_cols].values.tolist()[0]
  cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
  """
  Read a log JSON file and insert the data into time, user and songplay table

  Args:
    cur (cursor): A cursor object to execute SQL queries
    filepath (str): A path to a JSON file

  Returns:
    None
  """
  # open log file
  df = pd.read_json(filepath, lines=True)

  # filter by NextSong action
  df = df[df['page'] == 'NextSong']

  # convert timestamp column to datetime
  df['ts'] = pd.to_datetime(df['ts'], unit='ms')
  ts = df['ts']

  # insert time data records
  time_data = [
    ts,
    ts.dt.hour,
    ts.dt.day,
    ts.dt.weekofyear,
    ts.dt.month,
    ts.dt.year,
    ts.dt.dayofweek,
  ]

  column_labels = [
    'ts',
    'hour',
    'day',
    'week_of_year',
    'month',
    'year',
    'weekday',
  ]
  time_df = pd.DataFrame({k: v for k, v in zip(column_labels, time_data)})

  for i, row in time_df.iterrows():
    cur.execute(time_table_insert, list(row))

  # load user table
  user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

  # insert user records
  for i, row in user_df.iterrows():
    cur.execute(user_table_insert, row)

  # insert songplay records
  for index, row in df.iterrows():

    # get songid and artistid from song and artist tables
    cur.execute(song_select, (row.song, row.artist, row.length))
    results = cur.fetchone()

    if results:
      song_id, artist_id = results
    else:
      song_id, artist_id = None, None

    # insert songplay record
    songplay_data = (
      row.ts,
      row.userId,
      row.level,
      song_id,
      artist_id,
      row.sessionId,
      row.location,
      row.userAgent,
    )

    cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
  # get all files matching extension from directory
  all_files = []
  for root, dirs, files in os.walk(filepath):
    files = glob.glob(os.path.join(root, '*.json'))
    for f in files:
      all_files.append(os.path.abspath(f))

  # get total number of files found
  num_files = len(all_files)
  print('{} files found in {}'.format(num_files, filepath))

  # iterate over files and process
  for i, datafile in enumerate(all_files, 1):
    func(cur, datafile)
    conn.commit()
    print('{}/{} files processed.'.format(i, num_files))


def main():
  conn = psycopg2.connect('host=127.0.0.1 dbname=sparkifydb user=student password=student')
  cur = conn.cursor()

  process_data(cur, conn, filepath='data/song_data', func=process_song_file)
  process_data(cur, conn, filepath='data/log_data', func=process_log_file)

  conn.close()


if __name__ == '__main__':
  main()
