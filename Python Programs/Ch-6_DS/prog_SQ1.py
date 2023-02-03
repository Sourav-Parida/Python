#Adding element into a Stack
Stack= []
top = 0
def Push_value(Stack,top):
    ch = 'Y'
    while ch=='y' or ch=='Y':
        element = input("Enter the value to be added into the Stack :")
        Stack.append(element)   #Adding element into list
        top += 1           #To keep a count for number of elements added to Stack
        print("Do you wish to add more elements.... <y/n> :")
        ch= input("Enter your choice :")
        if ch == 'n' or ch == 'N':
            break
    print(Stack)
    #return top

Push_value(Stack,top)


        
    
