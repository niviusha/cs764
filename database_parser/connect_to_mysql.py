"""
This file is used for establishing connection to MySQL
database
It also includes the general operations that can be 
performed
"""
from __future__ import print_function
import MySQLdb
import helper
import sys

class MySQLConn:
  def __init__(self, *args, **kwargs):
    try:
      helper.check_argument_validity(['user', 'passwd', 'host', 'db'], kwargs)
      self.conn = MySQLdb.connect(user=kwargs['user'], passwd=kwargs['passwd'], host=kwargs['host'], db=kwargs['db'])
    except:
      print('Unexpected error: ', sys.exc_info()[0])
      raise
    else:
      print('Connection to ' + kwargs['db'] + ' established.')

  # For simply executing queries
  def execute(self, query):
    cursor = self.conn.cursor()
    cursor.execute(query)

  # This is mainly for select and project queries
  def execute_and_retrieve_data(self, query):
    cursor = self.conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

  def get_connection(self):
    return self.conn

  def get_database_name(self):
    return helper.parse_query_data(self.execute_and_retrieve_data('select database()'))[0]

  def get_user_name(self):
    return helper.parse_query_data(self.execute_and_retrieve_data('select current_user()'))[0]

