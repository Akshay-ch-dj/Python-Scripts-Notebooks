import mysql.connector
#from window_newacc import NewAccount
mydb = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = 'root',
database = 'akshay'
)

print (mydb)
mycursor = mydb.cursor()
mycursor.execute("USE akshay")
mycursor.execute("CREATE TABLE Customers (Name varchar(255),Dob varchar(255),Acc_no varchar(255))")
mycursor.execute("SHOW TABLES")
