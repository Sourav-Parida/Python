#To insert a new record into table student in
#MySQL using Python Interface

import mysql.connector
mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                               passwd="",\
                               database="school")
mycursor = mydb.cursor()
mycursor.execute("INSERT INTO student VALUES(2,'Pooja',21,'Chail',390)")
mycursor.execute("INSERT INTO student VALUES(3,'Radhika',18,'Shimla',388)")
mycursor.execute("INSERT INTO student VALUES(4,'Sonia',24,'Goa',300)")
mycursor.execute("INSERT INTO student VALUES(5,'Vinay',25,'Pune',410)")
mycursor.execute("INSERT INTO student VALUES(10,'Shaurya',15,'Delhi',345)")
mydb.commit()











    


    


    



    











