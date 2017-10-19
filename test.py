import psycopg2

db = psycopg2.connect(database="forum")
cursor = db.cursor()



results = cursor.execute('select content, time from posts order by time desc')

print (results.fetchall())
db.close()
