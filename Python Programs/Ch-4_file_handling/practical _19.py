import pickle
record = []
while True:
    roll_no = int(input ("Enter student Roll no :"))
    name = input ("Enter the student Name :")
    marks= int(input ("Enter the marks obtained :"))
    data = [roll_no, name, marks]
    record.append (data)
    choice = input ("Wish to enter more records (Y/N)2: ")
    if choice.upper () == 'N':
        break
f = open("student", "wb")
pickle.dump (record, f)
print ("Record Added")
f.close()
