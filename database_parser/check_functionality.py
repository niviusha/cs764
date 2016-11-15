"""
This file is mainly used to check the functionality of the 
other database features in the database_parser folder
"""
from __future__ import print_function
from connect_to_mysql import MySQLConn
from database_processor import DatabaseOps
from table_processor import TableOps
import helper

if __name__ == '__main__':
  # checking the MySQL connection and Database Ops
  conn = MySQLConn(user='', passwd='', host='', db='')
  dbobj = DatabaseOps(conn)
  print(dbobj.get_all_databases())
  #dbobj.switch_database('mysql')
  print(dbobj.get_all_tables())
  print(conn.get_database_name())
  print(conn.get_user_name())

  # checking TableOps
  tbobj = TableOps(conn)
  print(tbobj.get_columns('django_migrations'))
  print(tbobj.get_table_data('django_migrations'))
  print(tbobj.get_column_data('app', 'django_migrations'))
  print(tbobj.get_distinct_column_data('app', 'django_migrations'))
