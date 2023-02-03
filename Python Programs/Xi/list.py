# Functions with list
'''Write a program to pass any list and to
arrange allnumbers in descending order'''
def test1():
    def arrange (l,n):
    for i in range(n-1):
    for j in range(n-i-1):
    if l[j]>l[j+1]:
    temp=l[j]
    l[j]=l[j+1]
    l[j+1]=temp
'''Write a program to input nXm matrix and
find sum of all numbers using function.'''
def test2():
    def summat(a,m,n):
    s=0
    for i in range(m):
    for j in range(n):
    s+=a[i][j]
    return s
#Function call
