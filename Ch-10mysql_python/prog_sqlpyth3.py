
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='',db='school')
stmt=con.cursor()
query='select * from student;'
stmt.execute(query)
data=stmt.fetchone()
print(data)
