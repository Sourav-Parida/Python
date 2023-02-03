#Illustrating global and local variables
global x
x = 5
def func2():
    x = 3
    print(x)
x = x+1
print(x)

func2()
