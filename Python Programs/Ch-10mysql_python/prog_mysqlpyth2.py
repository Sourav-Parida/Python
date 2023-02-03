#To check for all the databases present in MySQL using Python

import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="")
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)






