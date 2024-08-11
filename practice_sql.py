import sqlite3

DB_NAME = 'band_data.db'

# create connection
conn = sqlite3.connect(database=DB_NAME)
cursor = conn.cursor()

# insert row
query = 'insert into events values("b4","c4","d4")'
cursor.execute(query)

# insert rows
data = [('b5', 'c5', 'd5'), ('b6', 'c6', 'd6')]
query = 'insert into events values(?,?,?)'
cursor.executemany(query, data)

# query database
query = 'select * from events'
cursor.execute(query)
rows = cursor.fetchall()
print(rows)

# query database
query = 'select band,city from events where band="b4"'
cursor.execute(query)
rows = cursor.fetchall()
print(rows)

# commit changes
conn.commit()

# close connection
conn.close()
