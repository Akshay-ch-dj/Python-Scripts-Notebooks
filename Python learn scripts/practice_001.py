import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = 'root',
database = 'akshay'
)

mycursor = mydb.cursor()
sql = "INSERT INTO login (user_id,password) VALUES(%s, %s)"
val = [("Albin","Student"), ("sanu", "123")]

mycursor.executemany(sql, val)
mydb.commit()
