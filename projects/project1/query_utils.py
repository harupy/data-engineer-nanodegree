def build_insert_query(table_name, columns):
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

  """
  cols = f"{', '.join(columns)}"
  vals = f"({', '.join(['%s'] * len(columns))})"
  return f"INSERT INTO {table_name} ({cols}) VALUES {vals}"


if __name__ == '__main__':
  import doctest
  doctest.testmod()
