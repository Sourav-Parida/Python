#Inserting element in a queue
Queue = []
rear = 0
def Insertion_Queue(Queue, rear):
    ch = 'Y'
    while ch == 'y' or ch=='Y':
        element = input("Enter the element to be added to the Queue :")
        rear = rear + 1     #rear is incremented by 1 and then insertion takes place
        Queue.append(element)   # adding element into list Queue
        print("Do you want to add more elements....<y/n> :")
        ch = input()
        if ch =='n' or ch =='N':
            break
    print("Contents of the queue are :",Queue)



    
        
Insertion_Queue(Queue, rear)
