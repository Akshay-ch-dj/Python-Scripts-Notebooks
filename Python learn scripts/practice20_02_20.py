import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = 'root',
database = 'akshay'
)

mycursor = mydb.cursor()

mycursor.execute("DELETE FROM login WHERE address LIKE '%ase%'")
myresult = mycursor.fetchall()
print (myresult)
