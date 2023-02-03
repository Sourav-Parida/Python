#Program to find maximum, minimum and mean value from the list
list1 = []   #Empty list
n =int(input("Enter the number of elements in the list : "))
i = 0
while i < n:
    x = int(input("Enter the elements of the list :"))
    list1.append(x)
    i = i+1
print(list1)

maximum = max(list1)
minimum = min(list1)
mean = sum(list1)/len(list1)
print("Maximum value is = ",maximum)
print("Minimum value is = ",minimum)
print("Average value is = ",mean)






      
