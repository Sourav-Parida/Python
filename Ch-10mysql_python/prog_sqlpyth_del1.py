#Deleting records through Python Interface

import mysql.connector
mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                               passwd="",\
                               database="school")
mycursor = mydb.cursor()
mycursor.execute("DELETE FROM student where Rollno = 1")
mydb.commit()
print(mycursor.rowcount,"Record (s) Deleted")



    



    


    








    


    


    



    











