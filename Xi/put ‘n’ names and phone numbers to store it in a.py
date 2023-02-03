'''program to input ‘n’ names and phone numbers to store it in a
dictionary and to input any name and to print the phone number of that particular
name.'''
def test1():
    phonebook=dict()
    n=input('Enter total number of friends-')
    n= int(n)
    i= 1
    while(i<=n):
        a=input("enter name")
        b=input("enter phone number")
        phonebook[a]=b
        i=i+1
        name= input("enter name")
        f=0
        l=phonebook.keys()
        for i in l:
            if(cmp(i,name)==0):
                print("Phone number= ",phonebook[i])
            f=1
            if (f==0):
                print("Given name not exist")





















    
