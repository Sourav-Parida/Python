#Program to read data from 2nd character into a list.

f =open("test.txt",'r')
print(f.read(2))
print(f.readlines())
print(f.read(3))
print("Remaining data")
print(f.read())


