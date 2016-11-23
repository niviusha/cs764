"""
Defines all the operations on a database
"""
from __future__ import print_function
from table_processor import TableOps
import helper
import json

class DatabaseOps:
  def __init__(self, db_connection):
    self.db_connection = db_connection

  def get_all_databases(self):
    return helper.parse_query_data(self.db_connection.execute_and_retrieve_data('show databases'))

  def get_all_tables(self):
    return helper.parse_query_data(self.db_connection.execute_and_retrieve_data('show tables'))

  def use_database(self, db_name):
    self.db_connection.execute('use ' + db_name)

  def get_context_dictionary(self):
    tables = self.get_all_tables()
    table_relation = []
    table_ops = TableOps(self.db_connection)
    all_cols = []
    for table in tables:
      columns = table_ops.get_columns(table)
      columns = [ table + "." + column for column in columns]
      all_cols.extend(columns)
    cont_dict = {
      'relations' : tables,
      'attributes': all_cols,
    }
    return json.dumps(cont_dict, indent=2, sort_keys=True)

  def get_join_path_dictionary(self):
    tables = self.get_all_tables()
    table_ops = TableOps(self.db_connection)
    join_path = {}
    for table in tables:
      primary_key = table_ops.get_primary_key(table)
      foreign_key = table_ops.get_foreign_key(table)
      join_path[table] = {
        'primary_key': primary_key,
        'foreign_key': foreign_key,
      }
    return json.dumps(join_path, indent=2, sort_keys=True)
