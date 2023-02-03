#To modify table student (adding a new column) in
#MySQL using Python Interface

import mysql.connector
mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                               passwd="",\
                               database="school")
mycursor = mydb.cursor()
mycursor.execute("Alter table student add(marks int(3))")


    



    











