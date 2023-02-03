#Program to illustrate writelines() method
#for writing list into the file

f =open("test4.txt",'w')
list =["Computer Science\n","Physics\n","Chemistry\n","Maths"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close()


