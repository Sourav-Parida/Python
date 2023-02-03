#Program to illustrate 'with' statement

with open("test1.text","w") as f:
    f.write("Python \n")
    f.write("is an easy \n")
    f.write("language \n")
    f.write("to work with \n")
    print("Is file closed : ",f.closed)
print("Is file closed : ",f.close())



    
    
