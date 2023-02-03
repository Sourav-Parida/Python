#Program to find whether an inputted number is a prime number or not
n = int(input("Enter the limit :"))
ctr=1
num = 2
while ctr<=n:
    i = 2
    flag = 0
    while i<num:
        if num%i ==0:
            break
        i = i+1
    else:
        print(num,"is a prime number")
        ctr=ctr+1
    num=num+1



    
