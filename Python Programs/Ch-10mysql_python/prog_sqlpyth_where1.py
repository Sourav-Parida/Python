#Implementing SELECT statement using
#WHERE clause in Python Interface

import mysql.connector
mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                               passwd="",\
                               database="school")
mycursor = mydb.cursor()
mycursor.execute("Select name,age,marks from student where city='Delhi'")
myrecords = mycursor.fetchall()
for x in myrecords:
    print(x)

    



    


    








    


    


    



    











