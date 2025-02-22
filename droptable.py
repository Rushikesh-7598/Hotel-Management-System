import sqlite3

connection=sqlite3.connect('Hotel.db')
sql="DROP TABLE Hotel"
cur=connection.cursor()
cur.execute(sql)
connection.commit()
print("Done")