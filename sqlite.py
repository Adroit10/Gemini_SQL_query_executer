import sqlite3

## connect to SQLite
connection=sqlite3.connect("student.db")

## create cursor object to insert record, create table

cursor=connection.cursor()

## create a table
table_info='''
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25));
'''
cursor.execute(table_info)

## insert more records

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A') ''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B') ''')
cursor.execute('''Insert Into STUDENT values('Devansh','Data Science','A') ''')
cursor.execute('''Insert Into STUDENT values('Jai','Web Dev','A') ''')
cursor.execute('''Insert Into STUDENT values('Nikita','Web Dev','A') ''')

## Display all records

print("The inserted records are")
data=cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()