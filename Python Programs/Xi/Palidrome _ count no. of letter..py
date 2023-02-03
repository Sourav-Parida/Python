#function for palidrome
def test1():
    str=input("Enter the String-")
    l=len(str)
    p=l-1
    index=0
    while (index<p):
        if(str[index]==str[p]):
            index=index+1
            p=p-1
        else:
            print ('String is not a palidrome')
            break
    else:
        print ("String is a Palidrome")
def test2():
    i=str(input("Enter the String-"))
    rev=0
    x=i
    while (i>0):
        rev=(rev*10+i%10)
        i=i//10
    if (x==rev):
            print ('String is not a palidrome')
    else:
        print ("String is a Palidrome")
def test3():
    a=str(input("Enter the String-"))
    b=a[1::-1]
    print(b)
    if (a==b):
        print ('String is a palidrome')
    else:
        print ("String is not a Palidrome")
