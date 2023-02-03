#Program to enter the numbers in a list using split () and to use all the functions related to list.
# numbers = [int(n, 10) for n in input().split(",")]
# print (len(numbers))
 
memo=[] 
for i in range (5):
    x=int(input("enter no. \n")) 
    memo.insert(i,x)
    i+=1
print(memo)
memo.append(25)
print("Second List")
print(memo)
msg=input("Enter any string : ")
newlist=[]
newlist[:0]=msg
l=len(newlist)
print(l)
