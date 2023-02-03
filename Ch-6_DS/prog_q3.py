#Displaying elements of the Queue
Queue = [2,4,5,'a']
rear = 3
def Display_Queue(Queue,rear):
    front = 0
    qlen =len(Queue)
    if qlen <= 0:   #Checks whether the queue is empty or not
        print("Queue is empty")
    else:
        print("The elements of the Queue are :")
        while front <= rear:
            print(Queue[front])
            front += 1

Display_Queue(Queue,rear)








    

