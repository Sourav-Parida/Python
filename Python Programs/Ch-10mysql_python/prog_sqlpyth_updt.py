#Updating records through Python Interface

import mysql.connector
mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                               passwd="",\
                               database="school")
mycursor = mydb.cursor()
mycursor.execute("UPDATE student set age = 28 where Name = 'Vinay'")
mydb.commit()
print(mycursor.rowcount,"Record (s) Updated")








    



    


    








    


    


    



    











