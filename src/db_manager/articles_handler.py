import db_handler as db

conn = None

def connect():
  global conn
  conn = db.connect("articles.db") 

def add_news_article(date, source, title, body):
  __new_article('news', date, source, title, body)

def add_sec_article(date, source, title, body):
  __new_article('sec', date, source, title, body)

def __new_article(table, date, source, title, body):
  global conn
  article_columns = ("date", "source", "title", "body")
  db.insert(conn, table, article_columns, (date, source, title, body)) 
