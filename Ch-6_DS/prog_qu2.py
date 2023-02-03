#Program to add, remove and display the book details usins list
#implmentation as a Queue
Library=[]
c='y'
while (c=='y'):
    print ("1. INSERT")
    print ("2. DELETE ")
    print ("3. Display")
    choice=int(input("Enter your choice: "))
    if (choice==1):
        book_id=input("Enter book_id : ")
        bname = input("Enter the book name :")
        lib = (book_id,bname)   #tuple created for a new book
        Library.append(lib)   #new book added to the list/queue
    elif (choice==2):
        if (Library==[]):
            print("Queue Empty")
        else:
            print("Deleted element is:",Library.pop(0))
    elif (choice==3):
        l=len(Library)
        for i in range(0,l):
            print (Library[i])
    else:
        print("wrong input")
    c=input("Do you want to continue or not : ")



    

    


    


    




    



