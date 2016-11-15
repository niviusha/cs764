"""
Defines all the operations on a table
"""
from __future__ import print_function
import helper

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

