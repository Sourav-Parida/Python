name = input("Enter your name: ")
age = input("Enter your age: ")
f = open("user_details.txt","a")
f.write(name)
f.write(age)
f.close()



