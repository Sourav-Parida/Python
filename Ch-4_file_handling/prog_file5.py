#Program to read all lines into a list (using readlines())

f =open("test.txt",'r')
lines =f.readlines()
for line in lines:
    print(line,end='')
f.close()



