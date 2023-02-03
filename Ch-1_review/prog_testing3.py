Creating a dictionary for student record
d1 = dict()
i = 1
num = int(input("Enter the no: "))
for i in range(num):
    a = input("Enter name :")
    b = input("Enter age :")
    d1[a] = b
    l = d1.keys()
    i = i + 1
    for i in l:
        print(i,"\t",d1[i])
        
