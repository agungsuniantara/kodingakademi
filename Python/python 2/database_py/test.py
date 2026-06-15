import pymysql
import pandas as pd

mydb = pymysql.connect(
    host="localhost", user="root", password="root", database="supermarket"
)

query = "SELECT * FROM karyawan_kontrak"
cursor = mydb.cursor()
cursor.execute(query)

data = cursor.fetchall()

print(cursor.description)

# per kolom
for column in cursor.description: 
    print(column[0])

# per baris
for row in data: 
    for value in row : 
        print(value)

cursor.close()
mydb.close()
