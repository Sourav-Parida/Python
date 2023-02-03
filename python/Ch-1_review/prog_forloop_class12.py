#Program to find the sum of 'n' natural numbers (for loop implementation)
n = int(input("Enter the limit : "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print("Sum is =",sum)


