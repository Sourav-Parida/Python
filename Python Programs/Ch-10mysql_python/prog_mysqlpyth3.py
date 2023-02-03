#To view the modified structure of table student in
#MySQL using Python Interface

import mysql.connector
mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                               passwd="",\
                               database="school")
mycursor = mydb.cursor()
mycursor.execute("Desc student")
for x in mycursor:
    print(x)


    


    


    



    











