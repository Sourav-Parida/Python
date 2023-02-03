import os
import pickle

#Accepting data for Dictionary
def insertRec():
    rollno = int(input ("Enter roll number: "))
    name = input ("Enter Name: ")
    marks = int (input ("Enter Marks:"))
    #Creating the Dictionary
    rec = {"Rollno": rollno, "Name": name,"Marks": marks}
    #Writing the Dictionary
    f=open ("student.dat", "ab")
    pickle.dump (rec, f)
    f.close()

#Reading the records
def readRec():
    x=25
    f = open("student.dat", "rb")
    while True:
        try:
            rec = pickle.load(f)
            for R in rec:
                #print('Roll Num:',rec[0])
                print(R[0]) 
        except EOFError:
            break
    '''rec = pickle.load(f)
    print(rec)'''
    f.close()

#Searching a record based on Rollno
def searchRollNo (r):
    f = open("student.dat", "rb")
    flag = False
    while True:
        try:
            rec = pickle.load (f)
            if rec['Rollno'] == r:
                print ("Roll Num: ", rec['Rollno'])
                print ("Name:", rec["Name"])
                print ("Marks:", rec["Marks"])
                flag = True
        except EOFError:
            break
    if flag == False:
        print ("No Record Found")
    f.close()

#Marks Modification for a RollNo
def updateMarks (r, m):
    f = open("student.dat", "rb")
    reclst = []
    while True:
        try:
            rec = pickle.load(f)
            reclst.append (rec)
        except EOFError:
            break
    f.close()
    for i in range (len (reclst)):
        if reclst [1] ['Rollno']==r:
            reclst [1] ['Marks'] = m
    f.open("student.dat", 'wb')
    for x in reclst:
        pickle.dump (x, f)
    f.close()

#Deleting a record based on RollNo
def deleteRec (r):
    f-open ("student.dat", "rb")
    recist - []
    while True:
        try:
            rec = pickle.load(f)
            reclst.append (rec)
        except EOFError:
            break
    f.close()
    f = open ("student.dat", "sb")
    for x in recist:
        if x['Rolino']==r:
            continue
        pickle.dump(x, f)
    f.close()
while True:
    print ('Type 1 to insert rec.')
    print ('Type 2 to display rec.')
    print ('Type 3 to search rec.')
    print ('Type 4 to update rec.')
    print ('Type 5 to delete rec.')
    print ('Enter your choice 0 to exit')
    choice = int(input ("Enter your choice:"))
    if choice == 0:
        break
    elif choice == 1:
        insertRec()
    elif choice == 2:
        readRec()
    elif choice == 3:
        r = int(input ("Enter a rolino to search:"))
        searchRollNo(r)
    elif choice == 4:
        r = int(input ("Enter a rollno:"))
        m = int(input ("Enter new Marks:"))
        updateMarks (r, m)
    elif choice == 5:
        print (input ("Enter a rollno:"))
        deleteRec (r)









