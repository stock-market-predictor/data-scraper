import sqlite3
import db_handler
 
def reset_news(cursor):
  cursor.execute("""delete from news""")

def reset_sec(cursor):
  cursor.execute("""delete from sec""")

db_handler.connect("articles.db", reset_news, reset_sec)
