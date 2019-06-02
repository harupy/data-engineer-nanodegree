def build_insert_query(table_name, columns, on_conflict=None):
  """
  Build an insert query

  Args:
    table_name (str): A table to insert data into
    columns (list of str): A list of column names

  Return:
    str: A query to insert data into a specified table

  Examples:
  >>> build_insert_query('test', ['col1', 'col2'])
  'INSERT INTO test (col1, col2) VALUES (%s, %s)'

  >>> build_insert_query('test', ['col1', 'col2'], "ON CONFLICT (col1) DO NOTHING")
  'INSERT INTO test (col1, col2) VALUES (%s, %s) ON CONFLICT (col1) DO NOTHING'

  """
  return "INSERT INTO {} ({}) VALUES ({}) {}".format(
    table_name,
    ', '.join(columns),
    ', '.join(['%s'] * len(columns)),
    on_conflict if on_conflict else ''
  ).strip()


if __name__ == '__main__':
  import doctest
  doctest.testmod()
