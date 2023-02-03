#Deleting an element into a Stack : pop()

Stack= [1,'A',3.5,'X']    # Elements present in Stack
top = 0
def Pop_value(Stack,top):
    st_len =len(Stack)  #Returns the total number of elements in the Stack
    if st_len <= 0:     #Checks for empty stack
        print("Stack is empty")
    else:
        element = Stack.pop()   #Removing an element from list
        top = top - 1           
        print("Element deleted from the list is :",element)
    
Pop_value(Stack,top)


