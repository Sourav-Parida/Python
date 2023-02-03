#Deleting an element into a Stack : pop()

Stack= [1,'A',3.5,'X']    # Elements present in Stack
top = 0
def Pop_value(Stack,top):
    if not Stack:     #Checks for empty stack
        print("Stack is empty")
    else:
        element = Stack.pop()   #Removing an element from top of the Stack
        top = top - 1           
        print("Element deleted from the list is :",element)
    
Pop_value(Stack,top)


