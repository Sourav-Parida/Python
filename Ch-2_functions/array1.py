#Arrays(list) passing to a function that calculates
#the arithmetic mean of list elements

def list_avg(lst):
    l = len(lst)
    sum = 0
    for i in lst:
        sum += i
    return sum/l

print("Input Integers :")
a = input()
a = a.split()
for i in range(len(a)):
    a[i] = int(a[i])


avrg = list_avg(a)

print("Average is :")
print(round(avrg,2))






