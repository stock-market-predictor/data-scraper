import sqlite3
import db_handler
 
def reset_news(cursor):
  cursor.execute("""DELETE FROM news""")

db_handler.connect("articles.db", reset_news)
