#Display Stack Elements
Stack= [76,"Python",56.7,'X',3] #Stack holding 5 elements
top = 4
def Display_element(Stack,top):
    st_len =len(Stack)
    if st_len <= 0:    #Checks whether Stack is empty or not
        print("Stack is empty")
    else:
        print("The Stack elements are :")
        i = top
        while (i >= 0):
            print(Stack[i])
            i =i - 1
    
Display_element(Stack,top)







        
    
