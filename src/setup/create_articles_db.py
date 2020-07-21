import sqlite3
import db_handler
 
def create_news(cursor):
  cursor.execute("""CREATE TABLE news
                (news_id INTEGER PRIMARY KEY, date TEXT, source TEXT, title TEXT, body TEXT)""")

def create_sec(cursor):
  cursor.execute("""CREATE TABLE sec
                (sec_id INTEGER PRIMARY KEY, date TEXT, source TEXT, title TEXT, body TEXT)""")

db_handler.connect("articles.db", create_news, create_sec)

