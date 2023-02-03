#Display Stack Elements
Stack= [76,"Python",56.7,'X',3] #Stack holding 5 elements
top = 4
def Display_element(Stack,top):
    if not Stack:    
        print("Stack is empty")
    else:
        print("The Stack elements are :")
        i = top
        while (i >= 0):
            print(Stack[i]) #Printing of the elements in reverse order
            i =i - 1
    
Display_element(Stack,top)



