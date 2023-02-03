#Program to iilustrate return statement returning multiple values
def add_diff(x,y):
    add = x+y
    diff = x-y
    return add,diff
a,b = add_diff(200,180)
print("The sum of two numbers is :",a)
print("The difference of two numbers is :",b)
