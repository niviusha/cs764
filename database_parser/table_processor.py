"""
Defines all the operations on a table
"""
from __future__ import print_function
import helper
import json

class TableOps:
  def __init__(self, conn):
    self.conn = conn;

  def get_columns(self, table_name):
    query = (
             "select column_name "
             "from information_schema.columns "
             "where table_schema = '" + self.conn.get_database_name() + "' "
             "and table_name = '" + table_name +"'"
            )

    columns = helper.parse_query_data(self.conn.execute_and_retrieve_data(query))
    return columns

  def get_column_data_type(self, column_name, table_name):
    query = (
            "select data_type "
            "from information_schema.columns "
            "where table_name = '" + table_name + "' and "
            " column_name = '" + column_name + "'"
    )
    return helper.parse_query_data(self.conn.execute_and_retrieve_data(query))[0]

  # Gets the entire table data
  def get_table_data(self, table_name):
    query = 'select * from ' + table_name;
    return self.conn.execute_and_retrieve_data(query)

  # Get data of a column
  def get_column_data(self, column_name, table_name):
    query = 'select ' + column_name + ' from ' + table_name
    return helper.parse_query_data(self.conn.execute_and_retrieve_data(query))

  # Get distinct column
  def get_distinct_column_data(self, column_name, table_name):
    query = 'select distinct ' + column_name + ' from ' + table_name
    return helper.parse_query_data(self.conn.execute_and_retrieve_data(query))

  # Get the constraints on the table columns
  def get_constraints(self, table_name):
    query = 'select table_name, column_name, constraint_name, referenced_table_name, referenced_column_name from information_schema.key_column_usage where table_name="'+table_name+'"'
    return self.conn.execute_and_retrieve_data(query)

  # Get the foreign key constraints of the table
  def get_foreign_key(self, table_name):
    key_cols = self.get_constraints(table_name)
    foreign_keys = []
    for col in key_cols:
      if "ibfk" in col[2]:
        val = {
            'column_name': col[1],
            'referenced_table_name': col[3],
            'referenced_column_name': col[4],
          }
        foreign_keys.append(val)
    if len(foreign_keys) == 0:
      return "NULL"
    return foreign_keys

  # Get primary key of the table
  def get_primary_key(self, table_name):
    key_cols = self.get_constraints(table_name)
    for col in key_cols:
      if col[2] == 'PRIMARY':
        return col[1]
    return "NULL"

  # Gets the list of unique values for all columns in the table
  def get_table_column_value_data(self, table_name):
    table_data = {
      table_name: {}
    }
    columns = self.get_columns(table_name)
    for column in columns:
      table_data[table_name][column] = self.get_distinct_column_data(column, table_name)
#      print(table_data[table_name][column])
    # This is not json serializable
    return table_data

  # Inserts the values into tables. The values are comma separated
  # corresponding to a column
  def insert_into_table(self, table_name, values):
    query = "insert into " + table_name + " values (" + values + ")"
    return self.conn.execute(query)
