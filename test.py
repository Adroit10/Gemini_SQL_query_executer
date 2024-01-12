import sqlite3

conn=sqlite3.connect('student.db')
cur=conn.cursor()
cur.execute('''SELECT * FROM STUDENT''')
rows=cur.fetchall()
conn.commit()
conn.close()
for row in rows:
    print(row)

