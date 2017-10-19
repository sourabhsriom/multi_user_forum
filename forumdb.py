# "Database code" for the DB Forum.

import datetime
import psycopg2



POSTS = [("This is the first post.", datetime.datetime.now())]

DBNAME = "forum"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor()



  results = cursor.execute('select content, time from posts order by time desc')

  return results.fetchall()
  db.close()



def add_post(content):
  """Add a post to the 'database' with the current timestamp."""

  db = psycopg2.connect("dbname=forum")
  cursor = db.cursor()

  query = 'insert into posts values(%s)' %content

  cursor.execute(query)

  db.commit()

  db.close()

  #POSTS.append((content, datetime.datetime.now()))
