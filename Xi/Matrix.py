#sum of matrices.
def test1():  
    import random
    m1=input ("Enter total number of rows in the first matrix")
    n1=input ("Enter total number of columns in the first matrix")
    a=[[random.random()for row in range(m1)]for col in range(n1)]
    a=int(a)
    for i in range(m1):
        for j in range(n1):
            a[i][j]=input()
        '''m2=input("Enter total number of rows in the second matrix")
        n2=input("Enter total number of columns in the second matrix")
        b=[[random.random()for row in range(m1)]for col in range(n1)]
    for i in range(2):
    for j in range(2):
    b[i][j]=input()
    c=[[random.random()for row in range(m1)]for col in range(n1)]
    if ((m1==m2) and (n1==n2)):
    print ("output is")
    for i in range(m1):
    for j in range(n1):
    c[i][j]=a[i][j]+b[i][j]
    print ((c[i][j],'\t',))
    print
    else
    print (“Matrix addition not possible”)'''







    
