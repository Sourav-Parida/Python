#To create a new database 'school' from python to mysql

import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE school")



