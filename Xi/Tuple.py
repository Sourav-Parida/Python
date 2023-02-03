def test1():
    t=tuple()
    n=int(input("Enter any number"))
    print (" enter all numbers one after other")
    for i in range(n):
        a=int (input("enter number"))
        t=t+(a,)
        print ("output is")
    print (t)
