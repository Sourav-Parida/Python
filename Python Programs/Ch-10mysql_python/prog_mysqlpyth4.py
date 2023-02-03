#To a new record into table student in
#MySQL using Python Interface

import mysql.connector
mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                               passwd="",\
                               database="school")
mycursor = mydb.cursor()
mycursor.execute("INSERT INTO student VALUES(")
for x in mycursor:
    print(x)


    


    


    



    











