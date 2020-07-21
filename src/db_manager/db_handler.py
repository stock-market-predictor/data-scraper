import atexit
import sqlite3

def connect(db_name):
  db_path = "../storage/" + db_name
  conn = sqlite3.connect(db_path)
  c = conn.cursor()
  atexit.register(c.close)
  return conn

def insert(conn, table, columns, args, autocommit=True):
  sql = "INSERT INTO " + table + __totuple(columns) + " VALUES" + __qmark_args(len(args))
  cursor = conn.cursor()
  cursor.execute(sql, args)
  if autocommit:
    conn.commit()
  return cursor.lastrowid

def update(conn, table, what, conditions):
  sql = "UPDATE " + table + " SET " + what + " " + conditions
  cursor = conn.cursor()
  cursor.execute(sql)
  if autocommit:
    conn.commit()
  return cursor.lastrowid

def select(conn, table, what, conditions):
  sql = "SELECT " + what + " FROM " + table + " " + conditions
  cursor = conn.cursor()
  return cursor.execute(sql).fetchall()

def __qmark_args(num):
  s = '('
  for i in range(num - 1):
    s += '?,'
  return s + '?)'

def __totuple(args):
  s = '('
  for arg in args:
    s += arg + ','
  return s[:len(s)-1] + ')'
