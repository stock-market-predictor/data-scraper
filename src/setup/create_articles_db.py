import sqlite3
import db_handler
 
def create_news(cursor):
  cursor.execute("""CREATE TABLE news
                (news_id INTEGER PRIMARY KEY, title TEXT, body TEXT)""")

db_handler.connect("articles.db", create_news)

