"""
Defines all the operations on a database
"""
from __future__ import print_function

class DatabaseOps:
  def __init__(self, db_connection):
    self.db_connection = db_connection

  def get_all_databases(self):
    return self.db_connection.execute_and_retrieve_data('show databases')

  def get_all_tables(self):
    return self.db_connection.execute_and_retrieve_data('show tables')

  def switch_database(self, db_name):
    self.db_connection.execute('use ' + db_name)

