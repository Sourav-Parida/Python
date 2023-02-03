#Adding numeric to a file using conversion function- str()

f =open("newtest.txt","w")
x =100
f.write("Hello World \n")
f.write(str(x))   #Numeric value is converted into string 
f.close()



