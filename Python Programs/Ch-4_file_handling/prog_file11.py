#Program to write list sequence in a binary file
def fOperation():
    import pickle
    list1= [10,20,30,40,100]
    f =open('list.dat','wb') #'b' in access mode represents binary file
    pickle.dump(list1,f) #writing contents to binary file
    print("File added to binary file")
    f.close()

fOperation()
