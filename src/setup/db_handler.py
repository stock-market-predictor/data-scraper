import sqlite3

def connect(db_name, *argv):
  db_path = __get_storage_path() + db_name
  conn = sqlite3.connect(db_path)
  c = conn.cursor()
  for arg in argv:
    arg(c)
  conn.commit()
  c.close()
  
def __get_storage_path():
  # TODO get absolute path to storage
  pass
