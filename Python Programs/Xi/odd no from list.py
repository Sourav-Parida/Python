n=int(input ('No. of inputs-'))
a=list(map(int,input('Enter the no.s:').strip().split()))[:n]
print('List is-',a)
list1 = a
for num in list1:
    if num%2==0:
        print("Even no. is the list:-" , num)
    else:
        print("Odd no. is the list:-" , num)
