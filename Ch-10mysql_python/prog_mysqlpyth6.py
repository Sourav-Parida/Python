#Executing SELECT statement using Python

import mysql.connector
mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                               passwd="",\
                               database="school")
mycursor = mydb.cursor()
mycursor.execute("Select * from student")
myrecords = mycursor.fetchall()
for x in myrecords:
    print(x)



    


    








    


    


    



    











